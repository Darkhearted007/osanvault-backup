# ÒsánVault Africa — Repository Migration Map

**Status:** Initial mapping; no production code moved by this document.

## 1. Scope

This map covers the current `osanvault-backup` repository and the ÒsánVault-specific supporting repositories `Osanvault-Verify` and `osanv-treasury-agent`. It intentionally excludes DDSN, IIPA, QuickTask, RiskPilot, RedSea Ledger, and other products from implementation dependencies.

## 2. Target structure

```text
apps/
  web/
  admin/
  investor/

services/
  api/
  verify/
  treasury/
  agents/

packages/
  auth/
  database/
  ui/
  sdk/
  types/
  config/
  audit/
  notifications/
  events/
  logging/
  security/

infra/
  docker/
  nginx/
  deployment/
  ci/
  monitoring/
  scripts/

docs/
```

## 3. Current-to-target mapping

| Current location | Target | Action | Notes |
|---|---|---|---|
| `api/` | `services/api/` | inspect then migrate | Preserve existing API behavior; establish `/api/v1` compatibility layer before changing routes. |
| `frontend/` | `apps/web/` | inspect then migrate | Candidate canonical web implementation; verify against other web variants first. |
| `website/` | `apps/web/` or `legacy/` | compare | Do not merge blindly; select one canonical implementation after functional comparison. |
| `www/` | `apps/web/` or `legacy/` | compare | Treat as a competing web variant until verified. |
| `site/` | `apps/web/` or `legacy/` | compare | Preserve until canonical frontend is selected. |
| `landing/` | `apps/web/` | consolidate | Public marketing pages should become routes/components of the canonical web app. |
| `public/` | `apps/web/` or `legacy/` | classify | Preserve public assets/routes that are still referenced. |
| `investor/` | `apps/investor/` | migrate | Investor-specific UI and flows only. |
| `ai/` | `services/agents/` | extract | Keep only ÒsánVault-relevant agents and adapters. |
| `bot.js` / bot scripts | `services/agents/` or messaging boundary | extract | Separate business logic from channel transport. |
| `telegram/` | messaging adapter | extract | Channel integration; no domain ownership. |
| `osanvault-bot-fullmoon.js` | messaging/automation | inspect | Preserve only if still operational and supported by tests. |
| `solana/` | `services/treasury/` or blockchain adapter | inspect | Keep blockchain integration separate from accounting logic. |
| `nft/` | tokenization boundary | inspect | Map only actual production functionality. |
| `data/` | domain database/import layer | inspect | Do not copy blindly; classify and validate each dataset before migration. |
| `messages/` / `messages.json` | `packages/notifications/` or app content | classify | Separate reusable templates from product copy. |
| `assets/` | `packages/ui/` or `apps/web/` | classify | Shared design assets only; product-specific assets remain with the app. |
| `styles.css` | `packages/ui/` or `apps/web/` | inspect | Consolidate only after frontend selection. |
| `scripts/` | `infra/scripts/` or domain tooling | classify | Move operational scripts by responsibility, not wholesale. |
| deployment shell scripts | `infra/deployment/` | classify | Preserve required scripts during transition; archive duplicates only after validation. |
| `nginx/` and `nginx.conf` | `infra/nginx/` | migrate | Environment-specific config must be separated from application code. |
| `ssl/` | external secret/certificate management | do not migrate secrets | Certificates/private keys must not be stored in the canonical source tree. |
| `security/` / `security_monitor.py` | `packages/security/` or `infra/monitoring/` | inspect | Separate application security helpers from infrastructure monitoring. |
| `analytics/` | `apps/web/` + `infra/monitoring/` | classify | Business analytics and infrastructure telemetry are different concerns. |
| `templates/` | app/domain package | classify | Keep only reusable templates. |
| `grants/` | `docs/` or archive | archive | Non-runtime material should not enter application packages. |
| root HTML pages | `apps/web/` | classify | Preserve public routes that remain part of the product. |
| `CNAME`, `robots.txt`, `sitemap.xml` | `apps/web/` / deployment | preserve | Keep production SEO/domain behavior intact. |
| `package.json` + lockfile | root workspace | redesign carefully | Establish workspace only after runtime dependencies are inventoried. |
| `node_modules/` | none | remove from source control | Generated dependency tree must never be a canonical source artifact. |
| runtime logs / `nohup.out` / `*.log` | none | remove from source control | Generated artifacts are not source. |
| binary `cloudflared-linux-arm` | `infra/` release artifact or external dependency | inspect | Prefer versioned external installation/release mechanism over committing large binaries. |
| `*.zip` archives | `legacy/` or external archive | inspect | Do not use nested source archives as live application dependencies. |
| webhook/secret files | secret manager | remove/rotate | Any committed secret must be treated as potentially compromised and rotated. |

## 4. Osanvault-Verify

Target:

`services/verify/`

Preserve the existing verification capabilities and adapt them behind a stable internal contract:

- identity verification
- document verification
- property verification
- organization verification
- fraud signals
- certificates/QR verification
- verification workflow

The service owns verification state and evidence metadata. It must not directly own treasury or investment state.

## 5. osanv-treasury-agent

Target:

`services/treasury/`

First extract stable interfaces for:

- accounts
- ledger entries
- transactions
- settlements
- escrow
- reconciliation
- treasury operations

Then adapt existing implementation behind those interfaces. Do not equate wallet balances with the internal accounting ledger.

## 6. Shared packages

Create only after repeated, stable behavior has been identified:

- `packages/types/` — canonical domain contracts
- `packages/config/` — validated configuration
- `packages/sdk/` — typed service clients
- `packages/auth/` — authentication integration contracts
- `packages/database/` — database access conventions
- `packages/audit/` — audit event contracts
- `packages/events/` — versioned domain event contracts
- `packages/notifications/` — channel-neutral notification contracts
- `packages/logging/` — structured logging conventions
- `packages/security/` — shared security primitives
- `packages/ui/` — only genuinely reusable design-system components

Do not create a shared package merely to move code. It must have a stable owner and reuse case.

## 7. Migration rules

1. No destructive move until the source behavior is identified and tested.
2. One capability is migrated at a time.
3. Legacy paths remain available during transition where required.
4. Database migrations are forward-compatible and reversible where practical.
5. Existing authentication behavior is preserved.
6. Existing deployment behavior remains available until replacement is validated.
7. Every migrated capability gets tests and documentation.
8. No secrets or generated artifacts are copied into the new structure.
9. No cross-domain database coupling is introduced during migration.
10. Each milestone is independently reviewable and revertible.

## 8. Migration sequence

### M0 — Baseline
Inventory, dependency graph, runtime entry points, deployment paths, secrets, and active production assets.

### M1 — Documentation
Finalize constitution, domain model, architecture, and this migration map.

### M2 — Workspace foundation
Introduce the canonical workspace without moving production code yet.

### M3 — Web consolidation
Select and establish the canonical public web implementation.

### M4 — API consolidation
Establish the canonical API boundary and compatibility routes.

### M5 — Shared packages
Extract stable shared contracts and utilities.

### M6 — Verification
Integrate the verification service boundary.

### M7 — Treasury
Integrate treasury interfaces and reconciliation model.

### M8 — AI and automation
Introduce ÒsánVault-scoped agent capabilities.

### M9 — Admin/operations
Establish the internal command center.

### M10 — Data migration and certification
Migrate validated data, reconcile, test rollback/restore, and certify production readiness.

## 9. External integration gate

DDSN, IIPA, QuickTask, RiskPilot, RedSea Ledger, and other systems remain outside the ÒsánVault implementation until M10 is complete and the internal API/event contracts have been formally versioned.
