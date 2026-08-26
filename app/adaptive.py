"""Local adaptive reasoning engine.

This is intentionally deterministic for the MVP: it evaluates question quality,
selects evidence relevant to the learner's question, tracks missed dimensions,
and generates a follow-up challenge. The interface is designed so an LLM provider
can replace the heuristic evaluator later without changing the scenario routes.
"""

import re

DIMENSION_KEYWORDS = {
    "baseline": ["baseline", "current", "today", "target", "actual", "historical", "benchmark", "cycle time"],
    "customer": ["customer", "client", "voice of customer", "voc", "experience", "expectation", "satisfaction"],
    "process": ["process", "handoff", "workflow", "step", "map", "queue", "touch time", "flow"],
    "rework": ["rework", "error", "missing", "defect", "redo", "repeat", "incomplete"],
    "queue": ["queue", "wait", "waiting", "delay", "handoff", "backlog", "aging"],
    "variation": ["variation", "segment", "distribution", "spread", "outlier", "special cause", "normal"],
    "control": ["control", "compliance", "risk", "audit", "policy", "regulatory", "control objective"],
    "incentive": ["incentive", "target", "bonus", "metric", "political", "stakeholder", "power", "resistance"],
    "data": ["data", "measure", "metric", "sample", "evidence", "analysis", "statistic", "calculate"],
}

CHALLENGES = {
    "baseline": "What would you use as the operational definition and baseline for that measure?",
    "customer": "How would you verify that this is the outcome the customer actually values?",
    "process": "Which process step or handoff would you examine, and what evidence would distinguish it from other steps?",
    "rework": "What evidence would separate rework from other causes of elapsed time?",
    "queue": "How would you prove that waiting time, rather than touch time, is driving the result?",
    "variation": "What segmentation would let you test whether different failure modes are being mixed together?",
    "control": "What control objective must remain true even if the process changes?",
    "incentive": "Whose metric or incentive could unintentionally reinforce the problem you are trying to solve?",
    "data": "What data would make your hypothesis falsifiable rather than just plausible?",
}


def normalize(text: str):
    return re.sub(r"\s+", " ", (text or "").strip().lower())


def detect_dimensions(text: str):
    value = normalize(text)
    found = []
    for dimension, keywords in DIMENSION_KEYWORDS.items():
        if any(keyword in value for keyword in keywords):
            found.append(dimension)
    return found


def score_question(question: str, phase: str, state=None):
    dims = detect_dimensions(question)
    score = min(100, 25 + len(dims) * 12)
    if len(question.split()) >= 8:
        score += 10
    if any(x in normalize(question) for x in ["why", "how", "what evidence", "how do we know"]):
        score += 10
    if state and phase in {"analyze", "improve", "control"} and "data" in dims:
        score += 5
    return min(score, 100), dims


def select_evidence(person: dict, question: str):
    dims = detect_dimensions(question)
    clues = person.get("clues", [])
    if not dims:
        return clues[:1], dims
    selected = []
    for clue in clues:
        clue_dims = detect_dimensions(clue)
        if set(dims) & set(clue_dims):
            selected.append(clue)
    return (selected or clues[:1])[:2], dims


def stakeholder_response(person: dict, question: str, state: dict, phase: str):
    score, dims = score_question(question, phase, state)
    evidence, _ = select_evidence(person, question)
    new_clues = [clue for clue in evidence if clue not in state.get("discovered_clues", [])]

    if not question.strip():
        reply = "That is a broad topic. Ask me about a specific measure, process step, customer outcome, incentive, or control."
        challenge = "What are you trying to rule in or rule out?"
    elif score < 45:
        reply = f"I can give you more, but your question is still broad. {person.get('opening', '')}"
        challenge = "What specific evidence would you need from me to test your hypothesis?"
    else:
        reply = person.get("opening", "")
        if evidence:
            reply += " " + " ".join(evidence)
        challenge = CHALLENGES[dims[0]] if dims else "What assumption are you making that you have not tested yet?"

    return {
        "reply": reply,
        "challenge": challenge,
        "score": score,
        "dimensions": dims,
        "new_clues": new_clues,
        "incentive": person.get("incentive", ""),
    }


def evaluate_reasoning(text: str, phase: str, state: dict, detail: dict):
    value = normalize(text)
    dims = detect_dimensions(value)
    score = min(100, 30 + len(dims) * 8)
    evidence = int(any(word in value for word in ["data", "evidence", "baseline", "measure", "sample", "trend"]))
    assumption = int(any(word in value for word in ["assume", "probably", "obviously", "must be", "clearly"]))
    stakeholder = int(any(s.lower().split()[0] in value for s in detail["stakeholders"]))
    if len(value.split()) > 25:
        score += 10
    if phase == "define" and "baseline" in dims:
        score += 8
    if phase == "measure" and "data" in dims:
        score += 8
    if phase == "analyze" and any(d in dims for d in ["variation", "rework", "queue"]):
        score += 8
    if phase in {"improve", "control"} and "control" in dims:
        score += 8
    score = max(0, min(100, score - assumption * 8))
    missing = []
    if "customer" not in dims:
        missing.append("customer perspective")
    if "incentive" not in dims:
        missing.append("stakeholder incentives")
    if evidence == 0:
        missing.append("evidence or baseline")
    return {
        "score": score,
        "dimensions": dims,
        "evidence": evidence,
        "assumption": assumption,
        "missing": missing[:3],
        "feedback": (
            f"Your reasoning is strongest where it connects the {phase} problem to observable evidence. "
            + (f"Next, test {missing[0]}." if missing else "You are covering the main operational dimensions; now make the next test explicit.")
        ),
        "next_question": CHALLENGES[dims[0]] if dims else "What evidence would change your mind?",
    }
