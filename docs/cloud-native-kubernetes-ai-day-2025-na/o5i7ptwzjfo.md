---
layout: default
title:
  "Lightning Talk: Mind the Topology: Smarter Scheduling for AI Workloads on
  Kubernetes - Roman Baron"
nav_order: 7
parent: Cloud Native Kubernetes Ai Day 2025 Na
type: Video Note
description:
  Roman Baron, a senior software engineer at Nvidia and maintainer of Sky
  Kaiuler, introduces the Kai scheduler, a Kubernetes-native scheduling framework
  optimized for AI workloads. He discusses the challenges of topology-aware scheduling,
  em...
resource: https://www.youtube.com/watch?v=o5i7pTWZjfo
tags:
  - cloud-native-kubernetes-ai-day-2025-na
  - video
  - learning
status: stable
generated:
  by: process:yt-conferences-okf
  at: 2026-09-12 00:00:00+00:00
---

# Summary

Roman Baron, a senior software engineer at Nvidia and maintainer of Sky Kaiuler, introduces the Kai scheduler, a Kubernetes-native scheduling framework optimized for AI workloads.
He discusses the challenges of topology-aware scheduling, emphasizing that modern AI workloads are distributed across multiple GPU nodes and require careful placement to optimize network bandwidth and latency.
Traditional Kubernetes scheduling, including pod affinity, often falls short because it does not account for the entire workload's communication patterns or the underlying cluster topology.
Kai addresses these issues by analyzing workload composition and communication requirements, enabling optimal pod placement within racks and zones to maximize performance.
Roman concludes by inviting interested contributors to join the Kai community and clarifies that while Kai is a scheduler, it works alongside other components like Dynamo, managing workloads through the Grove workload manager.

# Main Points

|   # | Main point                                                                                                                                       |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------------ |
|   1 | Roman Baron is a maintainer of Sky Kaiuler and a senior software engineer at Nvidia.                                                             |
|   2 | The RAI scheduler was open sourced as Kai scheduler at the previous CubeCon event.                                                               |
|   3 | Kai is a Kubernetes-native scheduling framework optimized for AI workloads.                                                                      |
|   4 | Topology-aware scheduling is increasingly important due to evolving compute and network architectures and new AI workload requirements.          |
|   5 | Modern AI workloads are distributed across multiple pods and GPU nodes, not limited to a single node.                                            |
|   6 | Simple scheduling based only on resource requirements can lead to suboptimal pod placement across racks or zones with varying network bandwidth. |
|   7 | High-speed connectivity often exists within racks, while bandwidth between racks is limited.                                                     |
|   8 | Optimal scheduling requires awareness of cluster network topology and workload communication patterns.                                           |
|   9 | Not all pods in a workload need to be placed together; communication patterns may dictate different optimal placements.                          |
|  10 | Ignoring topology can increase latency, reduce throughput, and degrade resource utilization.                                                     |
|  11 | Kubernetes pod affinity is insufficient due to its pod-by-pod scheduling approach.                                                               |
|  12 | Scheduling pods one by one without considering the entire workload can prevent optimal placement.                                                |
|  13 | Planning ahead for the entire workload enables better placement, such as grouping pods in a single rack.                                         |
|  14 | Disaggregated inference pipelines involve multiple pods with different roles (e.g., prefill, decode, frontend, monitoring).                      |
|  15 | Leader and worker pods within the same group require high bandwidth and low latency for model parallelism.                                       |
|  16 | KV cache transfers between prefill and decode groups are also important but secondary.                                                           |
|  17 | Naive scheduling may spread pods across racks or zones, reducing communication efficiency.                                                       |
|  18 | Kai considers workload composition and network proximity requirements for optimal pod placement.                                                 |
|  19 | Kai can collocate pods from the same group and consider cross-group topology constraints.                                                        |
|  20 | Prefill and decode groups can be placed in                                                                                                       |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=o5i7pTWZjfo)
