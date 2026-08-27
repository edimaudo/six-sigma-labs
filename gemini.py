"""Gemini-backed adaptive learning provider.

Uses Google's current GenAI Python SDK and the Gemini Interactions API.
The API key is read from GEMINI_API_KEY and is never stored in the database.
"""

import json
import os
from typing import Any

from google import genai

MODEL = os.getenv("GEMINI_MODEL", "gemini-3.7-flash")

class GeminiConfigError(RuntimeError):
    pass

class GeminiResponseError(RuntimeError):
    pass


def _client():
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise GeminiConfigError("GEMINI_API_KEY is not configured.")
    return genai.Client(api_key=api_key)


def _json_schema(kind: str):
    if kind == "stakeholder":
        return {
            "type": "object",
            "properties": {
                "reply": {"type": "string"},
                "challenge": {"type": "string"},
                "score": {"type": "integer"},
                "dimensions": {"type": "array", "items": {"type": "string"}},
                "new_clues": {"type": "array", "items": {"type": "integer"}},
                "incentive_signal": {"type": "string"},
            },
            "required": ["reply", "challenge", "score", "dimensions", "new_clues", "incentive_signal"],
        }
    return {
        "type": "object",
        "properties": {
            "score": {"type": "integer"},
            "feedback": {"type": "string"},
            "next_question": {"type": "string"},
            "missing": {"type": "array", "items": {"type": "string"}},
            "dimensions": {"type": "array", "items": {"type": "string"}},
            "evidence": {"type": "integer"},
            "assumption": {"type": "integer"},
        },
        "required": ["score", "feedback", "next_question", "missing", "dimensions", "evidence", "assumption"],
    }


def _call(prompt: str, kind: str, previous_interaction_id: str | None = None):
    client = _client()
    kwargs: dict[str, Any] = {
        "model": MODEL,
        "input": prompt,
        "response_format": {
            "type": "text",
            "mime_type": "application/json",
            "schema": _json_schema(kind),
        },
    }
    if previous_interaction_id:
        kwargs["previous_interaction_id"] = previous_interaction_id
    try:
        interaction = client.interactions.create(**kwargs)
        payload = json.loads(interaction.output_text)
        return payload, interaction.id
    except Exception as exc:
        raise GeminiResponseError(f"Gemini request failed: {exc}") from exc


def stakeholder_response(person: dict, question: str, state: dict, phase: str, previous_interaction_id: str | None = None):
    clues = person.get("clues", [])
    conversation = state.get("conversation", [])[-8:]
    prompt = f"""
You are the adaptive stakeholder in a Six Sigma operations simulation.
Your job is to respond like the stakeholder below, not like a tutor.

Scenario phase: {phase}
Stakeholder role: {person.get('role','')}
Stakeholder opening context: {person.get('opening','')}
Stakeholder incentive: {person.get('incentive','')}

Hidden evidence available to this stakeholder (the learner may only receive evidence you choose to reveal):
{json.dumps(clues, ensure_ascii=False)}

Recent investigation record:
{json.dumps(conversation, ensure_ascii=False)}

Learner question:
{question or '[No specific question]'}

Decision lenses when relevant:
- Logos: evidence and causal reasoning
- Pathos: human experience, trust, frustration, workload, consequences
- Ethos: responsibility, credibility, controls, fairness
- Economic: cost, capacity, value, opportunity cost
- Political: power, incentives, commitments, reputation
- Social: norms, team dynamics, status, trust, adoption

Rules:
1. Stay in character.
2. Do not reveal every clue just because it exists.
3. Reveal only clue indices directly relevant to the learner's question, and at most 2.
4. Never invent operational facts that are not in the scenario context or supplied evidence.
5. Reward specific, evidence-seeking questions. Broad questions should receive limited information and a probing challenge.
6. Account for organizational incentives, power, resistance, and competing objectives when relevant.
7. The score is the quality of the learner's question (0-100), not the quality of the learner as a person.
8. dimensions should name the concepts the question genuinely touches, such as baseline, customer, process, rework, queue, variation, control, incentive, or data.
9. challenge should be a Socratic follow-up question, not an answer.
10. Keep the response concise and realistic.
"""
    payload, interaction_id = _call(prompt, "stakeholder", previous_interaction_id)
    valid_indices = []
    for item in payload.get("new_clues", []):
        try:
            idx = int(item)
        except (TypeError, ValueError):
            continue
        if 0 <= idx < len(clues) and idx not in valid_indices:
            valid_indices.append(idx)
    payload["new_clue_indices"] = valid_indices[:2]
    payload["new_clues"] = [clues[idx] for idx in valid_indices[:2]]
    payload["score"] = max(0, min(100, int(payload.get("score", 0))))
    return payload, interaction_id


def evaluate_reasoning(text: str, phase: str, state: dict, detail: dict, previous_interaction_id: str | None = None):
    prompt = f"""
You are a senior Six Sigma instructor evaluating a learner's reasoning inside an operations simulation.
Use the learner's response and the scenario context below.

Current DMAIC phase: {phase}
Scenario: {detail.get('title','')}
Known stakeholders: {list(detail.get('stakeholders', {}).keys())}
Learner reasoning:
{text}

Scenario state:
{json.dumps({
    'visited_stakeholders': state.get('visited_stakeholders', []),
    'discovered_clues': state.get('discovered_clues', []),
    'decisions': state.get('decisions', []),
    'evidence_score': state.get('evidence_score', 0),
    'stakeholder_score': state.get('stakeholder_score', 0),
}, ensure_ascii=False)}

Rules:
1. Assess operational reasoning, not writing style.
2. Reward falsifiable hypotheses, baseline thinking, customer perspective, process thinking, data/evidence, variation, stakeholder incentives and appropriate DMAIC logic.
3. Identify unsupported assumptions.
4. Do not invent facts that are absent from the scenario.
5. Ask one strong Socratic next question that forces the learner to examine evidence, perspective, or consequences rather than supplying the answer.
6. Score 0-100.
7. evidence and assumption are 0 or 1 indicators.
8. missing should contain up to 3 important dimensions the learner has not addressed.
9. Keep feedback specific and concise.
"""
    payload, interaction_id = _call(prompt, "reasoning", previous_interaction_id)
    payload["score"] = max(0, min(100, int(payload.get("score", 0))))
    payload["evidence"] = 1 if payload.get("evidence") else 0
    payload["assumption"] = 1 if payload.get("assumption") else 0
    payload["missing"] = list(payload.get("missing") or [])[:3]
    return payload, interaction_id


def _teach_back_schema():
    return {
        "type": "object",
        "properties": {
            "score": {"type": "integer"},
            "feedback": {"type": "string"},
            "next_question": {"type": "string"},
        },
        "required": ["score", "feedback", "next_question"],
    }


def evaluate_teach_back(response: str, focus: str):
    client = _client()
    prompt = f"""
You are a demanding but constructive Six Sigma instructor using the Socratic method.
Evaluate a learner's teach-back response. Do not rewrite the response for them and do not simply give the textbook definition.

Focus: {focus}
Learner response:
{response}

Evaluate whether the learner demonstrates conceptual accuracy, operational understanding, and ability to apply the idea.
Return a score from 0-100, concise feedback identifying the strongest and weakest part, and one Socratic follow-up question that makes the learner defend or apply the concept.
"""
    try:
        interaction = client.interactions.create(
            model=MODEL,
            input=prompt,
            response_format={
                "type": "text",
                "mime_type": "application/json",
                "schema": _teach_back_schema(),
            },
        )
        return json.loads(interaction.output_text), interaction.id
    except Exception as exc:
        raise GeminiResponseError(f"Gemini request failed: {exc}") from exc
