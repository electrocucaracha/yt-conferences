---
layout: default
title: "Building Resilient Data Pipelines: The Power of Idempotency - Mihir Kavatkar"
nav_order: 89
parent: PyCon US 2025
type: Video Note
description: "Mihir, a bioinformatic software engineer at Memorial Sloan Kettering Cancer Center, presents a strategy for making data pipelines resilient through idempotency, a property ensuring that repeated op..."
resource: "https://www.youtube.com/watch?v=kT8YWX4NE2o"
youtube_stats:
  view_count: 2871
  like_count: 48
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

Mihir, a bioinformatic software engineer at Memorial Sloan Kettering Cancer Center, presents a strategy for making data pipelines resilient through idempotency, a property ensuring that repeated operations yield the same result.
He explains that while failure-proof pipelines are a myth, idempotency makes failures predictable and consistent, which is critical for mission-critical applications like clinical test result delivery.
The talk outlines several key design patterns to achieve this, including using atomic and distributed transactions to maintain consistency, implementing idempotency keys to prevent duplicate actions during retries, and employing checkpoint and recovery mechanisms to allow pipelines to resume from the last successful state rather than restarting entirely.
Additionally, he discusses compensation strategies for scenarios where strict atomicity is impossible, the importance of schema versioning and passive versioning for handling data transformations and concurrent updates, and the necessity of using fixed ranges in backfills to ensure predictable analytics.
Finally, Mihir advocates for a simple "identify, test, repeat" approach to testing, emphasizing the creation of unit and integration tests that simulate failures to verify predictability, and recommends using open-source tools like Pytest and standard SQL transactions to implement these patterns without overcomplicating the infrastructure.

# Main Points

|   # | Main point                                                                                                                                                            |
| --: | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Data pipelines are versatile workflows used for data transfer, streaming, genomic analysis, quality checks, and backfilling.                                          |
|   2 | Resiliency is critical because network failures, duplicate actions, and data inconsistencies cause business downtime, financial loss, and erroneous decision-making.  |
|   3 | Idempotency ensures an operation produces the same output regardless of how many times it is executed, making pipelines predictable and consistent.                   |
|   4 | Atomic transactions guarantee that operations result in either a consistent success or a fail state, preventing partial updates.                                      |
|   5 | Distributed transactions, such as two-phase or three-phase commits, maintain atomicity across multiple services, databases, or clusters.                              |
|   6 | Idempotency keys are unique identifiers attached to requests to prevent duplicate actions during retries, allowing servers to reject or handle repeated calls safely. |
|   7 | Checkpoint and recovery involves tracking the state of pipeline stages in a database to enable forward recovery from the last successful step after a failure.        |
|   8 | Compensation strategies, such as refund events, restore consistency when strict atomicity is impossible in distributed systems or event sourcing.                     |
|   9 | Schema versioning and passive versioning techniques ensure data transformations remain consistent during schema evolution and concurrent updates.                     |
|  10 | Backfills should use fixed ranges or window functions to ensure predictable results, avoiding unpredictable outputs caused by changing data contexts.                 |
|  11 | Testing idempotency involves identifying critical components, writing unit tests for potential failures, and simulating failures to verify predictability.            |
|  12 | Remote procedure calls within pipelines must be treated as dependencies where failures trigger retries using idempotency keys or state tracking.                      |
|  13 | Writing failing tests before fixing bugs ensures that specific issues are addressed and prevents regressions in CI/CD pipelines.                                      |
|  14 | Simple implementation of idempotency patterns, such as idempotency keys in Python, is often sufficient without complex workflow engines.                              |
|  15 | Existing tools like SQL transactions and open-source testing frameworks like pytest support the implementation of resilient data pipelines.                           |

# Video

[![Video thumbnail](https://img.youtube.com/vi/kT8YWX4NE2o/hqdefault.jpg)](https://www.youtube.com/watch?v=kT8YWX4NE2o)

[Watch on YouTube](https://www.youtube.com/watch?v=kT8YWX4NE2o)
