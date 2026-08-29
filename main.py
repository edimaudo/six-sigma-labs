from pathlib import Path
from typing import Annotated
import uuid
import os
import asyncio
import math

from fastapi import FastAPI, Form, Request, HTTPException
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.middleware.sessions import SessionMiddleware

from adaptive import GeminiConfigError, GeminiResponseError, evaluate_reasoning, evaluate_teach_back, stakeholder_response
from content import BELTS, BELT_ORDER, DIAGNOSTIC, DIAGNOSTIC_BANK, GLOSSARY, MATH_REFERENCE, SCENARIOS
from db import (
    add_attempt,
    add_journal,
    create_scenario_session,
    get_scenario_session,
    init_db,
    learner,
    list_attempts,
    list_journal,
    update_learner,
    update_scenario_session,
)
from scenarios import SCENARIO_DETAIL

BASE_DIR = Path(__file__).resolve().parent
app = FastAPI(title="Six Sigma Labs", version="2.2.0")
app.add_middleware(SessionMiddleware, secret_key=os.getenv("SSOL_SESSION_SECRET", "local-development-secret-change-me"), same_site="lax", https_only=False)
app.mount("/static", StaticFiles(directory=BASE_DIR / "static"), name="static")
templates = Jinja2Templates(directory=BASE_DIR / "templates")


@app.on_event("startup")
def startup():
    init_db()


def optional_user_id(request: Request) -> int | None:
    user_id = request.session.get("user_id")
    return int(user_id) if user_id else None


def current_user_id(request: Request) -> int:
    user_id = optional_user_id(request)
    if user_id is not None:
        return user_id

    # Authentication is intentionally disabled while the learning experience
    # is being validated. Create an anonymous learner scoped to this browser
    # session rather than attaching the visitor to a shared demo account.
    from db import create_anonymous_user
    user_id = create_anonymous_user()
    request.session["user_id"] = int(user_id)
    return int(user_id)


def has_diagnostic(request: Request) -> bool:
    user_id = optional_user_id(request)
    if user_id is None:
        return False
    profile = learner(user_id)
    return bool(profile and profile.get("diagnostic_total", 0))


def context(request: Request, **kwargs):
    user_id = optional_user_id(request)
    profile = learner(user_id) if user_id is not None else None
    return {"request": request, "belts": BELTS, "belt_order": BELT_ORDER, "learner": profile, "user_id": user_id, "diagnostic_complete": bool(profile and profile.get("diagnostic_total", 0)), "glossary": GLOSSARY, "math_reference": MATH_REFERENCE, **kwargs}


def get_scenario(scenario_id: str | None):
    base = next((s for s in SCENARIOS if s["id"] == scenario_id), None)
    if base:
        return base
    return SCENARIOS[0]


@app.get("/", response_class=HTMLResponse)
async def landing(request: Request):
    return templates.TemplateResponse(request=request, name="landing.html", context=context(request))


# Pricing route intentionally disabled while the learning product is being validated.
# @app.get("/pricing", response_class=HTMLResponse)
# async def pricing(request: Request):
#     return templates.TemplateResponse(request=request, name="pricing.html", context=context(request))

# Authentication routes retained in source for later paid-account activation.
# They are intentionally commented out of the product navigation and not linked
# from the landing page while the educational experience is validated.
# @app.get("/signup") ...
# @app.post("/signup") ...
# @app.get("/signin") ...
# @app.post("/signin") ...
# @app.post("/signout") ...

BELT_LEVEL_ANCHORS = ["W1", "Y1", "G1", "B1"]
BELT_LEVEL_BRANCHES = {
    "black": {"questions": ["B2", "B3", "B4", "B5", "G2", "G3"], "depth": ["B1", "B2", "B3", "B4", "B5", "G2", "G3"], "stretch": None, "backstop": ["G2", "G3"]},
    "green": {"questions": ["G2", "G3", "G4", "G5", "B2", "Y2"], "depth": ["G1", "G2", "G3", "G4", "G5", "B2", "Y2"], "stretch": "B2", "backstop": ["Y2"]},
    "yellow": {"questions": ["Y2", "Y3", "Y4", "Y5", "G2", "W2"], "depth": ["Y1", "Y2", "Y3", "Y4", "Y5", "G2", "W2"], "stretch": "G2", "backstop": ["W2"]},
    "white": {"questions": ["W2", "W3", "W4", "W5", "Y2", "W1"], "depth": ["W1", "W2", "W3", "W4", "W5", "Y2"], "stretch": "Y2", "backstop": []},
}

DIAGNOSTIC_BY_ID = {q["id"]: q for q in DIAGNOSTIC_BANK}

def _question_set(ids: list[str], repeat_w1: bool = False):
    out = []
    for qid in ids:
        q = dict(DIAGNOSTIC_BY_ID[qid])
        if repeat_w1 and qid == "W1":
            q = dict(q)
            q["display_id"] = "W1 · confidence check"
            q["id"] = "W1R"
        else:
            q["display_id"] = qid
        out.append(q)
    return out

def _answer_map(form):
    result = {}
    for q in DIAGNOSTIC_BANK:
        key = f"answer_{q['id']}"
        if key in form:
            result[q["id"]] = str(form.get(key))
    if "answer_W1R" in form:
        result["W1R"] = str(form.get("answer_W1R"))
    return result

def _correct(question_id: str, answer_value: str | None) -> bool:
    source_id = "W1" if question_id == "W1R" else question_id
    q = DIAGNOSTIC_BY_ID[source_id]
    return answer_value == str(q["answer"])

def _branch_from_anchors(answers: dict[str, str]) -> str:
    if _correct("B1", answers.get("B1")):
        return "black"
    if _correct("G1", answers.get("G1")):
        return "green"
    if _correct("Y1", answers.get("Y1")):
        return "yellow"
    return "white"

def _recommendation(branch: str, answers: dict[str, str]):
    cfg = BELT_LEVEL_BRANCHES[branch]
    depth_ids = cfg["depth"]
    depth_correct = sum(1 for qid in depth_ids if _correct(qid, answers.get(qid)))
    depth_total = len(depth_ids)
    pct = depth_correct / depth_total if depth_total else 0
    stretch_correct = cfg["stretch"] is None or _correct(cfg["stretch"], answers.get(cfg["stretch"]))
    idx = BELT_ORDER.index(branch)
    recommendation = branch
    note = ""
    if pct >= 0.8 and stretch_correct:
        recommendation = BELT_ORDER[min(idx + 1, len(BELT_ORDER) - 1)]
        note = "Strong performance in the branched tier suggests you are ready to begin one tier higher." if recommendation != branch else "Strong performance supports starting at this level."
    elif pct >= 0.8 and not stretch_correct:
        recommendation = branch
        note = "You handled the core tier well, but the stretch question suggests starting here rather than moving up."
    elif pct >= 0.5:
        recommendation = branch
        note = "You have a workable foundation at this level; the early lessons are worth reviewing."
    else:
        recommendation = BELT_ORDER[max(0, idx - 1)]
        note = "The depth check suggests reinforcing the previous tier before moving ahead." if idx > 0 else "Start with the White Belt foundations and build from there."
    return recommendation, depth_correct, depth_total, pct, stretch_correct, note

@app.get("/belt-level", response_class=HTMLResponse)
async def belt_level(request: Request):
    request.session.pop("belt_level_answers", None)
    request.session.pop("belt_level_branch", None)
    questions = _question_set(BELT_LEVEL_ANCHORS)
    return templates.TemplateResponse(
        request=request,
        name="diagnostic.html",
        context=context(request, questions=questions, round=1, total_rounds=2, branch=None, question_number_offset=0),
    )

@app.post("/belt-level", response_class=HTMLResponse)
async def belt_level_submit(request: Request):
    form = await request.form()
    round_number = str(form.get("round") or "1")
    business_area = str(form.get("business_area") or request.session.get("belt_level_business_area") or "")
    answers = _answer_map(form)

    if round_number == "1":
        branch = _branch_from_anchors(answers)
        request.session["belt_level_answers"] = answers
        request.session["belt_level_branch"] = branch
        request.session["belt_level_business_area"] = business_area
        branch_ids = BELT_LEVEL_BRANCHES[branch]["questions"]
        questions = _question_set(branch_ids, repeat_w1=(branch == "white"))
        return templates.TemplateResponse(
            request=request,
            name="diagnostic.html",
            context=context(request, questions=questions, round=2, total_rounds=2, branch=branch, business_area=business_area, question_number_offset=4),
        )

    stored = dict(request.session.get("belt_level_answers") or {})
    stored.update(answers)
    branch = str(request.session.get("belt_level_branch") or "white")
    business_area = str(request.session.get("belt_level_business_area") or business_area)
    recommendation, depth_correct, depth_total, depth_pct, stretch_correct, note = _recommendation(branch, stored)
    total_correct = sum(1 for q in DIAGNOSTIC_BANK if q["id"] in stored and _correct(q["id"], stored[q["id"]]))
    # W1 confidence check is intentionally not a new bank item and is excluded from the 20-question count.
    if "W1R" in stored and _correct("W1R", stored["W1R"]):
        total_correct += 1
    request.session["diagnostic_complete"] = True
    request.session["belt_level_answers"] = stored
    update_learner(
        current_user_id(request),
        business_area=business_area,
        belt=recommendation,
        diagnostic_score=total_correct,
        diagnostic_total=10,
    )
    by_belt = {belt: {"correct": 0, "total": 0} for belt in BELT_ORDER}
    for q in DIAGNOSTIC_BANK:
        if q["id"] in stored:
            by_belt[q["belt"]]["total"] += 1
            if _correct(q["id"], stored[q["id"]]):
                by_belt[q["belt"]]["correct"] += 1
    return templates.TemplateResponse(
        request=request,
        name="diagnostic_result.html",
        context=context(
            request,
            score=total_correct,
            max_score=10,
            belt=BELTS[recommendation],
            branch=BELTS[branch],
            depth_correct=depth_correct,
            depth_total=depth_total,
            depth_pct=round(depth_pct * 100),
            stretch_correct=stretch_correct,
            recommendation_note=note,
            by_belt=by_belt,
        ),
    )

# Backward-compatible alias for the previous diagnostic URL.
@app.get("/diagnostic", response_class=HTMLResponse)
async def diagnostic_legacy(request: Request):
    return RedirectResponse("/belt-level", status_code=303)

@app.post("/diagnostic", response_class=HTMLResponse)
async def diagnostic_legacy_post(request: Request):
    return RedirectResponse("/belt-level", status_code=307)


@app.get("/learn", response_class=HTMLResponse)
async def learn(request: Request):
    return templates.TemplateResponse(request=request, name="learn_index.html", context=context(request))


@app.get("/math", response_class=HTMLResponse)
async def math_redirect():
    return RedirectResponse("/glossary", status_code=303)


@app.get("/glossary", response_class=HTMLResponse)
async def glossary(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="glossary.html",
        context=context(request, glossary=GLOSSARY, math_reference=MATH_REFERENCE),
    )


@app.get("/case-studies", response_class=HTMLResponse)
async def case_studies(request: Request):
    q = (request.query_params.get("q") or "").strip().lower()
    belt = (request.query_params.get("belt") or "all").strip().lower()
    method = (request.query_params.get("method") or "all").strip()
    area = (request.query_params.get("area") or "all").strip()
    filtered = [
        s for s in SCENARIOS
        if (belt == "all" or s["belt"] == belt)
        and (method == "all" or s.get("method", "DMAIC") == method)
        and (area == "all" or s.get("area") == area)
        and (not q or q in " ".join([s["title"], s["area"], s["prompt"], s["difficulty"], s.get("method", "DMAIC"), s.get("source_title", "")]).lower())
    ]
    areas = sorted({s.get("area", "") for s in SCENARIOS if s.get("area")})
    return templates.TemplateResponse(request=request, name="case_studies.html", context=context(request, scenarios=filtered, query=q, belt_filter=belt, method_filter=method, area_filter=area, areas=areas))


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
        **module,
        "id": f"{belt_key}-{lesson_index:02d}",
        "index": lesson_index,
        "belt_key": belt_key,
        "belt": BELTS[belt_key],
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
    try:
        result, _interaction_id = await asyncio.to_thread(evaluate_teach_back, response, focus)
    except (GeminiConfigError, GeminiResponseError) as exc:
        return templates.TemplateResponse(
            request=request,
            name="feedback.html",
            context=context(request, result=None, response=response, next_url=next_url, error=str(exc)),
            status_code=503,
        )
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

    try:
        previous_id = state.get("gemini_stakeholder_interactions", {}).get(stakeholder)
        result, interaction_id = await asyncio.to_thread(
            stakeholder_response, person, question, state, state["phase"], previous_id
        )
    except (GeminiConfigError, GeminiResponseError) as exc:
        return templates.TemplateResponse(request=request, name="stakeholder.html", context=context(request, scenario=scenario, detail=detail, stakeholder=stakeholder, person=person, state=state, session_id=session, question=question, dialogue=None, error=str(exc)), status_code=503)
    visited = list(dict.fromkeys(state["visited_stakeholders"] + [stakeholder]))
    clue_ids = list(dict.fromkeys(state["discovered_clues"] + [f"{stakeholder}:{i}" for i in result.get("new_clue_indices", [])]))
    conversation = state.get("conversation", []) + [{
        "stakeholder": stakeholder,
        "question": question.strip(),
        "response": result["reply"],
        "score": result["score"],
        "dimensions": result["dimensions"],
    }]
    stakeholder_score = min(100, state.get("stakeholder_score", 0) + max(5, result["score"] // 5))
    evidence_score = min(100, state.get("evidence_score", 0) + len(result["new_clues"]) * 10)
    stakeholder_interactions = dict(state.get("gemini_stakeholder_interactions", {}))
    stakeholder_interactions[stakeholder] = interaction_id
    update_scenario_session(
        session, user_id,
        visited_stakeholders=visited,
        discovered_clues=clue_ids,
        conversation=conversation,
        stakeholder_score=stakeholder_score,
        evidence_score=evidence_score,
        gemini_stakeholder_interactions=stakeholder_interactions,
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
    try:
        result, interaction_id = await asyncio.to_thread(
            evaluate_reasoning, thinking, state["phase"], state, detail, state.get("gemini_reasoning_interaction_id") or None
        )
    except (GeminiConfigError, GeminiResponseError) as exc:
        return templates.TemplateResponse(request=request, name="scenario_feedback.html", context=context(request, scenario=scenario, detail=detail, state=state, result=None, thinking=thinking, session_id=session, error=str(exc)), status_code=503)
    add_attempt(user_id, "scenario_thinking", scenario_id, thinking, result["feedback"], result["score"])
    reasoning_score = min(100, max(state.get("reasoning_score", 0), result["score"]))
    update_scenario_session(session, user_id, reasoning_score=reasoning_score, gemini_reasoning_interaction_id=interaction_id)
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
async def consult_legacy(request: Request):
    return RedirectResponse("/case-studies", status_code=303)


@app.get("/api/scenarios")
async def scenario_api():
    return SCENARIOS


@app.get("/api/progress")
async def progress_api(request: Request):
    user_id = current_user_id(request)
    return {"learner": learner(user_id), "attempts": list_attempts(user_id), "journal_count": len(list_journal(user_id, 1000))}


@app.get("/health")
async def health():
    return {"status": "ok", "version": app.version, "gemini_configured": bool(os.getenv("GEMINI_API_KEY"))}


@app.exception_handler(404)
async def not_found(request: Request, exc):
    return templates.TemplateResponse(request=request, name="404.html", context=context(request), status_code=404)
