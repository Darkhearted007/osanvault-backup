# ÒsánVault Africa — Security Baseline

## Status

**Discovery baseline only.** This document records risks requiring remediation or verification. It does not claim that the current system is secure.

## Findings

### S1 — Environment secret handling

`.gitignore` excludes `.env` and `.vps_pass.enc`, which is useful, but ignore rules do not prove that secrets have never been committed. A repository-history secret scan is required before production certification.

### S2 — Committed runtime binary

`ai/ngrok` is a large committed binary. Runtime binaries should not be stored in the canonical source workspace unless their provenance, version, integrity, licensing, and execution purpose are documented. Prefer an external release/package mechanism where appropriate.

### S3 — Workflow write-back permissions

The deployment workflows commit generated content and push to `main`. This creates a privileged write path from scheduled automation into the production branch. The workflow should eventually use least-privilege `GITHUB_TOKEN` permissions, protected branches, and a controlled generated-artifact strategy.

### S4 — Workflow version pinning

Actions currently reference major tags such as `actions/checkout@v3`, `actions/setup-python@v4`, and Pages actions by major version. Production hardening should pin actions to trusted immutable SHAs after compatibility testing.

### S5 — Personal identity in automation

The scheduled workflow configures Git commits using a personal name and email. Automation should use a neutral bot identity unless a deliberate audit requirement says otherwise.

### S6 — Data files as persistence

JSON files under `api/` and `data/` should not be treated as authoritative financial, identity, or ownership records. Canonical persistence needs transactions, validation, authorization, auditability, and backup/reconciliation.

### S7 — Missing security contract

No certified authentication, authorization, session, MFA, tenant-isolation, or audit-log contract was established by this inventory pass. These must be explicitly documented before the platform is declared production-ready.

## Required controls before production certification

- Secret-history scan and remediation where required.
- Dependency/SCA scan.
- Static analysis for Python and any discovered frontend/backend languages.
- Workflow permission hardening.
- Immutable action pinning.
- Protected production branch.
- Centralized secret management.
- Authentication and authorization contract.
- Audit-log contract for consequential operations.
- Data backup and restore test.
- Supply-chain review for binaries and third-party actions.
- Security regression tests.

## Immediate policy

Do not commit credentials, access tokens, private keys, production database dumps, or personal secrets to the repository. Do not make a security-sensitive migration solely to improve repository cleanliness; preserve functionality first and migrate through controlled, reviewable changes.
