# ÒsánVault Africa — Enterprise Approval Matrix

## Purpose

Define the minimum maker/checker and authorization expectations for material platform operations. This is a policy baseline; implementation must map these controls to the actual roles, permissions and workflows after security review.

| Domain | Initiator | Reviewer | Approver | Execution | Audit |
|---|---|---|---|---|---|
| Asset onboarding | Asset Manager | Verification Officer | Asset Approver | Asset Service | Required |
| Ownership/material asset change | Asset Manager | Compliance/Verification | Authorized Approver | Asset Service | Required |
| Verification certification | Verification Officer | Senior Verification Officer | Verification Approver | Verify Service | Required |
| Investment offering | Investment Officer | Compliance | Investment Approver | Investment Service | Required |
| Treasury instruction | Treasury Operator | Finance/Control | Treasury Approver | Treasury Service | Required |
| Treasury settlement | Treasury Operator | Reconciliation/Control | Authorized Finance Approver | Settlement Adapter | Required |
| OSANV contract change | Token Administrator | Security/Technical Reviewer | Token Governance Approver | Deployment Pipeline | Required |
| Country-token activation | Country Administrator | Legal/Compliance | Country Governance Approver | Country Control Plane | Required |
| Country ecosystem activation | Country Administrator | Security/Compliance | Enterprise Approver | Control Plane | Required |
| Privileged access grant | Security Administrator | Control Reviewer | Security Approver | Identity System | Required |
| AI high-impact action | AI/Automation Operator | Domain Reviewer | Domain Approver | Authorized Service | Required |

## Rules

1. The same identity should not silently perform every material step where separation of duties is required.
2. Automated execution must preserve the authorization and approval context.
3. Emergency operations must use an explicit emergency policy and produce enhanced audit evidence.
4. Approval thresholds may vary by value, risk, country, asset class and regulatory requirement.
5. This matrix does not grant legal authority; it defines the software control model.
