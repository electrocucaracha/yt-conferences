---
layout: default
title: "Who Tests the Testers? Making and Testing Pipelines - Evan Kohilas"
nav_order: 50
parent: PyCon US 2025
type: Video Note
description: 'In his talk "Who Tests the Testers," Evan Cohilas explores the critical challenge of ensuring reliability in CI/CD pipelines, arguing that platform teams often lack the testing infrastructure to pr...'
resource: "https://www.youtube.com/watch?v=DhognqFaRow"
youtube_stats:
  view_count: 979
  like_count: 14
  channel_subscriber_count: 34500
tags:
  - pycon-us-2025
  - video
  - learning
status: stable
generated:
  by: process:yt-summarizer-okf
  at: 2026-11-22T01:39:37+00:00
---

# Summary

In his talk "Who Tests the Testers," Evan Cohilas explores the critical challenge of ensuring reliability in CI/CD pipelines, arguing that platform teams often lack the testing infrastructure to prevent their own configuration errors.
He illustrates this with a real-world example where a simple typo in a GitLab pipeline’s rule set caused a job dependency failure, highlighting that while pipelines are treated as code, they are rarely subjected to the same rigorous testing standards as application code.
To address this gap, Cohilas presents five distinct techniques for validating pipeline configurations: using linting tools for syntax checks, running end-to-end pipelines before merging, executing jobs locally with simulators, applying static analysis through his custom tool "CI Test," and dynamically generating pipelines using Python libraries.
He emphasizes that no single method is universally superior; instead, teams should evaluate the pros and cons of each approach based on their specific complexity and needs.
Ultimately, Cohilas advocates for simplicity, suggesting that reducing unnecessary complexity in CI configurations is the most effective way to minimize human error and maintain robust, frictionless developer workflows.

# Main Points

|   # | Main point                                                                                                                                                           |
| --: | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | The talk addresses the problem of human errors in CI/CD pipeline configurations and asks who tests the testing infrastructure itself.                                |
|   2 | Pipelines are described as factory lines that automate setup, build, test, and deployment while acting as quality control gates.                                     |
|   3 | A common failure mode occurs when pipeline rules or dependencies contain typos or mismatches, causing jobs to fail unexpectedly.                                     |
|   4 | The speaker argues that pipeline configurations are often not treated like code, meaning they lack systematic testing and validation.                                |
|   5 | Linting tools such as GitLab’s Visual Studio Code extension, syntax checker, and visualizer help detect schema errors but may miss logic or dependency issues.       |
|   6 | Running end-to-end pipelines before merging can reveal integration problems but is slow, manual, and difficult to scale for complex rule sets.                       |
|   7 | Local execution tools like GitLab-CI-L local and GitLab CI-LO allow individual jobs to run in containers, speeding up feedback loops without full pipeline overhead. |
|   8 | Static analysis testing frameworks, such as the CI test tool, can generate snapshots and diffs of pipeline configurations to detect rule mismatches.                 |
|   9 | Dynamically generating pipelines using Python libraries like GitLab-CI-Python allows for code reuse, variables, and programmatic testing of pipeline logic.          |
|  10 | While generated pipelines do not automatically fix dependency errors, they enable the creation of shared change sets to prevent rule inconsistencies.                |
|  11 | The choice of testing method depends on pipeline complexity, with simple pipelines potentially requiring no additional tooling.                                      |
|  12 | Simplicity is emphasized as the key principle, suggesting that reducing configuration complexity is often more effective than adding more testing layers.            |
|  13 | The speaker encourages developers to question existing pipeline components and use the minimum necessary tools to achieve reliable automation.                       |

# Video

[![Video thumbnail](https://img.youtube.com/vi/DhognqFaRow/hqdefault.jpg)](https://www.youtube.com/watch?v=DhognqFaRow)

[Watch on YouTube](https://www.youtube.com/watch?v=DhognqFaRow)
