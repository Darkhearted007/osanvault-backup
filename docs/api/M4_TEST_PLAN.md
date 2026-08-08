# M4 — Canonical API Test Plan

## Purpose
Prove that the new `/api/v1` boundary can be introduced without changing the meaning of existing ÒsánVault data.

## Contract tests

### Properties
- list properties
- retrieve property by id
- missing property returns canonical not-found error
- malformed id is rejected safely
- response fields match the documented contract

### Users
- retrieve authorized user
- unauthorized access is rejected
- missing user returns canonical not-found error
- legacy wallet-like identifier is not treated as identity proof
- `netBalance` is treated as legacy display data only

### Referrals
- retrieve referral statistics for an authorized user
- missing user returns canonical not-found error
- `netEarned` is treated as legacy display data only

## Regression tests

For each endpoint, compare the adapter response with the current legacy source for the same fixture. Differences must be explicit and documented.

## Security tests

- no secrets in responses
- no stack traces
- no filesystem paths
- authorization enforced before sensitive user data is returned
- request IDs available for error correlation

## Migration tests

- canonical web can switch to `/api/v1` without a feature regression
- legacy paths remain available during the compatibility window
- repeated reads are deterministic
- future writes must be idempotent

## Exit criteria

M4 is complete only when contract, regression, security, and compatibility tests pass and the canonical web candidate no longer depends directly on JSON storage paths.
