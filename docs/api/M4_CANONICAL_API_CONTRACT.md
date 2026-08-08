# M4 — Canonical ÒsánVault API Contract

## Status
Draft implementation contract. Legacy behavior remains the compatibility baseline until tests and production validation approve migration.

## Scope
This milestone covers only the current ÒsánVault core API domains:

- properties
- users
- referrals

Verification, treasury, AI, tokenization, and external ecosystem modules are intentionally outside this milestone.

## Legacy sources inspected

- `api/properties/data.json`
- `api/users/data.json`
- `api/referrals/data.json`

These are legacy data sources, not yet authoritative production databases.

## Canonical API boundary

All new application consumption should target:

`/api/v1/<domain>`

The compatibility layer may continue serving legacy paths until migration and regression testing are complete.

## Properties

### `GET /api/v1/properties`

Returns a collection of property records.

Legacy fields currently observed:

- `id`
- `name`
- `location`
- `price`
- `rentYield`
- `image`
- `tokenized`

The legacy `price` and `rentYield` values must not be interpreted as legally binding investment terms. Future canonical models must carry currency, valuation/source, effective date, status, and verification metadata.

### `GET /api/v1/properties/:id`

Returns one property by stable identifier.

The identifier must be treated as a canonical asset identifier only after the target data model establishes its ownership and lifecycle semantics.

## Users

### `GET /api/v1/users/:userId`

Returns the platform profile representation required by the requesting client.

The legacy source currently contains:

- `userId`
- `name`
- `properties`
- `netBalance`

`netBalance` must NOT become the authoritative financial balance. Treasury/accounting will later own financial balances through an auditable ledger.

### Security

User endpoints must not expose another user's sensitive information without authorization. Wallet-like identifiers in legacy fixtures are not proof of identity or ownership.

## Referrals

### `GET /api/v1/referrals/:userId`

Returns referral statistics.

Legacy fields currently observed:

- `userId`
- `referrals`
- `netEarned`

`netEarned` must not be treated as an authoritative treasury balance. Future referral rewards must be represented through explicit reward/ledger records.

## Error contract

New endpoints should converge on:

```json
{
  "error": {
    "code": "RESOURCE_NOT_FOUND",
    "message": "Resource not found",
    "requestId": "<request-id>"
  }
}
```

Do not expose stack traces, secrets, filesystem paths, or internal provider details.

## Compatibility rules

1. Existing consumers remain functional during migration.
2. Legacy data remains readable until a canonical store is validated.
3. New API contracts must not silently change financial semantics.
4. Writes must be idempotent where duplicate requests are possible.
5. Authentication and authorization behavior must not be weakened.
6. Every sensitive mutation must eventually produce an audit event.

## Migration order

1. Add contract tests against legacy behavior.
2. Implement `/api/v1` adapters over existing sources.
3. Migrate the canonical web client to `/api/v1`.
4. Validate regression behavior.
5. Introduce canonical domain persistence in a later data milestone.
6. Retire legacy endpoints only after usage is zero and rollback is available.
