---
layout: default
title:
  "Slurm Bridge: Slurm Scheduling Superpowers in Kubernetes - Alan Mutschelknaus
  & Tim Wickberg"
nav_order: 282
parent: Kubecon Cloudnativecon North America 2025
type: Video Note
description:
  In this presentation, Tim Wber and Alan Moouse introduce the Slurm Bridge,
  a component of the Slinky project, which integrates the Slurm HPC workload manager
  with Kubernetes to bring advanced scheduling capabilities to cloud-native environm...
resource: https://www.youtube.com/watch?v=Vi8chqAFuN0
tags:
  - kubecon-cloudnativecon-north-america-2025
  - video
  - learning
status: stable
generated:
  by: process:yt-conferences-okf
  at: 2026-09-12 00:00:00+00:00
---

# Summary

In this presentation, Tim Wber and Alan Moouse introduce the Slurm Bridge, a component of the Slinky project, which integrates the Slurm HPC workload manager with Kubernetes to bring advanced scheduling capabilities to cloud-native environments.
Slurm, widely used in supercomputing and AI training due to its multi-node scheduling and resource management, is being adapted through Slinky to coordinate with Kubernetes via modular components like the Slurm Operator and Slurm Bridge.
The Slurm Bridge leverages the Kubernetes scheduling framework to translate pod resource requests into Slurm placeholder jobs, allowing Slurm to make scheduling decisions while Kubernetes handles pod launching.
This integration supports hybrid deployments, topology-aware scheduling, and advanced resource claims, aiming to unify batch and production workloads on shared infrastructure.
The team discusses the technical challenges of mapping Kubernetes multi-node workload representations to Slurm and highlights ongoing efforts to simplify the reconciliation process between the two systems, with future improvements anticipated as Kubernetes evolves its workload primitives.

# Main Points

|   # | Main point                                                                                                                                      |
| --: | ----------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Slurm is a leading HPC workload manager, acting as both a job scheduler and resource manager.                                                   |
|   2 | Slurm manages most of the top 500 supercomputers and is widely used for AI training workloads due to its multi-node scheduling capabilities.    |
|   3 | Slurm is open source under GPL v2 or later with an OpenSSL exception.                                                                           |
|   4 | SKMD develops Slurm and Slinky, providing commercial support, training, and custom development; all SKMD products are open source.              |
|   5 | Slinky integrates Slurm with Kubernetes, acting as a toolkit of components, including the Slurm Operator and Slurm Bridge.                      |
|   6 | Slurm Bridge brings Slurm scheduling into the Kubernetes stack, using the Kubernetes scheduling framework.                                      |
|   7 | Slurm Bridge translates Kubernetes pods into Slurm placeholder jobs (external jobs) for scheduling.                                             |
|   8 | Pods are scheduled by Slurm but launched by Kubelet.                                                                                            |
|   9 | Two deployment models: hybrid nodes (both slurmd and kubelet) or external nodes (only kubelet).                                                 |
|  10 | Slurm Bridge uses Kubernetes scheduling extension points: pre-enqueue, pre-filter, filter, post-filter, and pre-bind.                           |
|  11 | Placeholder jobs in Slurm represent one or more pods; mapping is key for multi-node workloads.                                                  |
|  12 | The controller reconciles state between Kubernetes pods and Slurm placeholder jobs, ensuring synchronization and cleanup.                       |
|  13 | Slurm Bridge supports topology-aware scheduling and DRA (Device Resource Assignment) resource claims.                                           |
|  14 | Multiple Kubernetes resource types (pod group, job set, leader-worker set) can map to a single Slurm placeholder job for multi-node scheduling. |
|  15 | Demo showed Slurm Bridge running with only controller and REST API, using external nodes and DRA resource claims.                               |
|  16 | Complexity arises from translating Kubernetes multi-node constructs to Slurm's model and maintaining reconciliation.                            |
|  17 | Future improvements may include more event-driven synchronization between Slurm and Kubernetes.                                                 |
|  18 | Slurm Bridge positions Slurm as the top-level scheduler across converged infrastructure, differing from other projects like Flux.               |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=Vi8chqAFuN0)
