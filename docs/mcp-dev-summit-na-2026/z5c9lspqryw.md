---
layout: default
title: Code Mode Is Best Served in the Shell - Jan Curn, Apify
nav_order: 9
parent: Mcp Dev Summit Na 2026
type: Video Note
description:
  Yan, founder and CEO of Appify, discusses the challenges and solutions
  related to integrating AI agents with tool protocols, focusing on the MCP (Machine
  Control Protocol) and CLI (Command Line Interface) approaches. He explains that
  while...
resource: https://www.youtube.com/watch?v=Z5C9LSpQrYw
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

Yan, founder and CEO of Appify, discusses the challenges and solutions related to integrating AI agents with tool protocols, focusing on the MCP (Machine Control Protocol) and CLI (Command Line Interface) approaches.
He explains that while MCP became popular for connecting agents with tools, its widespread adoption led to inefficiencies, particularly due to clients loading all tool definitions into the context, which wastes tokens and reduces accuracy.
Yan reviews several solutions, including splitting context among sub-agents, dynamic tool discovery, and treating tools as code, but notes that these often require complex implementation.
He highlights the advantages of command-line tools, which AI models understand well due to extensive training data, allowing for progressive tool discovery and efficient context management, though command-line tools act as black boxes and lack standard protocols for secure remote access.
To combine the strengths of both approaches, Yan introduces MCPC, an open-source CLI client for MCP that enables agents to interact with MCP servers through familiar shell commands, supporting features like dynamic tool discovery, asynchronous tasks, and secure authentication.
He demonstrates MCPC’s capabilities and argues for making it the official shell SDK for MCP, aiming to bridge the gap between CLI and MCP and streamline AI tool integration.

# Main Points

|   # | Main point                                                                                                                                                                |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Yan, founder and CEO of Appify, presents on tools for AI, focusing on why code mode is best served in shell.                                                              |
|   2 | MCP became a popular open-source project in AI, leading to many servers and registries.                                                                                   |
|   3 | Criticism of MCP has increased recently, with complaints about context overload and inefficiency.                                                                         |
|   4 | Main problem: MCP clients/AI agents load all servers and tools into context, wasting tokens and reducing accuracy.                                                        |
|   5 | MCP protocol itself is not at fault; poor implementation by clients causes issues.                                                                                        |
|   6 | Solution 1: Split context into sub-agents, but this only partially mitigates the problem and can expose sensitive data.                                                   |
|   7 | Solution 2: Dynamic/progressive tool discovery—load tools only when needed, as used by top AI agents; more efficient but harder to implement.                             |
|   8 | Solution 3: Code mode—treat tools as code, generating code to call tools; models are better at code than tool calls, but implementation is complex.                       |
|   9 | Command-line tools avoid context overload by progressive discovery; models know common command-line tools from training data and can use help commands to learn new ones. |
|  10 | Command-line tools are run as code in sandbox environments, allowing efficient context management.                                                                        |
|  11 | Shell is highly familiar to models due to extensive training data and concise documentation.                                                                              |
|  12 | CLI is a universal interface but acts as a black box, lacking standard protocols and secure remote interaction.                                                           |
|  13 | Proposal: Combine MCP and CLI—wrap MCP with a CLI interface (MCPC) for agents to interact via shell.                                                                      |
|  14 | MCPC is an open-source universal CLI client for MCP, supporting full protocol compatibility, lightweight design, and code mode with JSON.                                 |
|  15 | MCPC features: sessions, authentication profiles, dynamic tool discovery, error handling, asynchronous tasks, agent payments via X42, and secure proxies.                 |
|  16 | MCPC enables AI agents to use MCP capabilities via shell without extra coding.                                                                                            |
|  17 | MCPC often outperforms native CLIs and MCP implementations in benchmarks.                                                                                                 |
|  18 | Appify plans to donate MCPC to the HTT foundation as an official she                                                                                                      |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=Z5C9LSpQrYw)
