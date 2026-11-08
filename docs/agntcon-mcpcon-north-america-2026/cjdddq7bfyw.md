---
layout: default
title: "Securing the Agentic Universe, One Layer at a Time - Aidan Sochowski, Runlayer"
nav_order: 87
parent: AGNTCon + MCPCon North America 2026
type: Video Note
description: "A founding engineer at RunLayer explains how their AI control plane helps enterprises monitor and govern the use of AI agents, addressing the fragmented nature of current monitoring solutions."
resource: "https://www.youtube.com/watch?v=cjdDDq7bfYw"
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

A founding engineer at RunLayer explains how their AI control plane helps enterprises monitor and govern the use of AI agents, addressing the fragmented nature of current monitoring solutions.
The speaker highlights internal findings from RunLayer’s 50-person team, which revealed approximately 300 untracked agents, tens of millions of weekly tool calls, and 24 billion unmonitored tokens, indicating significant "shadow AI" usage and inefficiencies.
To mitigate risks such as prompt injection, data exfiltration, and agent drift, the company implements layered defenses including pre-execution policy checks, real-time scanners for PII and malicious content, and probabilistic models to detect deviations from intended tasks.
Specific incidents, such as a customer support agent leaking data via email and a PR approval bot being manipulated by user context, demonstrate the necessity of strict identity scoping, fine-grained permissions, and continuous observability.
Ultimately, the presentation argues that while no single solution is perfect, combining deterministic rules with advanced monitoring is essential for balancing employee autonomy with security and cost control in enterprise AI environments.

# Main Points

|   # | Main point                                                                                                                                              |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | , MDM solutions on user devices, browser traffic analysis, and cloud agent telemetry.                                                                   |
|   2 | , classifying these as "shadow" AI usage.                                                                                                               |
|   3 | , specific actions, and session context before execution to prevent over-provisioned access.                                                            |
|   4 | , credentials, and known bad phrases to mitigate immediate risks.                                                                                       |
|   5 | , such as LLM-as-a-judge or decision models, can detect agent drift and nuanced issues but suffer from high latency and susceptibility to manipulation. |
|   6 | , highlighting the need for deterministic guardrails.                                                                                                   |
|   7 | (e.g., a resume screener writing to Google Docs) create contamination risks if external data is not properly siloed.                                    |
|   8 | , such as a recruiting agent with unnecessary access to Git runbooks, pose security risks even if they do not actively misuse those permissions.        |
|   9 | , requiring monitoring of retry rates and service protection.                                                                                           |
|  10 | , as switching to more expensive models without proper budgeting can significantly increase operational expenses.                                       |
|  11 | ; enterprises must balance strict rules with usability while using monitoring to mitigate risk and detect anomalies.                                    |

# Video

[![Video thumbnail](https://img.youtube.com/vi/cjdDDq7bfYw/hqdefault.jpg)]("https://www.youtube.com/watch?v=cjdDDq7bfYw")

[Watch on YouTube](https://www.youtube.com/watch?v=cjdDDq7bfYw)
