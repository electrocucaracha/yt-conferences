---
layout: default
title: "Kubernetes for Multi-Host Training and Inference: Workload Aware Sc... Eric Tune & Dominik Marcinski"
nav_order: 21
parent: "Maintainer Summit 2025 - NA"
type: Video Note
description: "Eric Ton and Dominic Merchinsky from Google presented on enhancing Kubernetes scheduling for large-scale AI workloads, specifically addressing the distinct challenges of pre-training, reinforcement..."
resource: "https://www.youtube.com/watch?v=RMJYCT31yp4"
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

Eric Ton and Dominic Merchinsky from Google presented on enhancing Kubernetes scheduling for large-scale AI workloads, specifically addressing the distinct challenges of pre-training, reinforcement learning, inference, and research.
They highlighted that pre-training requires rapid recovery from hardware failures to minimize downtime, while reinforcement learning necessitates the simultaneous coordination of heterogeneous accelerator and CPU workloads.
To address these needs, the speakers introduced a new Workload API in Kubernetes 1.35 that models groups of pods as unified entities, enabling the scheduler to enforce constraints such as topology awareness and all-or-nothing placement.
This approach distinguishes between workload awareness, which ensures components understand the impact of changes on the entire job, and workload scheduling, which allows for the atomic placement of multiple pods to prevent deadlocks and resource fragmentation.
The presentation concluded with a discussion on how this core integration aims to standardize workload management, improve fair sharing, and allow external schedulers like Ray to interact seamlessly with the Kubernetes control plane.

# Main Points

|   # | Main point                                                                                                                                                |
| --: | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Eric Ton and Dominic Merchinsky from Google presented on multi-host inference and training scheduling in Kubernetes.                                      |
|   2 | Pre-training workloads are the largest, typically multi-host and multi-domain, requiring rapid detection and restart after hardware or software failures. |
|   3 | Frameworks like Torch Elastic and Jax allow applications to continue running by replacing failed components without full restarts.                        |
|   4 | Reinforcement learning is a key post-training activity involving simultaneous accelerator and CPU workloads for inference and validation.                 |
|   5 | Serving large models requires multi-pod replicas, creating a new scheduling pattern distinct from standard single-pod deployments.                        |
|   6 | Research workloads require fair sharing, preemption, and fragmentation management among multiple smaller user jobs.                                       |
|   7 | Scheduling challenges are grouped into higher throughput, application-aware orchestration, topology awareness, and extensibility.                         |
|   8 | The core Kubernetes scheduler needs to support workload-level constraints such as topology and all-or-nothing requirements.                               |
|   9 | Workload awareness requires components to understand that pods are part of a larger workload to assess the impact of changes.                             |
|  10 | Workload scheduling involves a new phase where multiple pods are scheduled together in a single cycle to produce a placement proposal.                    |
|  11 | The scheduler must accept workload placement proposals atomically to avoid deadlocks and coordinate binding in an all-or-nothing fashion.                 |
|  12 | Rescheduling should consider the current workload state to determine if partial or full restart is necessary after failures or preemption.                |
|  13 | The Workload API in Kubernetes 1.35 introduces a top-level object mapping to true controllers like JobSet or Deployment.                                  |
|  14 | Workloads can consist of single gangs, multiple named gangs, or unenumerated gangs to support dynamic scaling scenarios.                                  |
|  15 | The API supports dynamic discovery of gangs to accommodate controllers like LeaderWorkerSet without requiring full mutability initially.                  |
|  16 | Future enhancements may include vertical scale-up requirements and coordination with cluster autoscalers for resource provisioning.                       |
|  17 | The scheduling hierarchy mirrors hardware topology, matching pod groups to node groups to optimize communication costs.                                   |
|  18 | External schedulers and frameworks like Ray should integrate with the core scheduler for atomic acceptance and resource validation.                       |
|  19 | The goal is to standardize workload concepts in the core while preserving the extensibility that allows diverse controller implementations.               |

# Video

[![Video thumbnail](https://img.youtube.com/vi/RMJYCT31yp4/hqdefault.jpg)](https://www.youtube.com/watch?v=RMJYCT31yp4)

[Watch on YouTube](https://www.youtube.com/watch?v=RMJYCT31yp4)
