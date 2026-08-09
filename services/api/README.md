# ÒsánVault Canonical API Service

This directory is the M4 compatibility boundary for the existing ÒsánVault data/API surface.

## Current status

M4 begins with contract and runtime discovery. The existing repository contains JSON-backed resources under `api/`, including properties, users, and referrals. Those resources remain the legacy source during this migration stage.

## Rules

- Do not mutate legacy data from a new handler until the compatibility contract is tested.
- Do not treat `netBalance` or `netEarned` as accounting truth.
- Do not change authentication behavior in this milestone.
- Do not introduce a database migration in M4.
- New endpoints belong under `/api/v1` once an executable runtime adapter is identified.

## Target resources

- `GET /api/v1/properties`
- `GET /api/v1/users`
- `GET /api/v1/referrals`

Implementation must preserve legacy behavior while introducing a canonical API boundary.