---
layout: default
title:
  "Dynamic MCPs: Agentic Discovery, Configuration, and Management of MCP Workloads
  - Jim Clark, Docker"
nav_order: 19
parent: Mcp Dev Summit Na 2026
type: Video Note
description:
  Jim Clark discusses his experiences and insights on the evolution of
  MCP (Machine Control Protocol) servers and agent tooling, drawing parallels to the
  Language Server Protocol's impact on development environments. He describes the
  initial...
resource: https://www.youtube.com/watch?v=3imd6g6nM2s
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

Jim Clark discusses his experiences and insights on the evolution of MCP (Machine Control Protocol) servers and agent tooling, drawing parallels to the Language Server Protocol's impact on development environments.
He describes the initial challenges of integrating tools across various SDKs and how MCP introduced a standard interface that simplified agent-tool interactions.
Clark explains the development of MCP Gateway and the concept of catalogs, which curate and govern available MCP servers, and introduces "primordial tools" like MCP find, add, and config that help agents dynamically discover, configure, and use relevant tools.
He highlights the importance of context management, deferred tools, sub-agents, and tool compression (such as code mode) to address the growing complexity as the number of MCP servers increases.
Throughout, Clark emphasizes the need for agents to efficiently select and configure tools, the benefits of sandboxed runtimes, and the ongoing challenges and opportunities in curating and securing MCP catalogs.

# Main Points

|   # | Main point                                                                                                                |
| --: | ------------------------------------------------------------------------------------------------------------------------- |
|   1 | Jim Clark prefers using spaces over tabs and uses the Nyx Darwin operating system.                                        |
|   2 | The presentation was created by dictating, using tools like Mermaid, MARP, FFmpeg, and PowerPoint templates.              |
|   3 | In November 2024, there were zero MCPs; Jim worked at Docker Labs and expected tools to be referenced in containers.      |
|   4 | Previously, using tools across different agent frameworks required building new adapters for each SDK.                    |
|   5 | MCP introduced a standard interface, freeing agents from being tied to specific tools or SDKs.                            |
|   6 | MCP is similar to the Language Server Protocol in decoupling tools from their environments.                               |
|   7 | By January 2025, MCPs had proliferated; the protocol enabled agents to access existing tools and APIs.                    |
|   8 | Contrary to early predictions, many new MCP servers were authored rather than just unlocking existing tools.              |
|   9 | MCP servers evolved from local to remote, requiring better handling of configuration and authorization (e.g., OAuth).     |
|  10 | MCPJSON files define how agents see and use MCPs; configuring them can be complex.                                        |
|  11 | Docker’s open-source MCP Gateway mediates agent access to MCP servers.                                                    |
|  12 | Inspired by Nyx and Direnv, environments should adapt based on project context.                                           |
|  13 | Agents need catalogs to know which MCP servers are available and trusted.                                                 |
|  14 | Primordial tools (e.g., MCP find, MCP add, MCP config) help agents discover, add, and configure MCPs dynamically.         |
|  15 | Agents can start with an empty session and build up context by discovering and adding MCPs as needed.                     |
|  16 | Memory is important for saving and reusing useful MCP sessions.                                                           |
|  17 | Elicitations allow agents or gateways to request user input for configuration.                                            |
|  18 | Context bloat is a challenge as agents load many MCP servers; deferred tools and sub-agents help manage relevant context. |
|  19 | Tool compression and code mode allow agents to combine multiple MCPs into a single tool or sandboxed environment.         |
|  20 | Live build agent loops enable iterative tool creation and testing within MCP sessions.                                    |
|  21 | Security and curation are important for                                                                                   |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=3imd6g6nM2s)
