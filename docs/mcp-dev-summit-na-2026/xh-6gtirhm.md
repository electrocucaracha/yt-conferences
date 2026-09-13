---
layout: default
title:
  "MCP Apps Best Practices: Patterns and Pitfalls - Olivier Chafik & Anton Pidkuiko,
  Anthropic"
nav_order: 53
parent: Mcp Dev Summit Na 2026
type: Video Note
description:
  Olivier and Anton from Anthropic introduced MCP apps, describing them
  as a protocol for AI applications akin to USB or HDMI for hardware, enabling seamless
  interoperability and interactive user experiences. They demonstrated features such
  a...
resource: https://www.youtube.com/watch?v=Xh__6GtirHM
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

Olivier and Anton from Anthropic introduced MCP apps, describing them as a protocol for AI applications akin to USB or HDMI for hardware, enabling seamless interoperability and interactive user experiences.
They demonstrated features such as efficient tool calls, interactive views (like a PDF viewer), and mechanisms for data access, authentication, and state persistence, emphasizing that MCP apps allow developers to build rich, responsive interfaces that minimize token usage by sending data directly to the app rather than through the model.
The talk covered best practices for structuring tool calls, updating model context, handling authentication, and ensuring accessibility, as well as upcoming features like direct model-to-view communication and partial input streaming for reduced latency.
They highlighted that MCP apps are standard web apps with added capabilities, support graceful degradation, and can be integrated into existing codebases, encouraging contributions and further exploration of the open-source ecosystem.
Audience questions addressed efficiency, data sharing between model and app, streaming, accessibility, and technical implementation details.

# Main Points

|   # | Main point                                                                                                                    |
| --: | ----------------------------------------------------------------------------------------------------------------------------- |
|   1 | Olivier and Anton from Anthropic presented on MCP apps.                                                                       |
|   2 | MCP apps spec was co-written with OpenAI and others.                                                                          |
|   3 | MCP is described as "USB for AI applications," enabling interoperability.                                                     |
|   4 | MCP apps allow tools to return interactive resources (e.g., HTML views) instead of just text, improving speed and efficiency. |
|   5 | Example: PDF viewer app can display, fill, and annotate PDFs interactively within the chat UI.                                |
|   6 | MCP apps sit atop tools, connect to servers, and manage input/output flexibly.                                                |
|   7 | Tool calls in MCP can include content (for the model), structured content (typed data), and meta (internal data).             |
|   8 | Tool results can include a unique view UUID for referencing views in further interactions.                                    |
|   9 | Data access: Apps can fetch data directly (like web apps) or use tool calls for authenticated data.                           |
|  10 | For authentication, use tool calls to avoid token expiration issues.                                                          |
|  11 | Apps can poll for data, make parallel calls, chunk data, and return binary blobs.                                             |
|  12 | Interactions can be managed via a command queue using the view UUID.                                                          |
|  13 | Upcoming spec will allow view-local tools for direct model-to-view communication.                                             |
|  14 | Apps can update the model context with text/images to keep the model aware of the app state.                                  |
|  15 | State persistence is planned for the spec; currently, use server-side storage or localStorage.                                |
|  16 | Universal servers can detect client capabilities and enable/disable app features accordingly.                                 |
|  17 | Apps should blend into host UI, support light/dark mode, avoid nested scrollbars, and use CSS variables.                      |
|  18 | Streaming partial tool inputs reduces latency; apps can process and display data as it streams in.                            |
|  19 | "Show me" feature streams HTML/SVG for inline visualizations.                                                                 |
|  20 | To share data with the model, update model context or expose tools for the model to pull data.                                |
|  21 | Accessibility relies on standard web practices; no special screen reader support implemented yet.                             |
|  22 | Partial streaming allows apps to render progress as inputs arrive; host is responsible for chunking responses.                |
|  23 | Encourageme                                                                                                                   |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=Xh__6GtirHM)
