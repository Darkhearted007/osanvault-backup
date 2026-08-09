# M5 Staging Execution & Reconciliation Runbook

## Purpose

Move the canonical persistence foundation from static validation into a controlled staging exercise without touching production data.

## Current gate

- PR: `#11`
- Branch: `feat/osanvault-canonical-foundation`
- Migration: `services/database/migrations/001_canonical_foundation.sql`
- CI: currently blocked before runner startup by the GitHub account billing lock; this is an infrastructure gate, not a test result.

## Safety rules

1. Do not execute the migration against production.
2. Use a disposable or dedicated staging PostgreSQL database.
3. Take a database snapshot before any staging migration.
4. Do not modify legacy JSON sources during reconciliation.
5. Do not introduce authentication, authorization, treasury, token issuance, or swap changes in M5.
6. Do not treat static validation as evidence that a PostgreSQL migration has executed successfully.

## Preflight

Run from the repository root:

```bash
python scripts/validate-m5.py
python scripts/reconcile-m5.py
python -m unittest discover -s services/api -p 'test_*.py' -v
```

Expected results:

- M5 staging validation reports `PASS`.
- Reconciliation preflight reports `PASS`.
- API compatibility tests pass.
- No database connection is required for these preflight checks.

## Staging migration

Only after the preflight passes, connect to the dedicated staging PostgreSQL instance and execute:

```bash
psql "$STAGING_DATABASE_URL" -v ON_ERROR_STOP=1 -f services/database/migrations/001_canonical_foundation.sql
```

Immediately verify that the ten canonical tables exist in the `osanvault` schema and that the migration transaction completed successfully.

## Reconciliation

The first reconciliation pass is structural. It confirms that the legacy collections can be mapped without losing required identity or relationship information:

| Legacy source | Canonical target | Key mapping |
| --- | --- | --- |
| `api/properties/data.json` | `osanvault.assets` | legacy `id` -> `legacy_id`; name/location/status metadata preserved |
| property records | `osanvault.offerings` candidates | asset association preserved; no offering is activated automatically |
| `api/users/data.json` | `osanvault.users` | `userId` retained as external subject; display name preserved |
| user property names | `osanvault.assets` relationships | references resolved by exact property name |
| `api/referrals/data.json` | reconciliation/audit subjects | user identity references verified; no financial ledger entry is created |

M5 must not infer financial balances into the canonical ledger merely because legacy JSON contains `netBalance` or `netEarned`. Those values require a separately approved financial reconciliation design.

## Post-migration verification

After staging execution:

1. Verify all ten canonical tables exist.
2. Verify foreign-key constraints are present.
3. Verify unique constraint on ledger idempotency keys.
4. Verify status checks reject invalid lifecycle states.
5. Run the API compatibility suite against the unchanged legacy surface.
6. Compare row counts and mapping reports.
7. Record any source records that cannot be mapped exactly.
8. Do not promote the migration to production until reconciliation is reviewed and signed off.

## Exit criteria

M5 is ready for the next phase only when:

- staging migration completes with `ON_ERROR_STOP=1`;
- all ten canonical tables and required indexes are verified;
- structural reconciliation has zero unexplained orphan references;
- legacy API compatibility remains intact;
- no production data has been changed;
- CI infrastructure is restored or an equivalent trusted CI gate is available.
