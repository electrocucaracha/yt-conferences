---
layout: default
title:
  "Breaking the Monolith: Decomposing and Governing Giant LLM Jobs Across Clusters
  - Kevin Wang, Huawei"
nav_order: 31
parent: Kubecon Cloudnativecon Europe 2026
type: Video Note
description:
  Kevin Juan discusses his experience as a maintainer and member of the
  technical oversight committee, focusing on challenges and solutions in multicluster
  AI workload management. He explains that while multicluster setups offer unified
  manag...
resource: https://www.youtube.com/watch?v=tCeWbdekqJE
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

Kevin Juan discusses his experience as a maintainer and member of the technical oversight committee, focusing on challenges and solutions in multicluster AI workload management.
He explains that while multicluster setups offer unified management and resource pooling, defining cluster boundaries and efficiently scheduling AI jobs remain difficult due to resource fragmentation and performance trade-offs.
Traditional monolithic job scheduling leads to resource inefficiency, prompting the development of projects like Volcano and Kamada to improve scheduling and resource sharing across clusters.
The new Volcano Global subproject and the Hyper Job API aim to enable more flexible, federated job splitting and scheduling, particularly for large AI training workloads, by supporting advanced parallelism strategies and dynamic resource allocation.
Kevin highlights ongoing improvements, such as smarter job splitting policies and better support for data and pipeline parallelism, and encourages the community to explore the released tools and contribute to future enhancements.

# Main Points

|   # | Main point                                                                                                                              |
| --: | --------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Kevin Juan serves on the technical oversight committee and multiple projects.                                                           |
|   2 | The talk focuses on his maintainer role and multicluster management in enterprise AI.                                                   |
|   3 | Multicluster setups offer unified management, cross-cloud GPU pooling, and resource abstraction.                                        |
|   4 | Cluster boundaries are typically defined by geography, capacity, or hardware specs.                                                     |
|   5 | Challenges include resource utilization, performance, and efficiency due to resource fragmentation.                                     |
|   6 | Traditional monolithic job scheduling leads to idle resources and inefficiency.                                                         |
|   7 | Techniques like bin packing and priority preemption help but are not complete solutions.                                                |
|   8 | Volcano project (since 2019) manages AI/ML workloads in single clusters.                                                                |
|   9 | Kamada project (since 2021) addresses multicluster resource management and scheduling.                                                  |
|  10 | Gaps remain in global queue management and fair sharing across clusters.                                                                |
|  11 | Volcano Global subproject was started to address global queue and fair sharing.                                                         |
|  12 | In 2024, Volcano Global was built on Kamada for priority and fair sharing in multi-tenant use cases.                                    |
|  13 | In 2025, Kamada was improved with advanced scheduling and failover mechanisms.                                                          |
|  14 | Basic resource management and task scheduling are resolved, but federation-native API abstraction is needed.                            |
|  15 | Extensible architecture for job splitting policy is required for different AI models and data setups.                                   |
|  16 | Three AI training parallelism patterns: tensor (requires single node), data (needs high bandwidth), pipeline (splits model vertically). |
|  17 | Pipeline parallelism is most practical for multicluster setups, minimizing cross-cluster data transfer.                                 |
|  18 | Asymmetric layer assignment (e.g., more layers to faster clusters) reduces resource bubbles and idle time.                              |
|  19 | Hyper job API allows defining and splitting jobs across clusters, customizing scheduling and propagation policies.                      |
|  20 | Hyper job controller analyzes, splits, and schedules jobs based on cluster status and constraints.                                      |
|  21 | Volcano Global manages global queue and prioritizes workloads; gang scheduling                                                          |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=tCeWbdekqJE)
