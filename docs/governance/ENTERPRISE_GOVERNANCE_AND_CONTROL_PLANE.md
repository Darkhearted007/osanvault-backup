# ÒsánVault Africa — Enterprise Governance & Control Plane

## Purpose

Define the authority model that protects ÒsánVault as it scales from a Nigerian enterprise into a pan-African infrastructure platform.

## Authority layers

```text
Corporate Governance
        ↓
Enterprise Policies
        ↓
Domain Ownership
        ↓
Roles & Permissions
        ↓
Workflow / Approval
        ↓
Execution
        ↓
Audit Evidence
```

## Domain authority

### Asset authority

Responsible for asset lifecycle policy, asset onboarding, ownership evidence and material asset-state changes.

### Verification authority

Responsible for verification policy, evidence standards, reviewer roles, certification and exception handling.

### Investment authority

Responsible for offering creation/approval, investor eligibility rules, allocations and disclosures, subject to applicable legal requirements.

### Treasury authority

Responsible for payment operations, settlement authorization, reconciliation, treasury controls and financial exception handling.

### Token authority

Responsible for token policy, contract registry, issuance/change approval, deployment controls and token lifecycle governance.

OSANV is the platform token. Country tokens require separate approval and country-level policy.

### Security authority

Responsible for privileged access, security policy, incident response, secrets, key management and security exceptions.

### AI authority

Responsible for agent policies, approved capabilities, model/provider controls, high-impact action restrictions and AI auditability.

### Country authority

Responsible for country activation, local requirements, partners, regulatory coordination, data/privacy requirements and country ecosystem configuration.

## Role model

The canonical platform should support roles such as:

- Platform Administrator
- Organization Administrator
- Asset Manager
- Verification Officer
- Investment Officer
- Treasury Operator
- Finance Approver
- Compliance Officer
- Security Administrator
- Token Administrator
- Country Administrator
- Auditor
- Support Operator
- AI/Automation Operator

Actual permissions must be capability-based rather than inferred solely from role names.

## Separation of duties

High-impact actions should support maker/checker patterns where appropriate.

Examples:

```text
Asset submission → Verification → Approval
Treasury instruction → Authorization → Settlement
Token change → Security review → Deployment approval
Country creation → Compliance review → Activation approval
```

A single privileged account should not silently control the complete lifecycle of a material operation.

## Permission architecture

Use explicit permissions such as:

- asset.create
- asset.update
- asset.approve
- verification.review
- verification.approve
- investment.create
- investment.approve
- treasury.initiate
- treasury.approve
- treasury.settle
- token.registry.manage
- token.contract.approve
- country.configure
- country.activate
- user.manage
- security.manage
- audit.read

## Approval policies

Approval requirements should be policy-driven based on:

- action type
- monetary/material value
- organization
- country
- asset class
- risk level
- user authority
- transaction status

## Audit

Every material action must record:

- actor/service identity
- organization/tenant
- action
- target entity
- before/after state where applicable
- timestamp
- request/correlation ID
- approval references
- reason where required

## AI controls

AI agents may recommend or execute only capabilities explicitly granted to the agent identity.

AI must not bypass authorization, approval, accounting controls or audit requirements.

## Emergency controls

The platform must support:

- privileged access suspension
- token/contract integration pause
- treasury operation pause
- country ecosystem suspension
- verification service suspension
- incident mode

Emergency controls must themselves be audited.

## Control-plane architecture

```text
                Admin / Operations
                       ↓
                Control Plane API
                       ↓
          ┌────────────┼────────────┐
          ↓            ↓            ↓
       Identity      Policy       Workflow
          │            │            │
          └────────────┼────────────┘
                       ↓
                Domain Services
                       ↓
                     Audit
```

The control plane governs services; it does not become a substitute for domain ownership.
