---
layout: default
title: "Who, May, Did: Composing Agent Identity with Verifiable... - Steven Mih, Action State Group, Inc."
nav_order: 66
parent: AGNTCon + MCPCon North America 2026
type: Video Note
description: 'The speaker introduces the "Evidence Book," an open-source project launched to address the growing need for verifiable records as AI agents transition from internal assistance to external, high-sta...'
resource: "https://www.youtube.com/watch?v=Fo0Qi6NqAeE"
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

The speaker introduces the "Evidence Book," an open-source project launched to address the growing need for verifiable records as AI agents transition from internal assistance to external, high-stakes actions.
The core component, the Agent Action Capsule, is an IETF standard that creates tamper-evident, cryptographic records of specific agent actions, such as tool calls and conversations, to solve issues where agents might rewrite logs or act without proper oversight.
These capsules are aggregated into the Evidence Book, which provides a standardized, semantic layer that allows different parties—such as customers, auditors, and regulators—to verify agent behavior and reconcile transactions without relying on self-reported data or custom, incompatible logs.
Additionally, the system incorporates "Terms Packs," which are versioned rubrics used to judge agent outputs against specific compliance requirements, such as the EU AI Act, ensuring that agents remain within defined operational boundaries.
The solution is designed to be decentralized and interoperable, supporting protocols like A2A and MCP, and allows for bilateral verification where both parties in a transaction can independently confirm the integrity of the shared evidence, thereby establishing trust in autonomous agent interactions.

# Main Points

|   # | Main point                                                                                                                                                                                                                                                 |
| --: | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | :** As AI agents shift from assisting to acting autonomously (especially externally), traditional logs are insufficient because agents can rewrite or omit them, and self-reported metrics lack independent verification.                                  |
|   2 | :** The presentation introduces a three-part open-source framework for agent identity and trust: Agent Action Capsules, Evidence Books, and Terms Packs.                                                                                                   |
|   3 | :** An IETF standard (RFC 9943) that creates a cryptographic, tamper-evident record of specific agent actions (tool calls, conversations). It captures identity, intent, and execution details at the moment of action.                                    |
|   4 | :** A standardized, append-only ledger that bundles multiple Action Capsules to provide semantic context and a verifiable history. It allows for bilateral reconciliation between parties (e.g., user and service provider) without exposing private data. |
|   5 | :** Versioned rubrics used to judge agent performance against specific criteria (e.g., compliance, loyalty, task completion). These are sealed into the Evidence Book to enable objective grading and compliance checking.                                 |
|   6 | :** The system supports multiple assurance levels:                                                                                                                                                                                                         |
|   7 | :** Local inclusion proofs that no data leaves the machine.                                                                                                                                                                                                |
|   8 | :** Optional third-party verification for higher assurance.                                                                                                                                                                                                |
|   9 | :** A service that recomputes and stamps the cryptographic math for the highest level of trust.                                                                                                                                                            |
|  10 | & Privacy:** The architecture is fully decentralized with no central authority. Data remains local unless explicitly shared. Users can request evidence from strangers to verify past performance (e.g., via a "Nanda Index" for agent discovery).         |
|  11 | :** The system supports A2A protocols and integrates with existing agent harnesses (LangGraph, CrewAI, Goose) via adapters or MCP. It is designed to be developer-friendly, allowing LLMs to trigger capsule creation for consequential actions.           |
|  12 | :**                                                                                                                                                                                                                                                        |
|  13 | :** Verifying that an agent performed a specific action (e.g., rebooking a flight) as agreed by both parties.                                                                                                                                              |
|  14 | :** Automating checks for regulations like the EU AI Act (e.g., Article 5 on manipulation) by applying Terms Packs to Evidence Books.                                                                                                                      |
|  15 | :** Agents can share their verified history of successful transactions to build trust with new counterparties.                                                                                                                                             |
|  16 | :** All components (specs, code, Evidence Book) are open source and free to use. Countersigning is currently free. Resources are available at agentactioncapsule.org and actionstate.ai.                                                                   |

# Video

[![Video thumbnail](https://img.youtube.com/vi/Fo0Qi6NqAeE/hqdefault.jpg)](https://www.youtube.com/watch?v=Fo0Qi6NqAeE)

[Watch on YouTube](https://www.youtube.com/watch?v=Fo0Qi6NqAeE)
