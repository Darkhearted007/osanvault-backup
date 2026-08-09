# M5 — Data Migration Rules

## Non-negotiable

- Legacy JSON is not deleted during M5.
- No production database cutover occurs in M5.
- No financial values are promoted to an authoritative ledger without reconciliation.
- No personally identifying fixture data is copied into new production fixtures without an explicit data classification decision.
- Every migration must be reversible until certification.

## Migration pipeline

```text
Legacy source
  -> inventory
  -> classify
  -> validate
  -> transform
  -> stage
  -> reconcile
  -> certify
  -> production cutover
```

## Reconciliation

For each migrated record, preserve a source reference and calculate deterministic counts/checksums where practical. Any mismatch blocks cutover.

## Initial domain priority

1. Identity and organizations
2. Assets/properties
3. Documents
4. Verification
5. Investment
6. Treasury
7. Tokenization
8. Community
9. Operations
10. Audit

Financial and tokenization migrations must follow the completion of the core identity/asset/verification model and an explicit reconciliation test plan.
