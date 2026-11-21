---
layout: default
title: "Why Software Engineering Best Practices Fail in Data Engineering - Constance Martineau"
nav_order: 81
parent: PyCon US 2026
type: Video Note
description: "Constance, a staff product manager at Astronomer, presents data from 400 million production pipeline runs to demonstrate that software engineering best practices, such as CI/CD and code reviews, fa..."
resource: "https://www.youtube.com/watch?v=EFB4fZuWGUc"
youtube_stats:
  view_count: 471
  like_count: 14
  channel_subscriber_count: 34500
tags:
  - pycon-us-2026
  - video
  - learning
status: stable
generated:
  by: process:yt-summarizer-okf
  at: 2026-11-20T08:08:06+00:00
---

# Summary

Constance, a staff product manager at Astronomer, presents data from 400 million production pipeline runs to demonstrate that software engineering best practices, such as CI/CD and code reviews, fail to address the primary causes of data engineering failures.
The analysis reveals that while the overall failure rate is 7%, these failures are highly concentrated in a small subset of pipelines and are largely unrelated to recent code deployments, with failure rates remaining statistically flat before and after deploy events.
Instead of code changes, the main drivers of instability are upstream data variance, runtime version stranding, and long-running workload fragility, indicating that the core issue is an inversion of control where external data inputs dictate code behavior rather than the other way around.
To address this, the speaker proposes a five-layer reliability framework, arguing that while Layer 1 (code correctness) is essential, the majority of production failures occur in Layers 2 through 5, which involve data validation, time correctness, state transition safety, and recovery mechanisms.
Consequently, teams should shift their focus from solely policing the deploy boundary to implementing contract testing for inputs, treating time as a first-class concern, and designing for graceful degradation to handle the unpredictable nature of upstream data.

# Main Points

|   # | Main point                                                                                                                                                        |
| --: | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | The speaker, Constance, is a staff product manager at Astronomer, which builds a managed Apache Airflow platform.                                                 |
|   2 | The talk analyzes 400 million production pipeline runs from 2025 to investigate the relationship between deploys and failures.                                    |
|   3 | The cohort-wide failure rate is 7%, but this is driven by a small tail where 3% of DAGs account for 67% of all failures.                                          |
|   4 | Most failures are not caused by recent code deploys but by runtime stranding, long-running workloads, and structurally broken pipelines.                          |
|   5 | A direct comparison of failure rates 24 hours before and after deploys shows no significant difference, indicating deploys are not the primary cause of failures. |
|   6 | Deploys act as attention anchors that make pre-existing failures more noticeable rather than causing new ones.                                                    |
|   7 | In data engineering, upstream data and constraints control the shape of the code, inverting the application development model where code controls behavior.       |
|   8 | CI/CD and code reviews effectively catch layer one errors like syntax and logic bugs, reducing dev failure rates from 15% to 7% in production.                    |
|   9 | The remaining 7% production failure rate represents a structural floor caused by issues outside the codebase, such as schema drift and late data.                 |
|  10 | A five-layer reliability framework is proposed, with layer one covering code correctness and layers two through five covering data, time, state, and recovery.    |
|  11 | Most software engineering tooling focuses on layer one, while the majority of data engineering failures occur in layers two through five.                         |
|  12 | Teams should contract test inputs for schema and freshness rather than just testing code logic.                                                                   |
|  13 | Time should be treated as a first-class concern by instrumenting SLA misses and late-arriving data as failures.                                                   |
|  14 | Systems should be designed for graceful degradation, including dead letter paths and idempotent backfills, to handle unexpected inputs.                           |
|  15 | Teams should identify and triage chronically broken DAGs separately to prevent them from skewing overall reliability metrics.                                     |
|  16 | The core takeaway is that time and data state are primary failure surfaces, not edge cases, and must be addressed to improve reliability.                         |

# Video

[![Video thumbnail](https://img.youtube.com/vi/EFB4fZuWGUc/hqdefault.jpg)](https://www.youtube.com/watch?v=EFB4fZuWGUc)

[Watch on YouTube](https://www.youtube.com/watch?v=EFB4fZuWGUc)
