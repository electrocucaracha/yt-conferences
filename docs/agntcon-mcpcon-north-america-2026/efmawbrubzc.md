---
layout: default
title: "Beyond Scraping: Building Agent-Ready Documentation Layers for MCP and... - Ayodeji Ogundare, Adyen"
nav_order: 9
parent: AGNTCon + MCPCon North America 2026
type: Video Note
description: 'The speaker from Idan’s developer relations team outlines their journey to make their documentation "agent-ready" by addressing the growing volume of AI bot traffic, which accounts for 11.6% of the...'
resource: "https://www.youtube.com/watch?v=efMAwbrUbZc"
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

The speaker from Idan’s developer relations team outlines their journey to make their documentation "agent-ready" by addressing the growing volume of AI bot traffic, which accounts for 11.6% of their requests.
They identified that traditional web designs optimized for human interaction hindered AI agents, who often struggled to discover relevant information and relied on outdated code snippets as absolute truth.
To solve this, the team implemented a four-layer strategy: adopting the LLM.txt standard for better discovery, serving all pages as structured Markdown for readability, enabling one-click local downloads for closed-source documentation to support offline access, and automating code snippet validation to ensure accuracy.
These efforts increased their code snippet compile pass rate from less than 1% to 92%, prioritizing accuracy over token efficiency to prevent AI hallucinations.
Looking ahead, the team plans to explore content negotiation, Web MCP for guided site discovery, and a unified knowledge base to further streamline how agents consume their documentation.

# Main Points

|   # | Main point                                                                                                                                                         |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   1 | # Key Points                                                                                                                                                       |
|   2 | • Speaker is IODG from developer relations team at IDN, working on making documentation agent-ready                                                                |
|   3 | • 11.6% of traffic to documentation came from AI bots/agents in 30 days (10+ million HTTP requests); 78% from user-directed assistants                             |
|   4 | • Developers now use AI agents to interact with documentation instead of reading it directly                                                                       |
|   5 | • Web and documentation were designed for humans, not agents—multiple design layers, buttons, accordions create challenges for AI parsing                          |
|   6 | • Less than 1% of code snippets compiled with latest SDKs before improvements                                                                                      |
|   7 | • AI agents treat documentation as source of truth; unlike humans, they don't recognize outdated or incorrect information                                          |
|   8 | • Four-layer approach implemented:                                                                                                                                 |
|   9 | : Adopted llm.txt standard to map site structure for agents                                                                                                        |
|  10 | : Made every page available in Markdown format with "last modified" metadata                                                                                       |
|  11 | : Enabled large-scale reading through local documentation download (10,000+ pages)                                                                                 |
|  12 | : Automated code snippet evaluation engine to ensure quality                                                                                                       |
|  13 | • Compilation success rate improved from <1% to 92%                                                                                                                |
|  14 | • Prioritized precision over token efficiency by including code snippets in all supported languages                                                                |
|  15 | • Next steps: content negotiation, evaluating other agent-readiness standards, exploring Web MCP, implementing unified knowledge language                          |
|  16 | • Recommendations: understand traffic patterns; generate Markdown natively; ensure documentation correctness; support local access for closed-source documentation |

# Video

[![Video thumbnail](https://img.youtube.com/vi/efMAwbrUbZc/hqdefault.jpg)](https://www.youtube.com/watch?v=efMAwbrUbZc)

[Watch on YouTube](https://www.youtube.com/watch?v=efMAwbrUbZc)
