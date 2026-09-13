---
layout: default
title:
  Optimizing Error Recovery for Cost-Ef... Radostin Stoyanov, Andrey Velichkevich
  & Viktória Spišáková
nav_order: 237
parent: Kubecon Cloudnativecon Europe 2026
type: Video Note
description:
  The presentation discusses research on optimizing error recovery for
  distributed AI model training using Kubernetes, focusing on transparent infrastructure-level
  checkpointing to minimize compute loss from failures. The team highlights real...
resource: https://www.youtube.com/watch?v=pvonHzx-z0o
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

The presentation discusses research on optimizing error recovery for distributed AI model training using Kubernetes, focusing on transparent infrastructure-level checkpointing to minimize compute loss from failures.
The team highlights real-world issues, such as a 34-day protein structure prediction job lost due to lack of recovery mechanisms, and explains that distributed workloads are especially vulnerable to failures in any component.
They categorize failures into infrastructure, AI engine, and user errors, noting that these can lead to significant interruptions and financial losses.
Their work centers on improving GPU checkpointing by integrating compression and deduplication techniques to reduce checkpoint size and restore time, and by enabling more efficient deployment within Kubernetes and the Kubeflow ecosystem.
The team demonstrates how their approach allows for suspending and resuming distributed training jobs with minimal overhead, and discusses ongoing efforts to integrate these features into open-source tools, inviting community collaboration for further development.

# Main Points

|   # | Main point                                                                                                                                                                       |
| --: | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Discussed optimizing error recovery for cost-efficient distributed AM model training with Kubernetes.                                                                            |
|   2 | Real scenario: 34-day protein structure prediction job lost due to node overheating and lack of recovery/checkpointing.                                                          |
|   3 | Distributed workloads amplify failure consequences, especially with many GPUs.                                                                                                   |
|   4 | Distributed workloads require gang scheduling; failure of any task can stall or kill the job.                                                                                    |
|   5 | Three main failure categories: infrastructure failures (e.g., network, file system), AI engine failures (e.g., CUDA errors), and user errors (e.g., misconfigurations).          |
|   6 | Failures in distributed training can lead to significant compute cost losses.                                                                                                    |
|   7 | Two main recovery methods: model checkpoints (user code, can cause overhead and GPU idle time) and infrastructure checkpoints (system-level, transparent, no user code changes). |
|   8 | Focus is on infrastructure checkpoints for distributed workloads.                                                                                                                |
|   9 | Explored transparent checkpointing and GPU checkpointing in Kubernetes.                                                                                                          |
|  10 | GPU checkpointing involves locking GPU computation, saving GPU state to host memory, and restoring it.                                                                           |
|  11 | Improved deployment by integrating CUDA checkpoint/restore APIs directly, removing need for external binaries.                                                                   |
|  12 | Disk I/O is a bottleneck for checkpointing; integrated compression to reduce checkpoint size and I/O.                                                                            |
|  13 | Optimized by skipping incompressible and zero-byte memory pages during checkpointing.                                                                                            |
|  14 | Achieved significant checkpoint size reduction and faster restore times, especially for inference workloads.                                                                     |
|  15 | For training jobs, implemented deduplication by checksumming GPU memory to save only changed data.                                                                               |
|  16 | Deduplication reduces checkpoint size by up to 90% for quantized/fine-tuned models; less effective for full precision training.                                                  |
|  17 | Integrated GPU checkpointing across the stack: Linux kernel, GPU driver, Kubernetes, and Python SDK (Kubeflow).                                                                  |
|  18 | Extended train job controller to trigger checkpointing on suspend/resume, supporting preemption and manual suspension.                                                           |
|  19 | Checkpoints saved as archives, convert                                                                                                                                           |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=pvonHzx-z0o)
