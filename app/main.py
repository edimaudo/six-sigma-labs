from pathlib import Path
from typing import Annotated

from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from .content import BELTS, DIAGNOSTIC, SCENARIOS

BASE_DIR = Path(__file__).resolve().parent.parent
app = FastAPI(title="Six Sigma Operations Lab", version="0.1.0")
app.mount("/static", StaticFiles(directory=BASE_DIR / "static"), name="static")
templates = Jinja2Templates(directory=BASE_DIR / "templates")

JOURNAL = []


def context(request: Request, **kwargs):
    return {"request": request, "belts": BELTS, **kwargs}


@app.get("/", response_class=HTMLResponse)
async def landing(request: Request):
    return templates.TemplateResponse(request=request, name="landing.html", context=context(request))


@app.get("/diagnostic", response_class=HTMLResponse)
async def diagnostic(request: Request):
    return templates.TemplateResponse(request=request, name="diagnostic.html", context=context(request, questions=DIAGNOSTIC))


@app.post("/diagnostic", response_class=HTMLResponse)
async def diagnostic_submit(request: Request, answers: Annotated[list[str] | None, Form()] = None):
    values = answers or []
    score = sum(1 for idx, q in enumerate(DIAGNOSTIC) if idx < len(values) and values[idx] == str(q["answer"]))
    if score <= 2:
        belt = "white"
    elif score <= 4:
        belt = "yellow"
    elif score <= 6:
        belt = "green"
    else:
        belt = "black"
    return templates.TemplateResponse(request=request, name="diagnostic_result.html", context=context(request, score=score, max_score=len(DIAGNOSTIC), belt=BELTS[belt]))


@app.get("/learn", response_class=HTMLResponse)
async def learn(request: Request):
    return templates.TemplateResponse(request=request, name="learn_index.html", context=context(request))


@app.get("/learn/{belt}", response_class=HTMLResponse)
async def belt_page(request: Request, belt: str):
    belt_key = belt.lower()
    if belt_key not in BELTS:
        return RedirectResponse("/learn", status_code=303)
    return templates.TemplateResponse(request=request, name="belt.html", context=context(request, belt=BELTS[belt_key], belt_key=belt_key))


@app.get("/scenario", response_class=HTMLResponse)
async def scenarios(request: Request, id: str | None = None):
    scenario = next((s for s in SCENARIOS if s["id"] == id), SCENARIOS[0])
    return templates.TemplateResponse(request=request, name="scenario.html", context=context(request, scenario=scenario))


@app.post("/journal")
async def journal_submit(request: Request, reflection: Annotated[str, Form()]):
    JOURNAL.append(reflection.strip())
    return RedirectResponse("/journal", status_code=303)


@app.get("/journal", response_class=HTMLResponse)
async def journal(request: Request):
    return templates.TemplateResponse(request=request, name="journal.html", context=context(request, entries=JOURNAL[-10:][::-1]))


@app.get("/consult", response_class=HTMLResponse)
async def consult(request: Request):
    return templates.TemplateResponse(request=request, name="consult.html", context=context(request))


@app.get("/api/scenarios")
async def scenario_api():
    return SCENARIOS


@app.get("/health")
async def health():
    return {"status": "ok"}
