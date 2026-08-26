from pathlib import Path
from typing import Annotated

from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from .content import BELTS, DIAGNOSTIC, SCENARIOS
from .db import add_attempt, add_journal, init_db, learner, list_attempts, list_journal, update_learner
from .socratic import evaluate

BASE_DIR = Path(__file__).resolve().parent.parent
app = FastAPI(title="Six Sigma Operations Lab", version="0.2.0")
app.mount("/static", StaticFiles(directory=BASE_DIR / "static"), name="static")
templates = Jinja2Templates(directory=BASE_DIR / "templates")

@app.on_event("startup")
def startup():
    init_db()


def context(request: Request, **kwargs):
    return {"request": request, "belts": BELTS, "learner": learner(), **kwargs}


@app.get("/", response_class=HTMLResponse)
async def landing(request: Request):
    return templates.TemplateResponse(request=request, name="landing.html", context=context(request))


@app.get("/diagnostic", response_class=HTMLResponse)
async def diagnostic(request: Request):
    return templates.TemplateResponse(request=request, name="diagnostic.html", context=context(request, questions=DIAGNOSTIC))


@app.post("/diagnostic", response_class=HTMLResponse)
async def diagnostic_submit(
    request: Request,
    answers: Annotated[list[str] | None, Form()] = None,
    business_area: Annotated[str, Form()] = "",
):
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
    update_learner(business_area=business_area, belt=belt_key, diagnostic_score=score, diagnostic_total=len(DIAGNOSTIC))
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
        return RedirectResponse("/learn", status_code=303)
    return templates.TemplateResponse(request=request, name="belt.html", context=context(request, belt=BELTS[belt_key], belt_key=belt_key))


@app.get("/lesson/{belt}/{lesson_index}", response_class=HTMLResponse)
async def lesson(request: Request, belt: str, lesson_index: int):
    belt_key = belt.lower()
    if belt_key not in BELTS or not (1 <= lesson_index <= len(BELTS[belt_key]["modules"])):
        return RedirectResponse("/learn", status_code=303)
    module = BELTS[belt_key]["modules"][lesson_index - 1]
    lesson_data = {"id": f"{belt_key}-{lesson_index:02d}", "index": lesson_index, "belt_key": belt_key, "belt": BELTS[belt_key], "title": module[1], "opening_question": module[2], "concepts": module[3], "teach_back": module[4]}
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
    add_attempt("teach_back", activity_id, response, result["feedback"], result["score"])
    return templates.TemplateResponse(request=request, name="feedback.html", context=context(request, result=result, response=response, next_url=next_url))


@app.get("/scenario", response_class=HTMLResponse)
async def scenarios(request: Request, id: str | None = None):
    scenario = next((s for s in SCENARIOS if s["id"] == id), SCENARIOS[0])
    return templates.TemplateResponse(request=request, name="scenario.html", context=context(request, scenario=scenario))


@app.post("/scenario/{scenario_id}/think", response_class=HTMLResponse)
async def scenario_think(
    request: Request,
    scenario_id: str,
    thinking: Annotated[str, Form()],
):
    scenario = next((s for s in SCENARIOS if s["id"] == scenario_id), SCENARIOS[0])
    result = evaluate(thinking, "general")
    add_attempt("scenario_thinking", scenario_id, thinking, result["feedback"], result["score"])
    return templates.TemplateResponse(request=request, name="scenario_feedback.html", context=context(request, scenario=scenario, result=result, thinking=thinking))


@app.post("/journal")
async def journal_submit(
    request: Request,
    reflection: Annotated[str, Form()],
    scenario_id: Annotated[str, Form()] = "",
    lesson_id: Annotated[str, Form()] = "",
):
    if reflection.strip():
        add_journal(reflection, scenario_id, lesson_id)
    return RedirectResponse("/journal", status_code=303)


@app.get("/journal", response_class=HTMLResponse)
async def journal(request: Request):
    return templates.TemplateResponse(request=request, name="journal.html", context=context(request, entries=list_journal()))


@app.get("/consult", response_class=HTMLResponse)
async def consult(request: Request):
    return templates.TemplateResponse(request=request, name="consult.html", context=context(request))


@app.get("/api/scenarios")
async def scenario_api():
    return SCENARIOS


@app.get("/api/progress")
async def progress_api():
    return {"learner": learner(), "attempts": list_attempts(), "journal_count": len(list_journal(1000))}


@app.get("/health")
async def health():
    return {"status": "ok", "version": app.version}
