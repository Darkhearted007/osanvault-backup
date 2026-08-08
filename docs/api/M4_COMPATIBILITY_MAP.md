# M4 — Legacy-to-Canonical Compatibility Map

| Legacy source | Current role | Canonical boundary | Migration action |
|---|---|---|---|
| `api/properties/data.json` | Property fixture/data source | `/api/v1/properties` | Adapter first; database later |
| `api/users/data.json` | User fixture/data source | `/api/v1/users` | Adapter first; identity store later |
| `api/referrals/data.json` | Referral fixture/data source | `/api/v1/referrals` | Adapter first; rewards/ledger model later |
| Browser-embedded wallet data | Client capability | API/service boundary | Remove sensitive/business logic from browser |
| Legacy `netBalance` | Display/fixture value | Treasury-owned balance | Never promote directly to authoritative balance |
| Legacy `netEarned` | Referral display/fixture value | Reward/ledger records | Never promote directly to treasury balance |

## Compatibility principle

The first API implementation should be an adapter over the existing data sources. This deliberately separates API contract stabilization from database migration.

## Forbidden shortcuts

- Do not create a new database merely to satisfy the API milestone.
- Do not reinterpret fixture balances as accounting records.
- Do not expose private credentials through the API.
- Do not make blockchain state the authoritative source for internal accounting.
- Do not delete legacy data before migration reconciliation.

## Acceptance criteria

- Existing data can be read through the new `/api/v1` contract.
- Response shapes are documented and tested.
- Authorization rules are explicit.
- Errors use the canonical error envelope.
- Legacy behavior remains available until migration approval.
