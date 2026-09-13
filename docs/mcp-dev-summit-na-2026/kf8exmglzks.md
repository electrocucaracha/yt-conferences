---
layout: default
title:
  "The MCP Gateway Pattern: Aggregation, Composition, and Beyond - Juan Antonio
  Osorio, Stacklok"
nav_order: 92
parent: Mcp Dev Summit Na 2026
type: Video Note
description:
  The speaker, Juan Antonio ("Oz"), introduces the topic of MCP gateways,
  discussing their similarities and differences with traditional API gateways, particularly
  in the context of scaling, security, and integration with large language model...
resource: https://www.youtube.com/watch?v=kF8EXMglZKs
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

The speaker, Juan Antonio ("Oz"), introduces the topic of MCP gateways, discussing their similarities and differences with traditional API gateways, particularly in the context of scaling, security, and integration with large language models (LLMs).
He emphasizes that while many established gateway patterns still apply, MCP gateways must address unique challenges such as stateful connections, efficient context management for LLMs, and tool aggregation, including handling tool naming collisions and security concerns like tool shadowing.
Oz demonstrates how gateways can compose workflows and meta-tools to reduce context bloat and improve agent efficiency, using examples from his own projects and showing how agents interact with these tools through a live demo.
He also touches on authentication strategies, token exchange, and the potential for gateways to support code-based tool composition, noting emerging patterns and ongoing community collaboration around the MCP specification.
The talk concludes with an invitation to participate in a survey and a Q&A session.

# Main Points

|   # | Main point                                                                                                                                                          |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Consensus reached among participants; most are using or running MCP servers, some at scale, some using gateways.                                                    |
|   2 | Presentation focuses on gateways and observed patterns from customer interactions.                                                                                  |
|   3 | Gateways provide a single source of truth, authentication, logging, and monitoring, similar to API gateways.                                                        |
|   4 | MCP gateways differ from API gateways due to LLM-specific nuances, especially in communication and context management.                                              |
|   5 | In MCP gateways, tokens and context utilization are critical; exposing too many tools can cause context bloat.                                                      |
|   6 | Security is a key concern; tool shadowing (tools pretending to be others) can be intercepted by gateways.                                                           |
|   7 | Gateways should provide visibility and trust mechanisms, including registries for MCP servers.                                                                      |
|   8 | MCP protocol is stateful, making session and connection management more complex than traditional API gateways.                                                      |
|   9 | Tools are first-class citizens in MCP; tool name collisions are common and require strategies like prefixing, overriding names/descriptions, or setting priorities. |
|  10 | Gateways must handle multiple authentication strategies and integrations (e.g., token exchange, downscoping, API keys).                                             |
|  11 | Meta tools (e.g., find tool, call tool) help manage context bloat by semantically indexing and wrapping tools, improving agent efficiency.                          |
|  12 | Workflows can be composed in gateways, allowing agents to execute complex tasks as single virtual tools, reducing non-determinism and unreliability.                |
|  13 | Demo showcased VMCP project, using YAML configuration to compose and expose tools, prefixing tools by workload, and running parallel calls.                         |
|  14 | Gateway enables structured outputs and efficient tool aggregation for agents.                                                                                       |
|  15 | Code mode and exposing tools via scripting languages (e.g., Starlark, Lua) are emerging patterns in gateways.                                                       |
|  16 | REST-to-MCP translation exists but is not optimal for LLMs.                                                                                                         |
|  17 | The MCP spec is evolving, with active discussions on gateway patterns and chaining.                                                                                 |
|  18 | Survey available for feedback on composition and LLM/MCP customization us                                                                                           |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=kF8EXMglZKs)
