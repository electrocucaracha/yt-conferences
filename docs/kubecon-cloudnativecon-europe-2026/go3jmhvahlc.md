---
layout: default
title:
  "To Swap or Not To Swap: Memory Management Design Patterns for AI Workloads
  in Kuber... Nic Vermande"
nav_order: 373
parent: Kubecon Cloudnativecon Europe 2026
type: Video Note
description:
  In this talk, Nick from Scaleups discusses the complexities and trade-offs
  of enabling swap on Kubernetes nodes for running large language model (LLM) workloads.
  He explains that while enabling swap can prevent out-of-memory (OM) kills and...
resource: https://www.youtube.com/watch?v=Go3JMhvAhlc
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

In this talk, Nick from Scaleups discusses the complexities and trade-offs of enabling swap on Kubernetes nodes for running large language model (LLM) workloads.
He explains that while enabling swap can prevent out-of-memory (OM) kills and keep services alive during memory spikes—especially in bursty or multimodel serving scenarios—it can also cause significant latency degradation if misconfigured, particularly with unlimited swap or insufficient resource limits.
Nick details the evolution of Kubernetes swap support, emphasizing the importance of using limited swap with NVMe storage and configuring quality of service (QoS) classes appropriately: guaranteed pods should have swap disabled, while burstable pods can benefit from proportional swap allocations.
He highlights that swap should be seen as a last line of defense after application-level memory management, and that careful monitoring and right-sizing of both memory requests and swap entitlements are crucial to avoid performance collapse.
Ultimately, the decision to use swap depends on workload latency sensitivity and cost considerations, and Nick provides a decision framework to guide when and how to enable swap for AI workloads in Kubernetes environments.

# Main Points

|   # | Main point                                                                                                                                |
| --: | ----------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Enabling swap on Kubernetes nodes can cause up to 8x latency degradation and 1.6 GB of memory thrashing if misconfigured.                 |
|   2 | Disabling swap can lead to immediate Out-Of-Memory (OM) kills and service outages.                                                        |
|   3 | The main risk with swap is OM kill or node failure due to swap exhaustion.                                                                |
|   4 | Unlimited swap was removed in Kubernetes 1.30 due to risk of a single pod exhausting swap and crashing the node.                          |
|   5 | Limited swap is now stable as of Kubernetes 1.34, is container-aware, and works within cgroup v2 boundaries.                              |
|   6 | Three Quality of Service (QoS) classes affect swap behavior:                                                                              |
|   7 | Guaranteed: no swap allowed.                                                                                                              |
|   8 | Burstable: proportional swap based on memory request.                                                                                     |
|   9 | BestEffort: no swap allocation.                                                                                                           |
|  10 | AI workloads differ from traditional web services due to unpredictable and dynamic memory usage.                                          |
|  11 | LLM inference requires both GPU VRAM (for model weights) and CPU RAM (for runtime, KV cache, tokenizer, etc.).                            |
|  12 | During traffic spikes, CPU memory demand can exceed cgroup limits, risking OM kills.                                                      |
|  13 | Two options: provision for peak (wastes resources) or average (risk OM kills); swap offers a third option if configured correctly.        |
|  14 | Memory hierarchy: L1 (GPU VRAM), L2 (VLM CPU memory pool), L3 (Kubernetes swap on disk).                                                  |
|  15 | Always prefer higher-level (faster) memory management; Kubernetes swap is a last-resort safety net.                                       |
|  16 | Scenario 1: Multimodel serving benefits from swap—prevents OM kills during brief memory spikes, saves cost.                               |
|  17 | Scenario 2: Sudden traffic spikes—swap keeps services alive during bursts, but requires correct CPU limits.                               |
|  18 | Scenario 3: Latency-sensitive inference and training—swap can destroy performance; avoid swap for these workloads.                        |
|  19 | Use NVMe for swap, never spinning disks.                                                                                                  |
|  20 | Monitor swap usage and set alerts for swap bytes and IO counts.                                                                           |
|  21 | Decision framework: use limited swap for burstable/multimodel workloads, avoid for real-time/training, never for databases/control plane. |
|  22 | Audit node memory, classify workloads by latency sensitivity, enable limited swap in                                                      |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=Go3JMhvAhlc)
