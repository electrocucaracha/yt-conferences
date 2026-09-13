---
type: Video Note
title: "What if MCP was Symmetric? - Jerome Swannack, Anthropic"
description: 'Jerome introduces an idea to improve the MCP protocol by enabling more composable and flexible systems through what he calls "symmetric MCP." He explains that current MCP servers are limited in their ability to interact, especially for adva...'
resource: https://www.youtube.com/watch?v=jFWIWfw0Nfs
tags: ["mcp-dev-summit-na-2026", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

Jerome introduces an idea to improve the MCP protocol by enabling more composable and flexible systems through what he calls "symmetric MCP." He explains that current MCP servers are limited in their ability to interact, especially for advanced use cases like agent orchestration, programmatic tool use (code mode), and attachment processing, due to complex authentication flows and scattered trust.
By making MCP symmetric—allowing clients to expose tools to servers and routing tool calls centrally through the client—developers could build more modular, secure, and composable systems, akin to an LLM operating system where components can be plugged together like Unix pipes.
Jerome shares his experience building a prototype of this approach, noting benefits such as improved composability, centralized control, and easier permission management, while acknowledging challenges around protocol extensibility, security, and user experience.
He concludes that although this is a significant conceptual shift, it could unlock richer MCP ecosystems and simplify the development of advanced features.
# Main Points

|   # | Main point                                                                                                                                                     |
| --: | -------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Jerome presents an idea to improve MCP protocol for new use cases and problem-solving.                                                                         |
|   2 | Jerome has been at the company for 2.5 years, was one of the first three engineers on MCP, and is based in London.                                             |
|   3 | MCP servers currently allow reading/exposing content, taking actions, and helping models think (e.g., sequential thinking, math).                              |
|   4 | Proposes "second order" MCP servers that leverage other MCPs installed on the client.                                                                          |
|   5 | Example use case: spinning up an agent that can access other MCP servers, currently difficult due to authentication and trust issues.                          |
|   6 | Context load management is currently handled by clients, leading to duplicated effort; suggests a pluggable, general solution.                                 |
|   7 | Programmatic tool use ("code mode") allows models to call tools via a runtime, reducing token usage and improving performance.                                 |
|   8 | Handling file attachments in MCP is currently cumbersome, involving base64 encoding and context window issues.                                                 |
|   9 | Problems with current approach: complexity spread across system, poor user experience, scattered tokens, poor composability, high token usage for attachments. |
|  10 | Proposes "symmetric MCP": allowing tool calls and tool lists on the client, enabling servers and clients to call each other's tools.                           |
|  11 | Symmetry allows decomposing the LLM OS, centralizing trust/authentication in the client, and routing tool calls like a switchboard.                            |
|  12 | Agent servers and code mode become pluggable into the MCP client, enabling more flexible and composable systems.                                               |
|  13 | Attachment processing becomes simpler by listing attachments as resources.                                                                                     |
|  14 | Enables user-configurable middleware (e.g., safety checks, retries, rate limiting, tool search, dynamic relays).                                               |
|  15 | Composability increases, similar to Unix pipes.                                                                                                                |
|  16 | Main reason for not implementing earlier: other priorities and protocol complexity.                                                                            |
|  17 | Symmetric MCP may increase client complexity but reduces overall system complexity and enables new use cases.                                                  |
|  18 | Security concerns exist; permissions must be managed to prevent malicious access                                                                               |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=jFWIWfw0Nfs)