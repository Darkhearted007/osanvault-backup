# M8 Data Ownership Matrix

| Domain | Authoritative owner | Derived data | External data | Sensitive controls |
|---|---|---|---|---|
| Identity | Identity service | Profile summaries | Identity providers | MFA, credential protection |
| Organizations | Organization domain | Metrics | External registries | Admin approval |
| Assets | Asset domain | Valuation/search indexes | Registry/geospatial sources | Ownership controls |
| Documents | Document domain | OCR/search metadata | Uploaded evidence | Access control |
| Verification | Verification domain | Risk/summary scores | Evidence providers | Reviewer/approval controls |
| Investment | Investment domain | Reporting views | Payment/provider records | Eligibility/approval |
| Treasury | Treasury/ledger | Aggregates | Payment/blockchain rails | Maker/checker, reconciliation |
| Tokenization | Tokenization domain | Market/display data | Blockchain state | Contract/deployment controls |
| Country | Country domain | Country metrics | Local sources | Activation approval |
| Workflow | Workflow domain | Operational metrics | External task sources | Policy authorization |
| Audit | Audit domain | Analytics indexes | Imported audit evidence | Append-only/tamper evidence |

## Token classification

- OSANV: platform token designation.
- NET: future Nigeria country-token namespace/design concept; historical NET references must be classified before migration.
- GET: future Ghana country-token namespace/design concept.

No country token is considered deployed merely because a symbol exists in documentation or configuration.

## Financial classification

- `LedgerEntry`: authoritative internal accounting record.
- Token balance: blockchain/token-system state.
- Asset valuation: valuation data, not cash accounting.
- Revenue: corporate accounting concept.

These must remain distinct in schemas and APIs.
