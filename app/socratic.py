"""Lightweight, deterministic Socratic feedback engine for the MVP.

This deliberately does not require an external model/API. It identifies a few
common reasoning patterns and responds with progressively deeper questions.
"""

KEYWORDS = {
    "problem": ["problem", "gap", "outcome", "baseline"],
    "customer": ["customer", "voc", "requirement", "ctq"],
    "data": ["data", "measure", "metric", "baseline", "sample"],
    "cause": ["cause", "root cause", "driver", "factor", "why"],
    "stakeholder": ["stakeholder", "manager", "employee", "compliance", "finance"],
    "variation": ["variation", "distribution", "spread", "sigma", "control chart"],
    "evidence": ["evidence", "test", "validate", "compare", "experiment"],
}


def evaluate(response: str, focus: str = "general") -> dict:
    text = (response or "").strip().lower()
    if len(text) < 25:
        return {
            "score": 1,
            "label": "Start with your reasoning",
            "feedback": "Your answer is too brief to evaluate. State what you would do, what evidence you need, and why.",
            "next_question": "What assumption are you making right now, and how would you test it?",
        }

    matched = [concept for concept, words in KEYWORDS.items() if any(w in text for w in words)]
    score = min(5, 1 + len(matched))

    if focus in {"define", "problem"} and "problem" not in matched:
        next_q = "What exactly is the performance gap, and compared with what baseline?"
    elif focus in {"measure", "data"} and "data" not in matched:
        next_q = "What data would you collect, and how would you define the measure consistently?"
    elif focus in {"analyze", "cause"} and "cause" not in matched:
        next_q = "What evidence would distinguish a plausible cause from a demonstrated cause?"
    elif focus in {"improve", "stakeholder"} and "stakeholder" not in matched:
        next_q = "Who is affected by the proposed change, and what incentive might make adoption difficult?"
    else:
        next_q = "What would change your mind about your current conclusion?"

    if score >= 4:
        label = "Strong reasoning"
        feedback = "You are connecting the method to evidence and the operating context. Push one step further by stating how you would validate the conclusion."
    elif score >= 3:
        label = "Good direction"
        feedback = "You have some of the right concepts. The next step is to make the logic explicit: claim → evidence → decision."
    else:
        label = "Developing"
        feedback = "You have started the analysis, but the reasoning needs a clearer operational definition and evidence path."

    return {"score": score, "label": label, "feedback": feedback, "next_question": next_q, "matched": matched}
