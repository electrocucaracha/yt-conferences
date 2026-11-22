---
layout: default
title: "Talks - Amitosh Swain: Testing Data Pipelines"
nav_order: 166
parent: PyCon US 2024
type: Video Note
description: "Amit, a data platform engineer at Topline, presents a comprehensive strategy for testing data pipelines, emphasizing that testing must occur both during the software development lifecycle and in pr..."
resource: "https://www.youtube.com/watch?v=o-tJ7OK3sSY"
youtube_stats:
  view_count: 563
  like_count: 8
  channel_subscriber_count: 34500
tags:
  - pycon-us-2024
  - video
  - learning
status: stable
generated:
  by: process:yt-summarizer-okf
  at: 2026-11-22T10:18:11+00:00
---

# Summary

Amit, a data platform engineer at Topline, presents a comprehensive strategy for testing data pipelines, emphasizing that testing must occur both during the software development lifecycle and in production to ensure data reliability.
He recommends starting with automated end-to-end testing, which involves running pipelines against known good snapshots to validate overall system behavior, followed by snapshot testing to detect regressions by comparing new outputs against stored production data samples.
To improve speed and cost-efficiency, he advocates for functional testing, which executes specific groups of tasks in isolation with controlled inputs, and unit testing, which isolates logic and orchestration components using mocks to verify code correctness without invoking expensive external resources.
Additionally, the talk highlights the critical importance of production data quality checks, such as validating invariants, checking for duplicates, and monitoring statistical distributions, to guarantee that the data delivered to end users is accurate and trustworthy.
Amit shares practical insights from his experience, including the use of tools like Soda Core and Great Expectations, and warns about the potential for high cloud costs during testing, suggesting the implementation of strict spending quotas and billing alerts to manage expenses effectively.

# Main Points

|   # | Main point                                                                                                                                         |
| --: | -------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Data pipelines require testing both during development and in production to ensure reliability and data quality.                                   |
|   2 | Automated end-to-end testing is recommended as a starting point because it covers a wide surface area with relatively low effort.                  |
|   3 | End-to-end tests involve taking a snapshot of known good data, running the pipeline, and comparing the output to expected results.                 |
|   4 | Snapshot testing helps validate refactoring or library upgrades by comparing new pipeline outputs against stored production data samples.          |
|   5 | Functional testing allows running groups of tasks in isolation, which is faster and cheaper than end-to-end testing but still uses real resources. |
|   6 | Effective functional testing requires separating pipeline logic from orchestration frameworks like Airflow to enable isolated execution.           |
|   7 | Unit tests are quick, cheap, and focused on specific code logic, helping to catch orchestration bugs and conditional rendering errors.             |
|   8 | Mocks in unit tests do not always behave like real systems, so caution is needed when relying solely on them for validation.                       |
|   9 | Production data quality checks are essential because data is often unclean and unpredictable, requiring continuous monitoring.                     |
|  10 | Data quality checks include validating invariants, checking for nulls, duplicates, and ensuring data types and distributions match expectations.   |
|  11 | Tools like Soda Core and Great Expectations provide frameworks for defining and running data quality checks.                                       |
|  12 | At Topline, the team uses an abstraction layer called Dagline to separate pipeline logic from Airflow for better testability.                      |
|  13 | The team implements unit tests for components, functional tests before code merge, and end-to-end runs for every deployment.                       |
|  14 | An in-house framework called Litmus, built on Soda Core and Great Expectations, runs data quality checks on demand and on schedule.                |
|  15 | Test data generation often involves sampling real production data or manually creating small datasets based on specific bug scenarios.             |
|  16 | Cloud costs for testing can be significant, requiring strict quota management and billing alerts to prevent unexpected expenses.                   |
|  17 | Separating orchestration code from business logic is critical for enabling effective functional and unit testing strategies.                       |

# Video

[![Video thumbnail](https://img.youtube.com/vi/o-tJ7OK3sSY/hqdefault.jpg)](https://www.youtube.com/watch?v=o-tJ7OK3sSY)

[Watch on YouTube](https://www.youtube.com/watch?v=o-tJ7OK3sSY)
