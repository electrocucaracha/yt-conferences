---
layout: default
title: "The Agent Has Left the Chat - Harald Kirschner, Microsoft"
nav_order: 39
parent: AGNTCon + MCPCon North America 2026
type: Video Note
description: "The Agent Host Protocol (AHP) is an open specification designed to decouple AI agent sessions from specific applications, allowing users to start, monitor, and control agents across multiple client..."
resource: "https://www.youtube.com/watch?v=TZMu0LhTG6k"
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

The Agent Host Protocol (AHP) is an open specification designed to decouple AI agent sessions from specific applications, allowing users to start, monitor, and control agents across multiple clients and remote environments.
By standardizing how agent state, tool calls, and approvals are shared, AHP enables seamless handoffs between local editors, cloud dev boxes, and mobile interfaces, ensuring that work continues uninterrupted regardless of the user's location.
The protocol addresses previous fragmentation in agent management by unifying access to skills, MCP servers, and sub-agents, providing a rich, stateful view of background processes that were previously invisible to users.
AHP also introduces robust multi-client synchronization, allowing different devices to join a session, replay missed interactions, and manage concurrent approvals without conflict.
Ultimately, this infrastructure supports diverse user interfaces, from traditional code editors to novel inbox-style dashboards and gamified experiences, empowering developers to orchestrate complex AI workflows with greater flexibility and efficiency.

# Main Points

|   # | Main point                                                                                                                                              |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | # Key Points                                                                                                                                            |
|   2 | • Agent sessions now run as independent processes outside VS Code's extension host, enabling session persistence across client disconnections           |
|   3 | • Agent Host Protocol (AHP) is an open specification allowing multiple clients to connect to a single agent session running on any host                 |
|   4 | • Agents can execute on various platforms: development containers, remote machines, cloud environments, and remain accessible via tunnels or SSH        |
|   5 | • Visual Studio Code unified on a single Copilot SDK runtime, optimizing token efficiency and performance compared to competitor models                 |
|   6 | • Clients joining agent sessions receive full conversation snapshots including all tool calls, approvals, and workspace state                           |
|   7 | • Multiple clients connecting to one session requires conflict resolution—first client to interact wins to prevent duplicate approvals                  |
|   8 | • Replay functionality allows clients reconnecting after disconnection to see missed updates without interruption                                       |
|   9 | • Sub-agents now appear as separate chats in the protocol, providing visibility into background agent activity and blocking dependencies                |
|  10 | • MCP (Model Context Protocol) state syncs across multiple locations—client customizations and remote MCPs must be coordinated on the host              |
|  11 | • Automations can run on the host without connected clients, allowing scheduled tasks and background operations                                         |
|  12 | • AHP differs from ACP (designed for single embedded agent) and A2A (agent-to-agent communication)—AHP handles multi-client observation and control     |
|  13 | • Agent Host Protocol v1.0 launched in October; supports publishing sessions and client-side features execution on the host                             |
|  14 | • Next-generation agent UIs don't require editor format—can implement inbox-style interfaces, dashboards, or alternative visualizations using AHP state |

# Video

[![Video thumbnail](https://img.youtube.com/vi/TZMu0LhTG6k/hqdefault.jpg)](https://www.youtube.com/watch?v=TZMu0LhTG6k)

[Watch on YouTube](https://www.youtube.com/watch?v=TZMu0LhTG6k)
