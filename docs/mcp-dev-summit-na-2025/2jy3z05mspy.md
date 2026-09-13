---
layout: default
title:
  "[Session] Resources: Building the Next Wave of MCP Apps with Shaun Smith,
  LLMindset"
nav_order: 5
parent: Mcp Dev Summit Na 2025
type: Video Note
description:
  The speaker discusses their experience integrating with MCP (Modular
  Communication Protocol), highlighting how MCP servers and tools enable large language
  models (LLMs) to combine tool calls and generate valuable outputs with minimal coordi...
resource: https://www.youtube.com/watch?v=2Jy3z05MspY
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

The speaker discusses their experience integrating with MCP (Modular Communication Protocol), highlighting how MCP servers and tools enable large language models (LLMs) to combine tool calls and generate valuable outputs with minimal coordination between server and host application developers.
They note the rapid adoption of MCP tools, driven by their ease of use and compatibility with existing APIs, but caution that adding more tools increases context consumption and can reduce performance and reliability, especially in multi-turn conversations.
The talk emphasizes the importance of resources—structured data with MIME types and URIs—which provide semantic context and can be embedded in prompts and tool results to improve LLM task performance and user experience.
The speaker also describes emerging user experience patterns, the benefits of in-context learning, and the potential of URI schemes to facilitate interoperability and richer applications.
They conclude by encouraging involvement in the MCP working group to further refine the protocol and enhance the ecosystem.

# Main Points

|   # | Main point                                                                                                                        |
| --: | --------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Initial integration with MCP involved generating images and combining with fetch server to create cat dioramas of current events. |
|   2 | LLMs can combine tool calls to produce valuable outputs, creating a sense of "magic."                                             |
|   3 | Tools make it easy for MCP server developers to provide information to LLMs via tool descriptions and results.                    |
|   4 | Tool adoption has increased due to the symmetry between MCP tool calling interface and completions/messages APIs.                 |
|   5 | Over 10,000 MCP servers are listed in registries.                                                                                 |
|   6 | MCP servers require minimal coordination between server and host application developers; only MCP protocol agreement is needed.   |
|   7 | Tool descriptions and results consume context, impacting performance.                                                             |
|   8 | Experiment showed using extra tools increased runtime by 47% and nearly doubled token consumption.                                |
|   9 | LLM reliability and performance drop in multi-turn conversations, especially with underspecified tasks.                           |
|  10 | Integrating tools differs from traditional APIs; tool results become the next conversation turn.                                  |
|  11 | User experience patterns are emerging for tool selection, but managing many tools can burden users.                               |
|  12 | Host/client applications must decide how to handle various content types (e.g., images, audio) from tool calls.                   |
|  13 | Most content is sent as plain text, but resources can embed text or binary data with MIME types and URIs.                         |
|  14 | Resources can be embedded in prompts and tool results, providing semantics and enabling intelligent handling.                     |
|  15 | Prompts can inject task context and improve LLM performance by consolidating context and reducing tool chaining.                  |
|  16 | Prompts support in-context learning with user-assistant pairs and embedded resources.                                             |
|  17 | Resources are subscribable, allowing updates and dynamic context mutation.                                                        |
|  18 | Sampling can be triggered at any time for summarization, prompt generation, or UI construction.                                   |
|  19 | URI schemes enable semantic contracts between MCP server developers and client application builders.                              |
|  20 | Standardized URI schemes facilitate interoperability and richer user ex                                                           |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=2Jy3z05MspY)
