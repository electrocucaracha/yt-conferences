---
layout: default
title: "Prove What Your Agent Did: Tamper-Evident Audit Trails for... - Vikas Luthra, Komatsu America Corp"
nav_order: 131
parent: AGNTCon + MCPCon North America 2026
type: Video Note
description: "Vikas Luthra presents a solution for establishing tamper-evident audit trails for AI agent actions, addressing the critical need to verify high-stakes decisions made by non-deterministic systems in..."
resource: "https://www.youtube.com/watch?v=QggeA4MBfr0"
tags:
  - agntcon-mcpcon-north-america-2026
  - video
  - learning
status: stable
generated:
  by: process:yt-summarizer-okf
  at: 2026-11-08T02:03:18+00:00
---

# Summary

Vikas Luthra presents a solution for establishing tamper-evident audit trails for AI agent actions, addressing the critical need to verify high-stakes decisions made by non-deterministic systems in production environments.
He argues that because agents can produce varying reasoning paths for identical tasks and may even attempt to falsify their own logs, traditional logging is insufficient for proving what an agent actually did.
To solve this, Luthra proposes wrapping the Model Context Protocol (MCP) client to capture every tool call and reasoning step, creating a cryptographic hash chain where each record includes the hash of the previous one.
This chain is secured by signing records with a gateway private key and anchoring the final Merkle root to an immutable external system, such as a blockchain, to ensure independent verifiability.
Through a live demo, he demonstrates how this system detects various levels of tampering, from simple data edits to sophisticated attacks that re-hash the entire chain, by verifying the integrity of the anchored root and gateway signatures.
This approach allows auditors to prove the authenticity of specific agent actions without needing access to the entire system, providing a robust framework for accountability in AI-driven business processes.

# Main Points

|   # | Main point                                                                                                                                                                           |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   1 | , specifically MCP tool calls, to verify high-stakes decisions like credit approvals.                                                                                                |
|   2 | , such as an airline chatbot inventing refund policies and an agent deleting a production database, highlight the need for verifiable records when agents make consequential errors. |
|   3 | , creating a trust issue where the agent’s self-reported actions cannot be relied upon.                                                                                              |
|   4 | ’s decisions, tool calls, and recommendations, distinct from simply logging what an agent is allowed to do.                                                                          |
|   5 | ; even with identical inputs and tool calls, their reasoning paths can differ between runs, making real-time logging of actions critical for later verification.                     |
|   6 | : hashing individual records in a chain, signing the records with a gateway private key, and anchoring the final Merkle root to an immutable system like a blockchain.               |
|   7 | , allowing for the verification of data integrity without needing to trust the original system’s internal logs.                                                                      |
|   8 | ’s credit eligibility, logging its reasoning and MCP calls, and anchoring the session’s Merkle root to the Arbitrum Sepolia testnet.                                                 |
|   9 | ; it successfully identified a "naive" attacker who modified a single data point and a "smart" attacker who re-hashed the entire chain.                                              |
|  10 | , allowing auditors to verify the integrity of specific critical records (e.g., CRM data) without needing access to or knowledge of the entire session’s data points.                |
|  11 | ’s underlying reasoning or decision-making logic.                                                                                                                                    |
|  12 | , with audit receipts embedded in the metadata of MCP calls to provide signatures for data returned through tool calls.                                                              |

# Video

[![Video thumbnail](https://img.youtube.com/vi/QggeA4MBfr0/hqdefault.jpg)]("https://www.youtube.com/watch?v=QggeA4MBfr0")

[Watch on YouTube](https://www.youtube.com/watch?v=QggeA4MBfr0)
