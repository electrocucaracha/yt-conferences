---
layout: default
title: "Your Tool Is in Another Castle: How Five Frameworks Reshape the...  - Thierry Damiba, Arcade.dev"
nav_order: 127
parent: AGNTCon + MCPCon North America 2026
type: Video Note
description: "Terry Damiba, a developer evangelist at Arcade, presents a critical analysis of the Model Context Protocol (MCP), arguing that while it standardized client-server communication, it failed to standa..."
resource: "https://www.youtube.com/watch?v=mF_pCrFvGY0"
tags:
  - agntcon-mcpcon-north-america-2026
  - video
  - learning
status: stable
generated:
  by: process:yt-summarizer-okf
  at: 2026-11-08T02:03:18+00:00
---

# Summary

Terry Damiba, a developer evangelist at Arcade, presents a critical analysis of the Model Context Protocol (MCP), arguing that while it standardized client-server communication, it failed to standardize how agent frameworks handle tool results.
Using the analogy of a smart intern in a windowless room, he illustrates that MCP tools act as external notes for actions the agent cannot perform, but the "stamp" indicating success or failure (such as the `is_error` flag) is often dropped or inconsistently processed by different frameworks.
This lack of standardization creates significant risks in production environments, where a declined payment might be incorrectly marked as successful if the framework discards the error flag, forcing developers to write custom, framework-specific glue code to parse text-based errors instead of relying on structured data.
To address this, Damiba introduces "kenai.com," a resource similar to caniuse.com that measures how 31 different frameworks and various agents handle MCP annotations, revealing that even major providers like OpenAI and LangChain process error states differently.
He concludes by advising developers not to rely solely on MCP conformance tests, as they do not verify framework behavior, and urges the community to establish a gold standard where frameworks must faithfully pass through all tool annotations to ensure reliable and safe agent operations.

# Main Points

|   # | Main point                                                                                                                                             |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   1 | , but in practice, it is not as standardized as expected, leading to inconsistent behavior across different agent frameworks.                          |
|   2 | , it does not standardize how agent frameworks handle specific metadata, such as the `is_error` flag.                                                  |
|   3 | (e.g., a declined card payment); the error status may be dropped by certain frameworks, causing the agent to incorrectly assume the action succeeded.  |
|   4 | "glue code" for each framework to handle errors, defeating the purpose of MCP’s standardization promise.                                               |
|   5 | : some drop the flag, some treat it as control flow, and others require opt-in settings to preserve it.                                                |
|   6 | , meaning compliance does not guarantee functional reliability across all agents.                                                                      |
|   7 | "kenai.com," a resource similar to caniuse.com, which measures how 31 different frameworks and various agents handle MCP annotations and error states. |
|   8 | , but there is no unified standard, resulting in a "wild west" scenario for developers.                                                                |
|   9 | ; they must test how specific frameworks handle tool results and error annotations.                                                                    |
|  10 | , such as "destructive" hints, cannot be treated as authorization mechanisms because they may be ignored or dropped by certain frameworks.             |
|  11 | , but currently, developers must write custom logic to interpret text-based errors if the structured flag is lost.                                     |

# Video

[![Video thumbnail](https://img.youtube.com/vi/mF_pCrFvGY0/hqdefault.jpg)](https://www.youtube.com/watch?v=mF_pCrFvGY0)

[Watch on YouTube](https://www.youtube.com/watch?v=mF_pCrFvGY0)
