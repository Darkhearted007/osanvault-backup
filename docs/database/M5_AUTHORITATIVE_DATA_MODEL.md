# M5 — ÒsánVault Authoritative Data Model

## Purpose

Define the target persistence boundary before any legacy JSON migration. This document is architectural; it does not change the current production data source.

## Domain ownership

### Identity
Owns users, organizations, roles, permissions, sessions and service identities.

### Assets
Owns properties, land parcels, projects, locations and asset lifecycle state.

### Documents
Owns document metadata, versions, hashes, storage references and document lifecycle state.

### Verification
Owns verification cases, evidence references, decisions, certificates and verification audit history.

### Investment
Owns offerings, subscriptions, allocations, holdings and distribution records.

### Treasury
Owns accounts, immutable ledger entries, settlement records, escrow records and reconciliation state.

### Tokenization
Owns token classes, asset-token associations, wallet associations and on-chain transaction references. It does not become the accounting source of truth.

### Community
Owns referrals, campaigns, rewards and community membership records.

### Operations
Owns tasks, approvals, notifications, jobs and operational state.

### Audit
Owns tamper-evident security and business audit records.

## Core invariants

1. Every authoritative business record has a stable identifier.
2. Domain ownership is explicit; unrelated services must not write directly into another domain's tables.
3. Treasury balances are derived from ledger entries, not wallet UI state or token balances.
4. Verification evidence is distinct from verification decisions.
5. Documents are represented by metadata, hashes and storage references; raw files are not the business source of truth.
6. Blockchain state is an external settlement/proof layer, not a replacement for internal accounting or sensitive personal data storage.
7. Sensitive records require tenant/organization ownership where applicable.
8. State transitions are auditable and authorization-controlled.
9. Legacy JSON remains read-only during the migration design stage.
10. No destructive migration occurs until extraction, transformation, reconciliation and rollback have been tested.

## Canonical relationship

```text
Organization
  └── User
       └── Asset
            ├── Documents
            ├── Verification Case
            └── Offering
                  └── Investment
                       └── Holding

Asset ──> Tokenization Record
Investment ──> Treasury Ledger / Settlement
All sensitive transitions ──> Audit
```

## Migration rule

The target model must first be implemented as migrations and tested against empty/staging data. Existing `api/*/data.json` resources remain legacy compatibility sources until M4/M5 migration certification is complete.
