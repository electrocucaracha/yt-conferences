---
layout: default
title:
  "Hooks, Not Hacks: Modular Enforcement for MCP Agents - Fred Araujo & Ian Molloy,
  IBM"
nav_order: 33
parent: Mcp Dev Summit Na 2026
type: Video Note
description:
  The video discusses the security challenges posed by autonomous agents,
  emphasizing that agents themselves—rather than just users—should be treated as potential
  insider threats within organizations. Traditional approaches, such as adding mo...
resource: https://www.youtube.com/watch?v=9lNFch7eGxQ
tags:
  - mcp-dev-summit-na-2026
  - video
  - learning
status: stable
generated:
  by: process:yt-conferences-okf
  at: 2026-09-12 00:00:00+00:00
---

# Summary

The video discusses the security challenges posed by autonomous agents, emphasizing that agents themselves—rather than just users—should be treated as potential insider threats within organizations.
Traditional approaches, such as adding more instructions or guidelines to prompts, are deemed insufficient for enforcing security and policy compliance, especially given the diversity of agent development stacks and protocols.
To address this, the presenters introduce CPax, an open-source Python library that provides standardized, composable hooks for enforcement and mediation across the agent stack.
CPax enables the separation of policy enforcement from agent logic through plugins that can handle tasks like access control, prompt injection detection, redaction, and taint tracking, making policies portable and adaptable across different frameworks.
The demo illustrates how CPax can enforce attribute-based policies, manage identity claims, and track information flow, ensuring that sensitive data is only accessible to authorized roles and preventing unauthorized actions, all while maintaining flexibility and extensibility for various agentic and middleware systems.

# Main Points

|   # | Main point                                                                                                                                                   |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   1 | Agents should be treated as insider threats; they can be security risks independent of user prompts.                                                         |
|   2 | Agents can be indirectly prompted to perform malicious actions via context sources like web searches, documents, GitHub issues, calendar invites, or emails. |
|   3 | Current industry practices rely too much on prompt instructions and guidelines, which do not provide real enforcement or security guarantees.                |
|   4 | There is no single point of enforcement or standard way to secure agents due to diversity in agent stacks, libraries, models, and protocols.                 |
|   5 | Security and controls need to be composable and enforceable across the entire stack.                                                                         |
|   6 | Policies for agents vary widely, from stylistic requirements to access controls and operational restrictions.                                                |
|   7 | Enforcement must occur at different stack layers depending on policy type: prompt layer, MCP layer, infrastructure, etc.                                     |
|   8 | CPax is introduced as a system of standardized hooks for enforcement, enabling interception, access control, and payload transformation.                     |
|   9 | Hooks can be added at various points: LLM proxy, agentic framework, tool calls, gateways, etc.                                                               |
|  10 | Plugins can be developed for guardrails, PII detection, stylistic requirements, tool filtering, error recovery, and more.                                    |
|  11 | CPax separates agent development from policy enforcement, improving portability and reducing vulnerabilities.                                                |
|  12 | Plugins and hooks are defined via a lightweight, installable Python library; plugins are configured via YAML and support dependency injection.               |
|  13 | Plugins can block, transform, or log actions, and are executed in priority order.                                                                            |
|  14 | Payloads are immutable and passed as copy-on-write to plugins to control side effects.                                                                       |
|  15 | CPax supports a common message format for interoperability and portability across systems and protocols.                                                     |
|  16 | Attribute-based policies can enforce access control, confidentiality, and integrity, with support for taint tracking and information flow control.           |
|  17 | Demo showed role-based redaction of sensitive data and prevention of unauthorized                                                                            |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=9lNFch7eGxQ)
