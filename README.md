# Six Sigma Operations Lab

A lean FastAPI MVP for an applied Six Sigma course built around question-first teaching, Socratic teach-back, simulated operations scenarios, reflection, and a consulting workspace.

## Stack
- FastAPI + Jinja2
- IBM Carbon-inspired visual language and tokens
- Plotly.js for interactive visualization
- Structured Python content model for White, Yellow, Green, and Black Belt learning paths

## Run
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Open http://127.0.0.1:8000

## Current MVP
- Landing page
- Six Sigma diagnostic quiz covering White → Black Belt
- White, Yellow, Green, Black Belt curriculum pages
- Every lesson starts with a question and ends with a teach-back prompt
- Scenario workspace with stakeholder list and Plotly chart
- Reflection journal (in-memory for prototype)
- Consulting workspace
- Health endpoint and scenario API

## Next build layers
- Auth + paid course access
- Persistent database
- AI Socratic tutor
- Scenario generation with structured rubrics
- Adaptive diagnostics
- Real data analysis workspace
- Learner progress and certification evidence
