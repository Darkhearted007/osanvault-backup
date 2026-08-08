# M2 — Delivery Path Validation

## Scope

This milestone stabilizes the existing ÒsánVault static-site delivery path without changing application business logic, authentication, database schema, or legacy data.

## Findings

1. The historical deployment workflow referenced `scripts/fetch-net-data.py`, but that file is not present in the repository.
2. The legacy page generator used `../` paths relative to the process working directory. This is fragile in CI and local execution.
3. The previous deployment workflow committed generated `site/` output back to `main` and required write access to repository contents.
4. The repository did not contain a root Python dependency manifest for the deployment build.
5. `data/net-data.json` and `data/properties.json` are currently the committed data inputs for the static generator.

## Changes

### Generator

`scripts/generate-pages.py` now resolves all inputs and outputs from the repository root using `pathlib.Path`, so execution is independent of the current working directory.

### CI/CD

`.github/workflows/deploy.yml` now:

- uses current major versions of the official GitHub Pages actions;
- grants only `contents: read`, `pages: write`, and `id-token: write` permissions;
- removes the workflow's ability to commit generated files back to `main`;
- validates the committed JSON data snapshot before generation;
- builds the site deterministically from repository data;
- supports manual `workflow_dispatch` execution;
- uses GitHub Pages artifact deployment.

### Dependencies

Added `requirements.txt` with the existing `requests` dependency.

## Deliberate non-change

The missing `fetch-net-data.py` was not invented or replaced with an unverified external data source. Until its intended provider and data contract are recovered and reviewed, the committed `data/net-data.json` snapshot remains the deterministic build input.

## Exit criteria

M2 is complete when:

- the generator runs from the repository root;
- the generator also runs from another working directory;
- JSON inputs validate;
- the Pages workflow can build without a missing-script failure;
- the workflow no longer writes generated files to `main`;
- production business logic remains unchanged.

## Next milestone

M3 — identify and certify the canonical ÒsánVault web implementation before moving it into `apps/web/`. No external ÒsánVault-adjacent repositories are to be integrated during M3.
