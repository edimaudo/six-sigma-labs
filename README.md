# Six Sigma Labs v2.2

Six Sigma Labs is an applied Six Sigma learning prototype built around questions, case studies, stakeholder reasoning, teach-back, reflection, and Gemini-powered feedback.

## Product structure

- **Belt level** — 10-question starting-level assessment.
- **Learn** — one integrated White, Yellow, Green, and Black Belt curriculum.
- **Case studies** — applied business challenges with DMAIC and DMADV / IDOV cases, stakeholder agents, organizational dynamics, and evidence-driven decisions.
- **Glossary** — searchable terms, references, and equations.
- **Journal** — learner reflection.

## Design system

The UI uses an editorial publication-inspired design system with serif-led typography, restrained rules, flat content rows, larger navigation, and IBM blue as the action/accent colour. It does not use IBM Carbon components or IBM Plex typography.

## Accessibility

The application targets WCAG 2.1 AA patterns across the rendered templates, including:

- semantic landmarks and one primary H1 per page
- skip navigation
- explicit form labels and fieldset legends
- visible keyboard focus indicators
- high-contrast text/link variants
- responsive layouts
- reduced-motion support
- persistent Small / Medium / Large type scaling
- persistent light/dark theme with system preference fallback
- descriptive chart text alternatives

A full WCAG conformance claim still requires a manual audit and assistive-technology testing against the deployed build.

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

SQLite is only suitable for the prototype. On Vercel the runtime database is stored in `/tmp` and is ephemeral. Use managed Postgres for durable learner data before production use.
