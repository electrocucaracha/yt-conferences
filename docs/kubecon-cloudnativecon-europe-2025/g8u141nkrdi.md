---
layout: default
title:
  Advancements in AI/ML Inference Workloads on Kubernetes From... Yuan Tang &
  Eduardo Arango Gutierrez
nav_order: 14
parent: Kubecon Cloudnativecon Europe 2025
type: Video Note
description:
  "The working group serving aims to enhance Kubernetes controllers and
  low-level components to make it easier for users to run Serbian workloads on Kubernetes.
  The group focuses on three main goals: enhancing Kubernetes controllers, investiga..."
resource: https://www.youtube.com/watch?v=G8U141NkrDI
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

The working group serving aims to enhance Kubernetes controllers and low-level components to make it easier for users to run Serbian workloads on Kubernetes.
The group focuses on three main goals: enhancing Kubernetes controllers, investigating orchestration and scalability, and exposing ways for pods to share resources like GPUs or communicate across multiple hosts.
The group is led by four co-chairs from Google Cloud, Red Hat, Nvidia, and Bit Dance, with over 330 members on Slack.
They have created a benchmark tool called inference perf to understand what impacts the performance of large language models, and are working on standards for caching and image volume sources to optimize performance.

# Main Points

|   # | Main point                                                                                                                                                   |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   1 | The working group serving aims to enhance Kubernetes controllers and make it easier to run Serbian workloads on Kubernetes.                                  |
|   2 | The group focuses on three main goals:                                                                                                                       |
|   3 | Investigating orchestration and scalability                                                                                                                  |
|   4 | Improving low-level container runtime bits (DRA) and exposing ways for pods to share resources                                                               |
|   5 | Enhancing dynamic resource allocation                                                                                                                        |
|   6 | The working group is led by multiple companies, including Google Cloud, Red Hat, Nvidia, and Bit Dance.                                                      |
|   7 | There are four work streams: autoscaling, multi-host and multi-node, dynamic resource allocation, and orchestration.                                         |
|   8 | The autoscaling work stream focuses on benchmarking and investigating metrics for autoscaling.                                                               |
|   9 | The multi-host and multi-node work stream addresses distributed workload management and scalability.                                                         |
|  10 | The dynamic resource allocation work stream aims to improve resource utilization and reduce latency.                                                         |
|  11 | The orchestration work stream explores the gateway API inference extension (GEE) and its potential for improving resource sharing across multiple use cases. |
|  12 | The community has been actively discussing caching and performance optimization, with a focus on standardizing metrics and tools.                            |
|  13 | The working group is open to feedback and contributions from vendors and end users.                                                                          |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=G8U141NkrDI)
