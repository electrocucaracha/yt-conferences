---
layout: default
title:
  "The Missing Metrics: Measuring Memory Interference in Cloud Native Systems
  - Jonathan Perry"
nav_order: 338
parent: Kubecon Cloudnativecon Europe 2025
type: Video Note
description:
  The speaker discusses "memory noisy neighbor," a phenomenon where one
  application takes more than its fair share of resources on a server, degrading performance
  for other applications. This issue is particularly problematic in cloud-native...
resource: https://www.youtube.com/watch?v=nXdGXdxmWNQ
tags:
  - kubecon-cloudnativecon-europe-2025
  - video
  - learning
status: stable
generated:
  by: process:yt-conferences-okf
  at: 2026-09-12 00:00:00+00:00
---

# Summary

The speaker discusses "memory noisy neighbor," a phenomenon where one application takes more than its fair share of resources on a server, degrading performance for other applications.
This issue is particularly problematic in cloud-native applications that run on physical servers with shared finite resources.
The speaker presents research and case studies showing the impact of memory noisy neighbors on performance, including a 53% increase in revenue per user and a 35% reduction in bounce rates from an optimized application running 400 milliseconds faster than its non-optimized counterpart.
To mitigate this issue, the speaker proposes using resource allocation capabilities to run more transactions on the same-sized servers, reducing tail latency by factors of five to fourteen.
The speaker also discusses building an open-source collector to measure and mitigate noisy neighbors, with a goal of achieving 1% overhead in line with traffic while significantly improving performance.

# Main Points

|   # | Main point                                                                                                                   |
| --: | ---------------------------------------------------------------------------------------------------------------------------- |
|   1 | Noisy neighbors can cause cache eviction, leading to slower access times and increased latency.                              |
|   2 | Google's case study shows that a 100ms increase in user response time leads to a 1% revenue loss.                            |
|   3 | A study by Raku 1024 found that optimizing an application reduced bounce rates by 35% and increased revenue per user by 53%. |
|   4 | Researchers have developed mechanisms to mitigate noisy neighbors, including:                                                |
|   5 | Vertical autoscaling                                                                                                         |
|   6 | Resource control                                                                                                             |
|   7 | Direct measurement of memory bandwidth and cache usage                                                                       |
|   8 | The goal is to measure P95/P99 latency and adjust resource allocation accordingly.                                           |
|   9 | The system aims to reduce overhead to <1% while improving performance by up to 5%.                                           |
|  10 | The collector will store data in parquet format, with storage requirements estimated at ~1MB/s.                              |
|  11 | Automatic mitigation can help solve memory saturation issues without requiring profiling or application changes.             |
|  12 | Vertical scaling can help mitigate noisy neighbors, but may not be the most cost-effective solution.                         |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=nXdGXdxmWNQ)
