# ÒsánVault Country Token Architecture

## Decision direction

ÒsánVault will distinguish between a **platform token** and a future family of **country-specific ecosystem tokens**.

### Platform token

**OSANV** remains the canonical ÒsánVault Africa platform token.

Its role is platform-wide utility, governance/staking where approved, and the common settlement/exchange interface for supported ecosystem functionality.

### Country ecosystem tokens

Country-specific tokens may represent a national ÒsánVault ecosystem or country participation layer. Examples discussed for the future architecture include:

- **NET** — Nigeria ecosystem token designation, retained as a future/currently-unissued country-token namespace rather than the old "NigeriaEstate Token" concept.
- **GET** — Ghana ecosystem token designation.

These are conceptual country-token identifiers at this stage. No country token should be treated as deployed, issued, redeemable, or financially active until a separate approved specification and deployment record exists.

## Critical distinction: old NET vs future NET

The historical **NET / NigeriaEstate Token** concept is deprecated as the original ÒsánVault platform-token design.

However, the symbol **NET** may be reserved/reused as the Nigeria country-token designation in the future, subject to legal, trademark, namespace, and technical review.

Therefore repository migration must NOT blindly delete every NET reference.

Every NET occurrence must be classified as one of:

1. historical platform-token concept;
2. migration/history artifact;
3. future Nigeria country-token namespace;
4. deployed/live asset reference (which must be independently verified);
5. unrelated identifier.

## Target ecosystem model

```text
                         ÒSÁNVAULT PLATFORM
                                |
                              OSANV
                     Platform-wide utility layer
                                |
          +---------------------+---------------------+
          |                     |                     |
         NET                   GET                  FUTURE
       Nigeria                Ghana              Country Token
          |                     |                     |
          +---------------------+---------------------+
                                |
                         Country ecosystems
                                |
                         Platform staking /
                       approved swap mechanisms
```

## Exchange architecture

Country tokens and OSANV must not be conflated.

A future country-token exchange may support a controlled relationship such as:

`Country Token <-> OSANV`

The exact mechanism (AMM, treasury-mediated conversion, order book, or another regulated structure) is deliberately unspecified until the token economics, liquidity model, legal classification, custody model, and security design are approved.

## Staking model

The intended conceptual model is:

- OSANV is the platform-wide staking/utility token.
- Country tokens provide country-specific ecosystem representation/utility where approved.
- A user may acquire or convert an eligible country token into OSANV for platform-wide staking/utility functions through an approved mechanism.
- Country-token balances remain distinct from OSANV balances.
- Token balances remain distinct from the internal treasury/accounting ledger.

## Country token registry

The canonical platform should eventually maintain a registry containing:

- country code
- token name
- symbol
- status
- network
- contract address
- issuer/issuer entity
- supply policy
- decimals
- legal/compliance status
- activation date
- conversion policy
- treasury/liquidity policy
- governance relationship

## Current status

No country token should be represented as deployed merely because its symbol appears in architecture documents. The current planning state is **design/reserved namespace**.

OSANV remains the only canonical ÒsánVault platform token at this stage.
