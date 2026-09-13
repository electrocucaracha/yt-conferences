---
layout: default
title:
  "[Session] Moving Past Simple MCP Tools to MCP Agents with Darren Shepherd
  - Obot AI"
nav_order: 17
parent: Mcp Dev Summit Eu 2025
type: Video Note
description:
  Darren Shepard, chief architect at OOT, discusses the evolution from
  simple MCP (Machine Communication Protocol) tools to more sophisticated MCP agents,
  emphasizing the importance of building conversational, agent-based interfaces rather
  th...
resource: https://www.youtube.com/watch?v=iRgMQmJwDNA
tags:
  - mcp-dev-summit-eu-2025
  - video
  - learning
status: stable
generated:
  by: process:yt-conferences-okf
  at: 2026-09-12 00:00:00+00:00
---

# Summary

Darren Shepard, chief architect at OOT, discusses the evolution from simple MCP (Machine Communication Protocol) tools to more sophisticated MCP agents, emphasizing the importance of building conversational, agent-based interfaces rather than just exposing raw API-like tools.
He argues that simply mapping APIs to MCP servers is insufficient for representing a company's services, controlling user experience, or ensuring security and privacy, especially in sensitive domains like banking.
Shepard introduces his project, Nanobot, which encapsulates an entire MCP host as an agent within an MCP server, enabling rich, stateful, and multimodal conversational experiences that can be accessed across various channels and clients.
Through live demonstrations, he shows how this approach supports agent-to-agent communication, maintains context, and allows for advanced features like elicitations and UI resources, ultimately providing a more controlled, secure, and user-friendly interface.
Shepard concludes by advocating for the adoption of agent-based MCP servers for customer-facing applications, highlighting the flexibility and improved user experience they offer compared to traditional fine-grained tool exposure.

# Main Points

|   # | Main point                                                                                                                                            |
| --: | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | The talk focuses on moving from simple MCP tools to MCP agents.                                                                                       |
|   2 | Darren Shepard, chief architect at OOT, is presenting.                                                                                                |
|   3 | MCP agents should be conversational, not just simple tools mapping to APIs.                                                                           |
|   4 | Current MCP server approach exposes raw tools, leading to unpredictable user experience and lack of company representation.                           |
|   5 | Security and privacy are major concerns, especially for sensitive domains like banking.                                                               |
|   6 | Exposing raw tools to any LLM is risky due to data harvesting and lack of control.                                                                    |
|   7 | The proposed solution is to build an MCP agent with a carefully chosen LLM, curated prompts, and secured tools.                                       |
|   8 | The agent is then exposed as a single MCP chat tool, enabling conversational interaction.                                                             |
|   9 | Nanobot is a project implementing this approach, acting as an MCP host within an MCP server.                                                          |
|  10 | Nanobot standardizes the agent interface and uses declarative configuration, making setup simple for users.                                           |
|  11 | The agent maintains conversational context and session state.                                                                                         |
|  12 | Nanobot supports multimodal interfaces and can be accessed via various channels (web, SMS, etc.).                                                     |
|  13 | Demonstrations showed agent-to-agent communication, human-in-the-loop confirmations, and integration with different clients (Goose, Claude, VS Code). |
|  14 | The approach allows for richer user experiences and better control over interactions.                                                                 |
|  15 | MCP UI and mime types enable adaptive interfaces for different channels.                                                                              |
|  16 | The chat method is designed to be asynchronous for improved user experience.                                                                          |
|  17 | The system supports both conversational agents and traditional fine-grained tools if needed.                                                          |
|  18 | Nanobot and its demo app are available at nanobot.ai and on GitHub.                                                                                   |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=iRgMQmJwDNA)
