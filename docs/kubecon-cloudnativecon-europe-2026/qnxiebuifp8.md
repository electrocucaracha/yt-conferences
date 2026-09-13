---
layout: default
title:
  "The Symbiosis of Storage and Workloads: Longhorn for Hyperconverged Bl...
  Jinhong Kim & Jangseon Ryu"
nav_order: 369
parent: Kubecon Cloudnativecon Europe 2026
type: Video Note
description:
  In this presentation, the speakers from Naver, a leading South Korean
  internet company, discuss the challenges of operating large-scale storage for distributed
  applications and how they addressed these issues by adopting a hyper-converged s...
resource: https://www.youtube.com/watch?v=qNxIebuifp8
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

In this presentation, the speakers from Naver, a leading South Korean internet company, discuss the challenges of operating large-scale storage for distributed applications and how they addressed these issues by adopting a hyper-converged storage model using Longhorn.
They explain that their previous centralized storage system led to cost inefficiency due to redundant replication and performance interference among workloads, while local disks introduced node locking and operational complexity.
To overcome these problems, they implemented a flexible model that combines the strengths of both centralized and local storage, focusing on five key goals: flexible replication, improved workload isolation, locality with service continuity, coordinated scheduling, and storage mobility.
By leveraging Longhorn’s data locality features and Kubernetes’ CSI storage capacity, they improved scheduling decisions to better align storage and workload placement, though they identified limitations in Kubernetes’ default scheduling, particularly for rescheduling events.
To address this, they developed a custom scheduler that considers both storage capacity and the location of existing replicas, enhancing storage-aware scheduling for hyper-converged environments.

# Main Points

|   # | Main point                                                                                                                                                                                                 |
| --: | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Presented experience operating large-scale storage at Naver, a leading South Korean internet company.                                                                                                      |
|   2 | Naver operates Kubernetes across ~60,000 nodes, 900,000 pods, and a storage platform with 5,000 nodes, 50,000 disks, 100 PB capacity, and 250,000 persistent volumes.                                      |
|   3 | Centralized storage (SE) works well for many workloads but is inefficient for distributed applications that handle their own replication.                                                                  |
|   4 | Main challenges identified: cost inefficiency (due to duplicate replication), performance interference (shared storage events impact latency), and operational complexity (node locking with local disks). |
|   5 | Needed a model combining centralized and local storage strengths; adopted a hyper-converged approach.                                                                                                      |
|   6 | Defined five key goals: flexible replication, better workload isolation, locality with service continuity, coordinated scheduling, and storage mobility.                                                   |
|   7 | Evaluated CNCF storage projects and chose Longhorn for its cloud-native, distributed block storage capabilities.                                                                                           |
|   8 | Longhorn uses local disks, exposes storage via CSI, and manages replica rebuilds and volume lifecycle.                                                                                                     |
|   9 | Coordinated scheduling is critical: aligning pod and storage placement to maintain locality and avoid unnecessary rebuilding.                                                                              |
|  10 | Longhorn offers data locality options: disabled, best effort, and strict; "best effort" chosen for flexibility and locality.                                                                               |
|  11 | Kubernetes’ default scheduler is unaware of storage capacity, leading to potential placement issues.                                                                                                       |
|  12 | CSI Storage Capacity enables Kubernetes to consider storage availability during scheduling.                                                                                                                |
|  13 | CSI Storage Capacity helps with initial pod placement but not with rescheduling after volumes are bound.                                                                                                   |
|  14 | Identified need for storage-aware scheduling that considers both capacity and replica locality.                                                                                                            |
|  15 | Developed a custom scheduler framework to prefer nodes with existing replicas and fallback to capacity-based placement.                                                                                    |
|  16 | Custom scheduler is being tested internally; aims to improve hyper-converged storage operations.                                                                                                           |
|  17 | Key takeaways: consider                                                                                                                                                                                    |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=qNxIebuifp8)
