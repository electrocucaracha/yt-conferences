---
layout: default
title: "Is Your Agent Any Good? Lessons From a Wide and a... - Ethan Lo & Jason Jiang, Adaptive Security"
nav_order: 50
parent: AGNTCon + MCPCon North America 2026
type: Video Note
description: "Ethan and Jason from Adaptive Security presented two distinct AI agent deployments at Agent Conf, highlighting that both wide-scale internal enablement and deep product-specific pipelines require r..."
resource: "https://www.youtube.com/watch?v=y9dJET0EOvI"
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

Ethan and Jason from Adaptive Security presented two distinct AI agent deployments at Agent Conf, highlighting that both wide-scale internal enablement and deep product-specific pipelines require rigorous, ongoing evaluation.
Ethan detailed an automated support bot built by the customer success team, which initially relied on human feedback for quality control but suffered from user fatigue and silent degradation due to external tool changes; this led to the implementation of automated LLM-as-judge evaluations to ensure consistent performance.
Jason described the email security detection pipeline, where the team prioritized building a robust evaluation framework before developing the agent itself, allowing them to confidently test model changes and reduce costs while maintaining detection accuracy.
Both speakers emphasized that agents are software requiring continuous maintenance, monitoring, and iterative improvement, as performance can subtly degrade over time due to changing dependencies or data shifts.
The core takeaway is that evaluation is an ongoing operation rather than a one-time project, necessitating adaptive strategies like shadow testing, trace analysis, and automated judging to ensure agents remain reliable and effective in production environments.

# Main Points

|   # | Main point                                                                                                                                                             |
| --: | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | : Ethan and Jason from Adaptive Security presented two distinct AI agent deployments: broad internal AI enablement and a deep email security detection pipeline.       |
|   2 | : Both deployments followed four steps: finding opportunities/judges, building the agent, designing the evaluation loop, and iterative improvement.                    |
|   3 | (Ethan)**:                                                                                                                                                             |
|   4 | , researches customer questions via knowledge base and logs, and drafts responses for Customer Success Managers (CSMs).                                                |
|   5 | , not the AI team, highlighting the importance of domain experts building solutions.                                                                                   |
|   6 | /down on Slack, which eventually stopped due to user fatigue and lack of maintenance.                                                                                  |
|   7 | : Agents are software requiring continuous maintenance, monitoring, and alerting.                                                                                      |
|   8 | : External tool changes (e.g., MCP connectors adding new capabilities) can cause unexpected agent behavior (e.g., auto-sending emails).                                |
|   9 | : Replaced human feedback with an automated LLM-as-judge system comparing drafted responses to final sent responses to ensure ongoing quality.                         |
|  10 | (Jason)**:                                                                                                                                                             |
|  11 | (6 weeks) before writing product code.                                                                                                                                 |
|  12 | , repeatable experiments and scaling to a larger engineering team.                                                                                                     |
|  13 | , single-prompt LLMs, and agentic LLMs with tool calls to classify email as malicious or safe.                                                                         |
|  14 | : Saving and analyzing agent traces is essential because quantitative metrics alone are insufficient for LLMs.                                                         |
|  15 | , preventing false positives that offline tests missed.                                                                                                                |
|  16 | : Reduced false positive rate by ~80% and LLM cost per email by over two-thirds.                                                                                       |
|  17 | : Volume of emails outpaced human annotation capacity.                                                                                                                 |
|  18 | : Implemented sampled annotations, focusing analyst time on hard cases or safe emails to detect missed threats, and using multiple runs to handle LLM non-determinism. |
|  19 | :                                                                                                                                                                      |
|  20 | , not a one-time project.                                                                                                                                              |
|  21 | (e.g., expired auth tokens) rather than failing catastrophically, requiring constant monitoring.                                                                       |
|  22 | (R&D, Sales) due to limited team size and the high cost of maintenance.                                                                                                |
|  23 | (debate) and adopting new models quickly helps refine ground truth and performance.                                                                                    |

# Video

[![Video thumbnail](https://img.youtube.com/vi/y9dJET0EOvI/hqdefault.jpg)]("https://www.youtube.com/watch?v=y9dJET0EOvI")

[Watch on YouTube](https://www.youtube.com/watch?v=y9dJET0EOvI)
