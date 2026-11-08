---
layout: default
title: "Cut The Noise: Building a Code Reviewer You Can Trust - Joah Gerstenberg, Block, Inc"
nav_order: 11
parent: AGNTCon + MCPCon North America 2026
type: Video Note
description: "Joe Agershtenberg, a tech lead at Block, discusses the critical shift in software development where AI models now generate code that is often more reliable than human-written code, making automated..."
resource: "https://www.youtube.com/watch?v=f6OVURAlYXI"
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

Joe Agershtenberg, a tech lead at Block, discusses the critical shift in software development where AI models now generate code that is often more reliable than human-written code, making automated verification the new bottleneck.
He argues that traditional linters and tests are insufficient, necessitating intelligent verification systems that prioritize precision over recall to avoid overwhelming human reviewers with noisy, incorrect feedback.
Agershtenberg details Block’s approach, which involves using a multi-agent architecture with specialized reviewers and a centralized coordinator to filter out false positives, ensuring that only high-confidence, high-severity issues reach human attention.
To manage costs and risk, he introduces a risk-based routing system that directs code changes to appropriate levels of review based on their potential impact on security, privacy, and compliance.
Finally, he emphasizes the importance of aligning agents with broader business context and containment strategies before code is written, advocating for collaborative platforms that integrate product, design, and engineering early in the process to ensure trustworthy and aligned autonomous development.

# Main Points

|   # | Main point                                                                                                                                                           |
| --: | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | , AI models began generating code that could be trusted, shifting the bottleneck from code authorship to code verification.                                          |
|   2 | , human reviewers are now reviewing three times as many lines of code as a year ago, transforming code review from a craft into a ritual of trust.                   |
|   3 | ; reviewers should only post findings they are highly confident are valid.                                                                                           |
|   4 | (validity of findings), recall (completeness of findings), address rate, and post-merge fix rate.                                                                    |
|   5 | , such as GitHub Copilot, have high precision but low recall, missing up to 74% of potential findings in pull requests.                                              |
|   6 | % to 50%, though this approach is costly due to sequential large model usage.                                                                                        |
|   7 | , similar to Meta’s approach, allows teams to apply expensive reviews to high-risk changes (e.g., security, money movement) and cheaper reviews to low-risk changes. |
|   8 | , but the goal is to reduce the need for manual code reading through better agent alignment.                                                                         |
|   9 | , ensuring agents understand the big picture and potential pitfalls.                                                                                                 |

# Video

[![Video thumbnail](https://img.youtube.com/vi/f6OVURAlYXI/hqdefault.jpg)]("https://www.youtube.com/watch?v=f6OVURAlYXI")

[Watch on YouTube](https://www.youtube.com/watch?v=f6OVURAlYXI)
