# NET Deprecation Record

## Decision

NET (NigeriaEstate Token) is deprecated and must not be treated as the current ÒsánVault token.

## Replacement

The canonical token designation is **OSANV**.

## Migration handling

Legacy NET references are retained only where required for historical traceability, migration provenance, contract history, or compatibility analysis. They must not be surfaced as a current token option.

## Safety rule

Do not perform a blind repository-wide string replacement. NET references must first be classified as:

- historical documentation
- migration backup
- legacy UI
- legacy contract
- data field
- deployed contract reference
- active/current implementation

Only active/current references should be changed to OSANV after verification.

## Outstanding verification

Determine whether any NET contract was ever deployed or used in a live transaction. Until that is established, the migration must not assert that NET had or did not have a live deployment.

## Effective architecture rule

All new ÒsánVault services and data models must use OSANV terminology. Financial accounting remains ledger-based and is not synonymous with token balance.