---
layout: default
title: "Unlocking Performance: Topology-Aware CPU Scheduling W... Praveen Krishna & Marlow Warnicke (Weston)"
nav_order: 7
parent: "Maintainer Summit 2025 - NA"
type: Video Note
description: "Tim Wikberg and Pine from Google presented a solution to address the performance degradation caused by misaligned CPU, GPU, and network resources in Kubernetes."
resource: "https://www.youtube.com/watch?v=1JO_73pVrLI"
tags:
  - maintainer-summit-2025-na
  - video
  - learning
status: stable
generated:
  by: process:yt-summarizer-okf
  at: 2026-11-16T17:23:58+00:00
---

# Summary

Tim Wikberg and Pine from Google presented a solution to address the performance degradation caused by misaligned CPU, GPU, and network resources in Kubernetes.
They explained that the current scheduling model lacks visibility into node micro-topology, leading to suboptimal placement for HPC and AI workloads that require strict hardware alignment.
To solve this, they introduced an open-source CPU DRA (Dynamic Resource Allocation) driver that exposes detailed CPU topology attributes, such as core type and L3 cache, allowing for precise resource requests.
A live demo demonstrated that this driver successfully aligns CPUs with GPUs and RDMA NICs on the same NUMA node, significantly improving performance compared to the standard kubelet static CPU policy.
The speakers also discussed ongoing efforts to coordinate DRA with existing Kubernetes mechanisms for proper resource accounting, preemption, and potential future extensions to memory and huge pages.

# Main Points

|   # | Main point                                                                                                                                                                                       |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   1 | Tim Wikberg, CTO of SchedMD, presented on using the Dynamic Resource Allocation (DRA) subsystem to improve CPU topology scheduling in Kubernetes.                                                |
|   2 | Current Kubernetes scheduling treats CPUs and memory as coarse-grained resources, leading to a disconnect between central scheduling and node-level binding by kubelet.                          |
|   3 | This misalignment between CPU allocation and GPU or NIC placement causes significant performance degradation, with benchmarks showing 10% to 40% latency or performance differences.             |
|   4 | HPC and AI workloads require precise hardware alignment, such as placing CPUs on the same NUMA node or PCIe switch as GPUs, which standard Kubernetes pod specs do not support.                  |
|   5 | The proposed solution is an open-source CPU DRA driver that allows precise requests for native resources like specific CPU cores, L3 caches, and NUMA nodes.                                     |
|   6 | The driver operates as a daemonset and requires the kubelet static CPU policy to be disabled to prevent conflicting cgroup management between kubelet and the DRA driver.                        |
|   7 | The driver publishes resource slices that expose detailed micro-topology attributes, including CPU ID, core type, and cache information, enabling the scheduler to view node hardware specifics. |
|   8 | Alternative modeling approaches, such as exposing socket-level capacity, are supported to improve scalability for larger clusters where per-CPU device exposure is too granular.                 |
|   9 | The architecture involves a kubelet plugin for handling DRA requests and an NRI plugin for enforcing cgroup settings and CPU pinning during container runtime.                                   |
|  10 | A live demo demonstrated that the DRA driver successfully aligns CPUs with GPUs and NICs on the same NUMA node, whereas standard kubelet static policy resulted in misaligned allocations.       |
|  11 | Use cases include resource alignment, fine-grained core type selection (performance vs. efficiency), and prioritized resource requests using DRA features.                                       |
|  12 | Ongoing challenges include coordinating accounting between DRA and standard pod specs, defining standard attributes for alignment, and addressing fragmentation issues.                          |
|  13 | The project aims to provide internal plumbing for schedulers like Slurm to enforce directed placement, rather than requiring end users to construct complex low-level resource claims.           |
|  14 | Future work includes exploring DRA for memory and huge pages, improving preemption logic based on DRA requests, and clarifying the transition from extended resources to full DRA mode.          |

# Video

[![Video thumbnail](https://img.youtube.com/vi/1JO_73pVrLI/hqdefault.jpg)](https://www.youtube.com/watch?v=1JO_73pVrLI)

[Watch on YouTube](https://www.youtube.com/watch?v=1JO_73pVrLI)
