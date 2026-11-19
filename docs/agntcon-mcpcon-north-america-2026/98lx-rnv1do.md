---
layout: default
title: "From Pain Points to Production: What We Learned Building MCP-Powered... - Nikolay Rodionov, Alpic"
nav_order: 129
parent: AGNTCon + MCPCon North America 2026
type: Video Note
description: "Nikolai, a founder at Alpec, presents lessons learned from building MCP and ChatGPT apps for major clients, emphasizing that AI agents are becoming the primary users of digital products."
resource: "https://www.youtube.com/watch?v=98lX-rnv1Do"
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

Nikolai, a founder at Alpec, presents lessons learned from building MCP and ChatGPT apps for major clients, emphasizing that AI agents are becoming the primary users of digital products.
He explains that MCP apps extend the Model Context Protocol by allowing servers to return HTML widgets rendered as iframes within AI hosts, enabling rich interactivity and branding.
To address the poor developer experience caused by this iframe architecture, Alpec developed Skybridge, an open-source TypeScript framework that provides end-to-end type safety, React hooks, and local hot-module reloading.
Key design principles include keeping the UI and model synchronized, designing for agentic intents rather than replicating site flows, and making the UI optional to support autonomous agents.
Additionally, developers must manage the model’s context budget, handle varying display modes across different hosts and devices, and strictly configure Content Security Policies (CSP) and tool annotations to ensure successful deployment and compliance with store requirements.

# Main Points

|   # | Main point                                                                                                                                                                                                                    |
| --: | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | , simulating agent runs, monitoring agentic traffic, and building agentic interfaces like MCP servers and apps.                                                                                                               |
|   2 | (MCP) that allows servers to return HTML widgets rendered as iframes within MCP hosts, enabling interactivity and custom branding.                                                                                            |
|   3 | , with over 12,000 apps and plugins in Cloud and ChatGPT stores, and new platforms like Grok and Muse beginning to accept third-party plugins.                                                                                |
|   4 | , as platforms like Cloud and ChatGPT now autonomously select and use connectors based on user intent without explicit user mention.                                                                                          |
|   5 | , featuring custom onboarding, context selection, file editors, and sidebar integration.                                                                                                                                      |
|   6 | , including the inability to test locally without tunnels, lack of end-to-end type safety, and incompatibility with modern web dev tools.                                                                                     |
|   7 | , offering type safety, React hooks, local hot module reload, embedded tunnels, and instant deployment.                                                                                                                       |
|   8 | , the model, and the UI, requiring synchronization between the model and UI state to ensure the model understands user actions.                                                                                               |
|   9 | , treating the app as capabilities for the model to orchestrate.                                                                                                                                                              |
|  10 | , ensuring compatibility with client-side generative UI trends.                                                                                                                                                               |
|  11 | , enables selective emphasis of data, and maintains compatibility with non-UI clients.                                                                                                                                        |
|  12 | ’s context budget by using the `meta` parameter for UI-only elements and providing data summaries to the model to prevent redundant text generation.                                                                          |
|  13 | (inline, full screen, picture-in-picture) render differently across hosts and devices; OpenAI has removed picture-in-picture and added a preferred display mode parameter, necessitating extensive QA across iOS and Android. |
|  14 | , improving interaction speed and smoothness.                                                                                                                                                                                 |
|  15 | (CSP) misconfiguration is the leading cause of deployment failures; developers must whitelist connect, resource, frame, and redirect domains to avoid security blocks.                                                        |
|  16 | , destructive hint, and idempotent hint are mandatory for store submission, as hosts use them to determine if user validation is required for potentially dangerous actions.                                                  |
|  17 | , providing actionable prompts to fix issues.                                                                                                                                                                                 |
|  18 | ; UI interactions like navigation can be handled client-side, while actions like saving require MCP server calls.                                                                                                             |
|  19 | , whereas generative UI protocols like A2UI require specific client support that leading hosts like ChatGPT do not currently provide.                                                                                         |

# Video

[![Video thumbnail](https://img.youtube.com/vi/98lX-rnv1Do/hqdefault.jpg)](https://www.youtube.com/watch?v=98lX-rnv1Do)

[Watch on YouTube](https://www.youtube.com/watch?v=98lX-rnv1Do)
