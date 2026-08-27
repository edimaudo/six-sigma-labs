# Six Sigma Operations Lab MVP v0.4

FastAPI + Jinja2 + SQLite + Plotly.js + Google Gemini prototype for an applied Six Sigma learning product.

## Product model

The application is built around:

**Question → Investigate → Apply → Teach → Reflect**

The scenario engine treats the organization as part of the process. Learners investigate simulated stakeholders with different incentives, ask questions to reveal evidence, make decisions, and receive Socratic challenges.

## Included in v0.4

- White, Yellow, Green and Black Belt curriculum structure
- Question-first lessons and teach-back
- Adaptive stakeholder dialogue using Google Gemini Interactions API
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

AI behavior is provided by Google Gemini through the official `google-genai` SDK and Gemini Interactions API. Stakeholder conversations, scenario reasoning evaluation, and teach-back feedback are not implemented with a local heuristic AI fallback.

Pricing is presentation-only in this build; no payment provider is connected.

## Gemini configuration

Set `GEMINI_API_KEY` in your local environment or Vercel project settings. `GEMINI_MODEL` defaults to `gemini-3.7-flash`. Google documents the Interactions API as the current default interface for new Gemini applications and supports chaining turns with `previous_interaction_id`.

## Vercel

The repository includes `vercel.json` for the FastAPI Python runtime. Add `GEMINI_API_KEY` and `SSOL_SESSION_SECRET` under Vercel Project Settings → Environment Variables before deployment.

**Persistence note:** the current prototype still uses SQLite. Vercel's serverless runtime should not be treated as durable storage, so production deployment should move user/scenario state to a hosted database such as Postgres.


## Production readiness notes

- `SSOL_DEMO_MODE` defaults to `false`; enable it explicitly only for a controlled demo environment.
- SQLite is suitable for local development only. Vercel serverless instances do not provide durable local filesystem persistence. Use a managed Postgres database for production learner accounts, journals, attempts, and scenario state.
- Keep `GEMINI_API_KEY` and `SSOL_SESSION_SECRET` in Vercel Environment Variables; do not commit them.
- The Gemini Interactions API is intentionally used for adaptive dialogue and structured evaluation.

## Vercel troubleshooting

The app uses Starlette `SessionMiddleware`, which requires the `itsdangerous` package. It is declared explicitly in `requirements.txt`. The deployment entrypoint is the root `main.py`, which imports `app.main:app`. Vercel installs Python dependencies declared in `requirements.txt` during the build.
