---
layout: default
title:
  "Progressive Tool Discovery: Using MCP Notifications To Manage C... Billy Hickman
  & Lilia Abaibourova"
nav_order: 73
parent: Mcp Dev Summit Na 2026
type: Video Note
description:
  The presenters discuss the challenge of managing tool discovery for AI
  agents at scale, drawing an analogy to the "paradox of choice" faced by users of
  streaming services. As Prime Video adopted AI agents for operational and development
  tas...
resource: https://www.youtube.com/watch?v=MFL5cRTBUX0
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

The presenters discuss the challenge of managing tool discovery for AI agents at scale, drawing an analogy to the "paradox of choice" faced by users of streaming services.
As Prime Video adopted AI agents for operational and development tasks, they encountered issues with context bloat and degraded performance when agents were given access to hundreds of tools via a shared MCP server.
To address this, they implemented a dynamic tool discovery system where agents initially access only a "find tools" function, allowing them to discover and load only the tools relevant to their current problem category, and unload them when no longer needed.
This approach reduces context size, improves agent performance, and allows for tools to be added or removed mid-session, though it requires governance to avoid tool overlap and some trade-offs in latency.
The team demonstrated this system with a running agent example and discussed its applicability, limitations, and future improvements, emphasizing that while effective internally, broader adoption depends on protocol compliance across different agent implementations.

# Main Points

|   # | Main point                                                                                                                                 |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------ |
|   1 | Problem: AI agents connected to MCPs face "tool bloat"—hundreds of tools in context degrade performance and increase hallucinations.       |
|   2 | Agents only need a few relevant tools per task, not all available tools.                                                                   |
|   3 | Prime Video team built shared MCP infrastructure to reduce tool duplication, but this led to rapid tool count growth and context overload. |
|   4 | Requirements identified: dynamic tool discovery/unloading, centralized security/permissions, and consistent MCP protocol implementation.   |
|   5 | Focus: dynamic tool discovery—agents should discover and load only relevant tools mid-session, unloading others to manage context size.    |
|   6 | Explored approaches: sub-agent tool discovery, per-agent tool configurations, and chose full dynamic discovery for scalability.            |
|   7 | Used MCP spec features: tool list change notifications and session tracking via MCP session ID.                                            |
|   8 | Implementation:                                                                                                                            |
|   9 | Agent starts with access to a single "find tools" tool.                                                                                    |
|  10 | "Find tools" maps tools to problem categories (e.g., operations, training, results).                                                       |
|  11 | Agent invokes "find tools" to discover and load tools relevant to the current problem category.                                            |
|  12 | Tools are dynamically added/removed from agent context as problem categories change.                                                       |
|  13 | Demo:                                                                                                                                      |
|  14 | Running agent discovers tools for marathon results, then switches to training tools, only loading what's needed for each task.             |
|  15 | Tools not relevant to the current problem category are unloaded from context.                                                              |
|  16 | Benefits:                                                                                                                                  |
|  17 | Only relevant tools appear in agent context, reducing context bloat.                                                                       |
|  18 | Tools can be added/removed mid-session.                                                                                                    |
|  19 | Useful for centralized/shared MCP servers across teams.                                                                                    |
|  20 | Limitations:                                                                                                                               |
|  21 | Requires governance to avoid tool overlap and maintain clean definitions.                                                                  |
|  22 | Some latency added due to dynamic loading/unloading.                                                                                       |
|  23 | Approach works best when clients are MCP protocol compliant.                                                                               |
|  24 | Future improvements: enable agents to search for tools by describing problems, not just deterministic mapping.                             |
|  25 | Approach works for both remote (HTTP streaming                                                                                             |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=MFL5cRTBUX0)
