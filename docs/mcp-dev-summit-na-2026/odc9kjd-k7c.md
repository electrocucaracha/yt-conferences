---
layout: default
title: "MCP's Missing Half: Why Second-Order Servers Don't Exist Yet"
nav_order: 83
parent: MCP Dev Summit NA 2026
type: Video Note
description: 'Jerome, an engineer at ThoughtWorks and early contributor to the Model Context Protocol (MCP), presents a proposal for "Symmetric MCP" to address significant limitations in current MCP server archi...'
resource: "https://www.youtube.com/watch?v=OdC9KJd-k7c"
tags:
  - mcp-dev-summit-na-2026
  - video
  - learning
status: stable
generated:
  by: process:yt-summarizer-okf
  at: 2026-11-15T16:54:07+00:00
---

# Summary

Jerome, an engineer at ThoughtWorks and early contributor to the Model Context Protocol (MCP), presents a proposal for "Symmetric MCP" to address significant limitations in current MCP server architectures.
He argues that existing "second-order" MCP servers, such as those for agent orchestration, programmatic code execution, and file processing, are difficult to implement due to fragmented authentication, poor composability, and inefficient context management.
The core idea of Symmetric MCP is to allow MCP clients to expose their own tools and resources to MCP servers, effectively turning the client into a central routing switchboard that manages trust and authentication.
This bidirectional approach simplifies complex workflows by enabling servers to call other servers through the client, thereby centralizing security and reducing the need for distributed OAuth tokens.
Jerome demonstrates that this model supports advanced use cases like multi-agent communication and dynamic tool creation, while also improving security and developer experience compared to the current fragmented ecosystem.

# Main Points

|   # | Main point                                                                                                                                                                     |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   1 | Jerome, a ThoughtWorks engineer and early MTP contributor, proposes "Symmetric MCP" to solve composability and authentication issues in the protocol.                          |
|   2 | Current MTP servers handle basic tasks like reading content, posting data, and sequential thinking, but lack advanced intermediary capabilities.                               |
|   3 | Second-order" MTP servers, such as agent runners, tool search, and code mode runtimes, are difficult to implement due to fragmented trust and complex OAuth flows.             |
|   4 | The concept aligns with Andrej Karpathy's "LLM Operating System" theory, where the LLM acts as a logic core with pluggable components for complex tasks.                       |
|   5 | Building agent servers or code mode runtimes currently requires spreading OAuth tokens across multiple servers, creating poor user experience and security risks.              |
|   6 | Handling file attachments is inefficient because it relies on base64-encoded strings in tool calls, which bloats the context window and complicates processing.                |
|   7 | Symmetric MCP allows clients to expose tools and resources to servers, enabling servers to call back into the client to access other connected servers.                        |
|   8 | This symmetry transforms the MTP client into a central switchboard or routing layer that manages authentication and tool requests between servers.                             |
|   9 | An agent server can use this symmetry to invoke tools from other MTP servers via the client, decoupling agent logic from specific tool implementations.                        |
|  10 | Code mode can be implemented as a pluggable MTP server that exposes a runtime to programmatically call tools routed through the client.                                        |
|  11 | Attachment processing becomes trivial as servers can list files as resources and return processed results, avoiding base64 encoding in tool parameters.                        |
|  12 | The architecture supports inter-agent communication by allowing MTP servers to act as both clients and servers, enabling dynamic tool creation at runtime.                     |
|  13 | User-configurable middleware, such as safety checks, rate limiting, and dynamic server relays, can be composed like Unix pipes within the ecosystem.                           |
|  14 | The primary barrier to adoption is the need for easier protocol extensions and bidirectional transport, which adds complexity to clients but simplifies overall system design. |
|  15 | A prototype demonstrated a hub-and-spoke model where an agent routes code execution through a code mode server and back to the client for final tool calls.                    |
|  16 | Security concerns regarding open permissions are mitigated by centralizing trust in the client, which is considered more secure than distributing tokens across servers.       |
|  17 | Sampling in MTP is viewed as a complementary feature where servers can provide tool lists for inference calls, improving the clarity of the specification.                     |

# Video

[![Video thumbnail](https://img.youtube.com/vi/OdC9KJd-k7c/hqdefault.jpg)](https://www.youtube.com/watch?v=OdC9KJd-k7c)

[Watch on YouTube](https://www.youtube.com/watch?v=OdC9KJd-k7c)
