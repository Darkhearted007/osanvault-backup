# ÒsánVault Africa — M8 Canonical Domain Model

## Purpose

This document translates the approved enterprise, business, token and governance decisions into the canonical ÒsánVault domain model. It is an architecture baseline, not a production database migration.

## Core bounded domains

```text
Identity & Organizations
        │
        ├──────────────┐
        ▼              ▼
      Assets       Documents
        │              │
        └──────┬───────┘
               ▼
          Verification
               │
               ▼
        Approved Asset State
               │
        ┌──────┴───────┐
        ▼              ▼
    Investment     Tokenization
        │              │
        ▼              ▼
     Holdings        OSANV / Country Tokens
        │
        ▼
      Treasury Ledger
               │
               ▼
        Settlement / Reconciliation
```

## Identity

Core entities:

- User
- Organization
- OrganizationMembership
- RoleAssignment
- Permission
- IdentityCredential

Identity owns authentication identity and organizational membership. It does not own asset or financial state.

## Assets

Core entities:

- Asset
- AssetType
- Property
- LandParcel
- Project
- OwnershipRecord
- AssetStatus
- AssetRelationship

Asset is the canonical root for real-world asset registration. Asset state changes must be auditable.

## Documents and evidence

Core entities:

- Document
- DocumentVersion
- EvidenceRecord
- DocumentHash
- DocumentRequirement

Documents provide evidence; they do not independently establish ownership without the applicable verification/approval process.

## Verification

Core entities:

- VerificationCase
- VerificationSubject
- VerificationEvidence
- VerificationReview
- VerificationDecision
- Certificate

Verification owns trust decisions. A verified state is a domain decision with evidence and audit history.

## Investment

Core entities:

- Offering
- OfferingAsset
- InvestorEligibility
- Subscription
- Allocation
- Holding
- Distribution

Investment models must remain legally configurable by country and product.

## Treasury

Core entities:

- LedgerAccount
- LedgerEntry
- Transaction
- SettlementInstruction
- Settlement
- Reconciliation
- TreasuryException

The treasury ledger is the authoritative accounting representation for platform-controlled financial records.

## Tokenization

Core entities:

- TokenizedAsset
- TokenClass
- ContractRegistryEntry
- ChainNetwork
- TokenOperation

OSANV is the platform-token designation.

Country tokens are separate entities and must reference a Country/Ecosystem. They must not be represented as OSANV balances.

## Country ecosystem

Core entities:

- Country
- CountryEcosystem
- CountryConfiguration
- CountryToken
- CountryActivation

Country configuration must not fork the core domain model unnecessarily.

## Operations

Core entities:

- Workflow
- WorkflowStep
- ApprovalRequest
- ApprovalDecision
- Task
- Notification

Operations provide controlled state transitions across domains.

## Audit and events

Core entities:

- AuditEvent
- DomainEvent
- SecurityEvent
- CorrelationRecord

Material state transitions must be attributable to an actor or service identity.

## Authority classification

Every persistent field must be classified as:

- AUTHORITATIVE — source of truth for the domain
- DERIVED — calculated from authoritative data
- LEGACY — retained only for migration/compatibility
- DEPRECATED — scheduled for removal
- EXTERNAL — sourced from an external system and independently validated

## Financial separation

```text
Company accounting
      ≠
Treasury ledger
      ≠
OSANV token balance
      ≠
Country token balance
      ≠
Asset valuation
```

Integration adapters may reconcile these systems but must not silently merge their semantics.

## Tenant and ownership boundaries

Organizations own or participate in resources through explicit relationships. Tenant isolation must be enforced at the data-access and authorization layers rather than inferred from UI context.

## Lifecycle principle

No entity should be deleted merely because its business state is obsolete. Where legally and operationally appropriate, lifecycle state, archival, retention and provenance should preserve auditability.

## Migration rule

Existing JSON and legacy records remain source material until mapped, validated, reconciled and certified. No destructive migration is authorized by this document.
