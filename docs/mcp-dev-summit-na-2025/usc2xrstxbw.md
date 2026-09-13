---
layout: default
title:
  "[Session] Pragmatic Scaling of Enterprise GenAI with MCP with Sambhav Kothari
  at Bloomberg"
nav_order: 18
parent: Mcp Dev Summit Na 2025
type: Video Note
description:
  Sambukqari, head of AI productivity at Bloomberg, discusses the company's
  journey in scaling enterprise generative AI (GenAI) development. He outlines Bloomberg's
  vast operational scale and longstanding AI expertise, noting that the main ch...
resource: https://www.youtube.com/watch?v=usc2XRStxbw
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

Sambukqari, head of AI productivity at Bloomberg, discusses the company's journey in scaling enterprise generative AI (GenAI) development.
He outlines Bloomberg's vast operational scale and longstanding AI expertise, noting that the main challenge was not building demos but transitioning applications from demo to production due to complex workflows and bottlenecks.
By adopting standardized protocols and aligning with the open MCP standard, Bloomberg enabled interoperability, loose coupling, and rapid integration of tools and agents, allowing over 9,000 engineers to contribute effectively.
This transformation reduced productionization time from weeks to minutes and fostered a dynamic ecosystem where tools and agents reinforce each other.
While this shift brought new challenges in tool management and governance, Bloomberg is committed to open-source collaboration to address these issues and continue advancing GenAI at scale.

# Main Points

|   # | Main point                                                                                                                                            |
| --: | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Sambukqari is the head of AI productivity at Bloomberg's AI engineering group, leading internal GenAI and ML platform teams.                          |
|   2 | Bloomberg operates at massive scale: 2.5 million documents, 1.5 billion messages, and 400 billion structured data points ingested daily.              |
|   3 | Bloomberg has over 25,000 employees, including 9,500+ engineers and 350 AI researchers.                                                               |
|   4 | AI has been used at Bloomberg for over 15 years, starting with news sentiment analysis in 2009 and neural networks for news discovery in 2020.        |
|   5 | GenAI development at Bloomberg revealed complex workflows with many stakeholders and handoff points.                                                  |
|   6 | The main bottleneck was transitioning applications from demos to production, not building demos themselves.                                           |
|   7 | Productionization gap slowed velocity; demos could be built in days, but productionization took weeks or months.                                      |
|   8 | Hypothesis: First-class support for AI integration-ready APIs, discoverability, and well-defined integration points would speed up productionization. |
|   9 | Protocols enable dependency inversion, interoperability, easy integration, and loose coupling at scale.                                               |
|  10 | Standardizing LLM APIs on the OpenAI API standard allowed easy swapping between LLMs/providers.                                                       |
|  11 | Tools were identified as the missing piece for scalable agent development; making tools config-driven enabled rapid agent creation.                   |
|  12 | Bloomberg developed internal tools protocol infrastructure before MCP was publicized.                                                                 |
|  13 | MCP (Model Component Protocol) aligned with Bloomberg’s approach and was adopted as an open standard.                                                 |
|  14 | MCP adoption enabled plug-and-play interoperability, both internally and with external agentic systems.                                               |
|  15 | Wide MCP adoption led to tool sprawl, discoverability, and governance challenges.                                                                     |
|  16 | Bloomberg is building a scalable internal registry of tools with metadata, usage policies, access control, and observability.                         |
|  17 | Middleware handles identity, access control, and observability; secrets and tokens are abstracted from developers.                                    |
|  18 | Over 9,000 engineers can now contribute to GenAI dev                                                                                                  |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=usc2XRStxbw)
