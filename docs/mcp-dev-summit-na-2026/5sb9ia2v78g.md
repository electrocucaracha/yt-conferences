---
layout: default
title: How Duolingo Built an AI Slackbot With 180+ MCP Tools
nav_order: 34
parent: Mcp Dev Summit Na 2026
type: Video Note
description:
  Aaron, a software engineer at Duolingo, describes the development of
  an AI-powered Slack app that integrates with MCP servers to streamline internal
  workflows. Initially, setting up MCP servers was complex and inconsistent, prompting
  effort...
resource: https://www.youtube.com/watch?v=5sb9iA2v78g
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

Aaron, a software engineer at Duolingo, describes the development of an AI-powered Slack app that integrates with MCP servers to streamline internal workflows.
Initially, setting up MCP servers was complex and inconsistent, prompting efforts to centralize instructions and standardize configurations, including hosting internal servers and simplifying authentication.
Despite these improvements, adoption remained low until the team built a Slack app that connects to over 15 MCP servers and AWS BigQuery, automating responses in help desk and incident channels, supporting human-in-the-loop verification for write operations, and allowing channel-specific customization.
The app emphasizes security and privacy by enforcing role-based access, requiring human approval for external write actions, sandboxing operations, and not logging private messages.
Since its launch in September 2025, the Slack bot’s adoption has grown to over 250 weekly active users, with response quality steadily improving, and Duolingo has open-sourced the core application code for others to use.

# Main Points

|   # | Main point                                                                                                   |
| --: | ------------------------------------------------------------------------------------------------------------ |
|   1 | Aaron, a software engineer at Duolingo, presented on building an AI Slack app using MCP.                     |
|   2 | Initial MCP server setup was complex and had a high barrier to entry.                                        |
|   3 | In May 2025, a centralized web page was created to simplify MCP server discovery and setup.                  |
|   4 | MCP servers varied in implementation, causing dependency and compatibility issues.                           |
|   5 | In August 2025, Duolingo began standardizing MCP servers:                                                    |
|   6 | First-party servers (e.g., GitHub, Atlassian) connect directly via AI editors.                               |
|   7 | Open-source servers were forked, authenticated, tracked, and hosted internally.                              |
|   8 | Shared service tokens were used for services with shared credentials.                                        |
|   9 | OAuth was used for services requiring individual access (e.g., Google, Slack).                               |
|  10 | Internal services were converted to MCP servers using a Python library built on FastMCP.                     |
|  11 | For AWS/BigQuery, direct CLI access was allowed instead of MCP.                                              |
|  12 | Local tools (e.g., Playwright, Simulator) were supported via local MCP tools.                                |
|  13 | By April 2026, Duolingo supported around 30 MCP servers and 300+ tools, half served internally.              |
|  14 | Even with simplified setup, adoption was low, so the team built the Duolingo AI Slack app in September 2025. |
|  15 | The Slack app uses Cloud Agent SDK (for MCP server access) and Slack Bot SDK (for messaging).                |
|  16 | The app connects to 15+ MCP servers and can run AWS BigQuery commands.                                       |
|  17 | Key features:                                                                                                |
|  18 | Auto-responds in help desk and incident channels.                                                            |
|  19 | Human-in-the-loop verification for write operations (e.g., pull requests, Jira tickets).                     |
|  20 | Customizable system prompts and per-channel settings.                                                        |
|  21 | Supports call skills, sub-agents, and collects user feedback.                                                |
|  22 | Eval tests ensure consistent and improving performance.                                                      |
|  23 | Security and privacy measures:                                                                               |
|  24 | Role-based access control.                                                                                   |
|  25 | Human approval required for external write operations.                                                       |
|  26 | Runs in a sandboxed VM environment.                                                                          |
|  27 | No logging of DM or private channel messages.                                                                |
|  28 | Adoption grew from 20 to 250+ weekly active users (about 30% of the company).                                |
|  29 | Upvote rate Ratings (1-5): 3                                                                                 |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=5sb9iA2v78g)
