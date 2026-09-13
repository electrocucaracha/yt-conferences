---
type: Video Note
title: "The Tool Abstraction Problem: Lessons Learned Building 1000+ MCP Tools - Sam Partee, Arcade.dev"
description: "The speaker discusses the concept of tool abstraction, drawing on extensive experience building over 10,000 tools, and emphasizes that tools designed for large language models (LLMs) require a different abstraction than traditional APIs mad..."
resource: https://www.youtube.com/watch?v=ddvDuSJgGZY
tags: ["mcp-dev-summit-na-2026", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

The speaker discusses the concept of tool abstraction, drawing on extensive experience building over 10,000 tools, and emphasizes that tools designed for large language models (LLMs) require a different abstraction than traditional APIs made for programmers.
Rather than simply wrapping APIs, effective tools for LLMs should be organized around specific tasks or intents, as this aligns better with how agents process instructions and reduces the complexity and failure rates associated with chaining multiple tools.
The speaker highlights that the quality of a tool’s description is the most significant factor in its successful selection and use by LLMs, far outweighing other considerations like context or naming, and recommends concise, action-oriented descriptions.
Research and benchmarks consistently show that task- and intent-based tools, with well-crafted descriptions, yield higher accuracy and reliability, while having too many tools or overly broad agent scopes leads to confusion and diminished performance.
The talk concludes by urging ongoing attention to description quality and thoughtful tool design, as these are the primary levers for improving agent effectiveness.
# Main Points

|   # | Main point                                                                                                                                   |
| --: | -------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Speaker has built over 10,000 tools, starting before MCP with their own open execution protocol.                                             |
|   2 | Early focus was on parsing and validating JSON outputs from models like GPT-3.                                                               |
|   3 | The "tool abstraction problem" is about creating a machine experience, distinct from user experience.                                        |
|   4 | API abstraction and tool abstraction are fundamentally different; APIs are for programmers, tools are for large language models or agents.   |
|   5 | Chaining multiple API calls as tools leads to high failure rates; chaining is the hardest problem.                                           |
|   6 | Tools should be designed around tasks or intents, not just as thin API wrappers.                                                             |
|   7 | Task- or intent-oriented tools are easier for agents to select and use effectively.                                                          |
|   8 | Organizing tools by tasks/intents aligns with how agents make to-do lists (inspired by girkin style).                                        |
|   9 | Evidence from papers and benchmarks (Apple's tool sandbox, Reddus, block, square, GitHub Copilot) supports task/intention-based tool design. |
|  10 | Description quality is the most important factor for tool selection and performance; iterating on descriptions yields a 10x improvement.     |
|  11 | Descriptions should be concise (ideally under 600 words), start with an action verb, and clearly state the task/intent.                      |
|  12 | The tool's name is the second most influential factor after the description.                                                                 |
|  13 | Progressive discovery introduces context over time but doesn't fully solve the tool count or chaining problems.                              |
|  14 | Having more than 20 tools leads to confusion for agents; breaking tasks into subtasks or sub-agents is recommended.                          |
|  15 | Chaining logic should be moved inside tools, making them task/intent-enabled functions.                                                      |
|  16 | Enumerate and name tools differently for flexibility, but avoid overly broad agents (over 40 tools).                                         |
|  17 | Descriptions are the key lever for tool effectiveness; continually optimize them.                                                            |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=ddvDuSJgGZY)