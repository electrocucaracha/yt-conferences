---
layout: default
title: "AI, CERN, and the Quest for GPU Custody: How CERN Leverages D... Diana Gaponcic & Jan-Philip Gehrcke"
nav_order: 12
parent: "Cloud Native & Kubernetes AI Day 2025 - Europe"
type: Video Note
description: "This presentation by Donna from CERN and Yan Philip from Nvidia explores the challenges of efficient GPU sharing in high-performance computing environments, specifically addressing the limitations ..."
resource: "https://www.youtube.com/watch?v=ZK5NKmua0nc"
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

This presentation by Donna from CERN and Yan Philip from Nvidia explores the challenges of efficient GPU sharing in high-performance computing environments, specifically addressing the limitations of traditional Kubernetes device plugins.
Donna explains that while CERN centralizes GPUs to maximize utilization, current methods like time slicing, MPS, and MIG require manual, per-node configuration that is inflexible and prone to idle time due to sub-optimal workloads.
Yan Philip introduces Dynamic Resource Allocation (DRA) as a solution that redefines Kubernetes' relationship with hardware by allowing users to request specific device configurations, fractions, or groups dynamically without pre-provisioning.
He highlights DRA’s ability to handle complex scenarios, such as dynamically provisioning Multi-Instance GPU (MIG) instances and establishing secure, high-bandwidth NVLink communication across nodes via a new "compute domain" primitive.
The session concludes with a live demonstration of cross-node GPU memory sharing and a discussion on DRA’s roadmap, noting that while available behind feature gates in Kubernetes 1.32, it is expected to become generally available and enabled by default in future releases.

# Main Points

|   # | Main point                                                                                                                        |
| --: | --------------------------------------------------------------------------------------------------------------------------------- |
|   1 | CERN centralizes GPUs into a common pool to maximize utilization for simulations, inference, and training.                        |
|   2 | Current GPU sharing methods like time slicing, MPS, and MIG suffer from manual configuration and per-node limitations.            |
|   3 | Time slicing involves context switching overhead and potential memory starvation between processes.                               |
|   4 | MPS provides spatial sharing with concurrent execution but requires manual node labeling for configuration.                       |
|   5 | MIG allows partitioning into isolated instances but demands pre-provisioning and manual eviction of existing workloads.           |
|   6 | Dynamic Resource Allocation (DRA) eliminates the need for pre-partitioning by enabling on-demand device configuration.            |
|   7 | DRA addresses the limitation of the traditional device plugin model, which only supports resource name and count.                 |
|   8 | DRA allows users to request specific device configurations, such as memory size or product name patterns.                         |
|   9 | DRA supports requesting groups of devices and abstract resources that span multiple nodes.                                        |
|  10 | DRA drivers are vendor-specific and required for the system to function, with NVIDIA providing a driver for GPUs.                 |
|  11 | DRA is currently behind a feature gate in Kubernetes 1.32 and is expected to be enabled by default in 1.34.                       |
|  12 | Kubernetes 1.33 will introduce support for dynamically provisioning Multi-Instance GPU (MIG) devices based on user requests.      |
|  13 | DRA enables the concept of a compute domain to facilitate high-bandwidth communication between GPUs across nodes.                 |
|  14 | The compute domain primitive securely sets up NVLink channels for multi-node workloads and handles cleanup after completion.      |
|  15 | A live demo demonstrated successful memory sharing between two GPUs on different nodes using DRA and NVLink.                      |
|  16 | Failure handling for multi-node GPU workloads remains the responsibility of the application layer for checkpointing and recovery. |
|  17 | High-bandwidth NVLink communication is primarily relevant for nodes within the same server rack or domain.                        |

# Video

[![Video thumbnail](https://img.youtube.com/vi/ZK5NKmua0nc/hqdefault.jpg)](https://www.youtube.com/watch?v=ZK5NKmua0nc)

[Watch on YouTube](https://www.youtube.com/watch?v=ZK5NKmua0nc)
