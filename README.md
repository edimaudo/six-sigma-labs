# Six Sigma Operations Lab MVP v0.4

FastAPI + Jinja2 + SQLite + Plotly.js prototype for an applied Six Sigma learning product.

## Product model

The application is built around:

**Question → Investigate → Apply → Teach → Reflect**

The scenario engine treats the organization as part of the process. Learners investigate simulated stakeholders with different incentives, ask questions to reveal evidence, make decisions, and receive Socratic challenges.

## Included in v0.4

- White, Yellow, Green and Black Belt curriculum structure
- Question-first lessons and teach-back
- Adaptive stakeholder dialogue using a local reasoning engine
- Evidence discovery based on the learner's question
- Scenario reasoning, evidence and stakeholder scores
- Persistent SQLite learner state
- Signup/signin using PBKDF2-SHA256 password hashing
- Pricing page and pricing section on landing page
- Responsive IBM Carbon-inspired visual language
- Dark/light mode; defaults to the user's system preference, otherwise dark
- Small / Medium / Large interface scaling (90% / 100% / 115%); Medium is default
- Keyboard focus states, skip navigation, semantic landmarks and reduced-motion support
- Custom 404 page
- Plotly.js scenario visualization

## Run locally

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
export SSOL_SESSION_SECRET='replace-with-a-long-random-secret'
uvicorn app.main:app --reload
```

Open `http://127.0.0.1:8000`.

The built-in demo user is `demo@sixsigma.local`. Its default password is `demo-only`; override it at first database initialization with `SSOL_DEMO_PASSWORD`.

## Notes

The adaptive engine is deterministic in this MVP. It is structured as a replaceable reasoning provider so an LLM-backed evaluator can be added later without changing the scenario UI or persistence model.

Pricing is presentation-only in this build; no payment provider is connected.
