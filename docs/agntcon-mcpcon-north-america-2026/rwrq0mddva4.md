---
layout: default
title: "Gotta Catch 'Em All: Agent Skills - Lizzie Siegle, Entire"
nav_order: 154
parent: AGNTCon + MCPCon North America 2026
type: Video Note
description: 'This presentation, titled "Gotta Catch Them All: Agent Skills," explores the concept of "skills" as reusable folders containing instructions and supporting files that guide AI agents through specif...'
resource: "https://www.youtube.com/watch?v=rWrQ0MddvA4"
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

This presentation, titled "Gotta Catch Them All: Agent Skills," explores the concept of "skills" as reusable folders containing instructions and supporting files that guide AI agents through specific tasks, such as code review or CI debugging.
The speaker argues that a skill is only worth keeping if it addresses a repetitive task where the agent might otherwise lack context or consistency, emphasizing that skills should define clear goals, constraints, and evidence requirements rather than prescribing every single action.
The talk introduces a practical framework for evaluating skills by testing them against various failure modes, including missing tools, outdated guidance, and irrelevant tasks, to ensure they provide useful boundaries and actionable feedback.
A significant portion of the discussion focuses on integrating these skills with Entire, a platform that links agent conversations to Git commits, allowing developers to recover the "why" behind code changes by tracing decisions back to their original agent sessions.
By combining the procedural guidance of skills with the historical context provided by Entire, developers can better understand the intent behind complex code logic, such as specific retry mechanisms, and make informed decisions about whether to modify or preserve existing behaviors.

# Main Points

|   # | Main point                                                                                                                                                              |
| --: | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | `skill.md` file with instructions and supporting files, providing agents with a repeatable procedure instead of requiring repeated manual explanations.                 |
|   2 | , offering a clear task, checkable results, and defined responses for missing information or failures.                                                                  |
|   3 | , references for specific situational details (e.g., auth guides), and assets for output formatting (e.g., templates).                                                  |
|   4 | , constraints, and evidence while allowing agent adaptability; vague descriptions hinder skill selection.                                                               |
|   5 | , tools perform actions, and the environment controls permissions; instructions do not grant execution rights.                                                          |
|   6 | , test it with unrelated tasks, missing dependencies, outdated guidance, and retrieved content containing external orders to ensure robustness.                         |
|   7 | , enabling the recovery of decision-making context ("why") that commits alone do not provide ("what").                                                                  |
|   8 | , such as limiting retries to GET requests to prevent duplicate orders.                                                                                                 |
|   9 | "Search," "Explain," and "What Happened" help agents trace decisions, inspect diffs, and verify that code changes align with recorded reasoning.                        |
|  10 | ’s value involves comparing performance with and without the skill, checking if cited sources support claims, and measuring corrections, elapsed time, and token usage. |
|  11 | ; they should be versioned, linked to current documentation, and rerun against saved examples to catch regressions when commands or conventions change.                 |
|  12 | , defining a checkable result, and specifying agent behavior when stuck, then iteratively improve the skill based on inspection of results.                             |

# Video

[![Video thumbnail](https://img.youtube.com/vi/rWrQ0MddvA4/hqdefault.jpg)](https://www.youtube.com/watch?v=rWrQ0MddvA4)

[Watch on YouTube](https://www.youtube.com/watch?v=rWrQ0MddvA4)
