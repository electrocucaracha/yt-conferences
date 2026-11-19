---
layout: default
title: "Architecting Agentic Commerce: The Universal Commerce... - Amit Handa & Shonan Shah, Google"
nav_order: 45
parent: AGNTCon + MCPCon North America 2026
type: Video Note
description: "Amit and Shona from Google present a framework for architecting safe agent e-commerce by following a single purchase end-to-end using two open protocols: UCP for commerce conversations and AP2 for ..."
resource: "https://www.youtube.com/watch?v=WRnh_fAWhyY"
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

Amit and Shona from Google present a framework for architecting safe agent e-commerce by following a single purchase end-to-end using two open protocols: UCP for commerce conversations and AP2 for payment authorization.
UCP solves the combinatorial explosion of agent-merchant integrations by allowing both parties to publish profiles that define shared capabilities, enabling standardized interactions for identity verification, catalog browsing, cart management, and checkout.
The system ensures security by keeping the merchant as the authoritative source of truth for prices and inventory, while payment is processed via tokens from credential providers, ensuring PCI DSS compliance without exposing raw card data.
To address the risk of prompt injection in autonomous scenarios, AP2 introduces cryptographic mandates that act as signed permission slips, allowing users to pre-authorize specific actions within strict constraints.
This design ensures that even if an agent is tricked, deterministic code checks against the signed mandate will block unauthorized transactions, providing a verifiable chain of custody and replayable evidence for dispute resolution.

# Main Points

|   # | Main point                                                                                                                                           |
| --: | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | # Key Points                                                                                                                                         |
|   2 | • Amit and Shona work at Google on e-commerce and payments respectively                                                                              |
|   3 | • UCP protocol handles e-commerce conversations and actions; AP2 handles authorized payment proof and payments                                       |
|   4 | • E-commerce with agents requires merchants to answer: who is the agent, what can we do together, did the human request this, and who is responsible |
|   5 | • Multiple agents and merchants create an N×M integration problem solved by shared protocols (N+M solution)                                          |
|   6 | • E-commerce ecosystem includes agent platforms, businesses, credential providers (wallets), and payment service providers                           |
|   7 | • UCP agent profiles carry identity headers; merchants verify domain ownership via HTTPS                                                             |
|   8 | • Merchants publish business profiles describing capabilities, services, endpoints, and payment handlers                                             |
|   9 | • Agents and merchants negotiate common capabilities through profile intersection                                                                    |
|  10 | • UCP supports namespaces allowing custom extensions beyond protocol specifications                                                                  |
|  11 | • "Ask" capability enables natural language questions beyond catalog; never acts independently                                                       |
|  12 | • Catalog provides flexible information sourcing (external feeds or UCP capability)                                                                  |
|  13 | • Cart capability provides estimates and continuation URLs without finalizing transactions                                                           |
|  14 | • Payment designed as state machine handling errors and recovery paths                                                                               |
|  15 | • Merchants remain authoritative; agents only render, never calculate prices                                                                         |
|  16 | • Payment handlers defined by wallet providers, hosted on their domains, not in UCP spec                                                             |
|  17 | • No card numbers circulate; agents obtain tokens from credential providers using merchant's handler configuration                                   |
|  18 | • AP2 introduces "mandate" concept: cryptographically signed digital authorization                                                                   |
|  19 | • Open mandate set before purchase by user; closed mandate created at transaction time                                                               |
|  20 | • Payment mandate visible to merchants; payment mandate visible to payment entities                                                                  |
|  21 | • User signatures occur on trusted surfaces (wallet apps), not LLMs                                                                                  |
|  22 | • SD-JWT format uses selective disclosure so each entity sees only relevant details                                                                  |
|  23 | • All verifications use deterministic code, never agents                                                                                             |
|  24 | • Prompt injection attacks fail because verification rejects rule violations                                                                         |
|  25 | • Each party signs receipts creating auditable chain from request through authorization                                                              |
|  26 | • Protocol agnostic to transport layer (REST, MCP)                                                                                                   |
|  27 | • Six key lessons: agent identity, capability discovery, information requests, merchant authority, token-only payments, assume model compromise      |
|  28 | • Specifications at ucp.dev and AP2 on GitHub with SDKs                                                                                              |

# Video

[![Video thumbnail](https://img.youtube.com/vi/WRnh_fAWhyY/hqdefault.jpg)](https://www.youtube.com/watch?v=WRnh_fAWhyY)

[Watch on YouTube](https://www.youtube.com/watch?v=WRnh_fAWhyY)
