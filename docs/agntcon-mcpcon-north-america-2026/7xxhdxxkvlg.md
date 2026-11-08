---
layout: default
title: "Keynote: Building the Git Forge of the Future - Thomas Dohmke, Entire"
nav_order: 116
parent: AGNTCon + MCPCon North America 2026
type: Video Note
description: "The speaker argues that the rapid adoption of AI coding agents has fundamentally disrupted the traditional software development lifecycle, creating a critical gap between the volume of generated co..."
resource: "https://www.youtube.com/watch?v=7XXHDXxkvLg"
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

The speaker argues that the rapid adoption of AI coding agents has fundamentally disrupted the traditional software development lifecycle, creating a critical gap between the volume of generated code and human comprehension.
With data showing a significant increase in pull requests and code changes, developers often face pressure to approve AI-generated work without fully understanding it, leading to a loss of trust in the review process.
To address this, the speaker proposes storing agent session logs as Git objects, linking them directly to code commits to preserve the intent and decision-making context behind changes.
Furthermore, the talk advocates for decentralized, distributed infrastructure to handle the scaling demands of agentic workflows, mirroring the ethos of Git and Linux to ensure resilience and developer freedom.
Ultimately, the vision is not to replace developers with agents, but to empower them to ship creative ideas without the bottlenecks of traditional centralized systems.

# Main Points

|   # | Main point                                                                                                                                                                                                      |
| --: | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | , with over 35 years of coding experience, highlights the shift from manual coding to using AI agents that generate code rapidly, often resulting in a gap between the speed of output and human understanding. |
|   2 | , significantly increasing the volume of work moving through the system.                                                                                                                                        |
|   3 | , causing the review queue to grow in both the number of changes and the amount of code within those changes.                                                                                                   |
|   4 | "YOLO merging," where developers approve AI-generated code without thorough review due to pressure, lack of time, or inability to understand the diff, leading to potential quality risks.                      |
|   5 | (SDLC), including DevOps and Agile, was designed around human-centric loops for writing, building, testing, and observing code.                                                                                 |
|   6 | , the challenge is ensuring that the original human intent travels with the code, as the agent may not fully capture the context or reasoning behind decisions.                                                 |
|   7 | ; the editor is now often a fallback, while new interfaces like terminal-based agents (e.g., Cloud Code, Codex) are becoming standard.                                                                          |
|   8 | , which contain the thought process, rejected approaches, and decision-making steps, are as valuable as the code itself for understanding intent and providing evidence during code reviews.                    |
|   9 | , linking them to commits via "checkpoints" to create a transparent history that allows teams to time-travel and verify that the diff matches the original intent.                                              |
|  10 | , as shown by Cloud Code and GitHub data, creates a bottleneck where human review capacity cannot keep up with AI output speed.                                                                                 |
|  11 | ; the speaker advocates for distributed and decentralized infrastructure, similar to the ethos of Git and Linux, to support global, diverse teams.                                                              |
|  12 | , control over data location, and independence, aligning with the open-source ethos and supporting the "largest team sport on Earth."                                                                           |
|  13 | , rate limits, or excessive process overhead.                                                                                                                                                                   |
|  14 | "agentic assembly line" where developers use agents to realize their biggest ideas, maintaining their role as the primary creators.                                                                             |

# Video

[![Video thumbnail](https://img.youtube.com/vi/7XXHDXxkvLg/hqdefault.jpg)]("https://www.youtube.com/watch?v=7XXHDXxkvLg")

[Watch on YouTube](https://www.youtube.com/watch?v=7XXHDXxkvLg)
