---
layout: default
title:
  "Building ChatGPT Apps: Principles for a New Kind of Interface - Elliot Garreffa,
  Ghost Team"
nav_order: 3
parent: Mcp Dev Summit Na 2026
type: Video Note
description:
  In this talk, Elliot Graff, co-founder of Ghost Team, discusses key principles
  for designing ChatGPT and MCP (multi-client platform) apps, emphasizing the shift
  from the traditional, fragmented web to an intent-based web where users prompt...
resource: https://www.youtube.com/watch?v=Km4ZZW0Aohc
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

In this talk, Elliot Graff, co-founder of Ghost Team, discusses key principles for designing ChatGPT and MCP (multi-client platform) apps, emphasizing the shift from the traditional, fragmented web to an intent-based web where users prompt for what they need and tools come to them.
Drawing on extensive data from tracking major app stores, he highlights the importance of starting with clear user intents and goals, optimizing tool descriptions as the new form of SEO to improve app discoverability, and designing for both the UI widget and the conversational text interface.
Graff stresses the need to build apps that leverage the model’s context and memory, support multi-turn conversations, and use negative constraints to prevent errors or hallucinations.
He also notes the significant differences between testing in staging environments and live usage, recommending realistic, large-scale, in-client testing.
Finally, he advises keeping apps simple and focused on refined intents, as those with fewer, well-designed tools tend to perform better in terms of user engagement and invocation rates.

# Main Points

|   # | Main point                                                                                                                                    |
| --: | --------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Building ChatGPT and MCP apps requires new design principles compared to traditional web and mobile apps.                                     |
|   2 | There is a shift from a fragmented web to an intent-based web, where users prompt and tools come to them.                                     |
|   3 | Ghost team builds and distributes ChatGPT and MCP apps, and tracks app store data for insights.                                               |
|   4 | Recent surge in ChatGPT app submissions, with 96 new apps in the last 10 days, including major brands.                                        |
|   5 | Three core components: ChatGPT interface (user prompts), MCP server (tools), and widget (UI element in conversation).                         |
|   6 | Tool descriptions are crucial for app discovery and function, similar to SEO/AEO.                                                             |
|   7 | Widgets allow private data visualization without exposing all data to the model.                                                              |
|   8 | Start with clear goals and user intents; design apps around specific intents and user personas.                                               |
|   9 | Tool descriptions act as system prompts; 57% of apps use negative constraints to prevent hallucinations or errors.                            |
|  10 | Error recovery and multi-turn context are important patterns in tool descriptions.                                                            |
|  11 | Let the model handle complex logic; multi-tool use can leverage the model’s context and memory for better results.                            |
|  12 | Design for both the UI widget and the appended text response; ensure they work together.                                                      |
|  13 | Control model responses to avoid speculation or undesired outputs.                                                                            |
|  14 | Design for conversation, not just single prompts; support multi-turn interactions and parameter updates.                                      |
|  15 | Only 7% of apps proactively design for multi-turn conversations.                                                                              |
|  16 | Testing in staging vs. live environments can yield up to 60% difference in behavior; test with realistic prompts at scale in the live client. |
|  17 | App distribution relies on both static (app store) and organic (prompt-based) discovery; optimize tool descriptions for visibility.           |
|  18 | One in seven app invocations fails; simpler apps with fewer, well-defined tools perform better.                                               |
|  19 | Key takeaways: understand the model/server/widget relationship, start with intent, optimize tool descriptions, and test live.                 |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=Km4ZZW0Aohc)
