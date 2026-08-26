from pathlib import Path
from typing import Annotated
import uuid
import os

from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.middleware.sessions import SessionMiddleware

from .adaptive import evaluate_reasoning, stakeholder_response
from .content import BELTS, DIAGNOSTIC, SCENARIOS
from .db import (
    add_attempt,
    add_journal,
    authenticate,
    create_scenario_session,
    create_user,
    get_scenario_session,
    init_db,
    learner,
    list_attempts,
    list_journal,
    update_learner,
    update_scenario_session,
)
from .scenarios import SCENARIO_DETAIL
from .socratic import evaluate

BASE_DIR = Path(__file__).resolve().parent.parent
app = FastAPI(title="Six Sigma Operations Lab", version="0.4.0")
app.add_middleware(SessionMiddleware, secret_key=os.getenv("SSOL_SESSION_SECRET", "local-development-secret-change-me"), same_site="lax", https_only=False)
app.mount("/static", StaticFiles(directory=BASE_DIR / "static"), name="static")
templates = Jinja2Templates(directory=BASE_DIR / "templates")


@app.on_event("startup")
def startup():
    init_db()


def current_user_id(request: Request) -> int:
    user_id = request.session.get("user_id")
    if user_id:
        return int(user_id)
    # Demo mode preserves the frictionless prototype experience.
    request.session["user_id"] = 1
    return 1


def context(request: Request, **kwargs):
    user_id = current_user_id(request)
    profile = learner(user_id)
    return {"request": request, "belts": BELTS, "learner": profile, "user_id": user_id, **kwargs}


def get_scenario(scenario_id: str | None):
    base = next((s for s in SCENARIOS if s["id"] == scenario_id), None)
    if base:
        return base
    return SCENARIOS[0]


@app.get("/", response_class=HTMLResponse)
async def landing(request: Request):
    return templates.TemplateResponse(request=request, name="landing.html", context=context(request))


@app.get("/pricing", response_class=HTMLResponse)
async def pricing(request: Request):
    return templates.TemplateResponse(request=request, name="pricing.html", context=context(request))


@app.get("/signup", response_class=HTMLResponse)
async def signup(request: Request):
    return templates.TemplateResponse(request=request, name="signup.html", context=context(request, error=""))


@app.post("/signup", response_class=HTMLResponse)
async def signup_submit(
    request: Request,
    name: Annotated[str, Form()] = "",
    email: Annotated[str, Form()] = "",
    password: Annotated[str, Form()] = "",
):
    email = email.strip().lower()
    if not name.strip() or "@" not in email or len(password) < 8:
        return templates.TemplateResponse(
            request=request,
            name="signup.html",
            context=context(request, error="Enter your name, a valid email, and a password of at least 8 characters."),
            status_code=400,
        )
    user_id = create_user(email, password, name)
    if not user_id:
        return templates.TemplateResponse(
            request=request,
            name="signup.html",
            context=context(request, error="An account already exists for that email."),
            status_code=409,
        )
    request.session["user_id"] = user_id
    return RedirectResponse("/diagnostic", status_code=303)


@app.get("/signin", response_class=HTMLResponse)
async def signin(request: Request):
    return templates.TemplateResponse(request=request, name="signin.html", context=context(request, error=""))


@app.post("/signin", response_class=HTMLResponse)
async def signin_submit(
    request: Request,
    email: Annotated[str, Form()] = "",
    password: Annotated[str, Form()] = "",
):
    user = authenticate(email, password)
    if not user:
        return templates.TemplateResponse(request=request, name="signin.html", context=context(request, error="Email or password is incorrect."), status_code=401)
    request.session["user_id"] = user["id"]
    return RedirectResponse("/learn", status_code=303)


@app.post("/signout")
async def signout(request: Request):
    request.session.clear()
    return RedirectResponse("/", status_code=303)


@app.get("/diagnostic", response_class=HTMLResponse)
async def diagnostic(request: Request):
    return templates.TemplateResponse(request=request, name="diagnostic.html", context=context(request, questions=DIAGNOSTIC))


@app.post("/diagnostic", response_class=HTMLResponse)
async def diagnostic_submit(
    request: Request,
    answers: Annotated[list[str] | None, Form()] = None,
    business_area: Annotated[str, Form()] = "",
):
    user_id = current_user_id(request)
    values = answers or []
    score = sum(1 for idx, q in enumerate(DIAGNOSTIC) if idx < len(values) and values[idx] == str(q["answer"]))
    if score <= 2:
        belt_key = "white"
    elif score <= 4:
        belt_key = "yellow"
    elif score <= 6:
        belt_key = "green"
    else:
        belt_key = "black"
    update_learner(user_id, business_area=business_area, belt=belt_key, diagnostic_score=score, diagnostic_total=len(DIAGNOSTIC))
    return templates.TemplateResponse(
        request=request,
        name="diagnostic_result.html",
        context=context(request, score=score, max_score=len(DIAGNOSTIC), belt=BELTS[belt_key]),
    )


@app.get("/learn", response_class=HTMLResponse)
async def learn(request: Request):
    return templates.TemplateResponse(request=request, name="learn_index.html", context=context(request))


@app.get("/learn/{belt}", response_class=HTMLResponse)
async def belt_page(request: Request, belt: str):
    belt_key = belt.lower()
    if belt_key not in BELTS:
        return RedirectResponse("/not-found", status_code=303)
    return templates.TemplateResponse(request=request, name="belt.html", context=context(request, belt=BELTS[belt_key], belt_key=belt_key))


@app.get("/lesson/{belt}/{lesson_index}", response_class=HTMLResponse)
async def lesson(request: Request, belt: str, lesson_index: int):
    belt_key = belt.lower()
    if belt_key not in BELTS or not (1 <= lesson_index <= len(BELTS[belt_key]["modules"])):
        return RedirectResponse("/not-found", status_code=303)
    module = BELTS[belt_key]["modules"][lesson_index - 1]
    lesson_data = {
        "id": f"{belt_key}-{lesson_index:02d}",
        "index": lesson_index,
        "belt_key": belt_key,
        "belt": BELTS[belt_key],
        "title": module[1],
        "opening_question": module[2],
        "concepts": module[3],
        "teach_back": module[4],
    }
    return templates.TemplateResponse(request=request, name="lesson.html", context=context(request, lesson=lesson_data))


@app.post("/teach", response_class=HTMLResponse)
async def teach(
    request: Request,
    response: Annotated[str, Form()],
    activity_id: Annotated[str, Form()],
    focus: Annotated[str, Form()] = "general",
    next_url: Annotated[str, Form()] = "/learn",
):
    result = evaluate(response, focus)
    add_attempt(current_user_id(request), "teach_back", activity_id, response, result["feedback"], result["score"])
    return templates.TemplateResponse(request=request, name="feedback.html", context=context(request, result=result, response=response, next_url=next_url))


@app.get("/scenario", response_class=HTMLResponse)
async def scenarios(request: Request, id: str | None = None, session: str | None = None):
    user_id = current_user_id(request)
    scenario = get_scenario(id)
    detail = SCENARIO_DETAIL[scenario["id"]]
    session_id = session or str(uuid.uuid4())
    create_scenario_session(session_id, user_id, scenario["id"])
    state = get_scenario_session(session_id, user_id)
    return templates.TemplateResponse(
        request=request,
        name="scenario.html",
        context=context(request, scenario=scenario, detail=detail, state=state, session_id=session_id),
    )


@app.post("/scenario/{scenario_id}/stakeholder", response_class=HTMLResponse)
async def scenario_stakeholder(
    request: Request,
    scenario_id: str,
    session: Annotated[str, Form()],
    stakeholder: Annotated[str, Form()],
    question: Annotated[str, Form()] = "",
):
    user_id = current_user_id(request)
    scenario = get_scenario(scenario_id)
    detail = SCENARIO_DETAIL[scenario["id"]]
    state = get_scenario_session(session, user_id)
    if not state or state["scenario_id"] != scenario["id"]:
        create_scenario_session(session, user_id, scenario["id"])
        state = get_scenario_session(session, user_id)

    person = detail["stakeholders"].get(stakeholder)
    if not person:
        return RedirectResponse(f"/scenario?id={scenario['id']}&session={session}", status_code=303)

    result = stakeholder_response(person, question, state, state["phase"])
    visited = list(dict.fromkeys(state["visited_stakeholders"] + [stakeholder]))
    clue_ids = list(dict.fromkeys(state["discovered_clues"] + [f"{stakeholder}:{i}" for i in range(len(result["new_clues"]))]))
    conversation = state.get("conversation", []) + [{
        "stakeholder": stakeholder,
        "question": question.strip(),
        "response": result["reply"],
        "score": result["score"],
        "dimensions": result["dimensions"],
    }]
    stakeholder_score = min(100, state.get("stakeholder_score", 0) + max(5, result["score"] // 5))
    evidence_score = min(100, state.get("evidence_score", 0) + len(result["new_clues"]) * 10)
    update_scenario_session(
        session, user_id,
        visited_stakeholders=visited,
        discovered_clues=clue_ids,
        conversation=conversation,
        stakeholder_score=stakeholder_score,
        evidence_score=evidence_score,
    )
    state = get_scenario_session(session, user_id)
    return templates.TemplateResponse(
        request=request,
        name="stakeholder.html",
        context=context(request, scenario=scenario, detail=detail, stakeholder=stakeholder, person=person, state=state, session_id=session, question=question, dialogue=result),
    )


@app.post("/scenario/{scenario_id}/decision", response_class=HTMLResponse)
async def scenario_decision(
    request: Request,
    scenario_id: str,
    session: Annotated[str, Form()],
    decision: Annotated[str, Form()],
):
    user_id = current_user_id(request)
    scenario = get_scenario(scenario_id)
    detail = SCENARIO_DETAIL[scenario["id"]]
    state = get_scenario_session(session, user_id)
    option = next((o for o in detail["decision_options"] if o["id"] == decision), None)
    if option and state:
        decisions = state["decisions"] + [option["id"]]
        phase = detail["phases"][min(len(decisions), len(detail["phases"]) - 1)]
        update_scenario_session(session, user_id, decisions=decisions, phase=phase)
        state = get_scenario_session(session, user_id)
    return templates.TemplateResponse(
        request=request,
        name="decision_feedback.html",
        context=context(request, scenario=scenario, detail=detail, state=state, session_id=session, decision=option),
    )


@app.post("/scenario/{scenario_id}/think", response_class=HTMLResponse)
async def scenario_think(
    request: Request,
    scenario_id: str,
    thinking: Annotated[str, Form()],
    session: Annotated[str, Form()],
):
    user_id = current_user_id(request)
    scenario = get_scenario(scenario_id)
    detail = SCENARIO_DETAIL[scenario["id"]]
    state = get_scenario_session(session, user_id)
    if not state:
        create_scenario_session(session, user_id, scenario["id"])
        state = get_scenario_session(session, user_id)
    result = evaluate_reasoning(thinking, state["phase"], state, detail)
    add_attempt(user_id, "scenario_thinking", scenario_id, thinking, result["feedback"], result["score"])
    reasoning_score = min(100, max(state.get("reasoning_score", 0), result["score"]))
    update_scenario_session(session, user_id, reasoning_score=reasoning_score)
    state = get_scenario_session(session, user_id)
    return templates.TemplateResponse(request=request, name="scenario_feedback.html", context=context(request, scenario=scenario, detail=detail, state=state, result=result, thinking=thinking, session_id=session))


@app.post("/journal")
async def journal_submit(
    request: Request,
    reflection: Annotated[str, Form()],
    scenario_id: Annotated[str, Form()] = "",
    lesson_id: Annotated[str, Form()] = "",
):
    if reflection.strip():
        add_journal(current_user_id(request), reflection, scenario_id, lesson_id)
    return RedirectResponse("/journal", status_code=303)


@app.get("/journal", response_class=HTMLResponse)
async def journal(request: Request):
    user_id = current_user_id(request)
    return templates.TemplateResponse(request=request, name="journal.html", context=context(request, entries=list_journal(user_id)))


@app.get("/consult", response_class=HTMLResponse)
async def consult(request: Request):
    return templates.TemplateResponse(request=request, name="consult.html", context=context(request))


@app.get("/api/scenarios")
async def scenario_api():
    return SCENARIOS


@app.get("/api/progress")
async def progress_api(request: Request):
    user_id = current_user_id(request)
    return {"learner": learner(user_id), "attempts": list_attempts(user_id), "journal_count": len(list_journal(user_id, 1000))}


@app.get("/health")
async def health():
    return {"status": "ok", "version": app.version}


@app.exception_handler(404)
async def not_found(request: Request, exc):
    return templates.TemplateResponse(request=request, name="404.html", context=context(request), status_code=404)
