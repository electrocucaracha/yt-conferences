---
layout: default
title:
  "The Hyperscale Uncertainty Principle: Debugging Tail Latency in a Trillion-Object...
  Yashraj Kakkad"
nav_order: 360
parent: Kubecon Cloudnativecon Europe 2026
type: Video Note
description:
  Yashraj Gakkad, a software engineer at Google Photos, discusses the challenges
  of maintaining referential integrity and managing tail latency at exabyte scale,
  where trillions of objects are stored and verified across massive relational met...
resource: https://www.youtube.com/watch?v=hpFqElHNLaY
tags:
  - kubecon-cloudnativecon-europe-2026
  - video
  - learning
status: stable
generated:
  by: process:yt-conferences-okf
  at: 2026-09-12 00:00:00+00:00
---

# Summary

Yashraj Gakkad, a software engineer at Google Photos, discusses the challenges of maintaining referential integrity and managing tail latency at exabyte scale, where trillions of objects are stored and verified across massive relational metadata and object storage systems.
To ensure consistency, Google Photos runs a large concurrency pipeline, initially partitioned into 16 logical segments for parallel processing, but encountered unpredictable runtimes and high tail latencies due to straggler reads, not data skew or join inefficiencies.
The root cause was identified as large, unsplittable work shards in the read stages, exacerbated by legacy infrastructure and compounded by the inefficiency of best-effort compute when preemptions caused significant wasted work.
The solution involved over-sharding—creating more, smaller work units than workers—and implementing dynamic work rebalancing (liquid sharding) to break up heavy tasks at runtime, significantly reducing tail latency and improving resource utilization.
Gakkad concludes with key lessons: architect for the P99 tail, respect physical infrastructure limits, over-shard and re-shard where possible, and carefully evaluate the true cost of preemptible compute at hyperscale, as software abstractions alone are insufficient for predictable, efficient operation at this magnitude.

# Main Points

|   # | Main point                                                                                                                                                                     |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   1 | Google Photos operates at exabyte scale with trillions of objects, requiring planetary-scale memory management.                                                                |
|   2 | Referential integrity is maintained between a massive relational metadata database and object storage; both must be consistent.                                                |
|   3 | No out-of-the-box solution exists for referential integrity at this scale; a large concurrency pipeline is used for verification, data loss detection, and garbage collection. |
|   4 | The user namespace is partitioned into 16 logical partitions, each with its own parallel referential integrity pipeline.                                                       |
|   5 | Despite uniform partitioning, runtimes were unpredictable and often exceeded the 3-day SLA due to high tail latencies.                                                         |
|   6 | Data skew was ruled out; partitions had less than 1% variation in object count, but performance variance remained high.                                                        |
|   7 | The main bottleneck was in the read stages from metadata and object storage, not in the join or post-processing.                                                               |
|   8 | High P95 and P99 latencies and error rates were observed; pipeline runtime was dominated by a small fraction of slow reads (stragglers).                                       |
|   9 | Request hedging was considered but only helps if latency is transient; otherwise, it risks self-inflicted DDoS.                                                                |
|  10 | Misalignment between logical pipeline partitions and physical object storage partitions was investigated but found not to be the root cause.                                   |
|  11 | Over-sharding is recommended: for n workers, use about 3n log n shards to hide tail latency and reduce straggler impact.                                                       |
|  12 | Legacy systems limited sharding; modernization and dynamic work rebalancing (liquid sharding) were introduced to split large work chunks at runtime.                           |
|  13 | Preemptible compute led to high waste (>70%) due to heavy shards being preempted and restarted.                                                                                |
|  14 | Key engineering truths learned:                                                                                                                                                |
|  15 | Architect for P99 tail latency; stragglers dominate batch pipeline runtime.                                                                                                    |
|  16 | Over-shard and use re-sharding after read stages for better parallelism.                                                                                                       |
|  17 | Respect infrastructure and bare metal limitations.                                                                                                                             |
|  18 | Evaluate ROI of preemptible compute; high retry rates can outweigh cost savings.                                                                                               |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=hpFqElHNLaY)
