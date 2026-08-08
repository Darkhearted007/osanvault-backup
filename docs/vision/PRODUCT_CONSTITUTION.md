# ÒsánVault Africa — Product Constitution

**Status:** Draft for architecture sign-off  
**Scope:** ÒsánVault Africa only  
**Phase:** Internal consolidation before external ecosystem integration

## 1. Purpose

ÒsánVault Africa is being consolidated into a production-grade digital infrastructure platform for verified African real-world assets, property workflows, investment infrastructure, treasury operations, and supporting intelligence.

This phase intentionally excludes DDSN, IIPA, QuickTask, RiskPilot, RedSea Ledger, and other external products. Those systems must not become dependencies until the internal ÒsánVault architecture is stable and certified.

## 2. Architectural principles

1. Preserve working functionality while refactoring incrementally.
2. Establish one canonical implementation for each production capability.
3. Business domains own their data and lifecycle rules.
4. APIs and domain events are the integration boundaries; arbitrary cross-domain database writes are prohibited.
5. Verification produces evidence and decisions; it does not directly authorize financial settlement.
6. The internal ledger is the financial record of truth; blockchain and payment providers are settlement/integration rails.
7. Sensitive personal, financial, and document data remains off-chain unless a specific legal and architectural decision authorizes publication of a non-sensitive proof or hash.
8. AI may assist, recommend, summarize, classify, and automate low-risk operations, but sensitive ownership, financial, permission, and compliance decisions require explicit policy and authorization controls.
9. Every privileged or consequential business action must be auditable.
10. Secrets, private keys, production credentials, and generated runtime artifacts must never be committed to source control.

## 3. Canonical business domains

- Identity and Organizations
- Assets and Property
- Documents
- Verification and Trust
- Investment and Holdings
- Treasury and Ledger
- Tokenization and Blockchain Records
- Community and Referrals
- Operations and Workflows
- Notifications
- AI and Intelligence
- Audit and Observability

## 4. Authoritative records

The platform must distinguish between authoritative records and external evidence.

- Asset registry: authoritative record for platform-managed asset metadata.
- Verification case: authoritative record of verification workflow, evidence references, decisions, and status.
- Investment holding: authoritative record of a platform user's recognized holding.
- Ledger: authoritative record of internal financial entries.
- Blockchain transaction: external settlement/proof record linked to an internal transaction.
- Uploaded document: evidence object; its metadata, version, hash, verification state, and audit history form the trusted document record.

## 5. Safety and control boundaries

No service may silently:

- transfer funds;
- change verified ownership;
- approve an investment offering;
- change user privileges;
- erase audit history;
- mark an asset verified without the required workflow;
- treat an AI recommendation as an authorization.

These operations require explicit authorization and audit records.

## 6. Compatibility rule

Existing production behavior remains the baseline. Refactoring must proceed through compatibility layers, adapters, feature flags, migrations, and reversible releases rather than destructive rewrites.

## 7. Definition of done for internal platform readiness

ÒsánVault is not ready for integration with external modules until it has:

- a canonical repository structure;
- a canonical domain model;
- controlled database migrations;
- stable API boundaries;
- verification and treasury service boundaries;
- centralized security and audit controls;
- tested backup and restoration procedures;
- CI/CD and rollback capability;
- production observability;
- documented operating procedures;
- passing integration and end-to-end tests.

## 8. Future integration rule

External products may consume ÒsánVault capabilities only through documented contracts. They must not become owners of ÒsánVault domain data or create hidden coupling to internal implementation details.
