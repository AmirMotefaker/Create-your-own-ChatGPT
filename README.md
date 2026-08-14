# Create Your Own ChatGPT with Python

[![GitHub stars](https://img.shields.io/github/stars/AmirMotefaker/Create-your-own-ChatGPT?style=flat&logo=github)](https://github.com/AmirMotefaker/Create-your-own-ChatGPT/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/AmirMotefaker/Create-your-own-ChatGPT?style=flat&logo=github)](https://github.com/AmirMotefaker/Create-your-own-ChatGPT/network/members)
[![Python modernization](https://github.com/AmirMotefaker/Create-your-own-ChatGPT/actions/workflows/python-modernization.yml/badge.svg)](https://github.com/AmirMotefaker/Create-your-own-ChatGPT/actions/workflows/python-modernization.yml)

A modern OpenAI Responses API CLI plus the original historical Jupyter notebooks that documented the project's early ChatGPT experiments.

## Modern 2026 path

The supported entrypoint is [`chat.py`](chat.py), backed by [`openai_service.py`](openai_service.py).

It uses:

- the official OpenAI Python SDK
- `client.responses.create(...)`
- `response.output_text`
- `OPENAI_API_KEY` from the environment
- `previous_response_id` for multi-turn conversation state
- `gpt-5.5` as the default model, overridable with `OPENAI_MODEL` or `--model`

### Setup

```bash
git clone https://github.com/AmirMotefaker/Create-your-own-ChatGPT.git
cd Create-your-own-ChatGPT
python -m venv .venv
```

Activate the environment:

```powershell
# Windows PowerShell
.venv\Scripts\Activate.ps1
```

```bash
# macOS / Linux
source .venv/bin/activate
```

Install dependencies:

```bash
python -m pip install -r requirements.txt
```

Set your API key locally — never commit it:

```powershell
$env:OPENAI_API_KEY = "your-key-here"
```

or:

```bash
export OPENAI_API_KEY="your-key-here"
```

Run one prompt:

```bash
python chat.py "Explain the Responses API in three bullets."
```

Or start an interactive multi-turn session:

```bash
python chat.py
```

Use another model when available to your account:

```bash
python chat.py --model gpt-5.5
```

## Historical notebooks

The original notebooks are intentionally preserved as an educational archive:

| File | Purpose |
| --- | --- |
| [`Create_your_own_ChatGPT_with_Python.ipynb`](Create_your_own_ChatGPT_with_Python.ipynb) | Lightweight historical Python/Jupyter walkthrough |
| [`Create your own ChatGPT.ipynb`](Create%20your%20own%20ChatGPT.ipynb) | Expanded historical notebook with background material and examples |

> [!IMPORTANT]
> The notebooks were created around the 2023-era OpenAI API ecosystem and can contain deprecated API patterns or model names. Use `chat.py` for the modern path.

## Validation

The repository includes offline unit tests and GitHub Actions validation:

```bash
python -m unittest discover -s tests -v
python -m compileall -q .
```

The CI workflow installs dependencies on Python 3.10 and 3.12, compiles the project, runs offline service tests, checks for accidental API-key patterns, and prevents legacy OpenAI calls from returning to the modern entrypoints.

## Security

- Keep `OPENAI_API_KEY` in your local environment or secret manager.
- `.env`, virtual environments, Python caches, and Streamlit secrets are ignored.
- No live paid API request is required by CI.

## Support the project

If the modern example or historical notebooks help you, consider giving the repository a ⭐.

## Author

**Amir Motefaker** — [GitHub](https://github.com/AmirMotefaker) · [Website](https://amirmotefaker.ir)
<!-- phase9-community-start -->
## Community and contributing

- Use [GitHub Discussions](https://github.com/AmirMotefaker/Create-your-own-ChatGPT/discussions) for how-to questions, learning conversations, and technical Q&A.
- Put answerable questions in the **Q&A** category so a useful reply can be marked as the answer.
- Use [Issues](https://github.com/AmirMotefaker/Create-your-own-ChatGPT/issues) for reproducible bugs or scoped feature work.
- Read [CONTRIBUTING.md](CONTRIBUTING.md) before sending code or documentation changes.
- Report security vulnerabilities through the private path described in [SECURITY.md](SECURITY.md), not in a public thread.

Small, useful contributions are welcome. `good first issue` and `help wanted` are reserved for real, deliverable contributor tasks rather than activity created for metrics.
<!-- phase9-community-end -->
