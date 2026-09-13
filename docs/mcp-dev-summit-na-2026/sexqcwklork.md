---
layout: default
title: "MCP Meets Java: Engineering the MCP Java SDK - Dariusz Jędrzejczyk, Broadcom"
nav_order: 57
parent: Mcp Dev Summit Na 2026
type: Video Note
description:
  Darius from Broadcom’s Spring OSS team discusses the development of the
  official Java SDK for MCP, highlighting Java’s longstanding enterprise adoption,
  strong integration capabilities, and performance advantages due to the JVM. The
  SDK was...
resource: https://www.youtube.com/watch?v=SeXqcwkLOrk
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

Darius from Broadcom’s Spring OSS team discusses the development of the official Java SDK for MCP, highlighting Java’s longstanding enterprise adoption, strong integration capabilities, and performance advantages due to the JVM.
The SDK was designed to enable quick experimentation and production readiness, opting for a pragmatic approach that balances type safety with extensibility, and avoids undesired states by leveraging Java’s static typing.
The team navigated evolving MCP transport protocols by introducing dedicated implementations for different transport types, ensuring clarity and reducing errors.
They also addressed challenges around concurrency, streaming, and authorization by building on Java’s multi-threading features, using reactive streams, and providing hooks for integration with established enterprise frameworks without re-implementing security solutions.
The SDK remains open to extension, supports pluggable JSON parsing, and aims to evolve alongside Java’s advancements, with future plans for a unified, loom-friendly API and ongoing work to achieve tier one conformance with the latest MCP specifications.

# Main Points

|   # | Main point                                                                                                                    |
| --: | ----------------------------------------------------------------------------------------------------------------------------- |
|   1 | Darius from Broadcom, Spring OSS team, works on Java SDK for MCP.                                                             |
|   2 | Java is widely adopted in enterprises, with 30+ years in production and ~30% of engineers using it.                           |
|   3 | 90% of Fortune 500 companies use Java; it's favored for integration and a broad ecosystem.                                    |
|   4 | Java's evolution focuses on AI integration and GPU performance.                                                               |
|   5 | Java SDK for MCP shows best performance in latency and throughput, with some memory tradeoff.                                 |
|   6 | JVM provides static typing, JIT compilation, and advanced garbage collection.                                                 |
|   7 | Java SDK for MCP was open-sourced soon after MCP's announcement; team of three.                                               |
|   8 | SDK design aimed for quick start, experimentation, and production readiness.                                                  |
|   9 | Chose not to use SPI approach for MCP; built around JDK HTTP client.                                                          |
|  10 | Implemented MCP server transport provider using Jakarta Servlet spec; not production-ready alone.                             |
|  11 | MCP protocol evolved from stdio to remote SSE, sessions, streamable HTTP, and stateless transports.                           |
|  12 | SDK introduced stateless transport support early for scalability.                                                             |
|  13 | Chose strong type safety over API stability to avoid conditional logic and user errors.                                       |
|  14 | SDK uses builders for assembling server/client abstractions with transport-specific APIs.                                     |
|  15 | Streamable transport allows session-based features; stateless transport restricts unsupported operations.                     |
|  16 | Java's multi-threading core; virtual threads (Project Loom) introduced in Java 21, but SDK targets Java 17 for compatibility. |
|  17 | Java lacks high-level streaming APIs; SDK uses reactive streams and plans for loom-friendly APIs.                             |
|  18 | SDK is open for extension, enabling integration with various frameworks and authorization schemes.                            |
|  19 | No built-in auth library; provides hooks for frameworks to handle authorization.                                              |
|  20 | Uses Jackson annotations for JSON binding; parsing is pluggable for framework compatibility.                                  |
|  21 | Key takeaways: stay pragmatic, cater to broad ecosystem, enforce type safety, and enable extensibility.                       |
|  22 | For retries/circuit breakers, use reactive operators or language constructs; circuit bre                                      |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=SeXqcwkLOrk)
