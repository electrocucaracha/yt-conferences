---
type: Video Note
title: "[Session] What MCP Middleware Could Look Like with Yoko Li from A16Z"
description: "Yoko, a partner at Andre and Horwood and an active developer, introduces her work on MCP (Machine Control Protocol) middleware, explaining its role as a horizontal layer between clients and services that centralizes functionalities like aut..."
resource: https://www.youtube.com/watch?v=0WGZNE9FcAk
tags: ["mcp-dev-summit-na-2025", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

Yoko, a partner at Andre and Horwood and an active developer, introduces her work on MCP (Machine Control Protocol) middleware, explaining its role as a horizontal layer between clients and services that centralizes functionalities like authentication, logging, and request handling.
She highlights the challenges developers face when building MCP clients, such as managing agent loops and complex integrations, and argues that middleware can streamline these processes by handling tasks like tool selection, parallelization, dynamic authentication, and logging.
Yoko categorizes middleware features into agent-facing (e.g., access control, rate limiting, user preferences, batching tool calls) and tool-facing (e.g., error normalization, PII reduction, workflow orchestration), emphasizing the need for infrastructure to support the growing ecosystem of MCP servers and tools.
She notes that as machine-initiated workloads increase, robust middleware will be essential for scaling and managing these autonomous processes.
Yoko encourages open sourcing in this space to foster ecosystem growth and invites further discussion from the community.
# Main Points

|   # | Main point                                                                                                                                                          |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Yoko is a partner at Andre and Horwood, leading early-stage investments in developer tools and AI.                                                                  |
|   2 | She is a developer who creates open source software, including an MCP light control repo.                                                                           |
|   3 | MCP middleware is a horizontal layer between client and services, providing functionalities like request interception, transformation, authentication, and logging. |
|   4 | Middleware centralizes functionalities between client, server, and third-party APIs.                                                                                |
|   5 | MCP clients require handling agent loops and integrations, such as tool selection, parallelization, authentication, logging, debugging, and runtime metrics.        |
|   6 | Service proxies allow a single MCP server to proxy requests to multiple MCP servers.                                                                                |
|   7 | Tool parallelization enables agents to make multiple tool calls and aggregate results.                                                                              |
|   8 | Current authentication is simplistic; dynamic, runtime-based authentication is lacking and should be centralized.                                                   |
|   9 | Logging services are needed to track agent tool choices, context, and execution.                                                                                    |
|  10 | Middleware features are categorized as agent-facing and tool-facing:                                                                                                |
|  11 | Agent-facing: access control, rate limiting, user preference-based tool use, batching tool calls.                                                                   |
|  12 | Tool-facing: error normalization, PII reduction, workflow orchestration.                                                                                            |
|  13 | Error normalization helps agents handle errors from third-party services more effectively.                                                                          |
|  14 | PII reduction can be implemented between server and third-party services.                                                                                           |
|  15 | Workflow orchestration is needed for long-running, transactional workloads.                                                                                         |
|  16 | MCP is a protocol, not infrastructure; more infrastructure is needed for broader adoption.                                                                          |
|  17 | There is a tool explosion problem: many MCP servers exist, but clients can only use a limited number of tools.                                                      |
|  18 | Middleware could help dynamically route, cache, and search tools for agents.                                                                                        |
|  19 | Machine-initiated workloads are increasing, requiring agents to autonomously pick tools at runtime.                                                                 |
|  20 | The demand for middleware will grow as machine-initiated workloads scale.                                                                                           |
|  21 | Open sourcing middleware is encouraged to grow the ecosyst                                                                                                          |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=0WGZNE9FcAk)