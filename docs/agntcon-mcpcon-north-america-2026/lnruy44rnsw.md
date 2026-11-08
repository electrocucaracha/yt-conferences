---
layout: default
title: "Engineering Multiagent Systems - Munindar Singh, North Carolina State University"
nav_order: 23
parent: AGNTCon + MCPCon North America 2026
type: Video Note
description: "Professor Munindar Singh from NC State University presents a framework for engineering multi-agent systems that integrates formal social norms with Large Language Models (LLMs) to overcome the limi..."
resource: "https://www.youtube.com/watch?v=lnRUY44RNSw"
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

Professor Munindar Singh from NC State University presents a framework for engineering multi-agent systems that integrates formal social norms with Large Language Models (LLMs) to overcome the limitations of traditional centralized computing.
He argues that current approaches, such as finite state machines and complex message schemas, lack semantic meaning and struggle with asynchronous interactions, whereas his proposed "social machine" model captures the meaning of interactions through logical commitments, authorizations, and prohibitions.
By using a declarative protocol language that defines social authority and causal validity, the system allows agents to reason about complex, nested commitments and handle asynchronous events naturally, reducing the need for rigid, predefined execution paths.
Singh demonstrates that this neuro-symbolic approach enables LLMs to act as flexible reasoning engines that can interpret user goals, select appropriate protocols, and make rational decisions while maintaining interoperability with existing standards like Google’s Universal Commerce Protocol.
Ultimately, this method provides a robust foundation for human-agent collaboration, allowing for accountability, norm violation management, and scalable multi-agent workflows that are both semantically correct and operationally efficient.

# Main Points

|   # | Main point                                                                                                                                                                                                                                                               |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   1 | : Engineering multi-agent systems to restore flexible, decentralized human-like interactions, moving beyond centralized server-based request-response models that limit autonomy.                                                                                        |
|   2 | : Effective protocols must be both **operational** (regulated execution) and **constitutive** (capturing semantic meaning), with the latter leveraging LLM reasoning capabilities.                                                                                       |
|   3 | : Traditional computing struggles with asynchronous calls and state management ("callback hell"); the proposed approach allows agents to naturally receive and process delayed responses without ad-hoc state recreation.                                                |
|   4 | (FSMs)**: Current protocols (e.g., NetBill, HL7) rely on uninterpreted FSM states, lacking semantic correctness. They fail to account for autonomous deviations (e.g., early payment) and generate excessive complexity.                                                 |
|   5 | & Norms**: Replace uninterpreted states with **social relationships** (e.g., commitments, authorizations). A "social machine" uses domain semantics (like money owed) to reason about state transitions logically.                                                       |
|   6 | : Commitments are formal technical entities with defined lifecycles (created, active, satisfied, violated, released). They support autonomy, allowing agents to create, cancel, or violate promises based on business logic.                                             |
|   7 | & Authority**: Agents must not be forced into commitments by others (violating autonomy). The framework defines **say-so** (social authority) to determine who can decide specific parameters (e.g., price, item) and which actions are mutually exclusive.              |
|   8 | : A compact, declarative language specifies actions, conflicts, and authority. This generates hundreds of valid execution paths, supports formal verification (safety/liveness), and reduces agent code size by orders of magnitude compared to schema-heavy approaches. |
|   9 | : Combines a symbolic layer (for precise, unambiguous logical reasoning about norms and commitments) with LLMs (for flexible goal interpretation, protocol selection, and common-sense reasoning).                                                                       |
|  10 | : The framework can formalize existing standards (e.g., Google’s Universal Commerce Protocol) to expose hidden correctness criteria and enable smaller, more efficient agents that interoperate with larger reference implementations.                                   |
|  11 | & Risks**: LLMs select protocols based on user goals and can combine multiple protocols. However, they require symbolic guidance to avoid syntax errors, hallucinations, and lack of common sense (e.g., purchasing a pen for $10,000).                                  |
|  12 | : Correctness properties depend on who is committing. For example, if X must arrive before Y, the behavior of X or Y changes based on which party holds the commitment, affecting accountability and interaction strategies.                                             |
|  13 | : Agents are permitted to knowingly violate norms if it serves business interests (e.g., airline overbooking), provided the system can reason about the consequences and penalties.                                                                                      |

# Video

[![Video thumbnail](https://img.youtube.com/vi/lnRUY44RNSw/hqdefault.jpg)]("https://www.youtube.com/watch?v=lnRUY44RNSw")

[Watch on YouTube](https://www.youtube.com/watch?v=lnRUY44RNSw)
