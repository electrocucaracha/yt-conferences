---
layout: default
title:
  The Latest in GPU, TPU, NIC and Other Device Support - WG Device Ma... John
  Belamaric & Patrick Ohly
nav_order: 362
parent: Kubecon Cloudnativecon Europe 2026
type: Video Note
description:
  The working group device management meeting, led by engineers from Intel,
  Google, and Nvidia, provided an update on the progress and future plans for Dynamic
  Resource Allocation (DRA) in Kubernetes. The group was formed to address limitatio...
resource: https://www.youtube.com/watch?v=MAwL8A1WCjw
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

The working group device management meeting, led by engineers from Intel, Google, and Nvidia, provided an update on the progress and future plans for Dynamic Resource Allocation (DRA) in Kubernetes.
The group was formed to address limitations in the device plug-in interface, aiming to simplify and improve the management and allocation of hardware accelerators like GPUs and TPUs through a more flexible API.
DRA, now generally available, introduces the resource slice and resource claim APIs to describe and allocate devices, enabling advanced scheduling and configuration, including support for partitionable devices and workload-aware scheduling.
Ongoing efforts focus on integrating native resources such as CPU and memory, enhancing support for complex hardware topologies, expanding the API to cover more device types and use cases, and improving day-two operations like device failure handling.
The session also highlighted recent contributions from new community members and announced that Nvidia and Google are donating their DRA drivers to the Kubernetes project, encouraging broader participation and further innovation in device management.

# Main Points

|   # | Main point                                                                                                                                                     |
| --: | -------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Working group focuses on dynamic resource allocation (DRA) in Kubernetes to improve device management, especially for accelerators.                            |
|   2 | DRA was created as an alternative to the device plug-in interface for more flexible hardware configuration and allocation.                                     |
|   3 | DRA is now generally available (GA); resource slice API describes devices on nodes, while resource claim API lets users request specific resources.            |
|   4 | Scheduler selects suitable devices based on resource claims; kubelet and container runtime make devices available to pods.                                     |
|   5 | DRA supports integration with NRI and CDI, offering flexibility inside the node.                                                                               |
|   6 | Current work includes aligning multiple device types (GPU, NIC, CPU) within nodes for optimal performance.                                                     |
|   7 | Efforts are underway to bring native resources (CPU, memory) under DRA management, moving scheduling decisions earlier to avoid late binding failures.         |
|   8 | Integration with SIG Scheduling’s workload-aware scheduling and pod group concepts enables gang scheduling and topological placement for multi-node workloads. |
|   9 | Expanding resource slice API to model more device types and use cases, including partitionable devices and bandwidth regulation for virtualized functions.     |
|  10 | Addressing current gaps such as lack of preemptibility for DRA-managed pods, targeted for Kubernetes 1.37.                                                     |
|  11 | Nvidia is donating GPU and compute domain DRA drivers; Google is donating a TPU driver; CPU driver is also available for DRA management.                       |
|  12 | DRA allows users to supply custom parameters in resource claims for advanced configuration (e.g., multi-instance GPUs, time slicing).                          |
|  13 | New contributors have implemented features like resource pool status API and metadata injection.                                                               |
|  14 | Working group meetings are held regularly with global participation; more contributors are welcome.                                                            |
|  15 | Partitionable devices feature is moving to beta in 1.36 after API improvements for scalability.                                                                |
|  16 | Resource slice API is designed for vendor use and expressiveness; resource claim API aims for user simplicity.                                                 |
|  17 | Examp                                                                                                                                                          |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=MAwL8A1WCjw)
