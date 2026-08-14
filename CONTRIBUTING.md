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
<!-- phase9-contributing-start -->
## Community channels

Choose the smallest channel that fits the work:

- **Discussions / Q&A** — how-to questions, usage help, design questions, learning conversations, and answers that may help other users.
- **Discussions / Ideas** — early ideas that are not yet scoped enough to become implementation work.
- **Issues** — reproducible bugs and feature requests with a concrete scope.
- **Pull requests** — focused implementation or documentation work tied to a real repository need.
- **Private vulnerability reporting** — security vulnerabilities or sensitive security details.

Repository Discussions: https://github.com/AmirMotefaker/Create-your-own-ChatGPT/discussions

### Contributor-friendly work

The repository uses GitHub's standard `good first issue` and `help wanted` labels. Maintainers should apply them only to real, bounded tasks with enough context for another contributor to finish the work.

Do not open empty, duplicate, or no-op pull requests to create activity.

### Co-authorship

Use Git's `Co-authored-by:` trailer only when another human materially contributed to the same change. Do not add fabricated or nominal coauthors. Genuine pair work is welcome and should preserve accurate attribution.

### Discussion answers

In Q&A discussions, the discussion author or a maintainer can mark the response that actually resolves the question as the answer. Never manufacture questions or accepted answers for profile metrics.
<!-- phase9-contributing-end -->
