---
layout: default
title: "[Keynote] MCP201: The Protocol in Depth with David Soria Parra at Anthropic"
nav_order: 7
parent: Mcp Dev Summit Na 2025
type: Video Note
description:
  In this talk, David, a technical staff member at Anthropic and co-creator
  of MCP, provides an in-depth overview of the MCP 2011 protocol, highlighting its
  core primitives—prompts, resources, and tools—and how they enable richer user experie...
resource: https://www.youtube.com/watch?v=C_nqAWHsldo
tags:
  - mcp-dev-summit-na-2025
  - video
  - learning
status: stable
generated:
  by: process:yt-conferences-okf
  at: 2026-09-12 00:00:00+00:00
---

# Summary

In this talk, David, a technical staff member at Anthropic and co-creator of MCP, provides an in-depth overview of the MCP 2011 protocol, highlighting its core primitives—prompts, resources, and tools—and how they enable richer user experiences beyond simple tool calling.
He explains that prompts allow MCP servers to offer dynamic, user-invoked templates for AI interactions, while resources let applications access and manage raw data or files, and tools are model-invoked functions that drive much of MCP’s unique capabilities.
David also introduces advanced features like sampling, which enables servers to request completions from clients’ configured models, and roots, which help servers identify relevant workspaces or data scopes.
He discusses the evolution of MCP from local deployments to web-based integrations, emphasizing the importance of authorization and scalability for broader adoption, including enterprise use cases.
Finally, David touches on upcoming developments such as agent support, asynchronous task execution, elicitation, a public registry API, and expanded SDK offerings, all aimed at making MCP a ubiquitous standard for LLM integrations.

# Main Points

|   # | Main point                                                                                                                                                                                                   |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   1 | David, member of technical staff at Anthropic and co-creator of MCP, presents an in-depth overview of MCP 2011 protocol.                                                                                     |
|   2 | MCP offers several primitives beyond tool calling: prompts, resources, tools, sampling, and roots.                                                                                                           |
|   3 | Prompts: Predefined templates for AI interactions; can be dynamic and fetch data; support argument autocompletion; easy to implement in editors like Visual Studio Code.                                     |
|   4 | Resources: Allow applications to access raw data (e.g., files, database schemas); enable flexible client-side usage such as embeddings or retrieval-augmented generation; increasingly supported in editors. |
|   5 | Tools: Code written by developers that models invoke; enable model-driven actions like querying databases or interacting with systems; widely used for creative integrations.                                |
|   6 | MCP interaction model:                                                                                                                                                                                       |
|   7 | Prompts are user-driven (e.g., slash commands).                                                                                                                                                              |
|   8 | Resources are application-driven.                                                                                                                                                                            |
|   9 | Tools are model-driven.                                                                                                                                                                                      |
|  10 | Sampling: Allows MCP servers to request completions from the client’s configured model, maintaining client control over security, privacy, and cost; planned for broader client support.                     |
|  11 | Roots: Enable MCP servers to query clients for relevant workspaces or URIs, restricting server operations to specific areas (e.g., project folders, Notion sections).                                        |
|  12 | Combining primitives enables richer AI application experiences (e.g., summarizing chat discussions using prompts, resources, tools, and sampling).                                                           |
|  13 | MCP is evolving from local-only servers to web-hosted servers, enabling integration with online accounts and services.                                                                                       |
|  14 | Key requirements for web-scale MCP: robust authorization and scalable infrastructure (e.g., streamable HTTP for REST-like and streaming interactions).                                                       |
|  15 | Enterprise support: MCP servers can be deployed internally, leveraging central identity providers for secure access to company resources.                                                                    |
|  16 | Future directions: asynchronous task execution, user elicitation, official registry API, multi-modality, new SDKs (Ruby, Go), and open-source registries.                                                    |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=C_nqAWHsldo)
