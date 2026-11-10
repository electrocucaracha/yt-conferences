---
layout: default
title: "1,149 Hackers Tried to Break Our AI Agent Guardrails. 0 Succeeded. Here's... - Uchi Uchibeke, APort"
nav_order: 38
parent: AGNTCon + MCPCon North America 2026
type: Video Note
description: "Uchi, founder of the recently sold payment company Chimoney, introduces Airport, a platform that authorizes AI agents before they act using the Open Agent Passport specification."
resource: "https://www.youtube.com/watch?v=Tw2gjRyoBMY"
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

Uchi, founder of the recently sold payment company Chimoney, introduces Airport, a platform that authorizes AI agents before they act using the Open Agent Passport specification.
This open standard allows organizations to issue digital passports to AI agents, defining their permissions, capabilities, and limits, including a kill switch to prevent rogue behavior.
In a live demo, the speaker illustrates how a customer support agent is authorized to access data but denied the ability to issue unauthorized refunds, with all actions logged for compliance.
To demonstrate the necessity of a deterministic policy layer over simple prompt instructions, Airport conducted a capture-the-flag challenge and benchmarked 14 AI models across eight labs using over 250,000 evaluations.
The results showed that while models alone were vulnerable to human-authored attacks, the addition of the authorization layer reduced security breaches to zero, highlighting the critical need for robust, real-time enforcement mechanisms in enterprise AI deployments.

# Main Points

|   # | Main point                                                                                                                                         |
| --: | -------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | , Uchi, built and sold Chimoney and is now building Airport, a company that authorizes AI agents before they act.                                  |
|   2 | (identifying who is calling), authentication (verifying identity), and authorization (deciding what actions are allowed).                          |
|   3 | , even if they possess valid API keys.                                                                                                             |
|   4 | (OAP) specification, an open standard for issuing passports to AI agents that define permissions, capabilities, limits, and include a kill switch. |
|   5 | ’s passport before any action is executed.                                                                                                         |
|   6 | , but a refund request was denied because the passport lacked refund capabilities.                                                                 |
|   7 | , including denials and reasons, are logged in an audit trail and verified by Airport’s hosted verifier.                                           |
|   8 | ’s tool-use hooks, checking permissions before file access, site visits, or tool calls.                                                            |
|   9 | (MDM) to push passports to all team devices, providing real-time visibility into developer agent activities.                                       |
|  10 | , which cascades the suspension to all agent instances across devices to stop rogue behavior.                                                      |
|  11 | ; a deterministic policy layer is required to enforce rules that models might otherwise ignore.                                                    |
|  12 | ; without enforcement, attackers succeeded in 588 of 788 attempts at Level 1.                                                                      |
|  13 | , the breach rate dropped to zero, proving the effectiveness of the enforcement layer.                                                             |
|  14 | ,371 human-authored attacks against 14 AI models from eight labs, resulting in over 250,000 evaluations.                                           |
|  15 | , models without an enforcement layer experienced breaches in 111 attacks, while models with the OAP policy layer had zero breaches.               |
|  16 | , GitHub Guard, and software delivery, offering policies for command execution, task completion, and data access.                                  |
|  17 | , including Crew AI, LangChain, and multiple coding harnesses.                                                                                     |
|  18 | , with a goal to maintain performance around 10 milliseconds to avoid bottlenecks.                                                                 |
|  19 | , open standards like OAP are essential to prevent rogue behavior and ensure secure agent authorization.                                           |

# Video

[![Video thumbnail](https://img.youtube.com/vi/Tw2gjRyoBMY/hqdefault.jpg)](https://www.youtube.com/watch?v=Tw2gjRyoBMY)

[Watch on YouTube](https://www.youtube.com/watch?v=Tw2gjRyoBMY)
