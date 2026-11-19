---
layout: default
title: MCP at 18 Months Shaun Smith
nav_order: 84
parent: MCP Dev Summit NA 2026
type: Video Note
description: "Jones, an NCP maintainer and Hugging Face employee, explains how the evolution of AI models through reinforcement learning has transformed the utility of the Model Context Protocol (MCP)."
resource: "https://www.youtube.com/watch?v=YDtpj9fFTus"
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

Jones, an NCP maintainer and Hugging Face employee, explains how the evolution of AI models through reinforcement learning has transformed the utility of the Model Context Protocol (MCP).
He notes that modern models now possess advanced capabilities for long-running tasks, dynamic tool calling, and code execution, which allow them to navigate complex environments and utilize shell access more effectively than at MCP's launch.
This shift enables significant efficiencies, such as bypassing expensive language model post-processing by directly generating user interface components or executing code in specialized environments.
Jones highlights the importance of standardized protocols like the Agent Iron Protocol and the open-sourced Responses API, which facilitate the bundling of interactive environments and improve interoperability across different models and tools.
He concludes that MCP has successfully achieved product-market fit by becoming commodity infrastructure, providing essential transportability and authentication that support both consumer and enterprise use cases, while also enabling the seamless integration of diverse AI capabilities into a unified ecosystem.

# Main Points

|   # | Main point                                                                                                                                               |
| --: | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | The speaker works at Hugging Face, maintaining NCP servers, the NCP maintainer role, and an open-source agent with full NCP capabilities.                |
|   2 | The debate surrounding NCP is considered more interesting than the protocol itself, which is viewed as a positive development.                           |
|   3 | At NCP launch, key features like queues, long-running code, reasonable remote transports, and agent skill agreements were missing.                       |
|   4 | Modern expectations now include handling 80 to 100 tool calls within a single session, similar to standard software engineering practices.               |
|   5 | Reinforcement learning in post-training allows models to navigate environments, score trajectories, and drive loops toward bigger goals.                 |
|   6 | Meta’s Agent library provides an open-source framework for conducting reinforcement learning experiments.                                                |
|   7 | A minimal harness with only 390 lines of code and a single shell tool achieved 47.6% on the SWE-bench benchmark.                                         |
|   8 | Smarter tool use and non-determinism have changed harnesses, which previously lacked shell access for local PC operations.                               |
|   9 | Models can now navigate environments, recover from mistakes, and learn through ingested context to enable effective skill usage.                         |
|  10 | Dynamic tool calling allows models to access thousands of specialized machine learning models through a 45-token tool definition.                        |
|  11 | NCP provides authentication to ensure correct licensing and supports multi-modal capabilities that shell tools cannot easily achieve.                    |
|  12 | Code execution tools allow agents to write and execute their own utilities, leveraging Bash as a dense general-purpose execution language.               |
|  13 | Modern models often ship with embedded code interpreters and compilers alongside inference compute.                                                      |
|  14 | There is a growing distinction between generation and execution environments, allowing for specialized model selection for different jobs.               |
|  15 | NCP enables the deployment of smaller, customized models as servers to achieve similar performance with lower costs.                                     |
|  16 | NCP facilitates side effects and extra processing of results, avoiding expensive output tokens for re-processing large data sets.                        |
|  17 | The emerging pattern involves using libraries like Prefect to generate user interface components directly instead of post-processing data via the model. |
|  18 | The boundaries between model creation, execution, and command changes are blurring in live products with lightweight sandboxes.                          |
|  19 | The Agent Iron Protocol, launched by Facebook, is a normative protocol that observes current practices to define shared patterns for agent deployment.   |
|  20 | The Agent Iron Protocol supports chaining, cancellation, and session-based management for scaling agent tasks.                                           |
|  21 | OpenAI’s Responses API normalizes patterns beyond the Chat Completions API and has been open-sourced.                                                    |
|  22 | The Responses API distinguishes between internal resources provided by the host and external resources supplied by the client.                           |
|  23 | Both the Agent Iron Protocol and Open Responses allow for bundling interactive environments and presenting a unified frontend.                           |
|  24 | NCP has not died but has achieved near-perfect product-market fit through experimentation.                                                               |
|  25 | NCP is particularly well-suited for consumer and enterprise cases due to ease of use and support for regulatory needs.                                   |
|  26 | Thousands of clients can connect via a simple URL with authenticated access, which is a significant advantage.                                           |
|  27 | The resource-based mechanism with URI schemes in NCP design has allowed for rapid rollout of new features like Apps SDK.                                 |
|  28 | Shell execution integrated into models has changed dynamics for standard I/O servers, providing progressive discovery.                                   |
|  29 | Tools like MCP CLI and MC Porter allow deploying NCP servers in execution environments to gain composability benefits.                                   |
|  30 | NCP has matured into commodity infrastructure, playing a central role in enabling transportability and portability.                                      |
|  31 | The true value of NCP lies in API access to resources or data that would otherwise be inaccessible.                                                      |

# Video

[![Video thumbnail](https://img.youtube.com/vi/YDtpj9fFTus/hqdefault.jpg)](https://www.youtube.com/watch?v=YDtpj9fFTus)

[Watch on YouTube](https://www.youtube.com/watch?v=YDtpj9fFTus)
