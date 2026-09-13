---
layout: default
title:
  "Lightning Talk: Resource Fairness and Utilization for Heterogeneous Batch/M...
  Yuki Iwai & Gabe Saba"
nav_order: 9
parent: Cloud Native Kubernetes Ai Day 2025 Na
type: Video Note
description:
  In this talk, Yuki from CyberAgent and Gabe from Google introduce Q,
  an AI workload scheduler designed to optimize resource allocation and fair sharing
  for heterogeneous batch machine learning platforms. Q operates as a secondary scheduler...
resource: https://www.youtube.com/watch?v=dKhF-hZi7CI
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

In this talk, Yuki from CyberAgent and Gabe from Google introduce Q, an AI workload scheduler designed to optimize resource allocation and fair sharing for heterogeneous batch machine learning platforms.
Q operates as a secondary scheduler in front of Kubernetes, providing advanced features such as all-or-nothing semantics, delayed pod creation, multi-cluster dispatching, and comprehensive quota management.
The presentation focuses on three fair resource distribution approaches: fair sharing with preemption, hierarchical fair sharing, and admission fair sharing based on historical data.
Through detailed examples, they demonstrate how Q uses dominant resource share (DRS) values and cohort hierarchies to dynamically preempt and allocate GPUs, ensuring efficient and equitable resource utilization across teams and projects.
The talk concludes with an explanation of how Q leverages historical usage snapshots and penalty mechanisms to further refine admission decisions and maintain scheduling fairness.

# Main Points

|   # | Main point                                                                                                                                         |
| --: | -------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Speakers: Yuki (CyberAgent) and Gabe (Google) discuss resource fairness and utilization in heterogeneous batch ML platforms using Q.               |
|   2 | Q is an AI workload scheduler, acting as a second scheduler in front of Kubernetes’ default scheduler.                                             |
|   3 | Q provides scheduling functionalities for AI workloads: all-or-nothing semantics, delayed pod creation, multi-cluster dispatching.                 |
|   4 | Q manages resource quotas across namespaces and clusters, controls machine type preferences (spot/reserved), and supports fair resource sharing.   |
|   5 | Focus of the talk: fair resource sharing for expensive accelerator devices (e.g., GPUs).                                                           |
|   6 | Goal: maximize accelerator utilization and distribute limited resources dynamically based on project/team priority.                                |
|   7 | Q offers three fair resource distribution approaches:                                                                                              |
|   8 | Fair sharing with preemption: maximizes current resource usage.                                                                                    |
|   9 | Hierarchical fair sharing: determines fair distribution across organizations.                                                                      |
|  10 | Admission fair sharing: uses historical data for fair scheduling and compute access.                                                               |
|  11 | Example: Three clusterQs (CQ1, CQ2, CQ3), each with 16 GPUs, grouped in a cohort, with CQ1 weighted higher.                                        |
|  12 | Q uses Dominant Resource Share (DRS) values in fair sharing and preemption decisions.                                                              |
|  13 | When resources are scarce, Q preempts workloads from clusterQs with higher DRS values first.                                                       |
|  14 | Scheduling prioritizes workloads from clusterQs with lower DRS values.                                                                             |
|  15 | Hierarchical fair sharing demonstrated with root cohort, subcohorts, and clusterQs; preemption starts at the cohort/clusterQ with the highest DRS. |
|  16 | Admission Fair Sharing (AFS): Q admits workloads only if enough capacity and considers historically consumed resources for admission.              |
|  17 | Q takes periodic snapshots of compute usage to calculate penalties for scheduling.                                                                 |
|  18 | Penalties (exponential moving average, 50% decay) prioritize workloads with lower historical usage.                                                |
|  19 | Two penalty types: usage penalty (per scheduling cycle) and entry penalty (when workload enters cluster).                                          |
|  20 | Entry penalty addresses burs                                                                                                                       |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=dKhF-hZi7CI)
