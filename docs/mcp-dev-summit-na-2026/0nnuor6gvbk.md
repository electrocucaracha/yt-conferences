---
layout: default
title:
  Goose as a Proving Ground for New MCP Features, and How To Use Them - Alex
  Hancock, Block
nav_order: 32
parent: Mcp Dev Summit Na 2026
type: Video Note
description:
  The speaker discusses bridging the gap between those with ideas for improving
  MCP or agents and those able to test and implement these ideas at scale. They introduce
  Goose, an open-source agent project originating at Block and now governed...
resource: https://www.youtube.com/watch?v=0nNUor6GVbk
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

The speaker discusses bridging the gap between those with ideas for improving MCP or agents and those able to test and implement these ideas at scale.
They introduce Goose, an open-source agent project originating at Block and now governed by the Linux Foundation, which serves as a collaborative proving ground for new MCP features and experimentation.
Goose emphasizes performance, stability, interoperability with open standards like MCP and ACP, and a willingness to rapidly experiment and evolve.
The talk highlights features such as "code mode" for efficient token usage, integration with the Agent Client Protocol to enable diverse client interactions, and support for MCP apps, including experimental features like AI-powered app front-ends.
The speaker invites the community to contribute experimental ideas and implementations to Goose, positioning it as a platform for real-world testing and collaborative innovation in the agent ecosystem.

# Main Points

|   # | Main point                                                                                                                                                                        |
| --: | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Audience asked if they have ideas for improving MCP or agents; fewer have projects to test those ideas.                                                                           |
|   2 | Goal is to close the gap between ideas and real-world testing.                                                                                                                    |
|   3 | Speaker is a software engineer at Block, core maintainer of Goose (open source agent), and MCP maintainer focusing on the Rust SDK.                                               |
|   4 | Goose is an open source agent project with a desktop app and terminal experience.                                                                                                 |
|   5 | Supports remote model access from major providers and local inference with embedded LLM provider.                                                                                 |
|   6 | Uses MCP for extensions and supports new features like apps.                                                                                                                      |
|   7 | Goose originated at Block, open sourced, and donated to the Linux Foundation as part of the Agentic AI foundation.                                                                |
|   8 | Agents can now be generated quickly; questions raised about what makes a permanent agent project valuable.                                                                        |
|   9 | Key focuses for agent projects: performance, stability, interoperability, willingness to experiment, and neutral/open governance.                                                 |
|  10 | Goose aims to be a proving ground for new and experimental MCP features.                                                                                                          |
|  11 | Encourages collaboration and contributions from the community for experimental MCP ideas.                                                                                         |
|  12 | Example feature: "code mode" inspired by Cloudflare and Anthropic, improves token usage and performance by executing code in a sandbox, reducing unnecessary data sent to models. |
|  13 | Open source collaboration led to integration with another project’s Rust library, simplifying Goose’s code mode implementation.                                                   |
|  14 | Goose implemented support for Agent Client Protocol (ACP), enabling more clients (desktop, mobile, web, terminal) to control agents via a standardized protocol.                  |
|  15 | ACP support allows flexible deployment and interaction between agents and clients.                                                                                                |
|  16 | Goose adopted MCP UI early, influencing its development into MCP apps.                                                                                                            |
|  17 | Goose supports MCP apps, including advanced features like sampling from app front-end code, enabling AI-powered apps.                                                             |
|  18 | Sampling from the app front-end is being incubated in Goose, with plans to formalize in the SDK.                                                                                  |
|  19 | Goose currently lacks support for long-running tasks in the host UI but Ratings (1-5): 3                                                                                          |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=0nNUor6GVbk)
