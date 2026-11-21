---
layout: default
title: "GopherCon 2025: Next-Gen AI Tooling with MCP Servers in Go - Katie Hockman"
nav_order: 17
parent: GopherCon 2025
type: Video Note
description: "Katie Hawkman, a Go developer at Merkari, presented a talk at GopherCon on the Model Context Protocol (MCP), an open standard that enables AI agents to interact with external tools and data sources..."
resource: "https://www.youtube.com/watch?v=BNVPE8k6Nmw"
youtube_stats:
  view_count: 4738
  like_count: 132
  channel_subscriber_count: 41100
tags:
  - gophercon-2025
  - video
  - learning
status: stable
generated:
  by: process:yt-summarizer-okf
  at: 2026-11-21T05:22:37+00:00
---

# Summary

Katie Hawkman, a Go developer at Merkari, presented a talk at GopherCon on the Model Context Protocol (MCP), an open standard that enables AI agents to interact with external tools and data sources to improve accuracy and functionality.
She explained that while AI assistants in IDEs often struggle with hallucinations or lack specific organizational context, MCP servers bridge this gap by providing structured access to APIs and internal systems, similar to how HTTP works for web applications.
Hawkman demonstrated the practical application of this technology by live-coding an MCP server in Go using the official Go SDK, which allowed AI agents in both Cursor and Visual Studio Code to accurately retrieve and analyze the GopherCon 2025 agenda.
The demo highlighted how minimal Go code could expose tools like listing sessions and retrieving specific details, enabling the AI to answer complex questions with precise, verified data rather than generic guesses.
She concluded by emphasizing that Go developers can now build these custom MCP servers themselves to empower AI agents with reliable, structured access to their specific development environments and workflows.

# Main Points

|   # | Main point                                                                                                                       |
| --: | -------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Katie Hawkman, formerly of Google and Datadog, now works on Go standardization at Merkari in Tokyo.                              |
|   2 | The talk focuses on the Model Context Protocol (MCP), an open standard for AI systems published in November 2024.                |
|   3 | 76% of programmers use or plan to use AI for coding, according to the 2024 Stack Overflow survey.                                |
|   4 | AI agents in IDEs often lack specific context and powerful tooling, leading to hallucinations or generic answers.                |
|   5 | MCP solves this by allowing AI models to interact with external tools in a consistent, system-agnostic way.                      |
|   6 | MCP servers empower LLMs to perform useful actions, such as creating GitHub issues or updating databases, using structured data. |
|   7 | The Go team is developing an official Go SDK for MCP, currently at version 0.3 with version 1 planned soon.                      |
|   8 | A live demo built an MCP server in Go to interface with the GopherCon 2025 agenda.                                               |
|   9 | The demo used the model context protocol/go SDK/MCP library to define a server and tools.                                        |
|  10 | The server was installed in Cursor and Visual Studio Code via configuration files in the user's home directory.                  |
|  11 | A "list sessions" tool was created to return all GopherCon session metadata, improving AI accuracy.                              |
|  12 | A "get session detail" tool was added to retrieve specific session information by ID, demonstrating parameter handling.          |
|  13 | The AI agent automatically selected the appropriate MCP tools without explicit user instruction.                                 |
|  14 | MCP tools allow for error handling, such as returning errors for invalid session IDs.                                            |
|  15 | The same Go code works across different IDEs like Cursor and Visual Studio Code, ensuring IDE-agnostic development.              |
|  16 | MCP enables AI agents to access structured, reliable data for CI/CD, code analysis, and company-specific APIs.                   |
|  17 | Developers can build custom MCP servers in Go to extend IDE capabilities without waiting for vendor support.                     |

# Video

[![Video thumbnail](https://img.youtube.com/vi/BNVPE8k6Nmw/hqdefault.jpg)](https://www.youtube.com/watch?v=BNVPE8k6Nmw)

[Watch on YouTube](https://www.youtube.com/watch?v=BNVPE8k6Nmw)
