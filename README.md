# Six Sigma Labs 

Six Sigma Labs is an applied socratic learning built around questions, case studies, stakeholder reasoning, teach-back and reflection

## Product structure

- **Belt level** — 10-question starting-level assessment.
- **Learn** — one integrated White, Yellow, Green, and Black Belt curriculum.
- **Case studies** — applied business challenges with DMAIC and DMADV / IDOV cases, stakeholder agents, organizational dynamics, and evidence-driven decisions.
- **Glossary** — searchable terms, references, and equations.
- **Journal** — learner reflection.

## Run locally

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload
```

## Gemini

Set `GEMINI_API_KEY` before using Gemini-powered activities. The application uses the Google `google-genai` SDK; there is no local AI fallback.

## Vercel

The repository is intentionally flat. `main.py` is the Vercel entrypoint and `vercel.json` routes requests to it.

Required environment variables:

```text
GEMINI_API_KEY=
GEMINI_MODEL=gemini-3.7-flash
SSOL_SESSION_SECRET=
SSOL_DB_PATH=
```
