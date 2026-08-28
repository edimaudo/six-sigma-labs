# Six Sigma Operations Lab — MVP v1.0

Applied Six Sigma learning prototype built with FastAPI, Jinja2, Gemini, SQLite for local/demo persistence, and Plotly.js.

## Product architecture
- **Level check**: 16-question placement quiz across White, Yellow, Green, and Black Belt.
- **Learn**: gated until the placement quiz is completed.
- **Lessons**: every teaching section begins with a question, then concepts, glossary terms, math, teach-back, and reflection.
- **Case studies**: the primary applied-learning experience. Each case starts with an operations problem and uses Gemini-powered stakeholder agents with different incentives and partial information.
- **Glossary**: reusable Six Sigma/Lean reference definitions.
- **Math**: formulas and plain-language explanations for the underlying quantitative methods.
- **Journal**: reflection tied to learning activities.
- **Display**: responsive UI, dark/light mode, Small/Medium/Large text-and-interface scale.

## Curriculum coverage
The content model now includes the White Belt and Yellow Belt foundations plus the supplied Green Belt and Black Belt lesson lists, including:
- Green Belt: organizational context, Lean, DFSS, Define, Measure, Analyze, Improve, Control, and case studies.
- Black Belt: Define fundamentals, Six Sigma metrics, project selection and economics, Lean enterprise, Measure, Analyze, regression/DOE, and Control.

## Authentication status
Signup, sign-in, and sign-out UI/routes are intentionally disabled/commented for this phase. The prototype creates/uses a local learner record so the educational flows can be tested without account friction. Re-enable real accounts when durable production persistence is introduced.

## Vercel
- Root-level `main.py` is the ASGI entrypoint.
- `vercel.json` configures the Python runtime.
- SQLite uses `/tmp` on Vercel because the deployment filesystem is not durable/writable. Use managed Postgres before paid production.
- Required environment variables: `GEMINI_API_KEY`, optional `GEMINI_MODEL`, and `SSOL_SESSION_SECRET`.


## Learning content update
The DFSS curriculum explicitly covers **DMADV (also known as IDOV)** for new development, with glossary definitions for both terms.

- **Design language**: editorial, Economist-inspired visual system using serif headlines, restrained rules, paper/ink palette, and red accent; this is an original implementation rather than a copy of proprietary brand assets.


## v2.0 learning and design notes
- Belt level and Learn are separate routes and Learn is no longer gated by the assessment.
- Pricing UI and route are intentionally disabled for now.
- The interface uses an editorial, Economist-inspired layout with IBM blue as the accent; IBM Carbon styling is not used.
