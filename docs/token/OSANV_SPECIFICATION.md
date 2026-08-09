# OSANV Canonical Specification — Architecture Baseline

## Current repository evidence

The `osanvault-africa` repository currently defines OSANV as the native governance and utility token and includes an OSANV token address configuration, OSANV governance parameters, staking configuration, and OSANV tokenomics UI. The contract address in the inspected application is currently the zero address, which indicates a placeholder rather than proof of a deployed production token contract.

## Canonical identity

- Name/designation: OSANV
- Symbol: OSANV
- Historical predecessor: NET / NigeriaEstate Token
- Status of NET: deprecated

## Supply baseline

The current tokenomics implementation states a total supply of 1,000,000,000 OSANV. This is an application-level tokenomics baseline and must not be treated as proof of an on-chain minted supply until the deployment registry and live contract state are independently verified.

## Architecture boundaries

OSANV is a platform token layer. It must not replace the internal financial ledger.

```text
Asset / Offering
      |
      +--> Internal Treasury Ledger  <-- accounting authority
      |
      +--> OSANV Token Layer         <-- token utility / governance / approved representations
      |
      +--> Blockchain Contract       <-- externally verifiable state
```

## Governance and staking

Existing application configuration contains governance and staking parameters. These values require product/legal/security review before being treated as production commitments. They must therefore remain configuration/specification data until the canonical contract registry and approved token policy are established.

## Contract registry requirement

Production contract addresses must be centrally registered with:

- chain
- network/environment
- contract name
- address
- deployment transaction
- deployment commit
- ABI version
- verification status
- deployer/owner controls
- upgradeability model
- effective date

Zero addresses are placeholders and must never be interpreted as deployed contracts.
