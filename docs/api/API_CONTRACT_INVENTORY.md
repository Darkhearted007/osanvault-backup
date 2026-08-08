# ÒsánVault Africa — API Contract Inventory

## Current state

The repository exposes legacy JSON-backed paths under `api/`:

- `api/properties/data.json`
- `api/referrals/data.json`
- `api/users/data.json`

These are data resources rather than a certified HTTP API specification.

## Canonical API groups

The future API should be organized by domain rather than by file-storage layout.

### Identity

- `POST /v1/auth/...`
- `GET /v1/users/me`
- `GET /v1/organizations/...`

### Assets

- `GET /v1/assets`
- `POST /v1/assets`
- `GET /v1/assets/{assetId}`
- `PATCH /v1/assets/{assetId}`
- `GET /v1/assets/{assetId}/documents`

### Verification

- `POST /v1/verification/cases`
- `GET /v1/verification/cases/{caseId}`
- `POST /v1/verification/cases/{caseId}/actions`

### Investment

- `GET /v1/products`
- `GET /v1/offerings`
- `POST /v1/subscriptions`
- `GET /v1/positions`

### Treasury

- `POST /v1/payments/intents`
- `GET /v1/accounts/{accountId}/ledger`
- `POST /v1/reconciliations`

### Tokenization

- `GET /v1/tokens`
- `GET /v1/tokenized-assets`
- `GET /v1/token-events`

### Community

- `GET /v1/referrals`
- `POST /v1/referrals`
- `GET /v1/rewards`

### AI

- `POST /v1/ai/runs`
- `GET /v1/ai/runs/{runId}`
- `GET /v1/ai/recommendations`

### Operations / audit

- `GET /v1/operations/jobs`
- `GET /v1/audit/events`

## API requirements

Every production mutation should define:

- authenticated actor;
- authorization policy;
- request validation;
- idempotency behavior where duplicate submission is possible;
- transaction boundary;
- audit event;
- error taxonomy;
- rate-limit behavior;
- correlation/request ID;
- pagination/filtering contract for collections.

## Compatibility rule

Legacy JSON endpoints must not be removed until a migration adapter or equivalent certified API exists and the data has been reconciled. The target routes above are contracts to be refined during implementation, not permission to expose unaudited financial operations.
