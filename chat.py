from __future__ import annotations

import argparse

from openai_service import DEFAULT_MODEL, generate_response


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Modern OpenAI Responses API example."
    )
    parser.add_argument(
        "prompt",
        nargs="*",
        help="Prompt to send. Omit it to start an interactive multi-turn session.",
    )
    parser.add_argument(
        "--model",
        default=DEFAULT_MODEL,
        help=f"OpenAI model ID (default: {DEFAULT_MODEL}; OPENAI_MODEL can override).",
    )
    return parser


def run_single(prompt: str, model: str) -> None:
    text, _ = generate_response(prompt, model=model)
    print(text)


def run_interactive(model: str) -> None:
    previous_response_id: str | None = None

    print(f"Interactive Responses API session — model: {model}")
    print("Type exit or quit to stop.")

    while True:
        try:
            prompt = input("\nYou: ").strip()
        except (EOFError, KeyboardInterrupt):
            print()
            return

        if prompt.lower() in {"exit", "quit"}:
            return

        if not prompt:
            continue

        text, previous_response_id = generate_response(
            prompt,
            model=model,
            previous_response_id=previous_response_id,
        )
        print(f"\nAssistant: {text}")


def main() -> None:
    args = build_parser()
    prompt = " ".join(args.prompt).strip()

    if prompt:
        run_single(prompt, args.model)
    else:
        run_interactive(args.model)


if __name__ == "__main__":
    main()
