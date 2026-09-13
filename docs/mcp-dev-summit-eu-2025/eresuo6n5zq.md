---
layout: default
title: "[Session] Building Scalable MCP Servers with Node with Matteo Colina - Platformatic.dev"
nav_order: 12
parent: Mcp Dev Summit Eu 2025
type: Video Note
description:
  The speaker introduces themselves as a Node.js developer and board member
  of the Open and GraphQL Foundations, then focuses on the Model Context Protocol
  (MCP), which enables AI models to interact with the digital world. They explain
  the ag...
resource: https://www.youtube.com/watch?v=ERESuo6n5ZQ
tags:
  - mcp-dev-summit-eu-2025
  - video
  - learning
status: stable
generated:
  by: process:yt-conferences-okf
  at: 2026-09-12 00:00:00+00:00
---

# Summary

The speaker introduces themselves as a Node.js developer and board member of the Open and GraphQL Foundations, then focuses on the Model Context Protocol (MCP), which enables AI models to interact with the digital world.
They explain the agentic loop in MCP, emphasizing its slow, iterative process and the need for coarse-grained tool functions due to high execution costs.
The talk highlights the challenges of building scalable, reliable, and stateful MCP servers, particularly over unreliable network connections, and discusses the limitations of current SDKs and the importance of message delivery guarantees.
To address these issues, the speaker describes their Node.js-based library, @platformatic/mcp, which uses Redis to manage state, support resumability, and handle authentication, while also detailing the complexities of implementing dynamic client registration with OAuth 2.1.
The presentation concludes with a demonstration of the system and an invitation to try the tools, noting the company's expertise in enterprise Node.js solutions.

# Main Points

|   # | Main point                                                                                                                        |
| --: | --------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Speaker is a Node.js developer, board member of the Open Foundation and GraphQL Foundation.                                       |
|   2 | Maintains widely used Node.js software with billions of downloads on npm.                                                         |
|   3 | Focus of talk: Model Context Protocol (MCP).                                                                                      |
|   4 | MCP allows AI models to interact with and change the digital world.                                                               |
|   5 | Agentic loop in MCP is slow; involves repeated calls between app, LLM, and tools.                                                 |
|   6 | Execution time for MCP actions is measured in seconds or minutes, unlike typical web requests.                                    |
|   7 | MCP tools should be coarse-grained due to high invocation costs.                                                                  |
|   8 | Streaming and server-sent events (SSE) are critical for long-running MCP systems.                                                 |
|   9 | MCP servers can be local (stdio, highly stateful) or remote (socket-based, different security needs).                             |
|  10 | Local MCP servers are extremely stateful; remote servers face challenges with state and connection reliability.                   |
|  11 | Official TypeScript SDK for MCP is stateful, making robust remote/serverless scaling difficult.                                   |
|  12 | TCP connections are unreliable; 20% may be dropped (per Cloudflare).                                                              |
|  13 | Sticky sessions are discouraged due to operational challenges.                                                                    |
|  14 | Message delivery guarantees: at most once (fire and forget), at least once (preferred), exactly once (complex).                   |
|  15 | MCP currently lacks at least once delivery guarantee but uses SSE with last-event-id for resumability.                            |
|  16 | Developed a Node.js library (@platformatic/mcp) using Redis to store state for scalable, resumable MCP servers.                   |
|  17 | State includes client authentication, stream states, and unique client IDs.                                                       |
|  18 | Supports OAuth 2.1 dynamic client registration (DCR), though DCR is complex and not well-supported by many authorization servers. |
|  19 | Demoed MCP server setup, authentication flow, and state management.                                                               |
|  20 | Noted challenges with DCR and OAuth providers like Auth0 and Okta.                                                                |
|  21 | Platformic builds enterprise Node.js systems and offers a free book on Node.js in the enterprise.                                 |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=ERESuo6n5ZQ)
