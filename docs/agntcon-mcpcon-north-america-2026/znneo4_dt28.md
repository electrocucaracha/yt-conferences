---
layout: default
title: "Building Buzz inside Buzz: How Engineering, Design, and Agents... - Will Pfleger & Taylor Ho, Block"
nav_order: 88
parent: AGNTCon + MCPCon North America 2026
type: Video Note
description: "Will and Taylor from Block presented how engineering and design collaborate within Buzz, a platform built on Nostr technology that emphasizes persistent, shared context through dedicated channels."
resource: "https://www.youtube.com/watch?v=ZnNeO4_dt28"
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

Will and Taylor from Block presented how engineering and design collaborate within Buzz, a platform built on Nostr technology that emphasizes persistent, shared context through dedicated channels.
They demonstrated a workflow where human developers and AI agents, such as Will’s Dune-themed team and Taylor’s agent Ned, co-create features like a generic harness mechanism that allows users to plug in any ACP-compatible agent without requiring manual pull requests or maintainer approval.
Taylor highlighted how design engineers can leverage this system by linking existing channels and pull requests to provide agents with rich context, avoiding the need for lengthy prompt dumps and enabling rapid prototyping of user interfaces.
The speakers explained that because all interactions are stored as signed events on a Nostr-compliant relay, the historical record of decisions and trade-offs remains permanently accessible, allowing teams to retrieve past reasoning months later for new projects or presentations.
Finally, they outlined the roadmap for a new Buzz architecture that shifts from a monolithic app to a fully pluggable ecosystem, supporting federated identity for enterprise security and enabling external clients to query the relay directly, thereby making the platform’s context and capabilities accessible beyond the native desktop application.

# Main Points

|   # | Main point                                                                                                                                                                  |
| --: | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | (Software Engineer) and Taylor (Design Engineer) from Block presented on how engineering and design collaborate within the Buzz app.                                        |
|   2 | , with early community demand for bringing custom agents and harnesses into the platform.                                                                                   |
|   3 | , starting with four built-in options: Buzz Agent, Goose, Cloud Code, and Codex.                                                                                            |
|   4 | , allowing users to mix and match agents with different execution environments.                                                                                             |
|   5 | "Bring Your Own Harness" feature was developed, allowing any harness that speaks the ACP protocol to be plugged in without requiring a pull request or maintainer approval. |
|   6 | : Every feature, bug, or investigation gets its own channel, serving as shared context for humans and agents.                                                               |
|   7 | , trade-offs, and implementation details, eliminating the need for separate tickets or Slack threads.                                                                       |
|   8 | , which dispatches worker agents for coding, followed by reviewer and tester agents for validation.                                                                         |
|   9 | "giant prompts," allowing agents to read PRs, docs, and past conversations to build context.                                                                                |
|  10 | , generating ASCII wireframes and identifying UX priorities without manual handoff docs.                                                                                    |
|  11 | (agent catalog model) to refine the harness selection UI, resulting in a cleaner interface with easy toggles and setup states.                                              |
|  12 | , meaning all messages and context are stored on relays as signed events, making them queryable by any client with the appropriate key.                                     |
|  13 | , shifting from a monolithic app to a system where features and harnesses are plugins, reducing the burden on core maintainers.                                             |
|  14 | (Model Context Protocol), exposing tools for sending messages, editing canvases, and managing channels.                                                                     |
|  15 | , allowing authentication via corporate identity providers like Okta in addition to private keys.                                                                           |
|  16 | (allow/deny), with sensitivity considerations for remote or sandboxed agents accessing sensitive data.                                                                      |
|  17 | , but its Nostr-compliant nature allows for custom client integrations and external data processing.                                                                        |

# Video

[![Video thumbnail](https://img.youtube.com/vi/ZnNeO4_dt28/hqdefault.jpg)](https://www.youtube.com/watch?v=ZnNeO4_dt28)

[Watch on YouTube](https://www.youtube.com/watch?v=ZnNeO4_dt28)
