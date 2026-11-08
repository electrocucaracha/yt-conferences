---
layout: default
title: "Keynote: From Black Box to Glass Box: Your 5-step Blueprint to... - Abhishek Choudhary, TrueFoundry"
nav_order: 110
parent: AGNTCon + MCPCon North America 2026
type: Video Note
description: "Abhishek, co-founder of TrueFoundry, addresses the critical challenge of deploying AI agents in production environments where the inherent unpredictability of large language models poses significan..."
resource: "https://www.youtube.com/watch?v=s7J2inKm69g"
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

Abhishek, co-founder of TrueFoundry, addresses the critical challenge of deploying AI agents in production environments where the inherent unpredictability of large language models poses significant security risks.
He argues that relying on prompt instructions to prevent agents from executing harmful actions is insufficient, citing real-world incidents involving major companies where agents ignored safety directives.
To solve this, he proposes transitioning from a "black box" to a "glass box" approach by implementing an AI gateway, which acts as a controlled door through which all agent actions must pass.
This gateway allows organizations to substitute dummy tokens with real credentials only at the point of egress, ensuring the agent never possesses sensitive data, while simultaneously enabling strict policy enforcement and comprehensive observability.
By centralizing control at this gateway, companies can make trust irrelevant, ensuring that agents are governed, monitored, and secured without needing to predict or control the internal behavior of the underlying models.

# Main Points

|   # | Main point                                                                                                                                                            |
| --: | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | "black box" (unpredictable, opaque) to a "glass box" (observable, governable).                                                                                        |
|   2 | , calling MCP servers, models, and file systems, often requiring long-running access to sensitive resources.                                                          |
|   3 | , especially in enterprise settings.                                                                                                                                  |
|   4 | , such as those involving OpenAI, Hugging Face, and Anthropic, demonstrate that agents can execute harmful actions even when prompts explicitly instruct them not to. |
|   5 | , such as malicious instructions from MCP servers.                                                                                                                    |
|   6 | ("please don't do anything wrong") is an insufficient security strategy.                                                                                              |
|   7 | "door" or gateway is established as the sole exit point for all agent actions, including API calls and internet access.                                               |
|   8 | , while the agent only sees dummy tokens, ensuring it never knows the actual secrets.                                                                                 |
|   9 | , such as blocking specific commands (e.g., `pip install`) or malicious queries to specific domains.                                                                  |
|  10 | , security, and governance by logging and monitoring all traffic passing through the door.                                                                            |
|  11 | "AI Gateway," which serves as the single point of control for agent actions.                                                                                          |

# Video

[![Video thumbnail](https://img.youtube.com/vi/s7J2inKm69g/hqdefault.jpg)]("https://www.youtube.com/watch?v=s7J2inKm69g")

[Watch on YouTube](https://www.youtube.com/watch?v=s7J2inKm69g)
