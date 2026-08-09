# M8 Legacy Source Mapping

## Current known sources

| Legacy source | Target domain | Initial treatment |
|---|---|---|
| `api/properties/data.json` | Assets / Property | Legacy source; validate and stage |
| `api/users/data.json` | Identity / Organization membership | Legacy source; classify fields |
| `api/referrals/data.json` | Community / Referral operations | Legacy source; map separately from finance |
| `data/properties.json` | Assets / Property | Legacy/duplicate candidate; reconcile |
| `data/net-data.json` | Token/market legacy data | Do not treat as authoritative; investigate provenance |

## Field classification principles

Legacy fields are not promoted to authoritative status solely because they exist in JSON.

Each field must be classified as:

- authoritative candidate
- derived
- compatibility-only
- deprecated
- unknown pending verification

## NET handling

Any legacy `NET`, `NigeriaEstate`, `NigeriaEstate Token`, or related token reference must be classified before migration.

The historical NET platform-token concept is deprecated. The future Nigeria country-token namespace may use NET, but this is not evidence of issuance or deployment.

## Migration stages

```text
Inventory
→ Profile
→ Map
→ Validate
→ Stage
→ Reconcile
→ Approve
→ Cutover
→ Verify
→ Archive
```

No legacy source is deleted during these stages.
