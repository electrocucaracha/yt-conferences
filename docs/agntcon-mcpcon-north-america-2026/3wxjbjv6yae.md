---
layout: default
title: "Beyond Pass/Fail: Measuring the Full Agent Experience - Sean Roberts, Netlify"
nav_order: 144
parent: AGNTCon + MCPCon North America 2026
type: Video Note
description: 'Shawn Roberts, VP of Applied AI at Netlify, argues that traditional pass/fail evaluations are insufficient for measuring the quality of MCP servers and the broader "Agent Experience" (AX).'
resource: "https://www.youtube.com/watch?v=3wXJbjV6YAE"
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

Shawn Roberts, VP of Applied AI at Netlify, argues that traditional pass/fail evaluations are insufficient for measuring the quality of MCP servers and the broader "Agent Experience" (AX).
He introduces Axis, an open-source tool that moves beyond simple success metrics by analyzing the entire lifecycle of an agent’s task, including tool discovery, execution, and error handling.
Axis evaluates performance across four distinct dimensions—goal achievement, environment, service, and agent behavior—to help developers identify whether failures stem from their own service, the surrounding environment, or the agent itself.
By running controlled scenarios with various agent configurations, such as different tool counts or CLI setups, the tool provides actionable insights into specific bottlenecks rather than just a binary result.
Roberts emphasizes that this granular observability is critical for business-critical features like MCP, allowing teams to make data-driven improvements and distinguish between issues they can fix and those caused by external factors like agent updates or environment constraints.

# Main Points

|   # | Main point                                                                                                                                                                       |
| --: | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | , VP of Applied AI at Netlify, presents on measuring Agent Experience (AX), a discipline focused on the end-to-end experience of agents working with services.                   |
|   2 | ; however, MCP is only one component of AX, which also includes skills, CLIs, and documentation.                                                                                 |
|   3 | (evals) often provide only binary pass/fail results, missing critical details such as tool call frequency, error recovery, and environmental issues.                             |
|   4 | "Axis," a free open-source tool that moves beyond binary checks by analyzing the entire agent journey through specific scenarios.                                                |
|   5 | : goal achievement, environment stability, service quality, and agent behavior.                                                                                                  |
|   6 | , call weight, success rate, and speed, allowing for precise identification of bottlenecks.                                                                                      |
|   7 | , MCP is the highest-converting channel for sign-ups to paid plans, making AX a business-critical priority rather than just a technical feature.                                 |
|   8 | , then run variants to test different configurations (e.g., MCP vs. CLI vs. Skills).                                                                                             |
|   9 | , contrary to previous assumptions.                                                                                                                                              |
|  10 | ; frequent agent updates can alter behavior, such as preferring web search over web fetch, which impacts how documentation is consumed.                                          |
|  11 | (DX) practices, such as automatic CLI updates, can break autonomous agent workflows, highlighting the need for distinct AX testing.                                              |
|  12 | /CD pipelines to run recurring evaluations, helping teams distinguish between issues caused by their service versus external factors like agent bugs or environment constraints. |
|  13 | ’s control.                                                                                                                                                                      |
|  14 | , agent error hooks, and user feedback, combined with offline evaluations to validate changes before deployment.                                                                 |
|  15 | , teams can determine if a regression is due to their service, the environment, or the agent itself, enabling targeted fixes and partner outreach when necessary.                |

# Video

[![Video thumbnail](https://img.youtube.com/vi/3wXJbjV6YAE/hqdefault.jpg)](https://www.youtube.com/watch?v=3wXJbjV6YAE)

[Watch on YouTube](https://www.youtube.com/watch?v=3wXJbjV6YAE)
