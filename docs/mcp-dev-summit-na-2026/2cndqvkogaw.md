---
type: Video Note
title: "Every API Is a Tool for Agents - Matt Carey, Cloudflare"
description: "In this talk, Matt from Cloudflare discusses the evolution of enabling agents to interact with APIs, focusing on the challenges of scaling tool access for agents due to large API specifications that exceed model context windows. He outlines..."
resource: https://www.youtube.com/watch?v=2cndQvkoGAw
tags: ["mcp-dev-summit-na-2026", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

In this talk, Matt from Cloudflare discusses the evolution of enabling agents to interact with APIs, focusing on the challenges of scaling tool access for agents due to large API specifications that exceed model context windows.
He outlines three main approaches: using command-line interfaces (CLIs), tool search, and allowing agents to write and execute code directly against typed SDKs in a secure, lightweight sandbox environment.
Matt demonstrates how Cloudflare’s dynamic workers, built on a customized V8 runtime, provide a fast and isolated execution environment for untrusted agent-generated code, enabling composability and safety.
He argues that this code execution approach offers greater flexibility and scalability compared to previous methods, and that recent infrastructure advances now make it feasible to securely run agent-generated code at scale.
The session concludes with a discussion on the importance of standard protocols like MCP for interoperability, the challenges of client implementation, and the potential for broader adoption of programmatic tool use as more robust sandboxing primitives become available.
# Main Points

|   # | Main point                                                                                                                                           |
| --: | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | The talk focuses on enabling agents to use APIs as tools, giving them "hands" to interact with the world.                                            |
|   2 | Matt works on agents and MCP at Cloudflare and maintains the TypeScript SDK.                                                                         |
|   3 | Early agent architectures bundled tools inside agents, leading to large context windows.                                                             |
|   4 | Cloudflare's API is massive (2.3 million tokens); loading all endpoints as tools is impractical.                                                     |
|   5 | Solution: Split API into multiple MCP servers, each covering a subset of endpoints, reducing context size but requiring users to select servers.     |
|   6 | MCP is a protocol for passing tools/capabilities over the wire; the main challenge is agent/client limitations, not MCP itself.                      |
|   7 | Approaches to tool access:                                                                                                                           |
|   8 | CLI: Agents use command-line interfaces, loading commands at runtime for progressive discovery.                                                      |
|   9 | Tool Search: Semantic/hybrid search loads a small set of relevant tools into the agent's context window.                                             |
|  10 | Code Mode: Agents write code (e.g., JavaScript) against a typed SDK, executed in a lightweight sandbox.                                              |
|  11 | Code Mode offers composability and type safety, allowing agents to chain actions and handle complex tasks.                                           |
|  12 | Running untrusted agent-generated code is risky; traditional solutions (DSLs, Docker, VMs) are too heavy.                                            |
|  13 | Cloudflare uses V8-based dynamic workers for fast, secure, isolated code execution without file system or network access by default.                 |
|  14 | Dynamic workers can execute agent code safely and efficiently, enabling new paradigms for agent interaction.                                         |
|  15 | Three main methods for progressive disclosure: CLI, tool search, and code mode; code mode combines flexibility and safety.                           |
|  16 | Cloudflare can now expose its entire API via a single MCP server using code mode, minimizing context size and progressively disclosing capabilities. |
|  17 | Building robust MCP clients is challenging; Cloudflare currently handles code execution server-side.                                                 |
|  18 | MCP standardizes communication between agents and backend services, especially when integrating with third-party agents.                             |
|  19 | Future: More primitives for secur                                                                                                                    |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=2cndQvkoGAw)