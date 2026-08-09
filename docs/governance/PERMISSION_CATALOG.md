# ÒsánVault Africa — Permission Catalog

## Purpose

Define capability-level permissions for the future RBAC/ABAC implementation. Permissions are intentionally separated from role names so enterprise policies can evolve without rewriting domain services.

## Identity

- user.read
- user.create
- user.update
- user.suspend
- organization.read
- organization.create
- organization.update
- role.assign
- permission.grant

## Assets

- asset.read
- asset.create
- asset.update
- asset.submit
- asset.review
- asset.approve
- asset.suspend
- asset.archive
- ownership.read
- ownership.change.request
- ownership.change.approve

## Documents

- document.read
- document.upload
- document.update
- document.verify
- document.archive

## Verification

- verification.create
- verification.read
- verification.review
- verification.request_evidence
- verification.approve
- verification.reject
- certificate.issue
- certificate.revoke

## Investment

- offering.read
- offering.create
- offering.update
- offering.submit
- offering.approve
- subscription.read
- subscription.create
- allocation.approve
- holding.read
- distribution.approve

## Treasury

- treasury.account.read
- treasury.operation.create
- treasury.operation.read
- treasury.operation.review
- treasury.operation.approve
- treasury.settlement.execute
- treasury.reconciliation.read
- treasury.reconciliation.resolve
- treasury.pause

## Tokenization

- token.registry.read
- token.registry.manage
- token.contract.read
- token.contract.change.request
- token.contract.review
- token.contract.approve
- token.deployment.approve
- token.pause
- country_token.configure
- country_token.approve
- country_token.activate

## Country ecosystem

- country.read
- country.configure
- country.review
- country.activate
- country.suspend

## AI

- ai.agent.read
- ai.agent.configure
- ai.run
- ai.recommendation.review
- ai.high_impact.approve
- ai.integration.manage

## Platform administration

- platform.config.read
- platform.config.change.request
- platform.config.approve
- integration.read
- integration.manage
- deployment.approve
- emergency.pause

## Audit and security

- audit.read
- audit.export
- security.event.read
- security.policy.manage
- secret.reference.manage
- privileged_access.request
- privileged_access.approve

## Implementation rule

Authorization must be evaluated server-side at the domain/service boundary. UI visibility is not authorization. Services must reject unauthorized actions even when called directly through an API or automation path.
