---
type: Video Note
title: "Path to V2 for MCP SDKs - Max Isbey, Anthropic"
description: "Max, the maintainer of the Python MCP SDK, presents an overview of the upcoming version 2 changes, focusing on transport mechanisms and breaking updates affecting both Python and other SDKs. He explains the evolution from standard IO and HT..."
resource: https://www.youtube.com/watch?v=SfdRReLa93s
tags: ["mcp-dev-summit-na-2026", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

Max, the maintainer of the Python MCP SDK, presents an overview of the upcoming version 2 changes, focusing on transport mechanisms and breaking updates affecting both Python and other SDKs.
He explains the evolution from standard IO and HTTP+SSE transports, which posed scaling challenges, to streamable HTTP and its stateful and stateless variants, highlighting issues with horizontal scaling and session management.
The new June specification introduces a stateless mode using multi-round trip requests (MRTR), allowing elicitation and sampling without persistent sessions, thus improving scalability and simplifying server architecture.
Additional changes include renaming components to reduce confusion, making server definitions more explicit and type-safe, introducing pluggable transports, and adopting a dispatcher pattern to facilitate custom transport integration.
Max also details efforts to ensure smooth migration through comprehensive guides and automated evaluation frameworks, with similar processes underway for the TypeScript SDK.
The talk concludes with a Q&A addressing technical nuances of the new stateless approach and its implications for state management and backward compatibility.
# Main Points

|   # | Main point                                                                                                                                                                                 |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   1 | Max presented updates on MCP SDKs v2, focusing on Python.                                                                                                                                  |
|   2 | MCP initially supported two transports: standard IO (for local development) and HTTP+SSE (for remote servers).                                                                             |
|   3 | HTTP+SSE required persistent open streams, making horizontal scaling difficult.                                                                                                            |
|   4 | Streamable HTTP introduced session IDs for correlating requests, but load balancers could route requests to different servers, causing issues with session state and elicitation/sampling. |
|   5 | Unofficial stateless mode allowed skipping session IDs, but disabled elicitation and sampling.                                                                                             |
|   6 | The new June spec introduces SHTTP stateless mode and MRTR (multi-round trip requests), enabling elicitation and sampling in stateless, horizontally scaled environments.                  |
|   7 | MRTR works by ending a request and asking the client to remake it with additional information, avoiding persistent connections.                                                            |
|   8 | Functions may rerun multiple times in stateless mode, requiring code changes and new programming patterns.                                                                                 |
|   9 | SDKs will provide a compatibility layer for single-server scenarios to ease migration.                                                                                                     |
|  10 | Fast MCP in the SDK has been renamed to MCP server to avoid confusion with an external project.                                                                                            |
|  11 | Low-level server decorators are being removed for more explicit, typed, and declarative handler definitions.                                                                               |
|  12 | Pluggable transports are being introduced, allowing custom transports like websockets or gRPC.                                                                                             |
|  13 | SDK architecture is being refactored around a dispatcher pattern to separate MCP types, wire format, and transport layers.                                                                 |
|  14 | Migration guides are being developed and tested using an evaluation framework with Claude to ensure upgrade documentation quality.                                                         |
|  15 | Beta release of Python SDK v2 is planned for Q2, with final release aligned with the new spec.                                                                                             |
|  16 | Improvements include dispatcher pattern, better auth handling, stateless by default, MRTR, and improved documentation.                                                                     |
|  17 | TypeScript SDK will also have breaking changes, migration guides, and evals for upgrade ease.                                                                                              |
|  18 | Open questions remain about session removal, notifications, and agent chaining                                                                                                             |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=SfdRReLa93s)