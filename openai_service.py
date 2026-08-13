from __future__ import annotations

import os
from typing import Any

from openai import OpenAI

DEFAULT_MODEL = os.getenv("OPENAI_MODEL", "gpt-5.5")
DEFAULT_INSTRUCTIONS = (
    "You are a helpful AI assistant. Be accurate, concise, and explicit when "
    "you are uncertain."
)


def _require_api_key() -> None:
    if not os.getenv("OPENAI_API_KEY"):
        raise RuntimeError(
            "OPENAI_API_KEY is not set. Store the API key in your environment; "
            "never commit it to source control."
        )


def generate_response(
    prompt: str,
    *,
    model: str | None = None,
    previous_response_id: str | None = None,
    client: Any | None = None,
) -> tuple[str, str]:
    cleaned_prompt = prompt.strip()
    if not cleaned_prompt:
        raise ValueError("Prompt must not be empty.")

    if client is None:
        _require_api_key()
        client = OpenAI()

    request: dict[str, Any] = {
        "model": model or DEFAULT_MODEL,
        "instructions": DEFAULT_INSTRUCTIONS,
        "input": cleaned_prompt,
    }

    if previous_response_id:
        request["previous_response_id"] = previous_response_id

    response = client.responses.create(**request)

    output_text = (response.output_text or "").strip()
    if not output_text:
        output_text = "[The API returned no text output.]"

    return output_text, response.id
