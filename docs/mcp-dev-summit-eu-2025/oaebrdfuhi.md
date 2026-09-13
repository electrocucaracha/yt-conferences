---
layout: default
title: "[Keynote] MCP Project Update with David Soria Parra - Anthropic"
nav_order: 23
parent: Mcp Dev Summit Eu 2025
type: Video Note
description:
  David, co-creator of MCP and technical staff at Anthropic, provides an
  overview of MCP’s progress as it nears its one-year anniversary. He highlights the
  rapid growth of the ecosystem, with over 10,000 MCP servers and a wide variety of
  clie...
resource: https://www.youtube.com/watch?v=-OAebRdfUhI
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

David, co-creator of MCP and technical staff at Anthropic, provides an overview of MCP’s progress as it nears its one-year anniversary.
He highlights the rapid growth of the ecosystem, with over 10,000 MCP servers and a wide variety of clients and SDKs now available, thanks to significant community contributions and collaborations with major companies.
The protocol has seen fast-paced development, including two major new versions, improvements in streaming, authorization, and structured output, while maintaining a focus on practicality and backward compatibility.
David discusses ongoing challenges such as scaling community governance, improving server quality, and enhancing SDK clarity, and outlines upcoming priorities like asynchronous tasks, statelessness, and server identity.
He encourages further community involvement, emphasizes the need for better tools and standards, and expresses excitement about underutilized features like structured output and resources, while acknowledging remaining issues around security, context, and model-specific prompting.

# Main Points

|   # | Main point                                                                                                                                                                      |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | David (DSP) is a co-creator of MCP and technical staff at Anthropic.                                                                                                            |
|   2 | MCP is approaching its one-year anniversary with over 10,000 servers deployed.                                                                                                  |
|   3 | The ecosystem has grown rapidly, with many clients and daily users.                                                                                                             |
|   4 | Early clients were limited; now there is a wide variety supporting more protocol features.                                                                                      |
|   5 | Visual Studio Code team is highlighted for leading feature implementation.                                                                                                      |
|   6 | Community has contributed several SDKs: Python, TypeScript, C (with Microsoft), Java (Spring AI), Go (recent 1.0 release), and PHP.                                             |
|   7 | MCP registries proliferated; a centralized registry API and open API spec were introduced for better discovery and flexibility.                                                 |
|   8 | Goal: enable agents to automatically select appropriate servers via the registry API.                                                                                           |
|   9 | Two new protocol versions released (March and June), with fast iteration and focus on practicality and backward compatibility.                                                  |
|  10 | March update reworked SSE streams, introduced streamable HTTP, and maintained standard IO.                                                                                      |
|  11 | Authorization improved with input from OATH community and major IDP providers; leaning into OATH, but challenges remain with fine-grained auth and dynamic client registration. |
|  12 | New protocol features: structured output, elicitations, resource links, tool annotations.                                                                                       |
|  13 | Community has grown, now includes an open Discord and formal governance board with members from OpenAI, Microsoft, AWS, Google, and Anthropic.                                  |
|  14 | Maintainers and community managers recognized for their contributions.                                                                                                          |
|  15 | Project faces scaling challenges in issue management and specification proposals; seeking more contributors.                                                                    |
|  16 | Plan to introduce SDK tiering for clarity on support and maintenance.                                                                                                           |
|  17 | Interest groups and working groups (e.g., financial services) are being encouraged.                                                                                             |
|  18 | Upcoming November 25th release will have a two-week freeze for testing and feedback.                                                                                            |
|  19 | Main focus areas: asynchronous tasks (AWS proposal), statelessness (Google proposal), and server identity.                                                                      |
|  20 | MCPY project and extension patterns for specialized use cases are in developmen                                                                                                 |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=-OAebRdfUhI)
