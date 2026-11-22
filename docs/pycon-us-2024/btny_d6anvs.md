---
layout: default
title: "Sponsor Presentations - Blockchain speaks Python: How to use it on Algorand to build real solutions"
nav_order: 36
parent: PyCon US 2024
type: Video Note
description: "The presentation introduces blockchain as a decentralized, trustless, and immutable distributed ledger technology that enables verifiable data and disintermediation through consensus mechanisms lik..."
resource: "https://www.youtube.com/watch?v=BTny_d6AnVs"
youtube_stats:
  view_count: 323
  like_count: 8
  channel_subscriber_count: 34500
tags:
  - pycon-us-2024
  - video
  - learning
status: stable
generated:
  by: process:yt-summarizer-okf
  at: 2026-11-22T10:18:11+00:00
---

# Summary

The presentation introduces blockchain as a decentralized, trustless, and immutable distributed ledger technology that enables verifiable data and disintermediation through consensus mechanisms like Proof of Work and Proof of Stake.
It highlights real-world applications on the Algorand network, including AGR Token for agricultural asset tokenization, Hasab Pay for digital payments in Afghanistan, Travel X for airline ticketing, Lofty for fractionalized real estate, and Folks Finance for decentralized finance instruments like flash loans.
The speaker explains that Algorand addresses the blockchain trilemma by balancing decentralization, security, and scalability, featuring instant finality and high throughput via its Pure Proof of Stake consensus and Algorand Virtual Machine (AVM).
A significant focus is placed on the Algorand Python tooling, which allows developers to write smart contracts in native Python that compile to the AVM, utilizing the Algorand Kit CLI for project setup, testing, and deployment.
The session concludes with a code walkthrough of a digital marketplace smart contract, demonstrating how Python classes define on-chain state and logic, and how automated client generation simplifies integration for developers.

# Main Points

|   # | Main point                                                                                                                                                                                    |
| --: | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Blockchain is a distributed ledger technology that is decentralized, trustless, and immutable, ensuring a single source of truth without relying on centralized servers.                      |
|   2 | The network achieves consensus through nodes that verify data independently, allowing anyone to run a node and check the validity of the ledger's state.                                      |
|   3 | Transactions are the fundamental units of state change, which are grouped into blocks to improve efficiency and linked via cryptographic hashes to create an immutable chain.                 |
|   4 | Consensus mechanisms like Proof of Work and Proof of Stake solve the problem of who has the right to add data to the ledger, removing the need to trust individual counterparties.            |
|   5 | Proof of Work requires solving compute-intensive challenges to add blocks, while Proof of Stake requires holding network tokens, aligning incentives to prevent malicious behavior.           |
|   6 | AgriToken demonstrates tokenization by digitizing agricultural crops in Latin America, allowing farmers to access liquidity and loans through digital representations of their assets.        |
|   7 | Hasab Pay uses Algorand as infrastructure for digital payments in Afghanistan, facilitating bill payments and peer-to-peer transfers while supporting UN World Food Program aid distribution. |
|   8 | TravelX leverages non-fungible tokens to create a peer-to-peer marketplace for airline tickets, reducing customer service costs and enabling easy resale without airline involvement.         |
|   9 | Lofty enables fractionalized real estate investment by allowing users to buy property shares with small amounts, granting them ownership and voting rights through tokenized LLC interests.   |
|  10 | Folks Finance illustrates decentralized finance by offering lending, borrowing, and flash loans, allowing users to access capital atomically without trusting traditional banks.              |
|  11 | Blockchain generations have evolved from Bitcoin's focus on digital currency to Ethereum's smart contracts, with Algorand focusing on scalability and solving the blockchain trilemma.        |
|  12 | The blockchain trilemma involves balancing decentralization, security, and scalability, with Algorand claiming to achieve a strong balance of all three aspects.                              |
|  13 | Algorand uses a pure proof of stake consensus mechanism with verifiable random functions to select participants for adding blocks, ensuring fair and verifiable randomness.                   |
|  14 | The Algorand Virtual Machine executes smart contracts using a limited instruction set optimized for blockchain, supporting operations from simple arithmetic to advanced cryptography.        |
|  15 | Algorand offers a 2.8-second block time, instant finality, and a throughput of approximately 10,000 transactions per second, ensuring fast and irreversible confirmations.                    |
|  16 | Algorand prioritizes consistency over availability based on the CAP theorem, meaning blocks are never reverted even if the network experiences partitions, unlike some other chains.          |
|  17 | Developers can build smart contracts and applications using Python, with Algorand Python compiling native Python code to run on the Algorand Virtual Machine.                                 |
|  18 | Algorand Kit is a command-line tool that simplifies project creation, environment setup, and deployment, while Algorand Utils provides libraries for interacting with the chain.              |
|  19 | Smart contracts are defined using Python classes inheriting from ARC4 standards, allowing developers to write logic in standard Python syntax that is compiled for the AVM.                   |
|  20 | Atomic transactions ensure that multiple operations, such as payments and asset transfers, happen together or not at all, preventing partial failures in complex interactions.                |
|  21 | Developers can test contracts using Pytest and a local network instance provided by Algorand Kit, which simulates the blockchain environment without requiring real fees.                     |
|  22 | Algorand Kit automatically generates client code from contract definitions, enabling seamless integration of smart contract methods into frontend, backend, or test code.                     |

# Video

[![Video thumbnail](https://img.youtube.com/vi/BTny_d6AnVs/hqdefault.jpg)](https://www.youtube.com/watch?v=BTny_d6AnVs)

[Watch on YouTube](https://www.youtube.com/watch?v=BTny_d6AnVs)
