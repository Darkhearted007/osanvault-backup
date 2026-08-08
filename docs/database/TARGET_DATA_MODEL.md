# ÒsánVault Africa — Target Data Model

## Design rule

The target model is a domain contract, not a request to immediately migrate the existing JSON files. Existing records must be mapped and reconciled before cutover.

## Core domains

### Identity

- `users`
- `organizations`
- `memberships`
- `roles`
- `sessions`
- `verification_profiles`

### Assets

- `assets`
- `properties`
- `asset_documents`
- `asset_valuations`
- `asset_status_history`

### Verification

- `verification_cases`
- `verification_checks`
- `verification_actions`
- `verification_evidence`

### Investment

- `investment_products`
- `offerings`
- `subscriptions`
- `positions`
- `ownership_events`

### Treasury

- `accounts`
- `ledger_entries`
- `payment_intents`
- `settlements`
- `reconciliations`

The internal ledger must remain authoritative for accounting. Blockchain/token records should represent externally verifiable state rather than silently becoming the accounting system.

### Tokenization

- `tokens`
- `tokenized_assets`
- `token_events`
- `wallet_links`

### Community / referrals

- `referral_codes`
- `referrals`
- `community_events`
- `rewards`

### AI / operations

- `ai_runs`
- `ai_recommendations`
- `jobs`
- `notifications`

### Audit

- `audit_events`
- `audit_chain_heads`
- `security_events`

## Cross-cutting fields

Entities should consistently support, where appropriate:

- immutable primary identifier;
- created/updated timestamps;
- lifecycle status;
- tenant/organization ownership where applicable;
- actor/source attribution;
- correlation/request identifier;
- soft-delete or archival policy where legally appropriate;
- integrity/audit references for consequential mutations.

## Migration mapping

| Legacy source | Target domain | Migration treatment |
|---|---|---|
| `api/users/data.json` | Identity | Parse, validate, deduplicate, reconcile |
| `api/properties/data.json` | Assets | Validate property schema and ownership evidence |
| `api/referrals/data.json` | Community | Reconcile referral relationships and rewards |
| `data/properties.json` | Assets | Compare against API property records |
| `data/net-data.json` | Investment/Tokenization | Classify each field before migration |

## Integrity rules

1. No financial balance is inferred from a UI field.
2. Ownership changes require an auditable event.
3. Verification state is distinct from user profile state.
4. Token balances do not replace internal ledger balances.
5. Historical records are immutable after certification except through explicit correcting events.
6. Migration scripts must be repeatable and produce reconciliation reports.
