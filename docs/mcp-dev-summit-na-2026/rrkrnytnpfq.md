---
layout: default
title: Progressive Tool Discovery Using MCP
nav_order: 81
parent: MCP Dev Summit NA 2026
type: Video Note
description: 'Billy Hickman and Lilia from Prime Video present a solution to the "paradox of choice" in AI agents, where exposing hundreds of MCP tools simultaneously degrades performance by overwhelming the con...'
resource: "https://www.youtube.com/watch?v=rRkrNYtnpfQ"
tags:
  - mcp-dev-summit-na-2026
  - video
  - learning
status: stable
generated:
  by: process:yt-summarizer-okf
  at: 2026-11-15T16:54:07+00:00
---

# Summary

Billy Hickman and Lilia from Prime Video present a solution to the "paradox of choice" in AI agents, where exposing hundreds of MCP tools simultaneously degrades performance by overwhelming the context window.
To address this, they implemented a dynamic tool discovery mechanism that initially exposes only a single "find tools" tool, which allows the agent to request specific toolsets based on defined problem categories such as operations or training.
By leveraging MCP session IDs and tools list change notifications, the system dynamically loads relevant tools into the agent’s context mid-session while unloading previously used ones, ensuring that only the necessary tools are active for the current task.
This approach significantly improves agent accuracy and reduces hallucinations, particularly for centralized MCP servers shared across teams, though it requires careful governance of tool definitions and problem category mappings.
The speakers demonstrated this pattern with a custom running agent that successfully switched between results and training tools during a session, highlighting the trade-off between added latency for dynamic discovery and the substantial gains in context efficiency and task-specific performance.

# Main Points

|   # | Main point                                                                                                                                                         |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   1 | The presentation addresses the problem of context bloat and performance degradation caused by exposing hundreds of MCP tools to AI agents simultaneously.          |
|   2 | The core solution is a dynamic tool discovery mechanism that allows agents to load only the relevant tools for a specific task, reducing context usage.            |
|   3 | The approach leverages two key MCP specification features: the tools list change notification and the MCP session ID header for tracking remote server sessions.   |
|   4 | A single initial tool named find tools is exposed to the agent, which contains descriptions of available problem categories to guide discovery.                    |
|   5 | When an agent invokes find tools with a specific problem category, the server persists this context and returns a list of relevant tool names.                     |
|   6 | The server then sends a tools list change notification, prompting the agent to refresh its tool list and load the newly discovered tools.                          |
|   7 | This process enables mid-session tool swapping, where previously loaded tools are removed from the context to make room for new ones relevant to the current task. |
|   8 | The system supports both remote MCP servers using streamable HTTP and local implementations using standard IO.                                                     |
|   9 | A live demo demonstrated an agent discovering marathon results tools to query finish times and then switching to training tools to generate a personalized plan.   |
|  10 | The approach is particularly beneficial for centralized MCP servers and gateways where tools are shared across multiple teams and organizational boundaries.       |
|  11 | Deterministic mapping of tools to problem categories was used initially, with future plans to implement more dynamic searching capabilities.                       |
|  12 | The solution requires client compliance with the MCP specification, specifically the ability to handle tools list change notifications.                            |
|  13 | While the approach reduces context load, it introduces a trade-off in latency due to the additional steps required for tool discovery and reloading.               |
|  14 | Governance remains necessary to ensure clean tool definitions and prevent overlap, as the discovery mechanism assumes well-defined tool categories.                |
|  15 | The pattern is applicable to any MCP-compliant client, though internal control over client implementations simplified adoption for the presenters.                 |

# Video

[![Video thumbnail](https://img.youtube.com/vi/rRkrNYtnpfQ/hqdefault.jpg)](https://www.youtube.com/watch?v=rRkrNYtnpfQ)

[Watch on YouTube](https://www.youtube.com/watch?v=rRkrNYtnpfQ)
