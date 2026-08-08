# ÒsánVault Africa — Dependency Graph

## High-level flow

```text
Legacy data sources
  ├── data/net-data.json
  ├── data/properties.json
  └── api/{properties,users,referrals}/data.json
          │
          ▼
   Python generation scripts
          │
          ▼
     static templates
          │
          ▼
        site/
          │
          ▼
     GitHub Pages deploy
```

```text
AI / automation scripts
  ├── dashboard bots
  ├── oracle/content scripts
  ├── property/post update scripts
  └── runtime helpers
          │
          ▼
   External services / generated content
```

## Dependency classes

### Presentation

- Root HTML pages
- Templates
- `site/` generated pages
- CSS and image assets

### Data

- Token/NET statistics
- Property records
- User records
- Referral records

### Generation

- Python scripts under `scripts/`
- Scheduled GitHub Actions

### AI/automation

- Python bots and update scripts under `ai/`
- `ai/ngrok` is a binary artifact and must be isolated from application source

### Delivery

- GitHub Actions
- GitHub Pages artifact/deployment
- Existing domain configuration (`CNAME`)

## Known broken or uncertain edges

1. `deploy.yml` references `scripts/fetch-net-data.py`, but that file was not found at the referenced path during this inventory pass.
2. `generate-pages.py` uses parent-relative paths and therefore depends on a specific working directory that the current workflow does not explicitly establish.
3. The repository does not currently expose a canonical Node dependency manifest through the code search; Node runtime assumptions must not be introduced without evidence.
4. Python dependencies are installed ad hoc inside workflows; there is no certified lockfile in the observed baseline.
5. Multiple automated workflows can write back to `main`, creating potential race conditions and generated-file drift.
6. Legacy JSON files function as data stores but have no declared schema/versioning/reconciliation contract.

## Canonical target direction

```text
                         ┌────────────────────┐
                         │ Canonical Web App  │
                         └─────────┬──────────┘
                                   │
                         ┌─────────▼──────────┐
                         │ Canonical API      │
                         └─────────┬──────────┘
                                   │
          ┌────────────────────────┼────────────────────────┐
          ▼                        ▼                        ▼
   Identity/Access            Asset Registry          Investment/Treasury
          │                        │                        │
          └────────────────────────┼────────────────────────┘
                                   ▼
                         Audit / Observability
                                   │
                                   ▼
                         External integrations
```

The target graph is architectural guidance only. It does not authorize replacing the current implementation until the corresponding domain and data contracts are certified.
