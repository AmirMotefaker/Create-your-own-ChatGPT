# Contributing

Thanks for helping improve this repository.

## Before you start

- Search existing issues before opening a new one.
- Use the issue templates for bugs and feature requests.
- For security vulnerabilities, follow `SECURITY.md` and use private vulnerability reporting instead of a public issue.
- Keep changes focused. Avoid unrelated formatting or generated-file churn.
- Never commit secrets or personal/private data.

## Development workflow

1. Fork or create a feature branch.
2. Make the smallest coherent change.
3. Run the repository validation steps.
4. Update documentation and tests when behavior changes.
5. Open a pull request using the repository PR template.

## Validation

```bash
python -m pip install -r requirements.txt
python -m compileall -q .
python -m unittest discover -s tests -v
```

## Pull requests

A good pull request explains:

- what changed,
- why it changed,
- how it was tested,
- security or compatibility implications,
- and any follow-up work.

The repository uses GitHub Actions as an automated validation gate.

## License note

Contributing does not change the repository's existing licensing status. Do not add, replace, or reinterpret a license as part of an unrelated pull request without an explicit maintainer decision.

Repository: `AmirMotefaker/Create-your-own-ChatGPT`
