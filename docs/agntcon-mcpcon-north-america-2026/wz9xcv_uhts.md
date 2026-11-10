---
layout: default
title: "How Open Standards Become Real: Lessons from Agent Plugins - Jonathan Hefner, Vercel"
nav_order: 46
parent: AGNTCon + MCPCon North America 2026
type: Video Note
description: "Jonathan Hefner, a developer at Vercel, presents a critical analysis of the challenges involved in developing open standards for AI agent plugins, specifically focusing on the tension between stand..."
resource: "https://www.youtube.com/watch?v=wz9xCv_UHts"
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

Jonathan Hefner, a developer at Vercel, presents a critical analysis of the challenges involved in developing open standards for AI agent plugins, specifically focusing on the tension between standard promises and implementer capabilities.
He argues that a standard’s value depends on the willingness of client implementers to support its requirements, as promising features that implementers cannot or will not provide erodes consumer trust and undermines the standard’s utility.
Using the proposal for "hooks" as a case study, Hefner illustrates how design decisions must balance the need for portable, cross-client functionality with the burden of implementation, suggesting that standards should cover ordinary needs to minimize the reliance on client-specific "escape hatches" that reduce portability.
He further emphasizes that not every problem should be solved within the core specification; instead, issues like dependency management are often better addressed by build tools or packaging formats, keeping the standard focused and reducing complexity.
Finally, Hefner advises that successful standardization requires early and continuous engagement with implementers to ensure their product visions and constraints are respected, noting that while there are no easy answers, negotiation and consensus-building are essential to creating standards that are both practical and widely adopted.

# Main Points

|   # | Main point                                                                                                                                                                                                                  |
| --: | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | , agent skills, and MCP, focusing on the tension between standard promises and implementer capabilities.                                                                                                                    |
|   2 | ; if implementers do not support a feature, the standard’s promise to consumers is broken, eroding trust.                                                                                                                   |
|   3 | , as adding a requirement without implementer commitment creates a gap between the standard and reality.                                                                                                                    |
|   4 | "hooks" in agent plugins aims to let clients run plugin code in response to events while minimizing the burden on client implementation.                                                                                    |
|   5 | , the design uses a "portable tool profile" that describes the operation kind and target file, allowing hook handlers to make decisions without interpreting client-specific data formats like patches or replacement text. |
|   6 | "escape hatch" allows plugin authors to access native tool inputs when the portable profile is insufficient, but this risks tying plugins to specific clients and reducing portability.                                     |
|   7 | ; for example, dependency management between skills is better handled by build or publishing tools rather than by adding complex fields to the skill specification itself.                                                  |
|   8 | , as it can discourage adoption and create long-term compatibility burdens.                                                                                                                                                 |
|   9 | , such as through namespaced extensions, allowing clients to define specific features without conflicting with future standard definitions.                                                                                 |
|  10 | , rather than being presented with a finished specification.                                                                                                                                                                |
|  11 | , standard designers must empathize with implementers’ constraints and resources to propose feasible solutions.                                                                                                             |
|  12 | (e.g., OpenAI, Visual Studio Code, Cursor, AWS Q) who commit to supporting the spec, which then encourages broader adoption.                                                                                                |
|  13 | "hooks" feature is currently the most complex part of the agent plugins standard, with a public pull request recently opened for discussion ahead of version 1.1.                                                           |
|  14 | , with no easy answers.                                                                                                                                                                                                     |

# Video

[![Video thumbnail](https://img.youtube.com/vi/wz9xCv_UHts/hqdefault.jpg)](https://www.youtube.com/watch?v=wz9xCv_UHts)

[Watch on YouTube](https://www.youtube.com/watch?v=wz9xCv_UHts)
