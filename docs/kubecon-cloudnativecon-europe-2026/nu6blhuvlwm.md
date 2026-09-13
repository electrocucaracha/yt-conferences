---
layout: default
title:
  "GPUs on Kubernetes: What Actually Happens When You Request Nvidia... Gulcan
  Topcu & Daniele Polencic"
nav_order: 130
parent: Kubecon Cloudnativecon Europe 2026
type: Video Note
description:
  The speakers introduce the complexities of using GPUs, particularly within
  Kubernetes environments. They begin by explaining foundational Linux concepts such
  as system calls, control groups (cgroups), and namespaces, which underpin containe...
resource: https://www.youtube.com/watch?v=nu6bLhuvlWM
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

The speakers introduce the complexities of using GPUs, particularly within Kubernetes environments.
They begin by explaining foundational Linux concepts such as system calls, control groups (cgroups), and namespaces, which underpin containerization technologies like Docker.
CPUs and GPUs are contrasted: CPUs handle unpredictable workloads with frequent context switching and precise memory allocation, while GPUs are optimized for predictable, repetitive tasks, executing one kernel at a time and allocating memory in large, imprecise chunks.
Unlike CPUs, GPU operations bypass the open-source Linux kernel and rely on proprietary drivers, making their inner workings less transparent.
Integrating GPUs with Kubernetes requires several additional layers—including the Nvidia driver, container toolkit, and device plugin—to expose GPU resources to containers, manage allocation, and ensure proper scheduling.
The process involves Kubernetes components recognizing GPU resources, scheduling pods accordingly, and leveraging hooks in the container runtime to inject necessary drivers and environment variables.
The talk emphasizes that running GPUs in Kubernetes is fundamentally different from standard workloads due to hardware constraints, opaque drivers, and the need for multiple integration layers, highlighting both the challenges and the importance of understanding these differences for effective deployment.

# Main Points

|   # | Main point                                                                                                              |
| --: | ----------------------------------------------------------------------------------------------------------------------- |
|   1 | Introduction by Daniele and Gutcha, instructors at Learn Q, authors of two books on GPUs and Kubernetes.                |
|   2 | Focus on basics of GPUs, their integration with Kubernetes, and associated challenges.                                  |
|   3 | Linux applications interact with hardware via system calls through the Linux kernel.                                    |
|   4 | Control groups (cgroups) limit resource usage; namespaces provide process isolation.                                    |
|   5 | Docker and similar tools abstract cgroups and namespaces to create containers.                                          |
|   6 | CPUs execute one instruction at a time; kernel manages multitasking via context switching.                              |
|   7 | CPU memory management maps virtual addresses to physical RAM; hardware handles mapping.                                 |
|   8 | GPUs differ fundamentally from CPUs; in GPU context, a "kernel" is a function running on data.                          |
|   9 | Data must be copied from RAM to GPU memory before computation; results must be copied back.                             |
|  10 | GPUs execute one kernel at a time to completion; no preemption or context switching.                                    |
|  11 | CUDA context manages GPU memory, kernel execution, and state for each process.                                          |
|  12 | Multiple programs using the same GPU each open their own CUDA context.                                                  |
|  13 | GPU memory allocation is pooled and imprecise; actual usage may be hidden from the user.                                |
|  14 | On CPUs, memory allocation is precise and managed by the Linux kernel; on GPUs, it's managed by a closed-source driver. |
|  15 | GPU driver is a black box; users have no visibility into its internal workings.                                         |
|  16 | In Kubernetes, pods are created via deployment, control plane, and kubelet.                                             |
|  17 | Three main interfaces in Kubernetes: container runtime, network, and storage interfaces.                                |
|  18 | Challenges with GPUs in Kubernetes: locating GPUs, isolating devices, driver management, and allocation.                |
|  19 | Four layers for GPU support in Kubernetes: GPU hardware, driver, Nvidia container toolkit, Nvidia device plugin.        |
|  20 | Nvidia container toolkit integrates with container runtime to expose GPU to containers.                                 |
|  21 | Nvidia device plugin registers GPU resources with kubelet and Kubernetes.                                               |
|  22 | Kubernetes scheduler allocates pods to nodes with available GPUs.                                                       |
|  23 | GPU containe                                                                                                            |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=nu6bLhuvlWM)
