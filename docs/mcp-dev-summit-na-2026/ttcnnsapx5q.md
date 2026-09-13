---
type: Video Note
title: "Code Mode Without the Code - Bob Dickinson, TeamSpark"
description: 'In this talk, Bob Dickinson introduces MCP Graph, a no-code, open-source solution for orchestrating workflows using MCP servers without generating or executing source code. He explains the limitations of "code mode" approaches, where LLMs g...'
resource: https://www.youtube.com/watch?v=tTCnNsaPX5Q
tags: ["mcp-dev-summit-na-2026", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

In this talk, Bob Dickinson introduces MCP Graph, a no-code, open-source solution for orchestrating workflows using MCP servers without generating or executing source code.
He explains the limitations of "code mode" approaches, where LLMs generate code to orchestrate tool calls, highlighting issues such as security risks, lack of observability, and challenges with context overload.
MCP Graph addresses these by using a declarative YAML-based DSL to define workflows as directed graphs, leveraging established tools like JSONata for data transformation and JSON Logic for conditional routing, making the system both transparent and inspectable.
Dickinson also describes the development of MCP Graph Toolkit, which equips agents with the same tools and context as human developers, enabling them to build, test, and deploy workflows more effectively.
The solution is complemented by a visualization tool (MCP Graph UX) and is designed to be composable, observable, and suitable for both individual and enterprise use, with future enhancements possible based on community feedback.
# Main Points

|   # | Main point                                                                                                                                                                              |
| --: | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Presentation introduces MCP Graph, a no-code orchestration solution for MCP tool workflows.                                                                                             |
|   2 | Speaker: Bob Dickinson, founder, CTO, open source maintainer, and builder of agent frameworks and MCP security tooling.                                                                 |
|   3 | Inspiration: "Code Act" paper (Apple ML blog, 2024) showed LLMs are better at generating code for algorithms than executing them directly.                                              |
|   4 | Code mode revolution: Multiple companies published papers advocating LLM agents building MCP servers for tool orchestration.                                                            |
|   5 | Traditional LLM tool calling struggles with dynamic orchestration and context overload, especially in multi-step workflows.                                                             |
|   6 | Two context overload types: tool catalog bloat (mostly solved) and tool calling bloat (large, irrelevant context in stack).                                                             |
|   7 | Code mode reduces context bloat by having agents generate MCP servers that orchestrate tool calls in code.                                                                              |
|   8 | Concerns with code mode: security risks, lack of observability, compliance issues, and generated code running in production.                                                            |
|   9 | Goal: Create a no-code, open-source, observable, composable, and agent-friendly solution for MCP orchestration.                                                                         |
|  10 | Existing enterprise workflow tools (Naden, Zapier, Workato) are mature, MCP-first, and recommended for large-scale needs.                                                               |
|  11 | MCP Graph: declarative YAML-based DSL for MCP tool aggregation and orchestration using directed graphs of nodes.                                                                        |
|  12 | Uses JSONata for data transformation and JSON Logic for conditional logic; both are well-supported by LLMs.                                                                             |
|  13 | Node types: entry, MCP (tool call), transform, switch (conditional), exit.                                                                                                              |
|  14 | MCP Graph can be installed as an npm package or from GitHub; includes a UX tool for visualization and debugging.                                                                        |
|  15 | Allows tool composition, reshaping, and creation of virtual MCP servers.                                                                                                                |
|  16 | Initial attempts to have agents build graphs failed due to lack of context/tools; solution: MCP Graph Toolkit server provides agents with development tools and debugging capabilities. |
|  17 | Iterative dev cycle with LLMs improved agent success in building workflows.                                                                                                             |
|  18 | MCP Graph, MCP Graph UX, and MCP                                                                                                                                                        |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=tTCnNsaPX5Q)