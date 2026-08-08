# ÒsánVault Africa — Canonical Domain Model

**Status:** Draft for architecture sign-off

## 1. Domain map

```text
Identity & Organizations
        │
        ├──────────────┐
        ▼              ▼
      Assets       Community
        │
        ├── Documents
        └── Verification
                │
                ▼
          Verified Asset
                │
        ┌───────┴────────┐
        ▼                ▼
    Investment       Tokenization
        │                │
        ▼                ▼
    Holdings       Blockchain Records
        │
        ▼
     Treasury / Ledger

All domains emit audited events and may trigger controlled workflows,
notifications, and AI recommendations.
```

## 2. Identity and Organizations

Core concepts:

- User
- Organization
- Membership
- Role
- Permission
- Session
- Service Identity

Identity owns authentication identity and access relationships. It does not own asset, investment, or treasury business state.

## 3. Assets

Core concepts:

- Asset
- LandParcel
- Property
- DevelopmentProject
- Location
- OwnershipRecord
- AssetStatus
- AssetDocumentReference

An asset has a controlled lifecycle. Suggested initial states:

`DRAFT → SUBMITTED → UNDER_REVIEW → VERIFICATION_PENDING → VERIFIED → APPROVED → ACTIVE → SUSPENDED → RETIRED`

State transitions must record actor, timestamp, reason, authorization, and relevant evidence.

## 4. Documents

A document record contains:

- document ID
- document type
- owner/tenant
- asset association where applicable
- storage reference
- content hash
- version
- verification state
- created/updated timestamps
- audit history

The binary file is evidence. The platform record and integrity metadata define the trusted document lifecycle.

## 5. Verification and Trust

Core concepts:

- VerificationCase
- VerificationSubject
- Evidence
- VerificationAction
- VerificationDecision
- Certificate
- FraudSignal

Verification transitions:

`CREATED → EVIDENCE_PENDING → UNDER_REVIEW → PASSED | FAILED | NEEDS_REVIEW → CLOSED`

A successful verification may produce a `VerifiedAsset` or other trusted state transition through a controlled domain operation.

## 6. Investment

Core concepts:

- Offering
- InvestorAccount
- EligibilityCheck
- Subscription
- Allocation
- Holding
- Distribution

Suggested lifecycle:

`OFFERING_CREATED → PUBLISHED → ELIGIBILITY_CHECK → SUBSCRIPTION → PAYMENT_PENDING → PAYMENT_CONFIRMED → ALLOCATION → HOLDING_ACTIVE → DISTRIBUTION → CLOSED`

No frontend may directly mutate these states outside the authorized application service.

## 7. Treasury and Ledger

Core concepts:

- TreasuryAccount
- LedgerEntry
- Transaction
- Settlement
- Escrow
- Reconciliation
- TreasuryOperation

Ledger entries must be immutable. Corrections occur through compensating entries, not destructive edits.

A transaction should support:

- idempotency key
- reference
- account
- asset/currency context
- debit/credit direction
- amount
- status
- settlement reference
- timestamps
- audit correlation ID

## 8. Tokenization and Blockchain Records

Core concepts:

- TokenizedAsset
- TokenClass
- Allocation
- WalletLink
- ChainTransaction
- ChainProof

Blockchain records reference internal business records. They do not replace the internal asset registry, identity system, or accounting ledger.

## 9. Community

Core concepts:

- CommunityMember
- Referral
- ReferralCampaign
- Reward
- CampaignEvent

Rewards must be represented as controlled business transactions and must not bypass treasury controls.

## 10. Operations and Workflows

Core concepts:

- WorkflowDefinition
- WorkflowInstance
- WorkflowStep
- Task
- Approval
- Action
- Assignment

Workflows coordinate domain actions but do not own domain data.

## 11. Notifications

A domain event may request a notification without knowing the delivery channel.

Supported channel abstractions may include:

- in-app
- email
- SMS
- WhatsApp
- Telegram

## 12. AI and Intelligence

Core concepts:

- AgentDefinition
- AgentRun
- ToolCall
- Recommendation
- HumanApproval
- AIActionAudit

AI output is advisory by default. Sensitive actions require policy evaluation and explicit authorization.

## 13. Audit

Audit records capture security and consequential business actions separately from normal domain events.

Security examples:

- login
- permission change
- API key creation
- document access
- administrator action

Business examples:

- property submitted
- property verified
- investment allocated
- settlement completed

## 14. Ownership rules

| Domain | Owns | Other domains access through |
|---|---|---|
| Identity | users, organizations, roles | auth/API contracts |
| Assets | asset/property state | asset APIs/events |
| Documents | document metadata and versions | document APIs |
| Verification | cases, evidence state, decisions | verification APIs/events |
| Investment | offerings, subscriptions, holdings | investment APIs/events |
| Treasury | accounts, ledger, settlements | treasury APIs/events |
| Tokenization | token records and chain references | tokenization APIs/events |
| Community | referrals and rewards | community APIs/events |
| Operations | workflow instances and tasks | workflow APIs/events |
| Audit | immutable audit history | audit API |

## 15. Design rule

No domain may directly update another domain's tables as part of normal application behavior. Cross-domain changes use application services, commands, APIs, or versioned events.
