---
layout: default
title: "Unconference Session: Reliable K8s Operator: How to Survive Eventual Consistency"
nav_order: 22
parent: "Maintainer Summit 2026 - Europe"
type: Video Note
description: "The speaker discusses the challenges of eventual consistency in Kubernetes, highlighting how delayed state propagation can lead to severe production issues, such as the DaemonSet controller duplica..."
resource: "https://www.youtube.com/watch?v=WqN5y6cpprA"
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

The speaker discusses the challenges of eventual consistency in Kubernetes, highlighting how delayed state propagation can lead to severe production issues, such as the DaemonSet controller duplicating pods due to stale data.
To address this, the presentation introduces a new capability in Kubernetes 1.36 that allows for the standardized comparison of resource versions, a change that is now required for API conformance.
This feature enables a proposed mechanism for controller stale control detection, which prevents reconciliation until the results of previous actions are observed, thereby mitigating the risks of acting on outdated information.
The speaker advocates for adopting similar standards in the controller-runtime community to ensure consistent behavior and avoid redundant development efforts.
Finally, the talk emphasizes the need for better guidance on graceful degradation, arguing that current best-effort approaches can cause clusters to fail catastrophically under stress rather than degrading safely.

# Main Points

|   # | Main point                                                                                                                                                     |
| --: | -------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Kubernetes relies on eventual consistency for speed and scalability, but the exact delay in state propagation is currently unknown.                            |
|   2 | Production issues arise when controllers miss their own writes, leading to duplicate resource creation, such as DaemonSet pods duplicating every five minutes. |
|   3 | A historical etcd watch starvation bug caused by gRPC HTTP2 prioritization resulted in a two-hour scheduler delay.                                             |
|   4 | Kubernetes has standardized comparable resource versions, requiring all conformant APIs to implement a global logical clock for version comparison.            |
|   5 | This standardization prevents alternative databases from skipping global locking mechanisms to claim performance advantages.                                   |
|   6 | A new proposal for controller stale control detection uses comparable resource versions to mitigate consistency issues.                                        |
|   7 | The proposed mechanism delays reconciliation if the controller has not yet observed the results of its previous action.                                        |
|   8 | This approach sits between eventual consistency and strong consistency by blocking new events until the last write is visible in the local cache.              |
|   9 | The stale control detection feature reached beta status in Kubernetes version 1.36.                                                                            |
|  10 | A parallel proposal exists for the controller-runtime community to address similar consistency challenges.                                                     |
|  11 | The goal is to establish unified standards for controller behavior to avoid redundant solutions across different ecosystems.                                   |
|  12 | Current Kubernetes features often prioritize availability over consistency, which can lead to harmful degradation at scale.                                    |
|  13 | Unhappy paths in controller logic are frequently untested, causing clusters to break rather than degrade gracefully under stress.                              |
|  14 | Running large-scale clusters, such as those with 5,000 nodes, can easily trigger out-of-memory conditions if stale data causes excessive resource creation.    |
|  15 | There is currently no official guidance in Kubernetes on how controllers should handle stale data or decide whether to stop reconciliation.                    |

# Video

[![Video thumbnail](https://img.youtube.com/vi/WqN5y6cpprA/hqdefault.jpg)](https://www.youtube.com/watch?v=WqN5y6cpprA)

[Watch on YouTube](https://www.youtube.com/watch?v=WqN5y6cpprA)
