---
type: Video Note
title: "Achieving Peak Performance Through Hardware Alignment in DRA - Gaurav Ghildiyal & Byonggon Chun"
description: "In this session, presenters Gorov from Google and Bang from Fluid Stack discuss achieving peak performance in AI/ML workloads by aligning hardware resources—such as CPUs, GPUs, and network cards—within Kubernetes clusters. They explain how..."
resource: https://www.youtube.com/watch?v=MjVtNltfwhc
tags: ["kubecon-cloudnativecon-north-america-2025", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

In this session, presenters Gorov from Google and Bang from Fluid Stack discuss achieving peak performance in AI/ML workloads by aligning hardware resources—such as CPUs, GPUs, and network cards—within Kubernetes clusters.
They explain how modern hardware topologies, including NUMA architectures and PCIe device locality, can significantly impact application performance, with misalignment sometimes reducing throughput to as low as 40% of the maximum.
The speakers introduce Device Resource Assignment (DRA) as a solution, enabling users to specify resource locality requirements and thus avoid performance drops due to misalignment.
They share benchmarking results demonstrating the substantial benefits of proper alignment and describe how DRA drivers, including community-driven projects like DRNet, facilitate topology-aware scheduling for GPUs, NICs, and CPUs.
The session concludes with best practices for understanding hardware topology, benchmarking workloads, and leveraging DRA for granular resource control, while also highlighting ongoing community efforts to further improve alignment capabilities in Kubernetes environments.
# Main Points

|   # | Main point                                                                                                                                   |
| --: | -------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Session focuses on achieving peak performance through hardware alignment in DRRA.                                                            |
|   2 | Speakers: Gorov (Google, GK networking team, DR net project) and Bang (Fluid Stack, GPU/data center operations).                             |
|   3 | Teams invest in GPU/TPU nodes, deploy Kubernetes clusters, and run AI/ML applications.                                                       |
|   4 | Benchmarking shows inconsistent performance; worst-case drops to 41% of maximum.                                                             |
|   5 | Agenda: modern hardware topologies, misalignment problems, DRA as a solution, benchmarks, best practices, and future outlook.                |
|   6 | Hardware evolution: from single CPU/memory to shared memory/multi-CPU, then to NUMA (Non-Uniform Memory Access) to reduce memory contention. |
|   7 | NUMA: CPUs have dedicated memory; remote memory access is slower than local.                                                                 |
|   8 | Tools: numactl, lstopo, Intel MLC to analyze system topology and memory access costs.                                                        |
|   9 | GPUs and NICs are PCIe devices; PCIe topology and features (like ACS) affect performance.                                                    |
|  10 | Misalignment (e.g., GPU and NIC on different PCIe switches or NUMA nodes) causes significant performance drops.                              |
|  11 | Kubernetes previously lacked mechanisms to express hardware alignment requirements in pod specs.                                             |
|  12 | DRA (Device Resource Assignment) enables resource locality awareness and alignment in Kubernetes scheduling.                                 |
|  13 | DRA drivers advertise resource locality; users define resource claims with locality requirements; scheduler allocates accordingly.           |
|  14 | DRA ecosystem includes drivers for RDMA NICs, AI accelerators, and CPUs.                                                                     |
|  15 | Benchmark use cases:                                                                                                                         |
|  16 | GPU-NIC alignment: Misalignment can drop performance to 40% of maximum; DRA allows specifying PCIe root alignment.                           |
|  17 | CPU-GPU alignment: Misalignment drops performance to 60%; random assignment yields ~83% of max.                                              |
|  18 | CPU-NIC alignment: Misalignment yields 71% of aligned bandwidth; DRA can help, but CPU DRA driver is experimental.                           |
|  19 | Multi-node accelerator placement: Partitioning and topology constraints affect job scheduling; Nvidia DRA driver supports GB200/300 systems. |
|  20 | Best practices: Know your hardware, identify bottlenecks, use                                                                                |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=MjVtNltfwhc)