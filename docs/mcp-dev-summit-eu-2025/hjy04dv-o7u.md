---
layout: default
title:
  "[Session] Too Many Tools: Surviving the MCP Tool Overload with Shalev Shalit
  - Webrix"
nav_order: 16
parent: Mcp Dev Summit Eu 2025
type: Video Note
description:
  In this presentation, Shalev, co-founder and CEO of Webbricks, discusses
  the challenges enterprises face when integrating too many tools into their AI agents,
  particularly the issues of context overload, attention dilution, and decreased pe...
resource: https://www.youtube.com/watch?v=hJY04dV-o7U
tags:
  - mcp-dev-summit-eu-2025
  - video
  - learning
status: stable
generated:
  by: process:yt-conferences-okf
  at: 2026-09-12 00:00:00+00:00
---

# Summary

In this presentation, Shalev, co-founder and CEO of Webbricks, discusses the challenges enterprises face when integrating too many tools into their AI agents, particularly the issues of context overload, attention dilution, and decreased performance and accuracy.
He outlines four main solutions: disabling unnecessary tools for simplicity, creating shareable toolkits tailored to specific roles or tasks, implementing a "search and call" method for environments with numerous APIs, and using dynamic MCPs (DMCPs) that allow tools to be added or removed as needed.
Each approach has its benefits and drawbacks, such as ease of use, shareability, or implementation complexity, and their effectiveness depends on the specific use case.
Shalev concludes by suggesting that the future lies in more sophisticated, capability-based tool management and a shift toward specialized agents working collaboratively, rather than relying on a single super-agent to handle all tasks.

# Main Points

|   # | Main point                                                                                                                                                                                                                    |
| --: | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Enterprises often accumulate too many tools, leading to complexity and inefficiency.                                                                                                                                          |
|   2 | Three main problems with too many tools: excessive context usage (increasing costs), LLM attention issues (causing mistakes), and reduced performance/accuracy (wrong tool usage).                                            |
|   3 | Four main solutions to manage tool overload:                                                                                                                                                                                  |
|   4 | **Disable Tools:** Manually enable/disable tools as needed; quick and simple for small toolsets but time-consuming and not easily shareable for larger teams or multiple clients.                                             |
|   5 | **Toolkits:** Group relevant tools into shareable sets for specific tasks or roles; easy to use and share but can become messy if tools are missing or roles require many tools.                                              |
|   6 | **Search and Call:** Use a search tool to find and call the right tool from a large pool; effective for many tools in the same domain or when relevant tools are hard to predefine, but lacks context and can be inefficient. |
|   7 | **DMCP (Dynamic MCP):** Dynamically add/remove tools based on need; maintains a stack of recently used tools, allows for flexible tool management, but not all clients support it and adding tools can be slow.               |
|   8 | Each solution fits different use cases; disabling tools is best for simple needs, toolkits for teams and roles, search and call for large API-based toolsets, and DMCP for dynamic, evolving tool needs.                      |
|   9 | Future directions include more sophisticated, capability-based tool management and moving from super-agents to specialized agents (A2A approach).                                                                             |
|  10 | Encouragement to try toolkits and provide feedback.                                                                                                                                                                           |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=hJY04dV-o7U)
