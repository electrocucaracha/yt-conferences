---
layout: default
title:
  "Project Lightning Talk: Bringing Agentic AI To Cloud Native With Kagent -
  Eitan Yarmush"
nav_order: 208
parent: Kubecon Cloudnativecon North America 2025
type: Video Note
description:
  "Eton Yarmish, an architect at solo.io and maintainer of K agent, introduces
  the K agent project by first explaining the fundamental components of an agent:
  a system prompt, a language model (LM), and tools. He describes the agent's core
  loo..."
resource: https://www.youtube.com/watch?v=oXBr9UAOG2M
tags:
  - kubecon-cloudnativecon-north-america-2025
  - video
  - learning
status: stable
generated:
  by: process:yt-conferences-okf
  at: 2026-09-12 00:00:00+00:00
---

# Summary

Eton Yarmish, an architect at solo.io and maintainer of K agent, introduces the K agent project by first explaining the fundamental components of an agent: a system prompt, a language model (LM), and tools.
He describes the agent's core loop, where a user message is processed by the system prompt and LM, which may call various tools such as GitHub, Docker, or Slack, often coordinated through MCP servers.
Yarmish likens the agent stack to a layered cake, with frameworks orchestrating agents that use tools, and notes that this structure is inherently declarative, making it suitable for Kubernetes.
K agent enables users to define agents in YAML by specifying the model configuration, system prompt, and tools, simplifying deployment and management within Kubernetes environments.
The project is new but gaining traction, with some companies already running it in production, and Yarmish invites attendees to learn more at the Solo IO booth.

# Main Points

|   # | Main point                                                                                                                                                                           |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   1 | K agent is an open source agent stack project.                                                                                                                                       |
|   2 | Eton Yarmish is an architect at solo.io and a maintainer of K agent and agent gateway.                                                                                               |
|   3 | The talk focuses on the concept of agents and the motivation behind creating K agent.                                                                                                |
|   4 | An agent consists of three components: a system prompt, an LLM (language model), and tools.                                                                                          |
|   5 | The agent's core loop: user sends a message, system prompt is appended, sent to the LLM, which decides if tools need to be called; this repeats as needed, then returns to the user. |
|   6 | Tools enable the agent to take actions, such as interacting with GitHub, Docker, Slack, or object storage.                                                                           |
|   7 | MCP is described as the "USB of tool connection," allowing different systems to interact with various tools; most projects now have an MCP server.                                   |
|   8 | The agent stack is likened to a "seven layer cake," with the framework at the top orchestrating agents, which use tools.                                                             |
|   9 | The process is seen as declarative, leading to the idea of running agents in Kubernetes like other workloads.                                                                        |
|  10 | K agent uses an API where agents are defined in YAML, specifying the model config, system prompt, and tools.                                                                         |
|  11 | K agent is designed to be easy to run on Kubernetes and understandable for those familiar with the Kubernetes ecosystem.                                                             |
|  12 | The project is new but gaining traction, with some companies already running it in production.                                                                                       |
|  13 | The speaker invites attendees to visit the Solo IO booth for more information and discussion.                                                                                        |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=oXBr9UAOG2M)
