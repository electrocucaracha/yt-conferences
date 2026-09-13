---
type: Video Note
title: "[Session] Do You Need an AI Gateway with Ignasi Barrera - Tetrate"
description: "The session discusses the growing need for AI gateways amid the rapid evolution of AI technologies, particularly with the rise of non-deterministic systems like large language models (LLMs) and autonomous agents. The speaker explains how tr..."
resource: https://www.youtube.com/watch?v=JBeHnvunf2M
tags: ["mcp-dev-summit-eu-2025", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

The session discusses the growing need for AI gateways amid the rapid evolution of AI technologies, particularly with the rise of non-deterministic systems like large language models (LLMs) and autonomous agents.
The speaker explains how traditional deterministic API interactions have shifted to more complex, probabilistic workflows, introducing new challenges such as context and tool bloating, tool confusion, protocol compatibility, and security concerns.
AI gateways, especially those with deep understanding of protocols like MCP, are presented as essential solutions for managing authentication, authorization, resiliency, observability, and policy enforcement in these environments.
The speaker highlights the Amboy AI Gateway project, which integrates AI features and MCP support into the established Amboy proxy, allowing for secure, efficient, and customizable management of AI agent interactions.
A demonstration shows how using such a gateway can streamline tool selection, reduce decision fatigue, and centralize security and policy controls, ultimately making AI systems more manageable and reliable in production settings.
# Main Points

|   # | Main point                                                                                                                                                        |
| --: | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Discussion focuses on the need for AI gateways in a crowded, hyped space.                                                                                         |
|   2 | Technology and workflows have shifted from deterministic APIs to non-deterministic systems like LLMs.                                                             |
|   3 | LLMs produce different outputs for the same input, creating trust and control challenges.                                                                         |
|   4 | Autonomous agents now interact with systems and make decisions on users’ behalf.                                                                                  |
|   5 | MCP (Multi-Channel Protocol) is rising, enabling agents to access external tools and enrich context.                                                              |
|   6 | Remote MCP servers are becoming common, making integration easier but introducing new challenges.                                                                 |
|   7 | Main API consumers are now agents, not just users or simple clients.                                                                                              |
|   8 | Tool and context bloating occur as agents access multiple MCP servers with many tools, leading to LLM context window issues and tool confusion.                   |
|   9 | Problems include tool confusion, tool shadowing, wasted tokens, and increased costs.                                                                              |
|  10 | Existing challenges: discovering trusted MCP servers, authentication/authorization, resiliency, high availability, load balancing, observability, and monitoring. |
|  11 | New challenges: context bloating, tool confusion, tool poisoning, need for guardrails, and decision fatigue.                                                      |
|  12 | Community is addressing some issues: MCP registry, evolving authorization specs, secure credential exchange, open inference for observability.                    |
|  13 | Deep understanding of MCP protocol is needed; most current solutions focus on HTTP metadata, not deep payload inspection.                                         |
|  14 | AI gateways can enforce policies, authentication, custom policies, resiliency, load balancing, and observability in a single place.                               |
|  15 | AI gateways can filter and expose only relevant tools to agents, reducing confusion and decision fatigue.                                                         |
|  16 | Production use of AI gateways requires considering maturity, documentation, community support, and operational best practices.                                    |
|  17 | Amboy AI Gateway is an open source project adding LLM and MCP support to the Amboy proxy, maintaining core features like resiliency and monitoring.               |
|  18 | Demonstration showed configuring agent profiles, limiting tool exposure                                                                                           |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=JBeHnvunf2M)