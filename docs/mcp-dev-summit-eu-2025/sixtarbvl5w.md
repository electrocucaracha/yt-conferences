---
type: Video Note
title: "[Session] MCP-UI: Next-gen Agentic Experiences"
description: "The speaker introduces MCPUI, an open protocol designed to address the limitations of text-based interfaces in chat environments by enabling providers to send interactive UI components, preserving their brand identity and enhancing user exp..."
resource: https://www.youtube.com/watch?v=SIXTArBVL5w
tags: ["mcp-dev-summit-eu-2025", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

The speaker introduces MCPUI, an open protocol designed to address the limitations of text-based interfaces in chat environments by enabling providers to send interactive UI components, preserving their brand identity and enhancing user experience.
MCPUI allows applications to break down their interfaces into composable, interactive "chunks" that can be embedded in chats, supporting complex interactions and communication between UI elements and the host through defined patterns such as notify, tool calls, prompts, and intents.
The protocol ensures security by sandboxing UI components in iframes and supports theming and rendering flexibility through features like custom CSS and remote DOM, allowing consistent experiences across different hosts.
MCPUI is already adopted by companies like Shopify, Postman, Goose, and Hugging Face, and supports multiple SDKs, making integration straightforward.
The project is community-driven, with ongoing work on authentication, native client support, and broader adoption, aiming to enable seamless, agentic workflows where users interact with multiple apps through a unified, interactive chat interface.
# Main Points

|   # | Main point                                                                                                                                                                |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | MCPUI addresses the "wall of text" problem in text-based interfaces by enabling providers to send UI components, preserving their identity.                               |
|   2 | Providers like Shopify, Airbnb, Amazon can send interactive UI chunks instead of just text, maintaining their brand and user experience.                                  |
|   3 | MCPUI is an open protocol for sending UI over MCP and standardizing host-UI communication.                                                                                |
|   4 | Community SDKs are available in Ruby, Python, TypeScript, with more in development.                                                                                       |
|   5 | Providers can break down their existing UI and serve it via MCPUI without abandoning their perfected interfaces.                                                          |
|   6 | Companies like Shopify, Postman, Goose, Hugging Face, and 11 Labs have adopted or are adopting MCPUI.                                                                     |
|   7 | MCPUI uses embedded resources and UI schemas to deliver interactive UI components to hosts.                                                                               |
|   8 | Defines communication patterns between UI chunks and hosts, enabling actions like delete, reassign, and analyze within the UI.                                            |
|   9 | Demo showed interactive sprint status management, with UI components communicating intents and actions to the host.                                                       |
|  10 | UI resources are returned from servers and rendered by hosts using client SDKs, supporting secure, sandboxed interactions.                                                |
|  11 | Enables agentic flows and complex interactions within and between apps, all in one chat interface.                                                                        |
|  12 | Supports a fragmented web experience where users interact with composable UI atoms from multiple providers in a single chat, reducing the need for multiple browser tabs. |
|  13 | MCPUI defines a communication protocol for UI chunks to notify, prompt, or send intents to the host, similar to islands architecture.                                     |
|  14 | State management can occur at the agent, UI (internal state), or backend levels, depending on use case.                                                                   |
|  15 | Security is ensured by running UI code in sandboxed iframes, restricting access and communication to post messages.                                                       |
|  16 | Theming is supported via custom CSS, theme tokens, and remote DOM, allowing UI to match host appearance.                                                                  |
|  17 | Future work includes authentication/authorization, supporting native clients, and abstract payloads for non-web e                                                         |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=SIXTArBVL5w)