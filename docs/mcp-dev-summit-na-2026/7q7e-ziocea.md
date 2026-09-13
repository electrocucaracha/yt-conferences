---
layout: default
title:
  "When MCP Isn’t Enough: Product Decisions Behind Scalable Agent Systems - Cansu
  Berkem, Datadog"
nav_order: 106
parent: Mcp Dev Summit Na 2026
type: Video Note
description:
  In this session, John Su, Product Director at Datadog, discusses the
  journey of turning AI agent prototypes into production-ready products, focusing
  on the development and deployment of Datadog’s Bits AI agent for on-call engineers.
  He emph...
resource: https://www.youtube.com/watch?v=7q7e_zioCEA
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

In this session, John Su, Product Director at Datadog, discusses the journey of turning AI agent prototypes into production-ready products, focusing on the development and deployment of Datadog’s Bits AI agent for on-call engineers.
He emphasizes that while building agents is now technically easier, the real challenges lie in product decisions around autonomy, risk, and user trust.
The team opted for a supervised autonomy model, allowing agents to investigate incidents but requiring human approval for actions, especially in high-risk or ambiguous scenarios.
They found that adaptive, hypothesis-driven reasoning outperformed fixed workflows, and transparency—such as surfacing uncertainty and providing clear feedback mechanisms—was crucial for user trust and product improvement.
Continuous feedback loops, careful experimentation with new models, and combining traditional ML with LLMs for different tasks were key strategies that enabled Bits to effectively assist thousands of engineers in real-world production environments.

# Main Points

|   # | Main point                                                                                                              |
| --: | ----------------------------------------------------------------------------------------------------------------------- |
|   1 | Session focuses on turning prototypes into production agents.                                                           |
|   2 | John Su is Product Director at Datadog, previously at Salesforce.                                                       |
|   3 | Key topics: autonomy, flexible reasoning, design for failure, transparency/trust, feedback loops, production readiness. |
|   4 | MCP made building AI agents easier with clean interfaces and fast iteration.                                            |
|   5 | Production environments require different considerations than prototyping.                                              |
|   6 | Datadog’s Bits product is an AI agent for on-call engineers, investigating alerts and surfacing root causes.            |
|   7 | Bits is used by 4,000 customers and tens of thousands of users, investigating thousands of alerts weekly.               |
|   8 | Scaling agents is now more about product decisions than engineering challenges.                                         |
|   9 | Autonomy is not binary; Bits uses a supervised approach—agent investigates, human approves actions.                     |
|  10 | Human involvement is required in high-risk or ambiguous environments (e.g., infra, payments, medical, security).        |
|  11 | Fully autonomous agents are suitable for low-risk, high-clarity tasks.                                                  |
|  12 | Initial fixed workflows failed in complex scenarios; adaptive, hypothesis-driven reasoning works better.                |
|  13 | Agents need to dynamically generate and test hypotheses, similar to engineers.                                          |
|  14 | Engineers can provide feedback and guide agents during investigations.                                                  |
|  15 | System surfaces uncertainty by marking investigations as conclusive or inconclusive, increasing trust.                  |
|  16 | Customers only pay for conclusive investigations.                                                                       |
|  17 | Frequent experimentation with new models is necessary, but readiness to roll back is crucial.                           |
|  18 | Transparency is enhanced by showing users the agent’s hypothesis tree and reasoning steps.                              |
|  19 | Feedback loops are vital; changing feedback options from “yes/no” to “no/not quite” improved actionable feedback.       |
|  20 | Continuous evaluation and feedback from users and internal engineers drive product improvement.                         |
|  21 | Combined LLMs for language/hypothesis reasoning with traditional ML for statistical analysis.                           |
|  22 | Key learnings: carefully shape autonomy, use flexible reasoning, surface uncerta Ratings (1-5): 4                       |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=7q7e_zioCEA)
