---
layout: default
title:
  "Building a Workflow Engine on MCP: Orchestrating Processes With Tasks - Donnie
  Adams, Obot AI"
nav_order: 5
parent: Mcp Dev Summit Na 2026
type: Video Note
description:
  Donnie Adams, a software architect at OOT and former high school math
  teacher, introduces himself and his team before presenting on MCP Tasks and their
  architecture. He explains how his team at OOT, inspired by Rancher’s use of Kubernetes
  t...
resource: https://www.youtube.com/watch?v=f8vPMlm0MaI
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

Donnie Adams, a software architect at OOT and former high school math teacher, introduces himself and his team before presenting on MCP Tasks and their architecture.
He explains how his team at OOT, inspired by Rancher’s use of Kubernetes to manage Kubernetes, built their chat application using MCP, demonstrating how chat interactions are implemented as tool calls within the MCP protocol.
Adams highlights the limitations of synchronous tool calls, such as lack of durability and issues with long-running tasks, and describes how his team initially implemented asynchronous task handling before it was standardized in the MCP specification.
He then reviews the official MCP Tasks specification, emphasizing its support for asynchronous workflows, state transitions, and improved client-server interactions.
Adams concludes by sharing a demo of a simple workflow engine he built in Gleam, illustrating the agent loop and task lifecycle, and notes that while his team shifted away from certain workflow implementations due to evolving needs and gaps in the specification, the MCP framework remains central to their approach.

# Main Points

|   # | Main point                                                                                                                                             |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   1 | Presenter: Donnie Adams, software architect at OOT, former high school math teacher and basketball coach, open-source contributor, new father.         |
|   2 | Presentation in New York City; first time visiting.                                                                                                    |
|   3 | Acknowledges contributions of entire engineering team.                                                                                                 |
|   4 | Agenda: Discuss MCP Tasks, architecture, demos, and transition to tasks specification.                                                                 |
|   5 | OOT’s founding staff created Rancher; inspired by Kubernetes managing Kubernetes.                                                                      |
|   6 | MCP architecture used for chat application; similar to Rancher’s approach.                                                                             |
|   7 | Typical agent loop: user request → server assembles history → LLM inference → tool use or response → server runs tool → response returned.             |
|   8 | "Ask the user" is treated as a tool in MCP.                                                                                                            |
|   9 | LLM inference = sampling request; tool calls = tool calls; ask the user = elicitation; agent response = tool call response.                            |
|  10 | Demo 1: Chat application is an MCP server using a "chat with nanobot" tool; user interacts with LLM via MCP tool.                                      |
|  11 | Chat responses are generated and displayed; all interactions run through MCP server.                                                                   |
|  12 | Limitation: Tool calls are not durable; server restarts, HTTP disconnects, or timeouts can cause data loss.                                            |
|  13 | Long-running tasks are problematic due to connection reliability.                                                                                      |
|  14 | Solution: Asynchronous tool calls using metadata to treat requests as async tasks; progress notifications sent to client.                              |
|  15 | Demo 2: Async chat requests update chat progress and history resources; runs in background, updates client via notifications.                          |
|  16 | Drawback: Requires clients to know implementation details; not universal or sustainable.                                                               |
|  17 | Tasks in MCP: Tools can declare support for tasks; tasks run asynchronously with defined state transitions (working, input required, terminal states). |
|  18 | Servers can send full task objects in notifications, reducing round trips.                                                                             |
|  19 | Tasks natively support user input via input required status.                                                                                           |
|  20 | Workflow experience at OOT designed to be interactive, allowing user-agent conversation and corrections.                                               |
|  21 | Chat application provided 80% of needed workflow functi                                                                                                |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=f8vPMlm0MaI)
