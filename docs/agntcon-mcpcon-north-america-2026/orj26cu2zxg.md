---
layout: default
title: "Generative UI at Scale with A2UI - Alan Blount & Vishal Motwani, Google"
nav_order: 95
parent: AGNTCon + MCPCon North America 2026
type: Video Note
description: "Alan and Vishal present a framework for generative UI in AI agents, arguing that text-only outputs are insufficient for complex user interactions and that visual interfaces are necessary to handle ..."
resource: "https://www.youtube.com/watch?v=orJ26CU2zxg"
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

Alan and Vishal present a framework for generative UI in AI agents, arguing that text-only outputs are insufficient for complex user interactions and that visual interfaces are necessary to handle the long tail of bespoke use cases.
They introduce A2UI, a system that allows agents to drive configuration-based UIs by exposing component schemas to LLMs, which then generate JSON configurations for native rendering across iOS, Android, and web platforms.
To address the inefficiency of raw JSON generation, they propose A2UI Express, a Python-like language that agents can use to describe UIs more naturally, which is then compiled into the required configuration format.
The system supports both controlled scenarios using decision models for low-latency, consistent outputs and free-form generation for novel interfaces, ensuring that developers can build services and components once and deploy them across various surfaces like Slack, Teams, and native apps.
The speakers emphasize that while configuration-driven UIs are not new, the integration of LLMs to dynamically generate these configurations represents a significant shift, enabling reliable, accessible, and consistent user experiences without requiring agents to write raw code.

# Main Points

|   # | Main point                                                                                                                                                 |
| --: | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | , addressing the shift from static sites and apps to agent-driven interfaces.                                                                              |
|   2 | , which is inefficient for users who prefer visual affordances, buttons, and graphical representations.                                                    |
|   3 | , but these are not generative and lack native device integration.                                                                                         |
|   4 | , such as complex travel booking scenarios with varying return dates.                                                                                      |
|   5 | (Agent-to-UI) is a framework that uses a renderer and component schemas to allow agents to manipulate existing frontend components.                        |
|   6 | , which are token-expensive and slow for LLMs to generate.                                                                                                 |
|   7 | , which is then compiled into A2UI JSON, improving efficiency and reducing token usage.                                                                    |
|   8 | , A2UI uses a macro compiler that translates high-level "nouns" (e.g., flight card) into smaller atomic components, preventing inconsistent UI generation. |
|   9 | , Android, Web, React, Angular, and Lit, ensuring the UI feels native to the device.                                                                       |
|  10 | , significantly reducing latency to as low as 300 milliseconds compared to free-form generation.                                                           |
|  11 | , with version 1.0 planned to include server-side functions, custom metadata, and mixed catalog support.                                                   |
|  12 | , from fully pre-designed UIs to free-form code generation, allowing agents to create new components when necessary.                                       |
|  13 | , including ChatGPT, Visual Studio Code, Slack, Teams, and email.                                                                                          |
|  14 | , ensuring compliance with legal and design standards.                                                                                                     |
|  15 | , add renderers to their apps, and contribute to the development of generative UI standards.                                                               |

# Video

[![Video thumbnail](https://img.youtube.com/vi/orJ26CU2zxg/hqdefault.jpg)]("https://www.youtube.com/watch?v=orJ26CU2zxg")

[Watch on YouTube](https://www.youtube.com/watch?v=orJ26CU2zxg)
