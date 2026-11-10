---
layout: default
title: "The Agentic Orchestration Stack: Durability, Guardrails, and Attestation - Yaron Schneider, Diagrid"
nav_order: 33
parent: AGNTCon + MCPCon North America 2026
type: Video Note
description: "Yaron Schneider, CTO of Dial Grid, argues that deploying AI agents in production requires robust guardrails to address the inherent unreliability of distributed systems and the probabilistic nature..."
resource: "https://www.youtube.com/watch?v=qGG4QzZ_Hzk"
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

Yaron Schneider, CTO of Dial Grid, argues that deploying AI agents in production requires robust guardrails to address the inherent unreliability of distributed systems and the probabilistic nature of LLMs.
He emphasizes that traditional software reliability challenges are amplified by AI, necessitating a focus on durable execution to prevent costly restarts, strict authentication and authorization to manage complex identity chains, and verifiable execution to provide tamper-evident proof of actions for regulatory compliance.
Schneider warns against relying solely on prompts or centralized AI gateways for security, advocating instead for a hybrid architecture where deterministic workflow engines orchestrate autonomous agents, enforce policy checks, and cryptographically sign every step of the execution process.
He recommends using open-source tools like Dapr to implement these distributed, secure, and auditable workflows, ensuring that agents can survive failures, maintain state, and operate within defined boundaries without compromising system integrity or security.

# Main Points

|   # | Main point                                                                                                                                                  |
| --: | ----------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | # Key Points                                                                                                                                                |
|   2 | • Yaron Schneider is CTO and co-founder of Dial Grid, president of Agent AI Foundation's workflows working group                                            |
|   3 | • Need to establish security guardrails in production before deploying AI agents autonomously                                                               |
|   4 | • AI promise: increased autonomy enables more automation and higher ROI                                                                                     |
|   5 | • Most AI-native companies focus on intelligence layer (reasoning, planning, decision-making) but haven't solved real-world production problems             |
|   6 | • LLMs are probabilistic systems—same prompt produces different executions; need to ensure agents behave correctly                                          |
|   7 | • Agent workflows should balance deterministic controls with autonomous capabilities, not be purely deterministic or fully autonomous                       |
|   8 | • Three critical questions before deploying agents: Can it survive failure? Are guardrails in place? Can execution be certified?                            |
|   9 | • Durable execution essential: if agent fails mid-task, must resume exactly where it left off, not restart from beginning                                   |
|  10 | • Don't treat prompts as security boundaries; implement deterministic validation steps after agent reasoning                                                |
|  11 | • Gateways are high-value attack targets; distribute risk by running multiple instances per domain instead of centralized single gateway                    |
|  12 | • Verifiable execution: cryptographically sign and certify every step to create tamper-proof audit trail for regulators                                     |
|  13 | • Implement: workflow engine supporting deterministic steps + autonomous agent calls + policies layer + cryptographic verification                          |
|  14 | • Dapr (CNCF project) provides distributed workflow engine with durable execution, cryptographic verification, policy middleware, and end-to-end encryption |
|  15 | • Observability must enable proving agent identity, authorization, and system actions; logs alone insufficient—need cryptographic attestation               |

# Video

[![Video thumbnail](https://img.youtube.com/vi/qGG4QzZ_Hzk/hqdefault.jpg)](https://www.youtube.com/watch?v=qGG4QzZ_Hzk)

[Watch on YouTube](https://www.youtube.com/watch?v=qGG4QzZ_Hzk)
