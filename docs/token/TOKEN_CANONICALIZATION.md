# ÒsánVault Token Canonicalization

## Status

Canonical token designation: **OSANV**.

Deprecated historical designation: **NET / NigeriaEstate Token**.

This document establishes the migration rule for the ÒsánVault Africa consolidation. No new platform component may introduce NET as a current token name, symbol, contract identifier, or tokenomics designation.

## Evidence

The canonical `osanvault-africa` application contains an explicit `OSANV_TOKEN_ADDRESS`, OSANV governance parameters, and OSANV staking configuration. The tokenomics UI identifies the native token as OSANV with a stated total supply of 1,000,000,000 OSANV. The repository also contains OsanVToken and IOSANVToken contract artifacts.

## Rules

1. OSANV is the only current token designation.
2. NET is historical/deprecated terminology.
3. Historical NET references must not be blindly deleted or globally renamed because they may belong to migration artifacts or historical records.
4. Any legacy NET record must carry explicit deprecated/historical semantics when migrated.
5. No new API, database model, UI, treasury component, or smart-contract integration may use NET as the current token identity.
6. Token balances must remain distinct from the authoritative internal treasury ledger.
7. Contract addresses must be sourced from a controlled contract registry and environment configuration; zero-address placeholders are not production deployments.

## Canonical naming

- Display name: OSANV
- Symbol: OSANV
- Historical name: NET / NigeriaEstate Token
- Historical status: deprecated

## Next audit

Before tokenization or treasury implementation, audit all accessible ÒsánVault repositories for NET, NigeriaEstate, OSANV, OsanVToken, contract addresses, chain IDs, tokenomics, staking, governance, and deployment references. The result must distinguish current production-intended artifacts from migration/history artifacts.