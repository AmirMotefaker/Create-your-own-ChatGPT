# Phase 6 - GitHub Repository Trust & Security Hardening Evidence

Generated: **2026-08-13T22:36:04Z**

Repository: `AmirMotefaker/Create-your-own-ChatGPT`

## Community health baseline

- Before Phase 6: **28%**
- Final community-health percentage is verified after merge and recorded in the GitHub Release.

## Repository security settings

| Control | Before | After |
| --- | --- | --- |
| GitHub Actions enabled | True | True |
| Require full-SHA action pinning | False | True |
| Default workflow permissions | `read` | `read` |
| Actions can approve PRs | False | False |
| Private vulnerability reporting | False | True |
| Vulnerability alerts | False | True |
| Dependabot security updates | True | True |

## Immutable GitHub Action pins

- `actions/checkout@d23441a48e516b6c34aea4fa41551a30e30af803` — v6
- `actions/setup-python@ece7cb06caefa5fff74198d8649806c4678c61a1` — v6, where used
- `actions/setup-node@249970729cb0ef3589644e2896645e5dc5ba9c38` — v6, where used
- `actions/upload-artifact@ea165f8d65b6e75b540449e92b4886f43607fa02` — v4, where used
- `github/codeql-action@ff2f1c621b7f889edc0d3c761ac2e6a3f8cdb0dd` — v4, where used

The publisher verified each SHA against the official GitHub-owned action repository before generating the branch.

## Community and trust files

- `SECURITY.md`
- `CONTRIBUTING.md`
- `CODE_OF_CONDUCT.md`
- `.github/CODEOWNERS`
- `.github/PULL_REQUEST_TEMPLATE.md`
- `.github/ISSUE_TEMPLATE/bug_report.yml`
- `.github/ISSUE_TEMPLATE/feature_request.yml`
- `.github/ISSUE_TEMPLATE/config.yml`
- `.github/dependabot.yml`

## License integrity

No license file present before or after Phase 6 generation.

Phase 6 intentionally does not choose or modify a software license.

## CodeQL setup compatibility

- Before: `not-configured`
- After: `not-configured; advanced workflow planned`

Default setup is disabled only when needed so the repository does not run conflicting default and advanced CodeQL configurations.

## Security automation

- Full-SHA workflow policy enabled.
- Read-only default `GITHUB_TOKEN`.
- Actions cannot approve PRs.
- Private vulnerability reporting enabled.
- Vulnerability alerts enabled.
- Dependabot security updates enabled.
- Dependabot version updates configured.
- CodeQL added only when technically appropriate for supported source code.
- Existing repository validation workflow hardened or a repository validation workflow added.

## Lifecycle

- Issue: #7
- Branch: `agent/trust-security-hardening-2026-v1`
- Target tag: `trust-security-v2026.08.14`

No secrets, private vulnerability data, security-alert contents, or private repository data are stored in this evidence.
