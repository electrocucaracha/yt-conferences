---
layout: default
title: "It's 2030. What Does Prow Look Like? - Petr Muller, Red Hat"
nav_order: 10
parent: "Maintainer Summit 2026 - Europe"
type: Video Note
description: "Peter, a maintainer of Prow, presents a critical assessment of the project’s current state, acknowledging that while it remains essential for Kubernetes’ CI/CD, GitHub automation, and policy enforc..."
resource: "https://www.youtube.com/watch?v=u5B27TaTwNM"
tags:
  - maintainer-summit-2026-europe
  - video
  - learning
status: stable
generated:
  by: process:yt-summarizer-okf
  at: 2026-11-16T15:59:05+00:00
---

# Summary

Peter, a maintainer of Prow, presents a critical assessment of the project’s current state, acknowledging that while it remains essential for Kubernetes’ CI/CD, GitHub automation, and policy enforcement, it faces significant challenges due to its age and the rapid evolution of the broader ecosystem.
He explains that Prow was built to solve specific Kubernetes problems in the late 2010s, often pioneering features like code ownership and automated merging before they became mainstream, but the project has struggled to keep pace with modern tools like GitHub Actions and Tekton, which offer easier setup, better integration, and advanced pipeline capabilities.
The talk highlights that Prow’s contribution activity has declined, partly because maintaining backward compatibility and complex legacy code deters new contributors, while the world around it has shifted toward more user-friendly, cloud-native, and secure CI solutions.
Despite these issues, the community emphasizes that Prow’s core functions—particularly granular permission management and large-scale CI execution—remain indispensable, as alternatives like GitHub Actions often lack the necessary security controls or scalability for Kubernetes’ specific needs.
The session concludes with a discussion on potential future directions, suggesting that Prow might evolve by delegating specific tasks, such as pipeline execution, to other systems like Tekton or GitHub Actions, while retaining its role as a coordination and permission proxy layer to ensure the project remains viable and relevant for the next decade.

# Main Points

|   # | Main point                                                                                                                                                                            |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Prow is a Kubernetes CI system originally built for the Kubernetes project that provides GitHub automation, policy enforcement, and chat operations.                                  |
|   2 | The Kubernetes community depends heavily on Prow for interpreting owners files, assigning reviewers, enforcing permissions, and automatically merging pull requests via Tide.         |
|   3 | Prow manages over 90 repositories across the Kubernetes and sig organizations, handling CI job execution, result reporting, and artifact inspection.                                  |
|   4 | Many Prow features, such as code ownership and automatic merging, were implemented before similar capabilities became mainstream in GitHub or other platforms.                        |
|   5 | The project has experienced a significant slowdown in contributions since 2020, with most foundational code built between 2017 and 2020.                                              |
|   6 | GitHub Actions and Tekton have evolved to offer features like reusable workflows and pipelines that Prow currently lacks or implements with greater complexity.                       |
|   7 | GitHub's evolving permission models, such as rule sets and branch protection, create integration challenges for Prow's Tide merge queue and ownership enforcement.                    |
|   8 | Security concerns have increased for CI systems due to supply chain attack risks, making modern maintenance more difficult than in the past.                                          |
|   9 | The project faces challenges in attracting new contributors due to the high complexity of remaining tasks and the requirement for strict backward compatibility.                      |
|  10 | Despite the slowdown, Prow remains functional and is valued by external projects for its ability to scale CI across multiple repositories with independent release cycles.            |
|  11 | Community discussion suggests that Prow should focus on acting as a coordination and permissions proxy layer rather than competing directly with GitHub Actions for basic CI tasks.   |
|  12 | There is interest in delegating complex pipeline execution to external systems like Tekton or GitHub Actions while retaining Prow's core governance and automation features.          |
|  13 | Some organizations prefer Prow over GitHub Actions due to better security controls and the ability to manage granular permissions without exposing enterprise-wide risks.             |
|  14 | The future of Prow may involve integrating with modern forge features and external CI tools to reduce maintenance burden while preserving its unique value in open source governance. |

# Video

[![Video thumbnail](https://img.youtube.com/vi/u5B27TaTwNM/hqdefault.jpg)](https://www.youtube.com/watch?v=u5B27TaTwNM)

[Watch on YouTube](https://www.youtube.com/watch?v=u5B27TaTwNM)
