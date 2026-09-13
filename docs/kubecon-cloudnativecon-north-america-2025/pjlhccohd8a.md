---
layout: default
title:
  "Tutorial: Build-a-Bot Workshop... Maia Iyer, Alan Cha, Mariusz Sabath, Anjali
  Telang & Andrew Block"
nav_order: 325
parent: Kubecon Cloudnativecon North America 2025
type: Video Note
description:
  The video presents a comprehensive walkthrough on building secure, trusted
  AI agents, emphasizing zero trust principles and leveraging open source technologies.
  The speakers introduce themselves and outline foundational concepts, defining A...
resource: https://www.youtube.com/watch?v=pjlhCCOhd8A
tags:
  - kubecon-cloudnativecon-north-america-2025
  - video
  - learning
status: stable
generated:
  by: process:yt-conferences-okf
  at: 2026-09-12 00:00:00+00:00
---

# Summary

The video presents a comprehensive walkthrough on building secure, trusted AI agents, emphasizing zero trust principles and leveraging open source technologies.
The speakers introduce themselves and outline foundational concepts, defining AI agents as autonomous systems that use tools (APIs or functions) to perform complex tasks, often mimicking human-like planning, reasoning, and feedback loops.
They discuss the importance of contextual security, highlighting pitfalls such as passing user API keys or using master keys, and advocate for OAuth with token exchange and workload identity (via Spiffy/Spire) to maintain granular access control and auditability.
The team demonstrates the Kajenti project, a Kubernetes-native, open source blueprint integrating Keycloak (OAuth provider), Spire (workload identity), and Vault (secure credential storage) to enable secure agent-tool interactions, illustrated through a GitHub issue management use case.
The session concludes with a discussion on scaling architectures using MCP gateways, the flexibility of integrating with service meshes, and ongoing efforts to address challenges like prompt injection and dynamic credential management, inviting community collaboration and experimentation.

# Main Points

|   # | Main point                                                                                                                                                    |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Introduction of speakers from Red Hat and IBM, focus on building secure AI agents.                                                                            |
|   2 | AI agents defined as autonomous systems/software performing tasks using tools, leveraging LLMs for natural language understanding and deterministic tool use. |
|   3 | Agent workflow: goal initialization/planning, reasoning/action execution, outcome review/learning/feedback loop.                                              |
|   4 | Tools are functions/APIs agents call for deterministic tasks; MCP (Model Context Protocol) standardizes agent-tool communication.                             |
|   5 | Multi-agent systems enable specialization, efficiency, modularity, scalability, observability, and improved security/auditing.                                |
|   6 | Zero trust security model: no inherent trust, every access verified, least privilege, per-request access, continuous evaluation.                              |
|   7 | Security anti-patterns: passing user API keys to agents/tools loses context; master keys break zero trust.                                                    |
|   8 | OAuth recommended for authorization; token exchange preserves context and separates identities between user, agent, and tool.                                 |
|   9 | Workload identity (e.g., Spiffy/Spire) replaces long-lived secrets with attested workload identities.                                                         |
|  10 | Legacy tools using API keys can be integrated via secure credential stores (e.g., Vault).                                                                     |
|  11 | Open source solutions: Keycloak (OAuth provider), Spire (workload identity), OpenBao/Vault (credential storage), all pluggable.                               |
|  12 | Kajenti project: Kubernetes-native, open-source blueprint for secure agentic applications, identifies integration gaps, provides demos.                       |
|  13 | Demo: Deploy agent and tool, configure Keycloak, use Spire for identity, demonstrate fine-grained access control via token scopes.                            |
|  14 | Agent-tool-user flow: user logs in, receives token, agent verifies, token exchange for tool access, Vault issues secrets as needed.                           |
|  15 | MCP Gateway centralizes authentication, tool selection, observability, and routing for agent-tool interactions.                                               |
|  16 | Service mesh can be used as an alternative to MCP Gateway depending on use case.                                                                              |
|  17 | Security considerations: guardrails (e.g., Trusty.AI) for prompt injection defens                                                                             |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=pjlhCCOhd8A)
