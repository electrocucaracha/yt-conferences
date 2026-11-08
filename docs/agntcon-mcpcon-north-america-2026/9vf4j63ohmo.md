---
layout: default
title: "How AT&T Is Building an Agentic Front... Natalie G., Sherman B., Emily W., Hector T. & Prateek B."
nav_order: 5
parent: AGNTCon + MCPCon North America 2026
type: Video Note
description: "AT&T is developing an agentic front door for enterprise HR to streamline complex, siloed processes for its 130,000 employees by replacing manual searches with a unified system that executes tasks r..."
resource: "https://www.youtube.com/watch?v=9vF4j63OHmo"
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

AT&T is developing an agentic front door for enterprise HR to streamline complex, siloed processes for its 130,000 employees by replacing manual searches with a unified system that executes tasks rather than just providing information.
The solution utilizes a multi-agent architecture featuring "constrained deep agents" that balance autonomy with strict guardrails, ensuring reproducibility, auditability, and compliance through deterministic stages and independent enforcement mechanisms.
To address scaling challenges, the team evolved their orchestration strategy to a vector-based routing system paired with an agent registry, allowing for efficient intent detection and dynamic workflow management across various HR domains.
The user experience is designed to accommodate diverse AI literacy levels by combining natural language processing with adaptive cards, creating a seamless interface that guides users through complex workflows while maintaining high standards for safety and human-in-the-loop approval for high-risk actions.
Key lessons from the project emphasize the necessity of continuous stakeholder alignment, iterative development, and early testing to navigate the rapidly evolving landscape of enterprise AI and ensure the system remains trusted and effective for end users.

# Main Points

|   # | Main point                                                                                                                                                                   |
| --: | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | &T is building a unified "agentic front door" for HR to replace manual, siloed processes for its 130,000 employees.                                                          |
|   2 | (e.g., coding time off) rather than just providing information, currently supporting 10 workflows with a goal of 70.                                                         |
|   3 | ; the team emphasizes iterative development and constant flexibility to maintain a shared vision.                                                                            |
|   4 | "constrained deep agents" that balance autonomy with rigid, procedural stages to ensure reproducibility, traceability, and auditability required by enterprise stakeholders. |
|   5 | , tool gating for high-risk actions, and delegated scopes where tokens never reside with the agent to ensure secure execution.                                               |
|   6 | "System 1" approach using vector-based routing and minimal LLM calls to improve scalability and reduce latency.                                                              |
|   7 | , enabling the orchestrator to automatically discover intents and index tools.                                                                                               |
|   8 | , creating a tamper-proof ledger for compliance and auditability.                                                                                                            |
|   9 | , ensuring a unified interaction style regardless of the underlying system.                                                                                                  |
|  10 | , using static questions and clarifying prompts to guide users who are unfamiliar with prompting.                                                                            |
|  11 | ; the team optimizes through parallelization and adjusted reasoning levels.                                                                                                  |
|  12 | , injecting context back into the thread only when necessary for execution.                                                                                                  |
|  13 | , involving testers early to catch edge cases, and adopting a top-down approach to define outcomes before building tools.                                                    |

# Video

[![Video thumbnail](https://img.youtube.com/vi/9vF4j63OHmo/hqdefault.jpg)]("https://www.youtube.com/watch?v=9vF4j63OHmo")

[Watch on YouTube](https://www.youtube.com/watch?v=9vF4j63OHmo)
