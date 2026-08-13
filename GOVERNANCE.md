# Repository Governance & Release Reliability

This document defines the repository-level governance contract for `AmirMotefaker/Create-your-own-ChatGPT`.

## Default branch

The default branch is protected by the active repository ruleset **Phase 7 - Main Governance**.

Changes to the default branch must:

- arrive through a Pull Request,
- use squash merge,
- pass the repository's required status checks,
- preserve linear history,
- resolve review conversations before merge,
- avoid force-pushes,
- and never delete the default branch.

For this personal repository, the ruleset intentionally requires **zero approving reviews**. This prevents direct pushes while avoiding a deadlock where the sole maintainer cannot approve their own Pull Request.

## Required checks

- `validate (Python 3.10)`
- `validate (Python 3.12)`
- `Analyze (python)`
- `CodeQL`

The names above are GitHub check contexts observed from successful repository runs, not guessed workflow names.

## Merge policy

Repository merge settings are standardized to:

- squash merge: enabled,
- merge commits: disabled,
- rebase merge: disabled,
- auto-merge capability: enabled,
- head branch deletion after merge: enabled,
- Update branch capability: enabled,
- squash commit title: Pull Request title,
- squash commit message: Pull Request body.

Auto-merge capability being enabled does **not** mean Dependabot is automatically merged. Dependency updates remain subject to the same required checks and maintainer decision.

## Dependency updates

Dependabot version and security updates must flow through Pull Requests and the required status checks.

Phase 7 does not enable unconditional Dependabot auto-merge.

## Release tags

The active repository ruleset **Phase 7 - Immutable Tags** allows creation of new tags but blocks update and deletion of existing tags.

If an erroneous release tag must ever be corrected, the maintainer must explicitly change or disable that ruleset first. Silent tag rewriting is not part of the release process.

## Artifact provenance

This repository does not currently publish a deterministic binary/package artifact as its supported release output, so Phase 7 does not create artificial attestations for source-only or notebook content.

If a future release pipeline produces distributable artifacts, provenance should be added at the build boundary.

## Release lifecycle

Meaningful releases should remain auditable:

Issue -> branch/commit -> Pull Request -> checks/evidence -> merge -> exact-SHA annotated tag -> GitHub Release.

## Issue retention

Issues are not automatically closed solely because they are old. Stale automation can hide useful historical context and is not enabled by this governance policy.

## Emergency changes

If repository governance must be temporarily relaxed for recovery:

1. document why,
2. change only the minimum required rule,
3. restore the governance contract immediately after recovery,
4. record the recovery in GitHub evidence.

License decisions remain outside this governance phase.
