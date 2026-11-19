---
layout: default
title: "The New Web: How MCP Apps Put Live UI Inside ChatGPT & Claude"
nav_order: 78
parent: MCP Dev Summit NA 2026
type: Video Note
description: "Adi Solomon and Adi Yosef introduce MCP Apps, an open standard that transforms text-based AI interactions into rich, interactive user experiences by allowing applications to send their own branded ..."
resource: "https://www.youtube.com/watch?v=TXe9hkWgxOI"
tags:
  - mcp-dev-summit-na-2026
  - video
  - learning
status: stable
generated:
  by: process:yt-summarizer-okf
  at: 2026-11-15T16:54:07+00:00
---

# Summary

Adi Solomon and Adi Yosef introduce MCP Apps, an open standard that transforms text-based AI interactions into rich, interactive user experiences by allowing applications to send their own branded UIs directly to hosts like ChatGPT, Visual Studio Code, and Claude.
The protocol leverages existing MCP primitives to render HTML resources within a sandbox, enabling users to interact with third-party tools—such as PostHog or Canva—without leaving the chat interface, thereby preserving brand identity and streamlining workflows.
This approach supports a "new web" philosophy where agents compose modular UI components from various services, replacing the need for multiple browser tabs and complex manual navigation.
The specification is rapidly evolving with community input, adding features like theming, reusable views, and interoperability with other generative UI methods, while maintaining a unified SDK that ensures applications built once can run across all supported hosts.
The presenters emphasize that MCP Apps is not just a technical upgrade but a fundamental shift in app distribution, offering developers access to a massive global user base and inviting the community to actively shape the future of this emerging web standard.

# Main Points

|   # | Main point                                                                                                                                                               |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   1 | MCP apps extend the Model Context Protocol to replace text responses with rich, interactive user interfaces across various platforms.                                    |
|   2 | The specification was developed rapidly over four months, driven by community efforts and support from Anthropic, OpenAI, and MCPUI.                                     |
|   3 | Major hosts including Visual Studio Code, Cursor, GitHub Copilot, ChatGPT, Postman, and Goose have adopted MCP apps as a standard for building applications.             |
|   4 | The core concept allows MCP servers to send HTML resources to hosts, which render them as interactive components within a sandboxed environment.                         |
|   5 | Interactivity is standardized by having the UI send messages, such as tool calls or notifications, back to the host rather than communicating directly with the backend. |
|   6 | This architecture ensures the model remains aware of user actions, allowing it to manage the flow and maintain context during interactions.                              |
|   7 | MCP apps preserve the branding and identity of third-party services, such as PostHog or Canva, while integrating them seamlessly into the chat experience.               |
|   8 | The technology supports both predefined UIs provided by apps and generative UIs created on the fly by the model, offering flexibility in how interfaces are rendered.    |
|   9 | The official SDK, known as Axed apps, enables developers to build applications once and deploy them across all compatible hosts without modification.                    |
|  10 | The specification is evolving to include features like theming, sampling, and reusable views to improve performance and user experience for complex applications.        |
|  11 | A new proposal called App Tools aims to allow agents to interact with applications as if they were human users, updating UIs in place rather than re-rendering them.     |
|  12 | The team is exploring the need for native mobile experiences beyond HTML iframes, though current use cases primarily rely on web-based rendering.                        |
|  13 | MCP apps are positioned as a new distribution channel, leveraging the massive user base of platforms like ChatGPT to reach a global audience.                            |
|  14 | Developers are encouraged to join the public working group meetings and contribute to the open-source repository to shape the future of the standard.                    |
|  15 | The initiative aims to transform the web into a composable ecosystem where agents assemble UI atoms from various services into a unified context.                        |
|  16 | Community engagement is facilitated through Discord channels and GitHub, where users discuss spec changes, share feedback, and collaborate on development.               |
|  17 | The goal is to establish MCP apps as the global standard for UI distribution, enabling rich experiences that were previously impossible in text-based interfaces.        |

# Video

[![Video thumbnail](https://img.youtube.com/vi/TXe9hkWgxOI/hqdefault.jpg)](https://www.youtube.com/watch?v=TXe9hkWgxOI)

[Watch on YouTube](https://www.youtube.com/watch?v=TXe9hkWgxOI)
