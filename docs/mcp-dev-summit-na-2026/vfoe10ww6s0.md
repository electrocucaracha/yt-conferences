---
type: Video Note
title: "Sponsored Session: Model Context Pragmatism - Jeremiah Lowin, Prefect"
description: "Jeremiah, CEO of Prefect, discusses the evolution of FastMPP, an opinionated framework for working with the Model Context Protocol (MCP). He explains that FastMPP aims to absorb MCP best practices so users can focus on their own data and lo..."
resource: https://www.youtube.com/watch?v=vfOe10Ww6s0
tags: ["mcp-dev-summit-na-2026", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

Jeremiah, CEO of Prefect, discusses the evolution of FastMPP, an opinionated framework for working with the Model Context Protocol (MCP).
He explains that FastMPP aims to absorb MCP best practices so users can focus on their own data and logic, but notes that previous efforts prioritized broad client compatibility at the expense of server innovation.
To address this, FastMPP 3 was redesigned around two core abstractions—providers and transforms—enabling rapid feature development and support for advanced capabilities like tool search, code mode, and progressive disclosure.
Jeremiah introduces Prefab, a new generative component library that allows developers to build interactive UIs directly in Python, facilitating richer user experiences within MCP apps without requiring extensive front-end expertise.
He emphasizes the importance of pushing the ecosystem to support the full range of MCP features, encourages adoption of these new tools, and answers audience questions about technical implementation and client compatibility.
# Main Points

|   # | Main point                                                                                                                   |
| --: | ---------------------------------------------------------------------------------------------------------------------------- |
|   1 | Jeremiah is CEO at Prefect and focuses on building software for building software.                                           |
|   2 | FastMPP is an opinionated framework for working with the model context protocol (MCP).                                       |
|   3 | FastMPP absorbs MCP best practices so users can focus on proprietary data and business logic.                                |
|   4 | The framework is popular, allowing observation of user behaviors and selective feature inclusion.                            |
|   5 | FastMPP intentionally excludes some features based on broad usefulness.                                                      |
|   6 | There is a gap: building advanced MCP servers feels limited due to client capabilities and ecosystem incentives.             |
|   7 | Past advice focused on simplifying servers for compatibility; now, the goal is to encourage building advanced servers.       |
|   8 | FastMPP 2 evolved rapidly but became difficult to innovate on due to complexity.                                             |
|   9 | FastMPP 3 was designed around two primitives: providers (source of tools/resources) and transforms (modify/namespace tools). |
|  10 | Most new features in FastMPP 3 are implemented as providers or transforms.                                                   |
|  11 | Examples of innovation enabled by FastMPP 3:                                                                                 |
|  12 | Tool search (inspired by Claude): exposes tool search to all clients via a transform.                                        |
|  13 | Code mode: allows executing small programs against the MCP server, available as a transform.                                 |
|  14 | Progressive disclosure: dynamically reveals tools based on user actions.                                                     |
|  15 | Emphasis on pushing clients to support more advanced MCP features.                                                           |
|  16 | Introduction of MCP apps: servers deliver full UIs directly to users, bypassing agents.                                      |
|  17 | Challenge: most FastMPP users are Python developers, but MCP apps require front-end (JS/TS) skills.                          |
|  18 | Most use cases are internal to companies, focusing on sharing data/workflows within trusted boundaries.                      |
|  19 | Prefab, a new generative component library, allows building interactive UIs in Python using a token-efficient DSL.           |
|  20 | Prefab integrates with FastMPP for interactive tools, MCP apps, and generative UIs.                                          |
|  21 | Prefab apps can provide features like file upload, interactive tables, and charts.                                           |
|  22 | Prefab code is converted to JSON, rendered as React apps, and sup                                                            |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=vfOe10Ww6s0)