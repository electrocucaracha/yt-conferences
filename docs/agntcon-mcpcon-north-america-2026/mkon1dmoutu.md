---
layout: default
title: "Context Is the Substrate: Production Patterns for... - Cassie Shum, Praxa, Inc"
nav_order: 24
parent: AGNTCon + MCPCon North America 2026
type: Video Note
description: "The speaker discusses how AI agents amplify existing organizational strengths and weaknesses, highlighting that enterprises often lack the engineering foundations necessary to leverage these tools ..."
resource: "https://www.youtube.com/watch?v=mkoN1DMoUTU"
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

The speaker discusses how AI agents amplify existing organizational strengths and weaknesses, highlighting that enterprises often lack the engineering foundations necessary to leverage these tools effectively.
To address this, the presentation outlines four key patterns for successful agent deployment: establishing a comprehensive context graph that includes architectural standards and product vision, maintaining a detailed agentic audit trail to track decisions and outcomes, reconciling the gap between initial intent and actual code reality, and ensuring visibility into system health to reduce inefficiencies.
The speaker emphasizes that agents require clear specifications, repeatable environments, and shared organizational context to avoid "AI slop" and excessive rework.
Ultimately, the goal is to close the widening gap between product and engineering teams by integrating fundamental software development practices with agentic workflows, ensuring that business outcomes, rather than just token usage, drive success.

# Main Points

|   # | Main point                                                                                                                                                                                              |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | # Key Points                                                                                                                                                                                            |
|   2 | • Speaker introduces context and context graphs, their relationship to agents, and patterns observed in production with clients                                                                         |
|   3 | • Speaker background: software developer, then architecture theorist, excited about agents enabling programming again; now helps enterprises implement agents efficiently                               |
|   4 | • Agents amplify organizational weaknesses and strengths; companies with poor engineering foundations struggle more with agent implementation than those with strong practices                          |
|   5 | • Three identified bottlenecks inhibiting AI impact: missing engineering fundamentals, teams creating agent fleets without organizational context, teams measuring activity instead of business results |
|   6 | • Gap widening between product and engineering organizations, exemplified by-product managers using outdated processes while developers have modern tools                                               |
|   7 | • Five pillars for closing product-engineering gap: specification drafting, iteration with specifications and context, testing/verification, fitness measurement                                        |
|   8 | • Two key loops: development cycle (idea → validation → development → testing → customer feedback) accelerated by agents; sharing context rapidly across teams                                          |
|   9 | • Four main patterns for effective agent implementation:                                                                                                                                                |
|  10 | : Share understanding across engineers, agents, product managers, customers, and business owners; include architectural standards, product vision, prior decisions, history, and dependencies           |
|  11 | : Track from idea through launch to customer reaction; feed insights back into context layer; document both paired work (with agent present) and unattended work (asynchronous tasks)                   |
|  12 | : Bridge gap between specification and actual code before and after implementation; ensure specification matches code execution                                                                         |
|  13 | : Monitor AI clutter through metrics like agent friction and technical health; use agent execution data to identify system inefficiencies                                                               |
|  14 | • Software factory requirements: attach work with specifications and acceptance criteria, create repeatable environments similar to production                                                          |
|  15 | • Agent retrospectives valuable: agents self-reflect after each execution on what they did, problems encountered, test steps, and decisions made                                                        |
|  16 | • Maturity levels for quality assurance: most teams at level one; progress toward end-to-end executions in realistic environments                                                                       |
|  17 | • Monday morning test ("steel thread"): pick small change, implement through entire system; if not possible, indicates need for pattern improvements                                                    |
|  18 | • Questions to evaluate agent effectiveness: frequency of agent-human communication, work rework, human intervention needs, context gaps                                                                |

# Video

[![Video thumbnail](https://img.youtube.com/vi/mkoN1DMoUTU/hqdefault.jpg)]("https://www.youtube.com/watch?v=mkoN1DMoUTU")

[Watch on YouTube](https://www.youtube.com/watch?v=mkoN1DMoUTU)
