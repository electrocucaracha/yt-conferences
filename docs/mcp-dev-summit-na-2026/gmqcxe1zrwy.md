---
type: Video Note
title: "Clients? Servers? Agents? The Beautiful Asymmetry of the MCP Spec - Rohit Ganguly, Descope"
description: "Rohit’s talk explores the asymmetry and evolving possibilities of the MCP (Model Control Protocol) specification, focusing on the dynamic relationships between clients, servers, and agents. Drawing from his experience at Dcope and Microsoft..."
resource: https://www.youtube.com/watch?v=GMQCXe1zrWY
tags: ["mcp-dev-summit-na-2026", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

Rohit’s talk explores the asymmetry and evolving possibilities of the MCP (Model Control Protocol) specification, focusing on the dynamic relationships between clients, servers, and agents.
Drawing from his experience at Dcope and Microsoft, he outlines how MCP structures interactions, with servers providing tools, resources, and prompts to clients, while clients can also offer features like sampling, roots, and elicitation back to servers—capabilities that are often underused but point to MCP’s future potential.
Rohit discusses the agent-to-agent paradigm, where agents act as both clients and servers, enabling more complex, autonomous, and cross-boundary workflows, though this introduces challenges around authorization, context management, and dynamic discovery.
He highlights ongoing developments such as enterprise-managed authorization, server cards for runtime discovery, nested task execution, and event-driven updates, all aimed at addressing MCP’s current limitations as agents become more autonomous and interconnected.
Ultimately, Rohit encourages experimentation with MCP’s flexible architecture, noting that as agents expose more server-like functionality, new opportunities and pricing models emerge, and the protocol continues to adapt to these innovative use cases.
# Main Points

|   # | Main point                                                                                                                       |
| --: | -------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Speaker: Rohit, works at Dcope, previously at Microsoft on Azure SDK and Azure MCP server projects.                              |
|   2 | Dcope is an identity/auth company; booth G8.                                                                                     |
|   3 | Talk focuses on the asymmetry of the MCP spec, clients, servers, and agents.                                                     |
|   4 | Goals: inspire curiosity, encourage experimentation with protocols, oversimplify complex topics, and explore MCP’s potential.    |
|   5 | MCP architecture:                                                                                                                |
|   6 | MCP host manages clients connecting to servers.                                                                                  |
|   7 | Harness: logic for orchestrating LLMs and context management.                                                                    |
|   8 | Authorization server exists but often overlooked by developers.                                                                  |
|   9 | MCP server provides:                                                                                                             |
|  10 | Tools: functions clients can use.                                                                                                |
|  11 | Resources: read-only data, e.g., file systems.                                                                                   |
|  12 | Prompts: instructions or templated workflows.                                                                                    |
|  13 | MCP client can provide to server:                                                                                                |
|  14 | Sampling: server requests client’s LLM/decision engine to interact with server.                                                  |
|  15 | Roots: file system or URI boundary hints.                                                                                        |
|  16 | Elicitation: server asks client/user for more info (no sensitive data).                                                          |
|  17 | URL elicitation: user is sent to browser for sensitive actions (e.g., OAuth, payments).                                          |
|  18 | MCP’s asymmetry: clients and servers have distinct, complementary roles.                                                         |
|  19 | Agent-to-agent connections via MCP are possible, though not a formal protocol.                                                   |
|  20 | Sub-agent structure: main agent delegates tasks to sub-agents, mirroring client-server relationships.                            |
|  21 | Context management is crucial for agent effectiveness.                                                                           |
|  22 | Trust boundaries: agent-to-agent connections become important when crossing organizational or trust domains.                     |
|  23 | Example: Sentry MCP server introduced agent/sub-agent mode for context management and trust boundaries.                          |
|  24 | OAuth in MCP: client gets token from authorization server to connect to server; URL elicitation handles third-party credentials. |
|  25 | Challenges:                                                                                                                      |
|  26 | Multiple downstream agents require multiple consents.                                                                            |
|  27 | Assumes a human is present for consent.                                                                                          |
|  28 | Dynamic agent discovery and runtime connections are complex.                                                                     |
|  29 | MCP was not designed for multi-hop or peer-to-peer connections.                                                                  |
|  30 | Roadmap/solutions:                                                                                                               |
|  31 | Ent Ratings (1-5): 3                                                                                                             |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=GMQCXe1zrWY)