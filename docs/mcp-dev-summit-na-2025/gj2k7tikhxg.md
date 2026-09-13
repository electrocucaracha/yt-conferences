---
type: Video Note
title: "[Session] Building and Deploying Remote MCP Servers with Dina Kozlov from Cloudflare"
description: "Dina Coslov, a product manager at Cloudflare, shares her experience working with the engineering team to simplify building MCP (Multi-Client Platform) servers, emphasizing how easy it has become to create remote MCP servers that retain user..."
resource: https://www.youtube.com/watch?v=gJ2K7tIKhxg
tags: ["mcp-dev-summit-na-2025", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

Dina Coslov, a product manager at Cloudflare, shares her experience working with the engineering team to simplify building MCP (Multi-Client Platform) servers, emphasizing how easy it has become to create remote MCP servers that retain user context across different clients.
She recounts her initial excitement using MCP to deploy code with Claude and highlights the importance of persistent user memory, which allows personalized experiences regardless of the client used.
Demonstrating her own MCP server, Best Reads, she shows how it tracks user preferences and book history to provide tailored recommendations, leveraging Cloudflare’s durable objects for built-in, per-user storage and context.
Coslov explains that deploying MCP servers on Cloudflare is straightforward, with built-in support for remote transport methods and automatic scaling, and encourages attendees to try building their own using provided examples and documentation.
She concludes by promising to share her Best Reads MCP server code on GitHub, inviting others to experiment and innovate with these tools.
# Main Points

|   # | Main point                                                                                                                  |
| --: | --------------------------------------------------------------------------------------------------------------------------- |
|   1 | Dina Coslov, Product Manager at Cloudflare, worked with engineering to simplify building MCP servers.                       |
|   2 | Audience was polled on experience with MCP and remote MCP servers.                                                          |
|   3 | Goal: demonstrate how easy it is to build a remote MCP server.                                                              |
|   4 | Dina’s first MCP experience involved using Claude to deploy code to Cloudflare.                                             |
|   5 | MCP enables Claude to deploy code directly, reducing manual steps.                                                          |
|   6 | Claude’s conversation history improves user experience by remembering preferences and context.                              |
|   7 | Limitation: context is lost when switching MCP clients, as memory is client-side.                                           |
|   8 | Importance of MCP servers holding user memory and context highlighted.                                                      |
|   9 | Demo: Dina built an MCP server called Best Reads to track book preferences and provide recommendations.                     |
|  10 | Best Reads uses authentication so multiple users can have personalized recommendations.                                     |
|  11 | MCP server logs user preferences and reading history, enabling personalized book suggestions across different clients.      |
|  12 | MCP servers on Cloudflare use durable objects, providing built-in memory and per-user storage.                              |
|  13 | Durable objects act as agents with compute and storage, creating a database for each user.                                  |
|  14 | This architecture removes the need for separate backend, reduces latency, and scales automatically.                         |
|  15 | Cloudflare MCP servers are globally deployed, running close to users and AI agents.                                         |
|  16 | Example code: tools set and retrieve user preferences using built-in state management.                                      |
|  17 | Cloudflare uses MCP servers to power secure, isolated environments for code execution, maintaining persistent user context. |
|  18 | Deploying an MCP server on Cloudflare is streamlined: click “deploy,” name the server, and it’s live.                       |
|  19 | Cloudflare MCP servers handle remote transport methods (streamable HTTP, server-sent events) by default.                    |
|  20 | Example MCP server includes pre-built tools for calculations.                                                               |
|  21 | Example code and Best Reads MCP server will be posted on GitHub for others to use.                                          |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=gJ2K7tIKhxg)