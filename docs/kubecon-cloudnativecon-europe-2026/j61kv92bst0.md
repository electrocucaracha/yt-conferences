---
type: Video Note
title: "Peeking Into the GPU Black Box: Continuous Profiling on Kubernetes With eBPF - Zahari Dichev"
description: "In this talk, Zahari, a software engineer at Buoyant, discusses the challenges of gaining observability into GPU usage within Kubernetes clusters, especially given the high costs and scarcity of GPU resources. He explains that while existin..."
resource: https://www.youtube.com/watch?v=J61kV92bSt0
tags: ["kubecon-cloudnativecon-europe-2026", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

In this talk, Zahari, a software engineer at Buoyant, discusses the challenges of gaining observability into GPU usage within Kubernetes clusters, especially given the high costs and scarcity of GPU resources.
He explains that while existing tools like Nvidia SMI and DCGM provide only basic, hardware-centric metrics, and advanced profilers like Nsite are too intrusive for production, there remains a significant gap compared to CPU observability.
Zahari introduces the use of eBPF uprobes to monitor application interactions with GPU device drivers, enabling the collection of higher-level metrics such as demand (kernel launches), back pressure (synchronization wait times), and contention (multi-process usage).
Through real-world incident examples, he demonstrates how these metrics can help operators distinguish between application and environment issues affecting GPU workloads.
However, he notes the limitations of current approaches, emphasizing the need for hardware vendors to provide better, low-overhead observability APIs to support cloud-native GPU usage and optimization.
# Main Points

|   # | Main point                                                                                                                                                                     |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   1 | Zahari, software engineer at Buoyant, presents on GPU observability using eBPF in Kubernetes clusters.                                                                         |
|   2 | GPU introspection is increasingly important due to high demand and cost of GPU hardware.                                                                                       |
|   3 | Existing GPU observability tools (Nvidia SMI, DCGM) provide only hardware-centric, node-level metrics (utilization, memory, temperature), lacking per-pod granularity.         |
|   4 | Advanced profilers like Nvidia Nsight offer deep insights but are unsuitable for production due to high overhead and manual operation.                                         |
|   5 | eBPF allows tracing of user-space function calls in device driver libraries (e.g., libcudart), enabling monitoring of GPU interactions at the process level.                   |
|   6 | Tools like Polar Signals and Grafana Bala use eBPF and Nvidia CUPTI to collect low-level GPU metrics (kernel launches, memory transfers) but still provide raw, granular data. |
|   7 | Research projects like Unomia BPF Time use eBPF with PTX instrumentation for advanced profiling but are intrusive and not production-ready.                                    |
|   8 | Operators need higher-level metrics to diagnose workload issues, not just raw traces.                                                                                          |
|   9 | Proposed key metrics:                                                                                                                                                          |
|  10 | GPU demand: kernel launches per second (work enqueued to GPU)                                                                                                                  |
|  11 | GPU back pressure: time host waits for device (synchronization delays)                                                                                                         |
|  12 | GPU contention: number of processes sharing the device                                                                                                                         |
|  13 | eBPF uprobes/uretprobes can collect these metrics by attaching to relevant driver functions for containerized workloads.                                                       |
|  14 | Profiling agent runs as a DaemonSet, monitors processes, attaches probes, aggregates events, and exports Prometheus metrics for visualization.                                 |
|  15 | Example incidents show how these metrics help distinguish between application and environment issues (e.g., logging changes, noisy neighbors, CPU bottlenecks).                |
|  16 | Limitations: eBPF cannot capture actual GPU execution times, kernel-level attribution, or fine-grained utilization due to GPU asynchrony and API boundaries.                   |
|  17 | Hardware vendors should provide better, low-overhead, multi-tenant observability APIs for GPUs.                                                                                |
|  18 | There is a signific                                                                                                                                                            |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=J61kV92bSt0)