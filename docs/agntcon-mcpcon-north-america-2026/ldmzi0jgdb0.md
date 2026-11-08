---
layout: default
title: "MCP In The Wild - Thomas Sarlandie, OpenAI"
nav_order: 106
parent: AGNTCon + MCPCon North America 2026
type: Video Note
description: "Thomas Aral from OpenAI’s plugins team emphasizes that developers should expose all their MCP server tools to the model without artificial limits, as the platform is designed to handle hundreds of ..."
resource: "https://www.youtube.com/watch?v=LDMzI0jGDb0"
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

Thomas Aral from OpenAI’s plugins team emphasizes that developers should expose all their MCP server tools to the model without artificial limits, as the platform is designed to handle hundreds of tools per server.
He advises against creating overly large schemas or using antipatterns like generic "list" and "run" commands, which increase latency and hinder fine-grained enterprise control.
Instead, developers must provide accurate annotations for every tool to enable efficient auto-approval for read-only actions and proper safety checks for destructive ones.
Additionally, Aral encourages the use of server instructions, recommending they be kept under 1,000 characters to optimize context window usage and improve tool discoverability.
Finally, he highlights OpenAI’s commitment to the MCP standard, noting support for new features like events and file uploads, and invites developers to engage directly with the team to share feedback and improve the ecosystem.

# Main Points

|   # | Main point                                                                                                                     |
| --: | ------------------------------------------------------------------------------------------------------------------------------ |
|   1 | , showing significant growth in installations and usage.                                                                       |
|   2 | ; OpenAI supports servers with hundreds of tools.                                                                              |
|   3 | /output definitions and textual descriptions to help the model understand tool usage.                                          |
|   4 | (megabytes in size) cause context window issues, leading OpenAI to truncate argument and tool descriptions.                    |
|   5 | "list" and "run" tools to hide specific actions is an antipattern that increases latency and hinders enterprise admin control. |
|   6 | , while destructive annotations trigger explicit user authorization checks.                                                    |
|   7 | , improving discoverability and enabling complex tool chaining.                                                                |
|   8 | % of public plugins currently use server instructions, which is an underutilized feature.                                      |
|   9 | ,000 characters, with the most important information placed at the beginning.                                                  |
|  10 | , including support for MCP apps, ChatGPT extensions, and events.                                                              |
|  11 | , and plugin extension demos are available at the event.                                                                       |

# Video

[![Video thumbnail](https://img.youtube.com/vi/LDMzI0jGDb0/hqdefault.jpg)]("https://www.youtube.com/watch?v=LDMzI0jGDb0")

[Watch on YouTube](https://www.youtube.com/watch?v=LDMzI0jGDb0)
