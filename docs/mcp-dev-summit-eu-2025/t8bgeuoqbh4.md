---
layout: default
title:
  "[Keynote] Scaling Commerice Interactivity Lessons from Shopify's Implementation
  of MCP UI"
nav_order: 30
parent: Mcp Dev Summit Eu 2025
type: Video Note
description:
  Samuel and Brett, engineers from Shopify, discuss the future of user
  interfaces (UI) in the context of the Model Context Protocol (MCP), a standard that
  enables AI models and tools to communicate and integrate seamlessly. They explain
  that...
resource: https://www.youtube.com/watch?v=T8bgEuOQbH4
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

Samuel and Brett, engineers from Shopify, discuss the future of user interfaces (UI) in the context of the Model Context Protocol (MCP), a standard that enables AI models and tools to communicate and integrate seamlessly.
They explain that while AI chatbots have become more intelligent and capable of accessing tools and APIs, interacting with them through text alone can feel limiting compared to the rich, domain-specific UIs users expect.
MCP UI addresses this by allowing servers to send UI resources—such as product cards, carts, and checkouts—to clients, enabling interactive and visually rich experiences within AI agents or chat environments.
The presenters demonstrate how MCP UI is used at Shopify and integrated into the open-source Libra Chat platform, allowing users to browse, add to cart, and purchase products through embedded UI components, with all user actions communicated back to the agent.
They also highlight the flexibility of MCP UI for styling and integration, discuss ongoing improvements, and invite attendees to learn more through deep-dive sessions and further resources.

# Main Points

|   # | Main point                                                                                                                   |
| --: | ---------------------------------------------------------------------------------------------------------------------------- |
|   1 | Samuel and Brett, engineers from Shopify, discuss the future of UI in MCP.                                                   |
|   2 | MCP stands for Model Context Protocol, not Model Context Prototype.                                                          |
|   3 | MCP is a standard for AI models and tools to communicate and integrate with each other.                                      |
|   4 | MCP reduces integration complexity, making tools and models composable and cross-compatible.                                 |
|   5 | LLMs have improved and now have access to tools and APIs, enabling real-world actions like booking taxis or making payments. |
|   6 | MCP allows standard discovery and execution of tools, similar to how USBC works for hardware.                                |
|   7 | Current AI interactions are often limited to text, but users expect richer, more interactive UIs.                            |
|   8 | MCP UI is a standard for servers to send UI resources to clients, bridging LLM intelligence and rich custom UIs.             |
|   9 | Shopify uses MCP UI to expose commerce components (product cards, carts, checkout) to any MCP client.                        |
|  10 | MCP UI is open source and not created or maintained by Shopify, but used internally and externally.                          |
|  11 | MCP UI can be used for various domains beyond commerce, such as maps, scheduling, and analytics dashboards.                  |
|  12 | UI resources in MCP responses include both text and UI components, ensuring LLMs know what’s displayed.                      |
|  13 | UI resources are provided as URLs, typically embedded as iframes, allowing sandboxing and security.                          |
|  14 | User actions in the UI (intents) are sent to the agent, making the LLM aware of user interactions.                           |
|  15 | Shopify is integrating MCP UI into Libre Chat, enabling product search and purchases via chat with embedded UI.              |
|  16 | Clients can render MCP UI components flexibly (in text stream, side pane, modal, etc.).                                      |
|  17 | Both UI interactions and text commands trigger the same intents and tool calls.                                              |
|  18 | Clients can style MCP UI components using CSS custom properties and parts, communicated via postMessage to the iframe.       |
|  19 | There is a proposal to allow iframes to read data attributes from parent pages for easier customization.                     |
|  20 | More information is available at mcpui.dev, with deep dive sessions and open invitations                                     |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=T8bgEuOQbH4)
