---
layout: default
title:
  "Making Topology-Aware Scheduling Practical for AI Workloads: From Discovery
  to Simula... Weizhou Lan"
nav_order: 216
parent: Kubecon Cloudnativecon Europe 2026
type: Video Note
description:
  In this session, Wulan, a senior tech lead at docloud, discusses making
  topology-aware scheduling practical for AI workloads, emphasizing the importance
  of network topology discovery and cost-effective validation approaches. He explains
  tha...
resource: https://www.youtube.com/watch?v=Jj8DNLA5hYc
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

In this session, Wulan, a senior tech lead at docloud, discusses making topology-aware scheduling practical for AI workloads, emphasizing the importance of network topology discovery and cost-effective validation approaches.
He explains that AI models, especially in large-scale clusters, generate significant network traffic, making it crucial to schedule workloads based on network topology to avoid congestion and ensure efficient communication.
Traditional scheduling methods using node labels and affinities are inadequate due to manual overhead, lack of dynamic awareness, and inability to represent hierarchical topologies.
Wulan reviews advanced schedulers like Q, Volcano, and K-Scheduler, which support hierarchical topology constraints and automate topology mapping, but notes their reliance on accurate node labels.
He highlights the need for automated topology detectors, such as Nvidia Topograph or custom builders using protocols like gNMI, to maintain up-to-date topology information.
For validation and testing, he recommends simulation tools like Cork and Nvidia Air, which allow for scalable, realistic testing environments without the need for extensive physical infrastructure.

# Main Points

|   # | Main point                                                                                                                                                                            |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | The session discusses making topology-aware scheduling practical for AI workloads, covering network topology discovery and cost-effective validation approaches.                      |
|   2 | Model chaining scenarios generate high network communication volumes, especially among GPUs.                                                                                          |
|   3 | Conventional dense models mostly use local traffic handled by leaf switches.                                                                                                          |
|   4 | Expert models (e.g., DeepSeek) create intensive all-to-all communication, traversing higher-level switches.                                                                           |
|   5 | Proper workload placement according to topology is necessary to avoid network congestion in large clusters.                                                                           |
|   6 | Inference scenarios involve complex RDMA traffic patterns, requiring topologically close node placement to minimize conflicts.                                                        |
|   7 | Multi-tenant environments require dynamic scaling across nodes, making topology awareness essential to prevent network contention and unfair resource allocation.                     |
|   8 | Three core scheduling strategies: task isolation, affinity (minimizing communication distance), and network health awareness (monitoring and rescheduling on failures).               |
|   9 | Objectives: guarantee job SLAs, minimize communication latency, maximize network infrastructure utilization, and ensure fairness among tenants.                                       |
|  10 | Native Kubernetes node affinity is unsuitable for AI workloads due to manual orchestration overhead, static labels, lack of hierarchical/global view, and risk of resource deadlocks. |
|  11 | Core requirements for topology-aware scheduling: hierarchical topology view, hard/soft topology constraints, and optimized switch paths for communication.                            |
|  12 | Open-source schedulers supporting topology-aware scheduling: Volcano, KAI Scheduler, and Q.                                                                                           |
|  13 | Q enhances native Kubernetes scheduling by using node labels and constraints to guide placement.                                                                                      |
|  14 | Volcano builds logical topology chains and integrates InfiniBand topology discovery, reducing manual labeling.                                                                        |
|  15 | KAI Scheduler uses topology CRDs and supports subgroup constraints for affinity-sensitive workloads.                                                                                  |
|  16 | Accurate node labeling is critical; manual labeling is unreliable at scale.                                                                                                           |
|  17 | Topo                                                                                                                                                                                  |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=Jj8DNLA5hYc)
