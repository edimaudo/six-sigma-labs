# Six Sigma Operations Lab — MVP v0.3

A FastAPI + Jinja2 applied Six Sigma learning prototype.

## Includes

- White, Yellow, Green and Black Belt learning paths
- Question-first lessons and teach-back/Socratic feedback
- Persistent learner, journal and attempt state in SQLite
- Branching scenario engine with stakeholder interviews, hidden incentives/clues, decision paths and DMAIC phase state
- Plotly.js scenario visualization
- IBM Carbon-inspired visual system
- Responsive layout
- WCAG-oriented focus states, semantic landmarks, labels, skip navigation, reduced-motion support, and accessible color contrast targets
- Small / Medium / Large type scale persisted in the browser; Medium is default
- Light / Dark theme toggle; uses the user's system preference when available and falls back to Dark
- Custom 404 page with the supplied copy

## Run

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Open `http://127.0.0.1:8000`.

## Scenario model

Scenario content is stored in `app/scenarios.py` so new simulations can be added independently from routing/UI code. The intended next step is to replace the deterministic stakeholder responses with model-backed adaptive dialogue while keeping the same state model.
