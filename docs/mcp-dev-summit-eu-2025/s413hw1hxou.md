---
type: Video Note
title: "[Session] MCP & Contextual Smart Tooling with Jason Kneen - BouncingFish"
description: "Jason, an experienced developer in the MCP (Model Context Protocol) ecosystem, shares his journey building tools and frameworks like Fluent MCP and MCPZ, and collaborating with companies such as Blackbox and Emergent. He discusses the chall..."
resource: https://www.youtube.com/watch?v=s413Hw1HXoU
tags: ["mcp-dev-summit-eu-2025", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

Jason, an experienced developer in the MCP (Model Context Protocol) ecosystem, shares his journey building tools and frameworks like Fluent MCP and MCPZ, and collaborating with companies such as Blackbox and Emergent.
He discusses the challenges of managing the vast number of available MCP tools, particularly the inefficiency and high token usage caused by loading unnecessary tools into system prompts.
To address this, Jason developed MCPZ CLI, allowing users to create modular, grouped toolboxes and virtual MCP servers for more efficient, task-specific tool selection.
He introduces the concept of "serlets," dynamic MCP servers that generate and serve only the necessary tools and context based on the current task and environment, optimizing resource usage and reducing noise.
Jason also describes advanced orchestration techniques, such as proxy servers and agent collaboration, enabling multiple models and agents to work together efficiently, share memory, and dynamically adapt tooling, ultimately streamlining AI-driven development workflows.
# Main Points

|   # | Main point                                                                                                                             |
| --: | -------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Jason has been building with MCP since its inception and created Fluent MCP and MCPZ.                                                  |
|   2 | He works with clients on app development, AI integration, and has collaborated with companies like Blackbox, Emergent, and Aentuity.   |
|   3 | Jason has contributed to and forked projects such as Claudia, Claudible, Kylo Code Desktop, and Open Code Desktop.                     |
|   4 | He handed over his Claude code Python package to Anthropic in exchange for a free max account and received credits from Kylo Code.     |
|   5 | The current landscape includes state-of-the-art and open-source models, workflow tools, and a variety of agents and tooling platforms. |
|   6 | MCP allows LLMs to discover, install, and integrate with thousands of tools, but security and tool overload are concerns.              |
|   7 | The main challenge is the large context window consumed by MCP tool schemas, leading to high token usage and inefficiency.             |
|   8 | Manual tool selection is common but inefficient; context re-engineering is key to reducing noise and hallucinations.                   |
|   9 | Taskmaster is cited as an example of breaking down tasks for focused LLM processing.                                                   |
|  10 | Context cleanup, such as removing irrelevant tool usage from prompts, is important for efficiency.                                     |
|  11 | Jason developed MCPZ CLI to create virtual MCP servers with grouped tools, allowing granular and semantic control over tool selection. |
|  12 | MCPZ enables efficient sharing and configuration of MCP servers and tools, but setup is still manual.                                  |
|  13 | He introduced the concept of MCP serlets: generative MCP servers that dynamically serve tools based on job requirements and context.   |
|  14 | Serlets can tailor tools, include memory, and adapt to model context windows, optimizing for efficiency.                               |
|  15 | Dynamic tooling allows for custom tools per task, memory management, and on-the-fly tool generation.                                   |
|  16 | Proxy servers and orchestrator apps can enforce MCP functions, enable dynamic tool serving, and coordinate multiple agents.            |
|  17 | Jason implemented systems to rotate between free models and providers, spreading rate limits and including local models.               |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=s413Hw1HXoU)