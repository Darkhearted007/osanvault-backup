# ÒsánVault Canonical Database Layer

This directory contains the M5 staging persistence design.

## Safety boundary

The migration in `migrations/001_canonical_foundation.sql` is **staging-only**. It must not be applied to production until extraction, transformation, reconciliation, rollback and certification gates are complete.

## Authority model

- `assets` owns canonical asset state.
- `documents` owns document metadata and hashes, not raw file contents.
- `verification_cases` owns verification lifecycle and decisions.
- `offerings` and `investments` own investment-domain state.
- `treasury_accounts` and `ledger_entries` own accounting state.
- `tokenization_records` stores blockchain references but is not accounting truth.
- `audit_events` records material state transitions.

## Migration sequence

1. Inventory legacy sources.
2. Classify fields and ownership.
3. Load sanitized fixtures into staging.
4. Execute the migration.
5. Transform legacy records into staging records.
6. Reconcile counts and deterministic identifiers/checksums.
7. Run application compatibility tests.
8. Produce a migration certification report.
9. Only then consider production cutover.

No production cutover is part of this milestone.
