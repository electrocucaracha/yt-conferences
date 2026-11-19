---
layout: default
title: "The #1 Mistake Building MCP Tools"
nav_order: 75
parent: MCP Dev Summit NA 2026
type: Video Note
description: "The speaker, who has built over 10,000 tools, argues that effective tool abstraction for Large Language Models (LLMs) differs fundamentally from traditional API design, which is intended for progra..."
resource: "https://www.youtube.com/watch?v=q1CG02bYEqY"
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

The speaker, who has built over 10,000 tools, argues that effective tool abstraction for Large Language Models (LLMs) differs fundamentally from traditional API design, which is intended for programmers.
He emphasizes that chaining multiple API calls is a major source of failure, with error rates exceeding 50% when six or more tools are involved, and advocates for creating single, task-specific tools that encapsulate complex workflows to improve accuracy.
A critical insight from his research is that the quality of a tool’s description acts as a "10x lever" for performance, as it is the most recent context the LLM processes and heavily influences tool selection.
To optimize this, he recommends keeping descriptions under 600 words, starting with an action verb, and focusing on clear task intents rather than abstract functions.
Finally, he warns that having more than 20 tools creates a "tool count cliff" that confuses agents, suggesting that developers should limit tool scope, use progressive discovery to manage context, and rigorously test both the deterministic execution and the LLM’s selection capabilities.

# Main Points

|   # | Main point                                                                                                                           |
| --: | ------------------------------------------------------------------------------------------------------------------------------------ |
|   1 | Tool abstraction is distinct from API abstraction because it is designed for large language models rather than programmers.          |
|   2 | Converting API endpoints directly into tools often fails because models struggle to chain multiple calls to complete a single task.  |
|   3 | Chaining tool calls is the hardest problem in agent execution, with failure rates exceeding 50% when six or more tools are required. |
|   4 | Effective tools should be high-level abstractions that encapsulate complex workflows into a single callable function.                |
|   5 | Tools should be organized around specific tasks and intents to align with how agents structure their todo lists.                     |
|   6 | Deterministic parts of tools must have 100% reliability, requiring rigorous unit testing alongside LLM evaluation.                   |
|   7 | Description quality is the most significant lever for improving tool selection accuracy and overall performance.                     |
|   8 | Tool descriptions should start with an action verb, be concise, and ideally stay under 600 words.                                    |
|   9 | The position of tool schemas in the context window makes descriptions the most recent memory for the model, influencing selection.   |
|  10 | Optimizing descriptions can reduce errors by approximately 10x and enable models to perform longer chains of activities.             |
|  11 | The tool count cliff is real, with agent performance degrading significantly when more than 20 tools are available.                  |
|  12 | Progressive discovery helps manage context usage but does not fully solve the underlying abstraction and chaining problems.          |
|  13 | If an agent requires more than 40 tools, its scope is likely too broad and should be redefined or split into sub-agents.             |
|  14 | Evidence from papers by Apple, Redis, Block, and GitHub Copilot supports the superiority of task-oriented tool design.               |
|  15 | Evaluating tools should involve multiple language models to ensure robustness across different model behaviors.                      |
|  16 | The goal of tool design is to maximize the accuracy of both tool selection and the resulting output.                                 |

# Video

[![Video thumbnail](https://img.youtube.com/vi/q1CG02bYEqY/hqdefault.jpg)](https://www.youtube.com/watch?v=q1CG02bYEqY)

[Watch on YouTube](https://www.youtube.com/watch?v=q1CG02bYEqY)
