---
layout: default
title: "Patterns for Shifting from MCP as a Basic API to... - James Ward, AWS & Alexander Ioffe, ExoQuery"
nav_order: 128
parent: AGNTCon + MCPCon North America 2026
type: Video Note
description: "James Ward and Alex Yafy present a strategic shift in Model Context Protocol (MCP) design, arguing that MCP endpoints should be treated as active participants in an agentic conversation rather than..."
resource: "https://www.youtube.com/watch?v=3ZagKglGbkk"
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

James Ward and Alex Yafy present a strategic shift in Model Context Protocol (MCP) design, arguing that MCP endpoints should be treated as active participants in an agentic conversation rather than static API documentation.
They emphasize that effective MCP descriptions must focus on the specific gaps in an agent’s existing knowledge, utilizing concise examples instead of exhaustive manuals to improve prompt efficiency and reduce reasoning errors.
To manage complexity, they recommend separating the "when" to call a tool from the "how" by creating a guided pathway of instructions and linked manuals, allowing agents to navigate through a structured map of resources.
Furthermore, the speakers highlight the importance of refining user baselines to correct agent assumptions and implementing synchronous progress reporting for long-running tasks, where the agent is instructed to poll for updates rather than waiting indefinitely.
Finally, they advocate for using evaluation frameworks and session tracking to continuously test and optimize these conversational patterns, ensuring that MCP servers provide not just data, but actionable guidance for successful agent execution.

# Main Points

|   # | Main point                                                                                                                                                                               |
| --: | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | , requiring a shift in mindset from technical specification to dialogue.                                                                                                                 |
|   2 | "dumping" comprehensive textbooks into descriptions; instead, identify the gap between what the agent already knows and what specific context is needed for the task.                    |
|   3 | "Hava Amina" (what the agent thought before the input) to diagnose and correct misaligned agent expectations and reasoning paths.                                                        |
|   4 | , as agents generalize better from specific instances, improving prompt efficiency and reducing reasoning time.                                                                          |
|   5 | "when to call" instructions from "how to use" details by creating a dedicated manual tool that agents can call for extended documentation, keeping primary descriptions concise.         |
|   6 | , using server instructions, getting-started tools, and linked manuals to direct agents through complex user journeys.                                                                   |
|   7 | ; establish baselines from schema and prompts, then refine specific deltas (like data skew or business idiosyncrasies) through iterative correction.                                     |
|   8 | , as standard MCP transport sessions are insufficient for complex tracking and versioning.                                                                                               |
|   9 | (30 seconds to 10 minutes) by returning partial units of progress and explicit instructions to call a wait endpoint, maintaining a synchronous user experience without async extensions. |
|  10 | , creating a feedback loop that guides the agent’s subsequent actions.                                                                                                                   |
|  11 | (evals) to test agent behavior by asking for the agent's intention during tool calls, allowing for offline analysis and iterative refinement of descriptions and documentation.          |

# Video

[![Video thumbnail](https://img.youtube.com/vi/3ZagKglGbkk/hqdefault.jpg)](https://www.youtube.com/watch?v=3ZagKglGbkk)

[Watch on YouTube](https://www.youtube.com/watch?v=3ZagKglGbkk)
