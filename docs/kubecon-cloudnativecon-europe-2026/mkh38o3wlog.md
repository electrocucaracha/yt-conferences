---
layout: default
title:
  "Hacking GPU Observability: eBPF & Ephemeral Containers in Action on Kubernetes
  - Brandon Kang"
nav_order: 136
parent: Kubecon Cloudnativecon Europe 2026
type: Video Note
description:
  In this presentation, Brendan from Akami discusses the challenges of
  monitoring and debugging GPU workloads in Kubernetes environments, emphasizing that
  GPUs often fail silently and traditional monitoring tools like Nvidia's DCGM only
  provi...
resource: https://www.youtube.com/watch?v=mkH38O3wLog
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

In this presentation, Brendan from Akami discusses the challenges of monitoring and debugging GPU workloads in Kubernetes environments, emphasizing that GPUs often fail silently and traditional monitoring tools like Nvidia's DCGM only provide hardware-level metrics without revealing root causes of performance issues.
He explains that GPU workloads differ significantly from CPU workloads, with problems such as throttling, memory bottlenecks, and data movement delays often going undetected by standard tools.
Brendan introduces eBPF, a Linux kernel technology, as a solution for deeper observability, allowing real-time monitoring of application, driver, and kernel interactions without modifying application code or breaking Kubernetes principles.
He demonstrates how eBPF can be used to trace CUDA runtime events and data transfers, improving both performance troubleshooting and security by detecting abnormal behaviors like unauthorized crypto mining.
Brendan also recommends using ephemeral containers for safe debugging in production, and outlines a layered architecture for full-stack GPU observability, combining DCGM, eBPF, and open-source tools to achieve comprehensive visibility and secure, cloud-native machine learning infrastructure.

# Main Points

|   # | Main point                                                                                                                                                       |
| --: | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | GPUs fail silently and unpredictably, unlike CPUs.                                                                                                               |
|   2 | Traditional GPU monitoring tools (e.g., Nvidia SMI, DCGM) provide hardware metrics like utilization, temperature, and memory usage but lack root cause analysis. |
|   3 | Hardware-level observability creates a "visibility illusion"—you see what happened, not why.                                                                     |
|   4 | GPU workloads are less predictable and more complex than CPU workloads.                                                                                          |
|   5 | Many GPU issues (e.g., throttling, contention, data movement delays) are not visible with standard tools.                                                        |
|   6 | Performance bottlenecks can occur in layers between application and hardware, such as CUDA runtime and driver layers.                                            |
|   7 | Traditional tools do not provide visibility into kernel-level events or application-GPU interactions.                                                            |
|   8 | Security risks exist due to lack of observability at the CUDA runtime level (e.g., unauthorized compute, crypto mining, abnormal memory transfers).              |
|   9 | Legacy profilers require code changes, introduce overhead, and break Kubernetes immutability principles.                                                         |
|  10 | eBPF (extended Berkeley Packet Filter) enables programmable, high-performance observability in the Linux kernel without modifying application code.              |
|  11 | eBPF can monitor system behavior across application, kernel, driver, and hardware layers in real time.                                                           |
|  12 | eBPF works regardless of framework (PyTorch, TensorFlow, etc.) and avoids vendor lock-in.                                                                        |
|  13 | eBPF-based monitoring can be implemented as a DaemonSet on Kubernetes worker nodes.                                                                              |
|  14 | Metrics collected via eBPF can be visualized in Grafana dashboards.                                                                                              |
|  15 | eBPF enables tracing of CUDA runtime functions (e.g., cudaLaunchKernel, cudaMemcpy) for deeper insight into performance and security issues.                     |
|  16 | Ephemeral containers can be used for safe debugging in production without modifying running applications.                                                        |
|  17 | Suggested workflow: detect issues with DCGM/eBPF, deploy ephemeral container for debugging, analyze, and fix without downtime.                                   |
|  18 | Full-stack GPU observability architecture includes visibility, telemetry, runtime tracing, security, and hardware layers.                                        |
|  19 | Open source tools                                                                                                                                                |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=mkH38O3wLog)
