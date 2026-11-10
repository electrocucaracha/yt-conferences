---
layout: default
title: "Part Man. Part Machine. All Open Source - Russell Spitzer, Snowflake"
nav_order: 90
parent: AGNTCon + MCPCon North America 2026
type: Video Note
description: "Russell Spitzer, a PMC for Apache projects like Iceberg and Polaris, argues that while LLMs have drastically reduced the cost of code generation, they currently lack the decision-making capabilitie..."
resource: "https://www.youtube.com/watch?v=ZobgRrhgmCM"
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

Russell Spitzer, a PMC for Apache projects like Iceberg and Polaris, argues that while LLMs have drastically reduced the cost of code generation, they currently lack the decision-making capabilities necessary for effective open source maintenance.
He highlights specific issues where AI agents fail to understand historical context, such as removing "Chesterton’s fences" or generating irrelevant security reports, which burdens maintainers with low-value pull requests.
Drawing an analogy to "centaur chess," Spitzer posits that the optimal workflow involves humans guiding AI tools, as human judgment combined with machine speed outperforms either alone.
To implement this, he describes a multi-agent review system that filters and prioritizes pull requests, ensuring that only high-quality, context-aware code reaches human maintainers.
Ultimately, he urges developers to remain actively involved in the review process, emphasizing that open source thrives on human collaboration and that agents should assist rather than replace the human decision-making loop.

# Main Points

|   # | Main point                                                                                                                                                                                                                                                              |
| --: | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | : Russell Spitzer, PhD in computational biology, PMC for Apache Iceberg, Polaris, Magpie, and Oozie.                                                                                                                                                                    |
|   2 | & LLMs**: LLMs have significantly impacted puzzle-solving competitions. In 2024, Claude 3.5 solved 14/20 easy problems; in 2025, advanced models solved all difficult problems instantly, removing differentiation between human and machine performance.               |
|   3 | : This shift has caused professional turmoil, leading to a "stages of grief" process regarding the role of engineers in the age of AI.                                                                                                                                  |
|   4 | : Creating code is now very cheap, evidenced by a doubling of pull requests in Apache Iceberg after the release of Opus. However, agents are currently poor at making high-level decisions, such as determining if a PR adds value or identifying true security issues. |
|   5 | :                                                                                                                                                                                                                                                                       |
|   6 | (e.g., flagging test classes or specification capabilities as vulnerabilities).                                                                                                                                                                                         |
|   7 | "Chesterton’s fences" (code existing for correctness, not performance) without understanding the historical context.                                                                                                                                                    |
|   8 | , nonsense comments that mislead future agents, and expand public API surface area unnecessarily.                                                                                                                                                                       |
|   9 | "Centaur" Model**: Drawing from Kasparov’s centaur chess, the most effective approach is a human-machine partnership where the human provides superior decision-making and process management, outperforming either a strong human or a strong AI alone.                |
|  10 | :                                                                                                                                                                                                                                                                       |
|  11 | : Spitzer uses a multi-agent system with specialized profiles (correctness, architecture, testing, style, process) to review PRs.                                                                                                                                       |
|  12 | : An additional agent challenges the initial reviews to reduce false positives.                                                                                                                                                                                         |
|  13 | : A final model condenses findings, but a human must review and decide which comments to propagate to the PR submitter.                                                                                                                                                 |
|  14 | : The focus is shifting from line-by-line code inspection to reviewing the provenance of the PR (prompts used, purpose, architectural intent).                                                                                                                          |
|  15 | : Apache Magpie uses AI skills to automate the handling of security reports, setting up private repositories and tracking issues, which helps manage the volume of reports that overwhelm traditional mailing list processes.                                           |
|  16 | :                                                                                                                                                                                                                                                                       |
|  17 | (e.g., reordering functions).                                                                                                                                                                                                                                           |

# Video

[![Video thumbnail](https://img.youtube.com/vi/ZobgRrhgmCM/hqdefault.jpg)](https://www.youtube.com/watch?v=ZobgRrhgmCM)

[Watch on YouTube](https://www.youtube.com/watch?v=ZobgRrhgmCM)
