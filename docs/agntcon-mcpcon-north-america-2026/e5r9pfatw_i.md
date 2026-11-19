---
layout: default
title: "Workshop: Hands-on A2A: Service... - Pedro Melendez, Sergio Villani & Sirisha Karra, Google"
nav_order: 8
parent: AGNTCon + MCPCon North America 2026
type: Video Note
description: "This hands-on workshop introduces the Agent-to-Agent (A2A) protocol, a standard designed to simplify communication between AI agents by replacing complex, custom REST integrations with a unified, s..."
resource: "https://www.youtube.com/watch?v=E5r9PfAtw_I"
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

This hands-on workshop introduces the Agent-to-Agent (A2A) protocol, a standard designed to simplify communication between AI agents by replacing complex, custom REST integrations with a unified, standardized approach.
The session explains that A2A addresses key challenges such as data privacy, context limits, and framework diversity by allowing agents to discover each other’s capabilities via "agent cards" and interact through defined protocols like JSON-RPC.
Participants engage in a Quick Labs environment to build an analytics agent using Google ADK, which queries BigQuery and interacts with MCP tools, before extending its functionality to communicate with remote gateway and corporate agents.
The lab demonstrates the practical differences between rigid REST API calls and dynamic A2A interactions, including multi-step authentication flows and agent discovery, while also highlighting the complementary roles of A2A for agent communication and MCP for tool connectivity.
Despite significant network connectivity issues during the live demo, the instructors provided workarounds and confirmed that the lab environment and code repository would remain accessible for participants to complete the exercises independently.

# Main Points

|   # | Main point                                                                             |
| --: | -------------------------------------------------------------------------------------- |
|   1 | # Key Points from A2A Workshop Transcript                                              |
|   2 | :**                                                                                    |
|   3 | , gRPC, JSON-RPC                                                                       |
|   4 | :**                                                                                    |
|   5 | :**                                                                                    |
|   6 | : remote agent announces capabilities via agent card in JSON format                    |
|   7 | :**                                                                                    |
|   8 | : non-deterministic, agent-to-agent communication, multi-turn dialogue, stateful tasks |
|   9 | : deterministic, tool-to-agent connection, single API calls, immediate results         |
|  10 | :**                                                                                    |
|  11 | (fails with typos) vs A2A (dynamic reasoning)                                          |
|  12 | : Switch agent from Google ADK to OpenAI, create A2A server                            |
|  13 | & Resources:**                                                                         |
|  14 | :**                                                                                    |

# Video

[![Video thumbnail](https://img.youtube.com/vi/E5r9PfAtw_I/hqdefault.jpg)](https://www.youtube.com/watch?v=E5r9PfAtw_I)

[Watch on YouTube](https://www.youtube.com/watch?v=E5r9PfAtw_I)
