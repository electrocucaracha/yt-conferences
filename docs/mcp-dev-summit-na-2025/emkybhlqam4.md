---
layout: default
title:
  "[Session] MCP Project Update with Jerome Swannack, Member of Technical Staff
  at Anthropic"
nav_order: 8
parent: Mcp Dev Summit Na 2025
type: Video Note
description:
  Jerome Swanik, a member of the core engineering team at Anthropic, introduces
  himself and shares his journey from aerospace engineering to working on the MCP
  protocol, motivated by the transformative potential of large language models. He
  r...
resource: https://www.youtube.com/watch?v=eMKyBHlqAm4
tags:
  - mcp-dev-summit-na-2025
  - video
  - learning
status: stable
generated:
  by: process:yt-conferences-okf
  at: 2026-09-12 00:00:00+00:00
---

# Summary

Jerome Swanik, a member of the core engineering team at Anthropic, introduces himself and shares his journey from aerospace engineering to working on the MCP protocol, motivated by the transformative potential of large language models.
He recounts the origin of MCP as a solution to automate on-call engineering tasks and describes how he helped spread MCP within Anthropic through demos and hackathons.
Over the past six months, the team has focused on enabling remote MCP, streamable HTTP transport, and expanding SDKs and developer tools, emphasizing the importance of birectional communication and minimizing server complexity.
Looking ahead, Swanik discusses upcoming protocol features like elicitation and tool output schemas, which aim to support richer agent interactions and more efficient handling of structured data.
He also highlights ongoing efforts to foster the developer ecosystem, improve discoverability, and transition MCP governance to a more open, community-driven model, inviting input from those with experience in protocol governance.

# Main Points

|   # | Main point                                                                                                                                         |
| --: | -------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Jerome Swanik, member of technical staff at Anthropic, core engineering team for MCP                                                               |
|   2 | Background in aerospace and rocketry; now based in London                                                                                          |
|   3 | Discovered LLMs via GPT-3 API, built a Discord bot, inspired to join the AI frontier                                                               |
|   4 | MCP origin: started as a personal project to automate on-call engineering tasks                                                                    |
|   5 | Joined MCP initiative after being approached by Justin and David to open source the protocol                                                       |
|   6 | Promoted MCP within Anthropic through demos, hackathons, tutorials, and unique server projects (e.g., unlocking front door, Factorio admin server) |
|   7 | MCP open sourced 6 months ago; rapid growth, strong community contributions, team scaling to support open source efforts                           |
|   8 | Recent technical focus: enabling remote MCP, OAuth, streamable HTTP transport (replacing SSE), new SDKs, and dev tools                             |
|   9 | Streamable HTTP chosen for progressive enhancement, bidirectionality, and to minimize server complexity; avoids ecosystem fragmentation            |
|  10 | Websockets and plain RESTful HTTP not chosen due to lack of necessary bidirectionality for agentic interactions                                    |
|  11 | Principle: more servers than clients expected, so protocol complexity pushed to clients                                                            |
|  12 | Upcoming protocol features: elicitation (in review) and tool output schema (in draft)                                                              |
|  13 | Elicitation: allows servers to request specific information from clients via JSON schema, enabling richer agentic interactions and dynamic UIs     |
|  14 | Tool output schema: allows structured tool results, improving efficiency, composability, and context window management                             |
|  15 | Recommendations for server builders: consider structured outputs for tools, especially for logging/observability                                   |
|  16 | Recommendations for client builders: prepare for handling elicitation and structured tool outputs, possibly via execution environments             |
|  17 | Ecosystem efforts: fostering developer community, more SDKs, open source example servers and clients, improved dev tools                           |
|  18 | Discoverability: MCP registry in progress                                                                                                          |
|  19 | Governance: aiming for open, community-driven project; exploring transition to                                                                     |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=eMKyBHlqAm4)
