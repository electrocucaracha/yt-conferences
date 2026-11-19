---
layout: default
title: "Should This Be an AI Agent? A Product Framework for Enterprise Adoption - Takeshwari Kamal, Uber"
nav_order: 54
parent: AGNTCon + MCPCon North America 2026
type: Video Note
description: "Takshwari, a Product Manager at Uber with a background in AI engineering at Google, presents a product-focused framework for developing AI applications, emphasizing the critical need to validate pr..."
resource: "https://www.youtube.com/watch?v=O7czSnUtZ14"
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

Takshwari, a Product Manager at Uber with a background in AI engineering at Google, presents a product-focused framework for developing AI applications, emphasizing the critical need to validate problem-solution fit before building.
She argues that many customer issues, such as resolving late package deliveries, are better addressed by simple automations or fixed workflows rather than complex AI agents, which should only be deployed when reasoning over infinite options is required.
The talk outlines a rigorous decision-making process that includes defining the target user, establishing strict guardrails to limit an agent’s "blast radius," and utilizing "shadow mode" to test AI recommendations against human decisions without direct customer impact.
Key considerations for scaling include analyzing cost-efficiency compared to human labor, managing latency through model hosting strategies, and ensuring high precision thresholds—typically 80–90%—for actions with financial or customer-facing consequences.
Finally, she highlights the importance of measuring long-term customer sentiment and adoption by closely collaborating with support teams and engineers, noting that AI agents can sometimes outperform humans in consistency and contextual understanding, but must be deployed with careful monitoring to maintain trust and reliability.

# Main Points

|   # | Main point                                                                                                                                                                                                                 |
| --: | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | : Takshwari is a Product Manager at Uber with a background in AI engineering, having worked at Google (Ads and DeepMind) and completed a master’s in AI research in 2018.                                                  |
|   2 | : The session is product-focused rather than technical, aiming to help audiences find the right product to build before investing in development, using a framework combining Anthropic, OpenAI, and Google methodologies. |
|   3 | : Most users prefer human interaction over AI agents for resolving issues like late orders, indicating a significant adoption barrier for AI customer service.                                                             |
|   4 | : An agent uses a model to choose actions, make tool calls, observe results, and adapt within set guardrails.                                                                                                              |
|   5 | :                                                                                                                                                                                                                          |
|   6 | : Rules decide every step; measurable and trackable.                                                                                                                                                                       |
|   7 | : Steps are recorded; suitable for compliance or credit approval; may use LLMs at specific steps.                                                                                                                          |
|   8 | : The model decides the next action; requires reasoning; suitable for infinite option universes.                                                                                                                           |
|   9 | :                                                                                                                                                                                                                          |
|  10 | ?** Identify beneficiaries (e.g., shopper, support rep).                                                                                                                                                                   |
|  11 | ?** Define capabilities and failure points.                                                                                                                                                                                |
|  12 | ?** Determine if a workflow suffices instead of an agent.                                                                                                                                                                  |
|  13 | ?** Ensure the solution holds up at volume.                                                                                                                                                                                |
|  14 | ?** Assess timing and potential for improvement.                                                                                                                                                                           |
|  15 | ?** Verify if it worked.                                                                                                                                                                                                   |
|  16 | : Missing Package**:                                                                                                                                                                                                       |
|  17 | : Help shoppers reach correct resolution with less effort.                                                                                                                                                                 |
|  18 | : Start with one market, one customer type, and one problem (missing package).                                                                                                                                             |
|  19 | : Map data from siloed systems (records, user info, payments) using MCPs (Model Context Protocol) to overcome bottlenecks.                                                                                                 |
|  20 | : Set a "blast radius" for agent decisions (e.g., time and call budgets).                                                                                                                                                  |
|  21 | : Initially, the AI drafts recommendations for human reps to accept/reject, measuring precision before full autonomy.                                                                                                      |
|  22 | : Prevent agents from issuing refunds or touching other customers without human approval.                                                                                                                                  |
|  23 | : Scenarios with conflicting evidence (e.g., photo proof of delivery vs. customer claim) require additional signals like user history and refund frequency to make fair decisions.                                         |
|  24 | :                                                                                                                                                                                                                          |
|  25 | : ~$5 per case.                                                                                                                                                                                                            |
|  26 | : ~$1.60 per case.                                                                                                                                                                                                         |
|  27 | : ~$0.80 per case.                                                                                                                                                                                                         |
|  28 | : Start with hybrid models to reduce cost while ensuring quality, then move to full automation as precision improves.                                                                                                      |
|  29 | :                                                                                                                                                                                                                          |
|  30 | (images, audio, text) and API rate limits.                                                                                                                                                                                 |
|  31 | : Hosting/fine-tuning own models offers better version control and prevents performance degradation from provider updates.                                                                                                 |
|  32 | : Use open-source or smaller models for simple tasks (e.g., checking delivery status) to reduce costs.                                                                                                                     |
|  33 | :                                                                                                                                                                                                                          |
|  34 | : Offline tests, human reviews, and LLM-as-a-judge evaluations.                                                                                                                                                            |
|  35 | : Underrated method to measure precision by comparing AI and human resolutions.                                                                                                                                            |
|  36 | : AI agents can be more stable and logical than humans, who may be swayed by exceptions.                                                                                                                                   |
|  37 | : AI can process audio nuances and cultural context (e.g., identifying specific item types) better than humans.                                                                                                            |
|  38 | : Aim for 80–90% precision for cases with direct customer impact or financial consequences.                                                                                                                                |
|  39 | :                                                                                                                                                                                                                          |
|  40 | ; roll back if sentiment degrades.                                                                                                                                                                                         |
|  41 | :                                                                                                                                                                                                                          |
|  42 | :                                                                                                                                                                                                                          |
|  43 | (e.g., documentation time).                                                                                                                                                                                                |

# Video

[![Video thumbnail](https://img.youtube.com/vi/O7czSnUtZ14/hqdefault.jpg)](https://www.youtube.com/watch?v=O7czSnUtZ14)

[Watch on YouTube](https://www.youtube.com/watch?v=O7czSnUtZ14)
