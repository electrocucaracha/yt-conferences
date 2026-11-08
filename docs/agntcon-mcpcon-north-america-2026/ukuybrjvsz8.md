---
layout: default
title: "The Agentic SDLC: How We Shipped AI-Native Software at a Legacy... - Austin Brown, A Place for Mom"
nav_order: 40
parent: AGNTCon + MCPCon North America 2026
type: Video Note
description: "Austin Brown, a principal engineer at A Place for Mom, presents a framework for an Agentic Software Development Life Cycle (SDLC) that integrates AI tools like Claude and Codex into daily engineeri..."
resource: "https://www.youtube.com/watch?v=UKuYBrJVsz8"
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

Austin Brown, a principal engineer at A Place for Mom, presents a framework for an Agentic Software Development lifecycle (SDLC) that integrates AI tools like Claude and Codex into daily engineering workflows.
He argues that AI coding is not a "cheat code" that diminishes fulfillment but rather a powerful tool that requires fluency, broad team access, and strict alignment through OKRs to prevent miscommunication.
To manage the increased velocity and volume of code generation, his team implemented a centralized MCP server for unified access to tools like Jira and GitHub, alongside a shared skills marketplace and weekly demos to foster knowledge sharing.
A critical innovation was the introduction of a risk-rating system for pull requests, which allows low-risk changes to be auto-merged, reducing median merge time by 69% and alleviating review bottlenecks.
However, Brown highlights the challenge of "comprehension debt," where the sheer volume of AI-generated code makes it difficult for humans to track all changes, leading him to advocate for focusing on design patterns, interfaces, and human-documented intent as the source of truth to maintain code quality and team alignment.

# Main Points

|   # | Main point                                                                                                                                                         |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   1 | :** AI coding is a tool for fulfillment, not a "cheat code" that removes the joy of building products.                                                             |
|   2 | :** Engineers need tool proficiency, fluency (knowing when to use/not use AI), and access to tools.                                                                |
|   3 | :** Teams require broad tool access, short feedback loops, and strict alignment via OKRs to prevent drift caused by high-speed AI development.                     |
|   4 | :** Built to democratize access to Jira, GitHub, observability, analytics, and SSO for all roles (engineering, product, design).                                   |
|   5 | :** Human-documented intent (e.g., whiteboards, PRDs) must remain the source of truth to prevent AI agents from inventing work or drifting from goals.             |
|   6 | :** Implemented a 10-agent review system using multiple models to identify blocking and "should fix" findings.                                                     |
|   7 | :** Bypassed human review for low-risk changes based on file patterns (e.g., Terraform is high risk, readme is low) and LLM judgment.                              |
|   8 | :** Reduced median time-to-merge from 28 hours to 8.5 hours (69% reduction) within five weeks by auto-merging low-risk PRs.                                        |
|   9 | :** Optimized ticketing to identify parallel tasks, allowing engineers to spawn sub-agents for independent work and avoid dependency chains.                       |
|  10 | :** Added strict rules to tickets (e.g., "do not proceed if links are inaccessible") to prevent AI hallucinations and drift from acceptance criteria.              |
|  11 | :** Created skills to proactively monitor feature flags and A/B tests, generating tickets or PRs for issues without human intervention.                            |
|  12 | :** Implemented guardrails in system prompts to ignore nitpicks and non-existent bugs, focusing only on code that is safer, faster, or clearer.                    |
|  13 | :** Acknowledged that the volume of AI-generated code makes it impossible for humans to review every line, necessitating a shift in review strategy.               |
|  14 | :** Shifted focus to interfaces and design patterns (e.g., Hexagonal Architecture) to allow agents to handle implementation details while humans review contracts. |
|  15 | :** Delegated heavy testing and local environment orchestration to GitHub Actions and Docker to manage token costs and memory constraints.                         |
|  16 | :** Worked with a dedicated developer platform team for foundational infrastructure, using metadata linking (Jira/Confluence) to connect artifacts.                |

# Video

[![Video thumbnail](https://img.youtube.com/vi/UKuYBrJVsz8/hqdefault.jpg)]("https://www.youtube.com/watch?v=UKuYBrJVsz8")

[Watch on YouTube](https://www.youtube.com/watch?v=UKuYBrJVsz8)
