---
layout: default
title: "The Other Half of MCP Apps: Building a Secure, Self-Hostable... - Mathew Goldsborough, NimbleBrain"
nav_order: 58
parent: AGNTCon + MCPCon North America 2026
type: Video Note
description: "Matt Goldsborough, founder and CEO of Nimble Brain, presented an open-source runtime that leverages MCP servers and apps to create composable, SaaS-like user interfaces."
resource: "https://www.youtube.com/watch?v=XErnMwNF4oI"
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

Matt Goldsborough, founder and CEO of Nimble Brain, presented an open-source runtime that leverages MCP servers and apps to create composable, SaaS-like user interfaces.
He argued that MCP has matured into a robust application packaging format, combining tools, rich UIs, and skills to allow developers to build full applications without relying on traditional REST APIs or proprietary chat-based sandboxes.
The platform addresses common development challenges by providing host primitives for identity, file management, and tool routing, enabling teams to deploy self-hosted solutions that keep data private while connecting to legacy systems and public cloud services.
Goldsborough detailed specific extensions like "facets" for dashboard metrics and lifecycle hooks for provisioning, which streamline the development process and ensure a consistent user experience across different MCP components.
By treating MCP as a standard distribution layer, Nimble Brain allows businesses to rapidly deploy agentic applications with lower development costs, greater flexibility, and the ability to integrate custom branding and workflows.

# Main Points

|   # | Main point                                                                                                                                                           |
| --: | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | , founder and CEO of Nimble Brain, presented on building an open-source runtime that leverages MCP and MCP apps to create composable, AI-native applications.        |
|   2 | , similar to historical formats like Windows executables or Java WARs, enabling the composition of tools, MCP apps, and skills into a cohesive product.              |
|   3 | , rather than relying solely on text-based chat interactions.                                                                                                        |
|   4 | (capabilities for LLMs), MCP apps (rich interactive UIs delivered over MCP), and skills (knowledge and know-how returned via MCP).                                   |
|   5 | "host primitives" such as files, conversations, tool routing, and identity, allowing developers to focus on building value rather than repetitive plumbing code.     |
|   6 | `server.json` files, compliant with MCP registry formats, which can be dynamically installed and rendered in iframes within the UI.                                  |
|   7 | (e.g., finance, engineering) can connect to specific tools like Stripe, GitHub, or Linear within a single managed service platform.                                  |
|   8 | , private clouds, or on-premises, enabling integration with legacy systems, internal APIs, and private data warehouses.                                              |
|   9 | "facets" (dashboard stats/metadata) without consuming LLM tokens, enhancing performance and user experience.                                                         |
|  10 | (Synapse), ensuring cohesive branding and dark mode support.                                                                                                         |
|  11 | `/notify` host extension standardizes user notifications (toasts) across the platform, replacing inconsistent log-line-based messaging with a unified UI experience. |
|  12 | (e.g., domains, email inboxes) automatically upon installation or uninstallation within the workspace.                                                               |
|  13 | "bring your own MCP client," allowing users to connect external coding agents or harnesses while maintaining a consistent internal dashboard for business users.     |
|  14 | , while keeping data ownership with the customer.                                                                                                                    |
|  15 | , citing a lack of robust support for A2UI and a preference for designed, CRUD-style applications with agentic layers rather than purely generative UIs.             |
|  16 | , capable of connecting to public cloud services and private legacy systems via MCP brokers, supporting a hybrid public-private architecture.                        |

# Video

[![Video thumbnail](https://img.youtube.com/vi/XErnMwNF4oI/hqdefault.jpg)]("https://www.youtube.com/watch?v=XErnMwNF4oI")

[Watch on YouTube](https://www.youtube.com/watch?v=XErnMwNF4oI)
