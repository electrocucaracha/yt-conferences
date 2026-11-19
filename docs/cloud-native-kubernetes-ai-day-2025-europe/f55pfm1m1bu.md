---
layout: default
title: "Accelerate Your AI/ML Workloads With Topology-Aware Scheduling in Kueue - Michał Woźniak & Yuki Iwai"
nav_order: 8
parent: "Cloud Native & Kubernetes AI Day 2025 - Europe"
type: Video Note
description: "The presentation introduces Q, a Kubernetes-based queue manager designed to optimize computational resource allocation for AI workloads by addressing the limitations of standard Kubernetes scheduli..."
resource: "https://www.youtube.com/watch?v=F55pFM1M1bU"
tags:
  - cloud-native-kubernetes-ai-day-2025-europe
  - video
  - learning
status: stable
generated:
  by: process:yt-summarizer-okf
  at: 2026-11-15T17:34:27+00:00
---

# Summary

The presentation introduces Q, a Kubernetes-based queue manager designed to optimize computational resource allocation for AI workloads by addressing the limitations of standard Kubernetes scheduling, such as resource fragmentation and suboptimal pod placement.
Q functions as a quota manager that supports fair sharing, hierarchical cohorts, and various hardware types like GPUs and TPUs, ensuring that AI training jobs, which require all pods to run simultaneously, are admitted only when sufficient resources are available to prevent deadlocks.
A key feature discussed is topology-aware scheduling, which uses node labels to reconstruct the physical cluster hierarchy (zone, block, rack, node) and places pods with neighboring ranks on closely connected servers to minimize high-latency network communication.
This approach significantly improves performance, with internal benchmarks showing a 15% reduction in training time for GPT-2 models, while also reducing admission and preemption errors by providing Q with accurate physical capacity awareness.
The talk concludes by highlighting recent updates in Q version 0.11, including the introduction of an "auto mode" to simplify adoption, and outlines future plans to integrate tighter scheduling logic with the Kubernetes scheduler and offer configurable algorithms for balancing utilization and fragmentation.

# Main Points

|   # | Main point                                                                                                                                                                                                     |
| --: | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Q functions as a quota manager for computational resources like GPUs, supporting fair sharing, hierarchical cohorts, and various provisioning types such as reservations and spot instances.                   |
|   2 | The system supports a broad portfolio of worker types, including Kubernetes jobs, Job Sets, Ray Jobs, Deployment Sets, and App Wrappers for training and inference workloads.                                  |
|   3 | Without Q, the Kubernetes scheduler may fail to schedule all pods of an AI training job simultaneously, leading to deadlock situations where jobs cannot make progress.                                        |
|   4 | Q resolves admission issues by checking quotas before admitting workloads, ensuring that only jobs with sufficient resources are scheduled to prevent fragmentation-related failures.                          |
|   5 | Standard quota-based admission has limitations, including potential admission mistakes due to resource fragmentation and the inability to handle fine-grained scheduling constraints effectively.              |
|   6 | Topology-aware scheduling in Q addresses performance issues by packing pods closely on neighboring servers connected by low-latency networks, which is critical for AI training communication patterns.        |
|   7 | Since Kubernetes lacks a standard for topological information, Q proposes a convention using node labels to identify cluster, block, rack, and node positions.                                                 |
|   8 | A new Topology API allows administrators to specify node labels for topology, linked to Resource Flavors to define machine pools with common characteristics.                                                  |
|   9 | Q reconstructs a topology tree from node labels and calculates capacity by subtracting usage from task workloads and non-Q pods from the node's allocatable status.                                            |
|  10 | Users can specify scheduling requirements via pod template annotations, including required topology for strict domain placement, preferred topology for spill-over, or unconstrained topology for flexibility. |
|  11 | Q operates in scheduling cycles, creating snapshots of the topology tree and using bottom-up and top-down BFS passes to identify suitable domains and map them to concrete nodes.                              |
|  12 | Rank-based ordering ensures that pods with neighboring ranks are placed on the same node to optimize data exchange performance for AI training frameworks.                                                     |
|  13 | Benchmarks show that using Q for training the GPT-2 model on 32 nodes can reduce training time by approximately 15% compared to standard scheduling.                                                           |
|  14 | Version 0.11 of Q introduces full quota management features, including fair sharing and hierarchical cohorts, along with an auto mode to reduce adoption friction.                                             |
|  15 | Future improvements include configurable algorithms for balancing utilization and fragmentation, cost-aware scheduling for pod sets, and tighter integration with the Kubernetes scheduler.                    |
|  16 | Internal node topology scheduling is currently out of scope, and automatic discovery of network topology via protocols like Cisco CDP is not part of Q's responsibilities.                                     |
|  17 | Q currently requires being the main scheduler for the cluster to enforce topology-aware scheduling, as it does not yet support pod affinities or anti-affinities delegated to the Kubernetes scheduler.        |
|  18 | Rank extraction relies on labels set by job frameworks, with custom code for each supported job type to interpret rank information from labels like completion indices.                                        |

# Video

[![Video thumbnail](https://img.youtube.com/vi/F55pFM1M1bU/hqdefault.jpg)](https://www.youtube.com/watch?v=F55pFM1M1bU)

[Watch on YouTube](https://www.youtube.com/watch?v=F55pFM1M1bU)
