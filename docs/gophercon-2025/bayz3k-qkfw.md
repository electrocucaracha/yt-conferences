---
layout: default
title: "GopherCon 2025: Profiling Request Latency with Critical Path Analysis - Felix Geisendörfer"
nav_order: 13
parent: GopherCon 2025
type: Video Note
description: Felix Gazender from Data Dog presents a method for profiling request latency in Go applications using critical path analysis to address the limitations of traditional profiling tools.
resource: "https://www.youtube.com/watch?v=BayZ3k-QkFw"
youtube_stats:
  view_count: 2156
  like_count: 75
  channel_subscriber_count: 41100
tags:
  - gophercon-2025
  - video
  - learning
status: stable
generated:
  by: process:yt-summarizer-okf
  at: 2026-11-21T05:22:37+00:00
---

# Summary

Felix Gazender from Data Dog presents a method for profiling request latency in Go applications using critical path analysis to address the limitations of traditional profiling tools.
He explains that while Go’s execution tracer provides comprehensive data on goroutine state transitions, manually analyzing this data to understand off-CPU latency and its impact on user experience is complex and often misleading.
To solve this, Gazender proposes applying critical path analysis—a technique originally developed for project management—to identify the specific sequence of dependent activities that determine the total request duration.
This approach allows engineers to distinguish between critical bottlenecks, such as specific mutex contentions or scheduling delays, and subcritical background activities that do not directly affect latency.
By automating this analysis, the method can generate precise insights into which code paths are responsible for tail latencies, enabling more effective performance optimization and better contextualization of profiling data for engineering teams.

# Main Points

|   # | Main point                                                                                                                                                       |
| --: | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Go is a compiled language with a high-performance runtime, making it suitable for fast software and team environments.                                           |
|   2 | Go provides built-in observability tools like pprof and the execution tracer with low overhead, enabling production profiling.                                   |
|   3 | Traditional profiling often yields incomplete stack traces, making it difficult to determine the impact of issues like mutex contention on user experience.      |
|   4 | The execution tracer captures scheduler events and goroutine state transitions, providing a complete picture of program activity over time.                      |
|   5 | Feeding raw execution trace data into LLMs is impractical due to massive data volumes and high costs, requiring data slicing and analysis.                       |
|   6 | Request annotations via the runtime/trace package allow developers to define request boundaries and attach metadata for better context.                          |
|   7 | Critical path analysis identifies the longest chain of dependent activities to determine which components most significantly impact overall latency.             |
|   8 | This technique helps distinguish between critical bottlenecks and subcritical activities that have Slack time and do not affect total completion time.           |
|   9 | Concurrency patterns like worker pools and buffered channels can create missing edges in trace data, complicating backward path analysis.                        |
|  10 | Heuristics such as setting time limits for exploration are needed when return paths are missing, but they must be applied carefully to avoid false positives.    |
|  11 | Mutex contention between unrelated requests can create misleading dependencies, requiring stack trace analysis to distinguish true critical paths.               |
|  12 | The algorithm generally produces accurate results for common Go concurrency patterns, matching human analysis in most real-world scenarios.                      |
|  13 | Critical path analysis reveals specific latency contributors like scheduling latency, which is often difficult to quantify and communicate to engineering teams. |
|  14 | Stitching artificial stack traces from critical path data can provide better context for incomplete traces and improve flame chart readability.                  |
|  15 | Aggregating critical path data across requests allows for profiling specific latency percentiles, such as P50 versus P99, to prioritize optimizations.           |
|  16 | DataDog has contributed to reducing execution tracer overhead from 10-20% to 1-2%, making advanced analysis feasible in production.                              |
|  17 | The team is working on open-sourcing these analysis tools and contributing libraries to facilitate testing and processing of execution trace data.               |

# Video

[![Video thumbnail](https://img.youtube.com/vi/BayZ3k-QkFw/hqdefault.jpg)](https://www.youtube.com/watch?v=BayZ3k-QkFw)

[Watch on YouTube](https://www.youtube.com/watch?v=BayZ3k-QkFw)
