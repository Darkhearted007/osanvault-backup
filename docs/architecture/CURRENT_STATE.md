# ÒsánVault Africa — Current-State Inventory

**Baseline branch:** `feat/osanvault-internal-foundation`

## Purpose

This document records the repository state before application consolidation. It is intentionally descriptive and does not prescribe destructive migration.

## Repository shape observed

The repository is currently a legacy/static-web oriented codebase with several parallel concerns:

- Static HTML pages at the repository root, including `about.html` and `add-net.html`.
- A Python-based page-generation path under `scripts/`.
- Generated-site output under `site/` referenced by deployment automation.
- JSON-backed data under `data/` and API-style JSON endpoints under `api/`.
- AI/automation scripts under `ai/`.
- Static assets under `assets/`.
- GitHub Actions workflows for deployment and scheduled content generation.
- Existing architecture-control documents added by the internal-consolidation foundation PR.

The repository also contains a committed `ai/ngrok` binary (~26 MB). This is treated as an infrastructure artifact and must not be assumed to belong in the canonical application workspace.

## Runtime observations

### Website generation

`scripts/generate-pages.py` reads token/property data and templates, generates `index.html`, `net.html`, and `properties.html`, and copies selected static pages into `site/`.

Important finding: the script uses paths beginning with `../`, while the deployment workflow invokes it from the repository root as `python3 scripts/generate-pages.py`. Because relative paths are resolved from the process working directory, this execution path is inconsistent with the script's assumptions and must be tested/fixed during migration rather than silently relied upon.

### API/data layer

The `api/` tree currently exposes JSON files for properties, referrals, and users. These are legacy data stores, not yet a canonical database/API contract.

### Automation

The deployment workflow:

1. checks out the repository;
2. installs Python `requests`;
3. invokes `scripts/fetch-net-data.py`;
4. invokes `scripts/generate-pages.py`;
5. commits generated `site/` changes back to `main`;
6. deploys `site/` through GitHub Pages.

Current finding: `scripts/fetch-net-data.py` was not found at the referenced path on this baseline branch. This workflow therefore requires validation before being treated as production-capable.

A second scheduled workflow installs Python dependencies, executes `scripts/fetch-generate-fullmoon.py`, and commits all resulting changes back to `main`. This automation is outside the canonical architecture until its ownership and data source are verified.

## Dependency state

No repository `package.json` was returned by the repository code search during this inventory pass. Therefore a Node.js dependency graph must not be inferred. Python dependencies are currently workflow-local rather than represented by a canonical lockfile/requirements manifest.

## Domain/data state

Observed legacy data domains include:

- Properties
- Users
- Referrals
- NET/token statistics
- AI-generated/public content

These map to future canonical domains but remain legacy until their persistence, ownership, and integrity requirements are verified.

## Authentication and authorization

No canonical authentication or authorization implementation has been certified by this inventory pass. Existing security behavior must therefore be preserved during discovery and explicitly documented before consolidation.

## Migration classification

| Area | Current classification | Action |
|---|---|---|
| Root HTML | Legacy presentation | Inventory, then migrate only required pages |
| `site/` | Generated presentation | Keep as output target until replacement is verified |
| `scripts/` | Legacy automation | Test individually before migration |
| `api/*.json` | Legacy data | Freeze as source-of-truth candidates; migrate through reconciliation |
| `ai/` | Mixed automation/AI artifacts | Separate code from runtime/binary artifacts |
| `assets/` | Static assets | Deduplicate and migrate |
| GitHub Actions | Operational automation | Harden after dependency audit |
| Architecture docs | Control plane | Canonicalize under `docs/architecture` |

## Gate for next phase

No legacy data should be deleted and no production deployment path should be replaced until the dependency graph, target data model, API contract inventory, and security baseline are reviewed together.
