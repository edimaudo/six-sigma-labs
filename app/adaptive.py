"""Compatibility layer for the Gemini-backed adaptive engine."""
from .gemini import (
    GeminiConfigError,
    GeminiResponseError,
    evaluate_reasoning,
    evaluate_teach_back,
    stakeholder_response,
)

__all__ = [
    "GeminiConfigError",
    "GeminiResponseError",
    "evaluate_reasoning",
    "evaluate_teach_back",
    "stakeholder_response",
]
