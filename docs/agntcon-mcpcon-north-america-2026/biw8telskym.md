---
layout: default
title: "Superpowering ChatGPT with mcp Extensions - Victor Lin, OpenAI"
nav_order: 6
parent: AGNTCon + MCPCon North America 2026
type: Video Note
description: "Victor from OpenAI’s plugins team introduces MCP extensions, a set of new APIs and proposals designed to make plugins feel more native and first-party within ChatGPT."
resource: "https://www.youtube.com/watch?v=Biw8telskYM"
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

Victor from OpenAI’s plugins team introduces MCP extensions, a set of new APIs and proposals designed to make plugins feel more native and first-party within ChatGPT.
The core motivation is to treat ChatGPT as a lean platform rather than a monolithic super-app, allowing developers to personalize the experience through plugins while OpenAI handles foundational infrastructure like conversation loops and thread management.
Key improvements include enabling full-screen display modes by default to support persistent work sessions, allowing developers to declare supported display modes ahead of time for faster rendering, and integrating WebMCP to let the AI model directly interact with app UIs, thereby breaking the "iframe" barrier.
Additionally, extensions provide hooks into various parts of the ChatGPT interface, such as settings, onboarding, and the sidebar, ensuring that plugins can integrate seamlessly into the broader user workflow.
This approach aims to create a more immersive, model-aware experience where users can perform complex tasks without leaving the ChatGPT environment, leveraging the familiarity and robustness of the existing MCP specification.

# Main Points

|   # | Main point                                                                                                                          |
| --: | ----------------------------------------------------------------------------------------------------------------------------------- |
|   1 | # Key Points                                                                                                                        |
|   2 | • Victor from OpenAI's plugins team announced MCP (Model Context Protocol) extensions at Dev Day                                    |
|   3 | • Extensions are adjustments to existing MCP specifications to make plugins and MCPs appear more native within ChatGPT              |
|   4 | • Example extension: mention search allows users to provide custom suggestion lists for mentions (e.g., Slack people or channels)   |
|   5 | • ChatGPT desktop codebase grew to over 1 million lines of code by June due to product-specific logic                               |
|   6 | • OpenAI is shifting ChatGPT from a super-app to a platform model where developers add functionality via plugins                    |
|   7 | • Internal OpenAI teams now ship products as plugins rather than adding code to desktop                                             |
|   8 | • MCP is used because developers are already familiar with it as an API standard                                                    |
|   9 | • Roslyn (AI research tool) needed custom TIFF file viewer; solved via MCP by declaring file type support in metadata               |
|  10 | • Presentations team needed custom gallery input view; solved by supporting custom resource input in formal requests                |
|  11 | • MCP applications previously only displayed inline; extensions enable full-screen as default display mode                          |
|  12 | • Display mode can now be declared in HTML metadata before rendering, allowing immediate mode determination and placeholder display |
|  13 | • Users expect everything in ChatGPT to be model-aware; MCPs previously broke this immersion as "glorified iframes"                 |
|  14 | • MCP web support now allows agents to interact with UI elements (search, delete, pay) directly within applications                 |
|  15 | • Browser use integrated as alternative for applications not supporting MCP web                                                     |
|  16 | • ChatGPT extensions now provide hooks to multiple app areas: conversation, settings, onboarding, sidebar, chat panel, tabs         |
|  17 | • Full-screen became expected default for MCP app rendering; developers should use it for better user experience                    |
|  18 | • MCP web within iframes enables model interaction without breaking user immersion                                                  |
|  19 | • Community feedback available at community.openai.com and public GitHub repository for MCP extensions                              |

# Video

[![Video thumbnail](https://img.youtube.com/vi/Biw8telskYM/hqdefault.jpg)]("https://www.youtube.com/watch?v=Biw8telskYM")

[Watch on YouTube](https://www.youtube.com/watch?v=Biw8telskYM)
