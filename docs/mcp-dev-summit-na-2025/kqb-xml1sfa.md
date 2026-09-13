---
layout: default
title:
  "[Session] MCP vs ACP vs A2A: Comparing Agent Protocols with Laurie Voss from
  LlamaIndex"
nav_order: 14
parent: Mcp Dev Summit Na 2025
type: Video Note
description:
  Lori, VP of Developer Relations at Llama Index, introduces a rapid overview
  of agent-to-agent communication protocols, noting that while she initially knew
  of only three, her research uncovered 13 in total. She distinguishes between context...
resource: https://www.youtube.com/watch?v=kqB_xML1SfA
tags:
  - mcp-dev-summit-na-2025
  - video
  - learning
status: stable
generated:
  by: process:yt-conferences-okf
  at: 2026-09-12 00:00:00+00:00
---

# Summary

Lori, VP of Developer Relations at Llama Index, introduces a rapid overview of agent-to-agent communication protocols, noting that while she initially knew of only three, her research uncovered 13 in total.
She distinguishes between context-oriented protocols, like MCP and agents.json, which focus on providing context for LLMs, and inter-agent protocols, such as A2A, AITP, and others, which aim to enable agents to discover, communicate, and collaborate with each other.
Most protocols are still incomplete, with MCP standing out for its adoption and focus, though it lacks some features like robust async support and protocol negotiation found in others like Agora.
Lori highlights key unsolved challenges across all protocols, including the need for a unified registry, effective authorization, and reputation systems to ensure secure and reliable agent interactions.
She concludes that while MCP currently meets most needs and has significant traction, the field is evolving rapidly, and open questions remain about the future direction of agent communication standards.

# Main Points

|   # | Main point                                                                                                                                             |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   1 | Speaker is Lori, VP of Developer Relations at Llama Index, formerly co-founder of npm Inc.                                                             |
|   2 | Topic: Overview of agent-to-agent communication protocols in AI.                                                                                       |
|   3 | Initially knew of 3 protocols, discovered 11 more during research.                                                                                     |
|   4 | Disclaimer: Speaker is a recent learner of these protocols, not a contributor, and opinions are personal.                                              |
|   5 | Llama Index aims to support all protocols, with easy server/client setup for MCP.                                                                      |
|   6 | Key resource: April 2023 paper by Yangadel, provides taxonomy and analysis of protocols.                                                               |
|   7 | 13 real protocols discussed; most aim for agent collaboration, except MCP.                                                                             |
|   8 | Agents should discover, authenticate, communicate, form coalitions, negotiate, and solve problems together.                                            |
|   9 | Currently, no protocol fully solves agent-to-agent communication; most are incomplete.                                                                 |
|  10 | MCP is closest to a standard but not focused on inter-agent communication.                                                                             |
|  11 | Protocol taxonomy: context-oriented (providing LLMs with context, e.g., MCP, agents.json) vs. inter-agent (enabling agent communication, negotiation). |
|  12 | MCP: Well-known, context-oriented, request/response model.                                                                                             |
|  13 | agents.json: File describing APIs and their usage for agents, based on OpenAPI.                                                                        |
|  14 | A2A: Google's protocol, focuses on async agent calls, expects long-running tasks, aims for agent-to-agent communication.                               |
|  15 | DID: Uses W3C distributed identity, blockchain-based, enables agent discovery, but is "blockchainy."                                                   |
|  16 | AITP: Blockchain-focused, enables agents to bid for tasks, emphasizes cost of interactions.                                                            |
|  17 | Two ACP protocols: "Connect" (Cisco, includes agent hosting/execution, registry) and "Communication" (IBM, fork of MCP, diverging toward A2A).         |
|  18 | Agora: Starts with natural language, upgrades to formal protocol as needed, LLM-first, mostly conceptual.                                              |
|  19 | Several domain-specific protocols exist (human-agent, robot-agent), not general-purpose.                                                               |
|  20 | Elmos: From Eclipse Foundation (IBM), similar to other protocols.                                                                                      |
|  21 | Agent Protocol: Minimal differentiation, claims to be the only agent protocol.                                                                         |
|  22 | MCP has the most adoptio                                                                                                                               |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=kqB_xML1SfA)
