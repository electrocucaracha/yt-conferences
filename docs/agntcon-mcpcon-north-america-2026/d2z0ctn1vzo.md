---
layout: default
title: "Hand the Agent the Clicker - Giovanni Laquidara, Amazon"
nav_order: 149
parent: AGNTCon + MCPCon North America 2026
type: Video Note
description: 'Giovanni, a developer advocate at Amazon, presents "PortHole," an open-source tool designed to facilitate collaboration between humans and AI agents when developing and testing TV applications.'
resource: "https://www.youtube.com/watch?v=D2Z0CtN1vZo"
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

Giovanni, a developer advocate at Amazon, presents "PortHole," an open-source tool designed to facilitate collaboration between humans and AI agents when developing and testing TV applications.
The tool addresses the complexity of context switching between emulators and remote controls by providing a unified interface that includes a browser-based view, a CLI, and an MCP server, all connected to a central server that manages the emulator session.
By exposing a set of primitives and operations, PortHole allows both users and agents to interact with the TV screen in real-time, featuring an observability layer that logs actions with distinct icons for human and agent inputs to ensure transparency.
The architecture was refined to avoid resource conflicts and duplicate data streams by routing all surfaces through a single API, which also enforces policy checks and provides structured JSON outputs for better agent comprehension.
Key design principles include prioritizing read operations for verification, implementing guardrails to pause or block agents, and enabling annotations within the browser view to allow humans to provide direct feedback to the AI, thereby streamlining the iterative development process.

# Main Points

|   # | Main point                                                                                                                                                                         |
| --: | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | "PortHole," an open-source tool designed to optimize collaboration between humans and AI agents when developing and testing TV applications on emulators and real devices.         |
|   2 | (Fire OS/Android and Vega OS/Linux) and the need for real-time observability of app behavior.                                                                                      |
|   3 | , such as sending touch inputs, navigating, and managing app lifecycle (start/stop).                                                                                               |
|   4 | : a browser-based web app, a Command Line Interface (CLI), and a Model Context Protocol (MCP) server.                                                                              |
|   5 | , annotation capabilities for design feedback, and a real-time observability log distinguishing between human and agent actions.                                                   |
|   6 | , outputting JSON objects to facilitate structured data interpretation by AI agents.                                                                                               |
|   7 | , including collaboration primitives like pausing the agent or synchronizing with human input.                                                                                     |
|   8 | /CLI and MCP caused issues such as invisible agent actions, resource conflicts, and duplicated error handling.                                                                     |
|   9 | "engine" interface.                                                                                                                                                                |
|  10 | , maintains continuous session flow, and prevents resource duplication by having all surfaces call the same underlying API.                                                        |
|  11 | (basic inputs), operations (groups of primitives), and workflows (complex, high-level sequences), with read operations being more frequent than write operations for verification. |
|  12 | , requiring structured outputs (JSON), clear error descriptions, retry-ability indicators, and nullability handling to aid both human and agent understanding.                     |
|  13 | , preventing unintended damage or interference during collaborative development.                                                                                                   |
|  14 | , allowing humans to provide visual feedback (e.g., color changes) that the AI agent can interpret and implement.                                                                  |
|  15 | , keeping logic out of the surfaces, prioritizing read operations, and ensuring clear coordination mechanisms between humans and agents.                                           |
|  16 | , verify workflow correctness, and implement UI, MCP, and CLI components to enable effective human-agent collaboration.                                                            |

# Video

[![Video thumbnail](https://img.youtube.com/vi/D2Z0CtN1vZo/hqdefault.jpg)]("https://www.youtube.com/watch?v=D2Z0CtN1vZo")

[Watch on YouTube](https://www.youtube.com/watch?v=D2Z0CtN1vZo)
