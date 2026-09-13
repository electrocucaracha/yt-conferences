---
layout: default
title: Human in the Loop, Agent in the Flow - Harald Kirschner & Connor Peet, Microsoft
nav_order: 35
parent: Mcp Dev Summit Na 2026
type: Video Note
description:
  The speakers discuss how modern agent interfaces, particularly in VS
  Code, are moving beyond simple text-based interactions to provide richer, more interactive
  experiences through the MCP (Multi-Client Protocol). They highlight the "missing...
resource: https://www.youtube.com/watch?v=chJb_BbE050
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

The speakers discuss how modern agent interfaces, particularly in VS Code, are moving beyond simple text-based interactions to provide richer, more interactive experiences through the MCP (Multi-Client Protocol).
They highlight the "missing middle"—the space between basic text input/output and full agent autonomy—where structured inputs like elicitations, task progress tracking, and interactive MCP apps enhance user control and engagement.
Demonstrations show how URL elicitations, tasks, and sampling enable more nuanced workflows, such as securely loading data, tracking long-running processes, and efficiently analyzing large outputs without overwhelming the context window.
MCP apps allow for dynamic, visual, and interactive outputs, supporting use cases like dashboards, whiteboards, and configuration wizards, with graceful degradation for clients lacking full app support.
The talk emphasizes the importance of designing agent experiences that empower users, improve collaboration, and leverage advanced protocol features for more effective and efficient workflows.

# Main Points

|   # | Main point                                                                                                                                          |
| --: | --------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Text-only chat interfaces are insufficient for MCP; richer interactions are needed.                                                                 |
|   2 | The "missing middle" refers to interactive elements between simple text input/output and agent autonomy.                                            |
|   3 | Structured input (elicitations) allows the server to ask clarifying questions and control flow, even between tool calls.                            |
|   4 | Form elicitations use JSON schema for explicit input; agent does not see raw input.                                                                 |
|   5 | URL elicitations enable offloading input steps to a server, useful for configurations and confirmations.                                            |
|   6 | MCP apps provide interactive outputs, allowing users to drill into content and interact beyond text.                                                |
|   7 | Tasks support long-running operations, showing progress and allowing background work.                                                               |
|   8 | Tasks can return statuses, support reconnection, and handle large data flows over extended periods.                                                 |
|   9 | MCP apps can render before tool calls finish, enabling rich, interactive UIs and custom elicitations.                                               |
|  10 | Sampling allows the MCP server/app to request inference from the client’s language model, enabling efficient data summarization and transformation. |
|  11 | Large tool outputs are handled efficiently by storing results in files and generating JSON schemas for token-efficient extraction.                  |
|  12 | MCP apps gracefully degrade: if a client doesn’t support apps, fallback to text-based outputs is possible.                                          |
|  13 | Real-world use cases include Storybook, Figma, Amplitude, Teal Draw, and Excalidraw, providing visual and interactive experiences.                  |
|  14 | MCP apps and tools enable more autonomy and control for users, especially in planning and review workflows.                                         |
|  15 | Elicitations and schemas improve input flows compared to CLI tools.                                                                                 |
|  16 | Tasks and progress indicators provide better control and transparency than CLI logs.                                                                |
|  17 | Secure, sandboxed iframes are used for output, supporting rich UI safely.                                                                           |
|  18 | Scoped token tools allow gradual enabling of features as users grant more permissions.                                                              |
|  19 | Tool annotations (read-only, destructive, idempotent, open world) inform users of tool side effects.                                                |
|  20 | Server instructions and linked r                                                                                                                    |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=chJb_BbE050)
