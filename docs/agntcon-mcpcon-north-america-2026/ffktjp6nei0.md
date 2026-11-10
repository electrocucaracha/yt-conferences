---
layout: default
title: "The Restraint Pattern: A Reliability Model for Agents That Act in Public - Bharat Patel, Independent"
nav_order: 143
parent: AGNTCon + MCPCon North America 2026
type: Video Note
description: 'Bharat Patel presents the "restraint pattern," a design framework for customer-facing AI agents that prioritizes reliability and trust over simple uptime by disciplining when agents should answer v...'
resource: "https://www.youtube.com/watch?v=fFKtjp6neI0"
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

Bharat Patel presents the "restraint pattern," a design framework for customer-facing AI agents that prioritizes reliability and trust over simple uptime by disciplining when agents should answer versus when they should escalate to humans.
The core thesis is that agents should act as "first responders" grounded in verifiable sources rather than "resolvers" of high-stakes judgment calls, thereby preventing costly errors like confident misinformation or prompt injection.
The pattern comprises six sub-patterns: a unified routing table to categorize questions and define escalation paths, a one-thread mechanism to ensure consistent answers across duplicate inquiries, a yield protocol to prevent agents from overriding human interventions, a confidence gate that uses composite scoring to block low-quality responses, a zero-blast-radius approach that separates execution from reasoning to mitigate security risks, and a signals-over-logs strategy that feeds structured data to improve reasoning efficiency and safety.
By implementing these mechanisms, organizations can ensure that agents only provide answers when they have high certainty, while seamlessly escalating complex or ambiguous issues to specialized experts, thus maintaining customer confidence in AI systems.

# Main Points

|   # | Main point                                                                                                                                                                                                                                        |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | : For customer-facing agents, reliability is defined by the "restraint pattern"—the discipline to know when to answer with grounded truth and when to escalate to humans or specialized agents, rather than focusing solely on uptime or latency. |
|   2 | : Agents should act as "first responders," not resolvers. They must answer questions grounded in cited sources (runbooks, dashboards) and escalate judgment-based or high-stakes decisions (e.g., killing jobs, declaring incidents) to experts.  |
|   3 | :                                                                                                                                                                                                                                                 |
|   4 | : One Routing Table**:                                                                                                                                                                                                                            |
|   5 | "channel-first" approach where each channel has unique rules.                                                                                                                                                                                     |
|   6 | , correct sources, escalation paths, and confidence thresholds regardless of the input channel.                                                                                                                                                   |
|   7 | , not new agent setups.                                                                                                                                                                                                                           |
|   8 | : The topic classifier is a single point of failure, mitigated by certainty scores.                                                                                                                                                               |
|   9 | : One Thread Pattern**:                                                                                                                                                                                                                           |
|  10 | (text, context, author, time) to identify duplicate questions across channels.                                                                                                                                                                    |
|  11 | , while subsequent threads receive a link to it, maintaining consistency.                                                                                                                                                                         |
|  12 | : Requires tuning similarity cut-offs to avoid merging distinct but similar questions.                                                                                                                                                            |
|  13 | : Yield Pattern**:                                                                                                                                                                                                                                |
|  14 | "human takeover back-off." If a human engages, the agent marks the thread as human-owned and stops generating responses.                                                                                                                          |
|  15 | : Requires a mechanism to summon the agent back if the human requests additional context.                                                                                                                                                         |
|  16 | : Confidence Gate**:                                                                                                                                                                                                                              |
|  17 | , source truth, and retrieval scores against routing table thresholds.                                                                                                                                                                            |
|  18 | , the agent escalates to a human or expert agent with context instead of answering.                                                                                                                                                               |
|  19 | : Zero Blast Radius**:                                                                                                                                                                                                                            |
|  20 | ; these are delegated to tools or second-layer systems.                                                                                                                                                                                           |
|  21 | : Sacrifices full "fix-it-for-me" automation to ensure security in public channels.                                                                                                                                                               |
|  22 | : Signals, Not Logs**:                                                                                                                                                                                                                            |
|  23 | , typed data (e.g., job status, SLA, event counts) instead of raw logs.                                                                                                                                                                           |
|  24 | : Better model reasoning, cost efficiency (fewer tokens), reduced prompt injection risk, and deterministic answers from MCP tools/APIs.                                                                                                           |
|  25 | :                                                                                                                                                                                                                                                 |
|  26 | : The restraint pattern and its six sub-patterns are universal for any public-facing agent system, ensuring customer trust by prioritizing correct, grounded answers over confident guesses.                                                      |

# Video

[![Video thumbnail](https://img.youtube.com/vi/fFKtjp6neI0/hqdefault.jpg)](https://www.youtube.com/watch?v=fFKtjp6neI0)

[Watch on YouTube](https://www.youtube.com/watch?v=fFKtjp6neI0)
