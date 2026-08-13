# Phase 7 - Repository Governance & Release Reliability Evidence

Generated: **2026-08-13T23:30:06Z**

Repository: `AmirMotefaker/Create-your-own-ChatGPT`

## Baseline

- Repository rulesets before Phase 7: **0**
- Squash merge before: **True**
- Merge commits before: **True**
- Rebase merge before: **True**
- Auto-delete branch before: **False**

## Required check contexts

- `validate (Python 3.10)`
- `validate (Python 3.12)`
- `Analyze (python)`
- `CodeQL`

These check names come from successful GitHub check runs observed before Phase 7.

## Target governance

- Pull Request required for default-branch changes.
- Zero mandatory approvals for a personal repository.
- Review threads must be resolved.
- Required checks must pass.
- Squash merge only.
- Linear history.
- Force-push blocked.
- Default-branch deletion blocked.
- Existing tags protected from update/deletion.
- Dependabot remains behind Pull Request + CI gates.
- No unconditional Dependabot auto-merge.

## Release provenance

No attestation workflow is added because the repository does not currently produce a deterministic distributable artifact.

## Lifecycle

- Issue: #12
- Branch: `agent/governance-release-reliability-2026-v1`
- Target tag: `governance-v2026.08.14`

Repository-level settings and ruleset IDs are applied after this PR's checks pass and are recorded in the final GitHub Release and completed Issue.

No secret values, private security findings, license changes, or product behavior changes are included in this evidence.
