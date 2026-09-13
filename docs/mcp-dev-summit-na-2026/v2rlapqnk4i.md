---
layout: default
title:
  "Intent Engineering: The Death of the Mono-Directional Prompt - Rizel Scarlett,
  Block, Inc."
nav_order: 38
parent: Mcp Dev Summit Na 2026
type: Video Note
description:
  The speaker discusses the evolution of prompt engineering in AI, noting
  its importance in the early days when models like GPT-3 were unpredictable and required
  carefully crafted prompts. However, with advancements in AI, particularly after...
resource: https://www.youtube.com/watch?v=v2rlaPQnK4I
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

The speaker discusses the evolution of prompt engineering in AI, noting its importance in the early days when models like GPT-3 were unpredictable and required carefully crafted prompts.
However, with advancements in AI, particularly after December 2025 and the introduction of more capable models and agent-based systems, prompt engineering has been largely replaced by context engineering and intent engineering.
Context engineering focuses on providing agents with the necessary information through structured documentation, but can suffer from issues like context overload.
Intent engineering, on the other hand, ensures that AI agents truly understand user intentions, using tools like MCP apps for clarifying, confirming, and interpreting intent through interactive interfaces and structured elicitation.
The speaker demonstrates these concepts with examples and highlights the importance of intent engineering in areas like code review, where understanding the agent’s intent is crucial for scalable and reliable collaboration.
The talk concludes by emphasizing that while prompt engineering was foundational, intent engineering is now essential for effective human-AI collaboration.

# Main Points

|   # | Main point                                                                                                                                   |
| --: | -------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | The talk focuses on the evolution from prompt engineering to context and intent engineering in AI.                                           |
|   2 | Prompt engineering was crucial in early AI models like GPT-3, requiring precise phrasing due to small context windows and unpredictability.  |
|   3 | Modern AI models (post-December 2025, e.g., Opus) have shifted the focus from prompt engineering to collaborating and orchestrating agents.  |
|   4 | Prompt engineering is being replaced by context engineering and intent engineering.                                                          |
|   5 | Context engineering involves providing agents with structured information (e.g., markdown files, docs) rather than crafting perfect prompts. |
|   6 | Overloading agents with too much context can lead to "context rot," causing confusion and hallucinations.                                    |
|   7 | Solutions to context rot include managing context windows, using patterns like loops, beads for memory, and delegating to sub-agents.        |
|   8 | Ambiguity remains a problem: agents may have enough information but still not understand user intent.                                        |
|   9 | Intent engineering ensures agents understand what the user actually means, not just what is said.                                            |
|  10 | Example: Telling an agent to "delete it" may result in deleting an entire project if intent is unclear.                                      |
|  11 | Many discuss intent engineering, but few implement it due to lack of awareness or tools.                                                     |
|  12 | MCP provides primitives for intent engineering: clarifying, confirming, and refining intent before execution.                                |
|  13 | MCP apps allow users to interact with agents via UI, improving intent alignment.                                                             |
|  14 | MCP elicitation enables agents to pause and request structured input for clarification.                                                      |
|  15 | MCP sampling lets agents explore multiple interpretations and reason before acting.                                                          |
|  16 | Combining these features allows for better clarification, confirmation, and interpretation of intent.                                        |
|  17 | Intent engineering is already possible and should be adopted now.                                                                            |
|  18 | Intent is also important in code review, helping reviewers understand agent decisions and changes.                                           |
|  19 | Automated scans (e.g., GitHub actions) can help detect prompt injection risks in contributed co                                              |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=v2rlaPQnK4I)
