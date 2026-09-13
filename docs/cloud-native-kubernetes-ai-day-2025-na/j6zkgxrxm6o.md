---
layout: default
title:
  "Fit-to-Serve: How a New DRA Capability for Dynamic Device... Sunyanan Choochotkaew
  & Tatsuhiro Chiba"
nav_order: 4
parent: Cloud Native Kubernetes Ai Day 2025 Na
type: Video Note
description:
  The presentation discusses optimizing distributed AI model inference
  serving, focusing on resource allocation and scheduling challenges in Kubernetes
  environments. The speakers highlight the complexity of balancing workloads due to
  varying...
resource: https://www.youtube.com/watch?v=j6zkGxrxm6o
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

The presentation discusses optimizing distributed AI model inference serving, focusing on resource allocation and scheduling challenges in Kubernetes environments.
The speakers highlight the complexity of balancing workloads due to varying model sizes, input/output requirements, and hardware constraints, emphasizing that simply increasing GPU resources does not always yield better performance or utilization.
They introduce the Device Resource Allocation (DRA) framework and its new consumable capacity feature, which allows more flexible and granular allocation of device resources—such as partitioning GPUs for multiple workloads and sharing resources more efficiently.
Through a demonstration, they show how DRA enables dynamic allocation and scheduling of GPU resources based on actual workload needs, preventing both underutilization and resource contention.
The talk concludes by encouraging feedback and further exploration of these features to improve large-scale AI inference serving.

# Main Points

|   # | Main point                                                                                                                                                              |
| --: | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Discussion focuses on improving diamond schedule scaling of AI model serving using new DRA (Device Resource Allocation) capability.                                     |
|   2 | Distributed inference at scale requires sophisticated load balancing and routing due to non-uniform workloads and varying input/output sizes.                           |
|   3 | LMD provides a Kubernetes-native way to run distributed inference at scale, optimizing for cache location and resource allocation.                                      |
|   4 | Scaling distributed inference involves tuning model hosting, tensor parallelism, disaggregation methods, and hardware selection (CPU, GPU, TPU).                        |
|   5 | Estimating required GPU compute and memory resources to meet SLOs is complex due to model size and workload dependencies.                                               |
|   6 | Experiments show increasing GPU count does not always improve latency; optimal resource allocation is model-dependent.                                                  |
|   7 | GPU resources are often underutilized or overestimated; returning unused resources to the pool is beneficial.                                                           |
|   8 | Previous work includes adaptive resource optimization by predicting usage and adjusting GPU allocation dynamically.                                                     |
|   9 | Scaling granularity matters: options include single GPU, MIG (Multi-Instance GPU), and dynamic allocation via APIs for zero-scale inference.                            |
|  10 | Device plug-ins register hardware resources with Kubernetes; current methods require pre-configuration for mixed slices and time slicing.                               |
|  11 | Limitations of current device plug-in management include need for pre-configuration, lack of fine-grained sharing guarantees, and requirement for secondary schedulers. |
|  12 | DRA moves device selection decisions from kubelet/device plug-in to the scheduler, enabling more flexible resource allocation.                                          |
|  13 | Consumable capacity feature in DRA allows allocating a device to multiple resource claims and partitioning device capacity (e.g., virtual GPU memory).                  |
|  14 | DRA supports sharing devices among multiple pods, bandwidth-limited network allocations, and potential IO/native resource requests.                                     |
|  15 | Demo shows DRA allocating GPU resources to small, medium, and large models based on defined capa                                                                        |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=j6zkGxrxm6o)
