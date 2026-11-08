---
layout: default
title: "Breaking the Governance Bottleneck: Why Scaling Control Gets Agents to... - Rania Khalaf, WSO2"
nav_order: 134
parent: AGNTCon + MCPCon North America 2026
type: Video Note
description: "The speaker from a global open-source middleware company discusses the critical challenges of deploying AI agents into production, emphasizing that their probabilistic nature and ability to execute..."
resource: "https://www.youtube.com/watch?v=CrucZZk25n8"
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

The speaker from a global open-source middleware company discusses the critical challenges of deploying AI agents into production, emphasizing that their probabilistic nature and ability to execute actions with side effects make them difficult to govern using traditional deterministic software principles.
To address this, the company advocates for an "agent halo" approach, which involves separating governance controls from the agent’s core logic to create a framework-agnostic layer of safety.
This includes implementing production-grade agent identity, defining granular permissions and scopes, and establishing runtime guardrails for interactions with LLMs and MCP servers.
The presentation highlights their "Agent Manager" platform, which supports observability through OpenTelemetry, custom evaluators, and kill switches to mitigate risks, while also addressing the need to manage third-party agents that interact with enterprise systems.
Ultimately, the speaker argues that proper architectural governance, rather than relying on prompt-based constraints, is essential for ensuring security, accountability, and the safe scaling of agentic workflows.

# Main Points

|   # | Main point                                                                                                                                                                    |
| --: | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | ’s company provides a 100% open-source digital stack for agentic enterprises, including identity, integration, API, and agent platforms, with customers in over 90 countries. |
|   2 | , non-deterministic, and capable of taking actions with side effects at massive scale, unlike deterministic software.                                                         |
|   3 | , leading to unexpected errors despite passing complex benchmarks.                                                                                                            |
|   4 | : pilots stuck due to insufficient governance or rapid deployment without controls leading to security incidents and anxiety.                                                 |
|   5 | , security, and governance concerns, with statistics ranging from 40% to 95% cancellation rates.                                                                              |
|   6 | , have complex identity requirements, and require runtime governance rather than just pre-deployment testing.                                                                 |
|   7 | ; they require middleware that accounts for their nature to prevent damage.                                                                                                   |
|   8 | , creating a "moral crumple zone" where humans are blamed but cannot be held fully responsible for complex system failures.                                                   |
|   9 | "harnesses" and control planes, recognizing that the system surrounding the model significantly impacts outcomes.                                                             |
|  10 | , frameworks, and providers without redefining guardrails for each.                                                                                                           |
|  11 | "Agent Halo" concept involves surrounding the agent with guardrails, identity, permissions, and observability to ensure safety and performance.                               |
|  12 | , providing perimeter guardrails for LLMs, MCP servers, and inbound/egress traffic.                                                                                           |
|  13 | , enabling cryptographically verifiable credentials and role-based access control.                                                                                            |
|  14 | , allowing for trace analysis and the definition of evaluators to monitor agent performance and behavior.                                                                     |
|  15 | : company-wide (e.g., PII masking), specific to an agent (e.g., HIPAA compliance), or specific to tools and endpoints.                                                        |
|  16 | , such as role-based access control, are superior to prompt-based guardrails, which can be ignored or forgotten during context summarization.                                 |
|  17 | , requiring different governance approaches based on the level of control and access available.                                                                               |
|  18 | , it must manage agent identity and access for third-party agents (e.g., OpenClaw, Muse) interacting with its services.                                                       |
|  19 | , requiring businesses to be discoverable and accessible to them through proper API and MCP server configurations.                                                            |
|  20 | ; for example, a robot dog’s normal behavior of taking frequent photos can trigger false positive loop alerts, requiring custom anomaly detection.                            |
|  21 | , data, observability, and workflow planes to allow flexible deployment across private data centers and public clouds.                                                        |
|  22 | , including MCP, A2A, OAuth, and OpenCori, which is donated to the CNCF and provides sandboxing for agents.                                                                   |

# Video

[![Video thumbnail](https://img.youtube.com/vi/CrucZZk25n8/hqdefault.jpg)]("https://www.youtube.com/watch?v=CrucZZk25n8")

[Watch on YouTube](https://www.youtube.com/watch?v=CrucZZk25n8)
