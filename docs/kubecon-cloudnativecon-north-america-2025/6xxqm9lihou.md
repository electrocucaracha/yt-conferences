---
layout: default
title:
  Building Scalable End-to-end Latency Metrics From Distributed Trace - Kusha
  Maharshi, Bloomberg
nav_order: 32
parent: Kubecon Cloudnativecon North America 2025
type: Video Note
description:
  Kosha Mahersi, a senior software engineer at Bloomberg, presents how
  her team built a scalable system for generating end-to-end latency metrics using
  distributed tracing. She explains that Bloomberg’s telemetry infrastructure team
  supports...
resource: https://www.youtube.com/watch?v=6xxqm9LIhoU
tags:
  - kubecon-cloudnativecon-north-america-2025
  - video
  - learning
status: stable
generated:
  by: process:yt-conferences-okf
  at: 2026-09-12 00:00:00+00:00
---

# Summary

Kosha Mahersi, a senior software engineer at Bloomberg, presents how her team built a scalable system for generating end-to-end latency metrics using distributed tracing.
She explains that Bloomberg’s telemetry infrastructure team supports other engineering teams who require precise latency monitoring for complex, high-stakes financial systems, where even millisecond delays can have significant financial impacts.
Traditional methods for tracking end-to-end latency were insufficient, so the team adopted distributed tracing, which models workflows as directed acyclic graphs (DAGs) of spans, each with timing and parent-child relationship data.
To generate latency metrics at scale, they developed two main approaches: one aggregates trace bundles by rule to ensure all relevant spans are processed together, while the other uses a partial DFS handoff between processing instances to address load imbalance.
Mahersi discusses the trade-offs of each method, such as memory load and handling fan-in patterns, and notes that while their system does not currently address clock skew, it provides flexible rule-based latency tracking essential for monitoring, alerting, and improving reliability in distributed systems.
The talk concludes with a Q&A covering technical details like state management, time drift, Kafka partitioning, and rule configuration.

# Main Points

|   # | Main point                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| --: | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Kosha Mahersi, Senior Software Engineer at Bloomberg, presented on generating end-to-end latency metrics at scale using distributed tracing.                                                                                                                                                                                                                                                                                                       |
|   2 | The telemetry infrastructure team provides observability and monitoring solutions for internal engineering teams handling high-volume, low-latency financial systems.                                                                                                                                                                                                                                                                              |
|   3 | Latency of even milliseconds can result in significant financial loss, making end-to-end latency monitoring critical.                                                                                                                                                                                                                                                                                                                              |
|   4 | Distributed tracing was adopted as a unified solution for tracking requests across complex distributed systems.                                                                                                                                                                                                                                                                                                                                    |
|   5 | Distributed traces consist of spans (operations) with unique IDs, timing information, and parent-child relationships, forming a directed acyclic graph (DAG).                                                                                                                                                                                                                                                                                      |
|   6 | Engineers define rules to identify start and end events (e.g., "consume" to "publish") for measuring end-to-end latency.                                                                                                                                                                                                                                                                                                                           |
|   7 | Latency is calculated by running a depth-first search (DFS) on the trace DAG to find paths between start and end events and aggregating timing data.                                                                                                                                                                                                                                                                                               |
|   8 | At scale, spans from many machines are ingested into Kafka topics; a partitioner ensures all spans from the same trace are grouped.                                                                                                                                                                                                                                                                                                                |
|   9 | Complexities arise when traces are interconnected (trace bundles), requiring all related spans to be processed together.                                                                                                                                                                                                                                                                                                                           |
|  10 | Two approaches were developed: 1. Aggregating trace bundles by rule: Bundler service groups spans by trace bundle and potential rule match, enabling DFS in Dagger service. Downside: potential load imbalance with heavy rules. 2. Partial DFS handoff: Dagger instances run DFS until a fan-in is encountered, then hand off partial results to other instances. This approach reduces load imbalance but can be affected by deep fan-in chains. |
|  11 | Current state management for bundler is best effort; persistent storage is a desired future improvement.                                                                                                                                                                                                                                                                                                                                           |
|  12 | The system does not handle clock skew; highly latency-sensitive systems may use custom solutions.                                                                                                                                                                                                                                                                                                                                                  |
|  13 | Kafka topics are partitioned by hashed trace IDs for communication between services.                                                                                                                                                                                                                                                                                                                                                               |
|  14 | Rules for matching can use                                                                                                                                                                                                                                                                                                                                                                                                                         |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=6xxqm9LIhoU)
