---
layout: default
title:
  "MCP Servers in the Wild: Managing Tool Complexity at Scale - Arnav Balyan,
  Concierge AI"
nav_order: 58
parent: Mcp Dev Summit Na 2026
type: Video Note
description:
  "The speaker discusses strategies for managing MCP servers as tool complexity
  increases, highlighting two main challenges: large tool descriptions and schemas
  that can exceed model context windows, and the need for servers to guide tool sele..."
resource: https://www.youtube.com/watch?v=Ek3FbC0__04
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

The speaker discusses strategies for managing MCP servers as tool complexity increases, highlighting two main challenges: large tool descriptions and schemas that can exceed model context windows, and the need for servers to guide tool selection as use cases shift from analytical to state-changing actions.
To address these, the speaker introduces patterns such as progressive tool disclosure (grouping tools hierarchically and revealing them dynamically), code-based execution (using a sandbox for the model to process large tool outputs via code), and plan-based execution (having the model generate execution plans in JSON).
The effectiveness of each approach depends on the number of tools and their dependencies: plain mode works best for fewer than 22 tools, search mode for over 50 stateless tools, and planner or code modes for tools with dependencies.
The speaker also mentions emerging areas like generative UI and distribution challenges, and introduces the open-source Concurge SDK, which helps convert servers into these optimized representations with minimal effort.

# Main Points

|   # | Main point                                                                                                                                                                                                                 |
| --: | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | MCP server adoption is rapidly increasing, with over 130 million downloads in February 2026 and a 250x increase since November 2024.                                                                                       |
|   2 | Two main challenges arise as tool complexity grows: large tool descriptions/schemas saturating model context windows, and the need for servers to guide tool selection as use cases become state-changing and high-stakes. |
|   3 | Beyond 20 tools, tool descriptions and schemas can exceed context window limits; beyond 550 tools, 200k token context is reached.                                                                                          |
|   4 | Solutions include progressive tool disclosure, code execution, and plan-based execution.                                                                                                                                   |
|   5 | Progressive tool disclosure groups tools into categories, reducing visible tools and allowing hierarchical navigation; tool groups can be nested and dependencies enforced.                                                |
|   6 | Tool update notifications enable dynamic exposure of tools/groups, allowing the agent to see only relevant tools at each step.                                                                                             |
|   7 | Workflows can be created by connecting tool groups with dependencies, ensuring agents follow required sequences (e.g., login before checkout).                                                                             |
|   8 | Shared memory can be used to maintain state across tool groups, enabling AI-native apps with stateful interactions.                                                                                                        |
|   9 | Code-based execution exposes a code sandbox as a tool, letting the model write code to process large tool outputs without overloading the context window.                                                                  |
|  10 | Plan-based execution allows the model to write a JSON plan for tool orchestration, referencing outputs of previous steps.                                                                                                  |
|  11 | Tool search pattern reduces hundreds of tools to two: a search tool and an execute tool; commonly implemented on the client side.                                                                                          |
|  12 | Study of 50+ MCP servers shows: plain mode is best for <22 tools; search is best for >50 stateless tools; planner/code is best for tools with dependencies.                                                                |
|  13 | Plane mode is fastest but uses most tokens; code mode is most token-efficient; search mode is slowest.                                                                                                                     |
|  14 | Emerging areas: generative UI for personalized tool output rendering, and improved server distribution/discovery.                                                                                                          |
|  15 | Concurge SDK is an open source project to help convert servers                                                                                                                                                             |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=Ek3FbC0__04)
