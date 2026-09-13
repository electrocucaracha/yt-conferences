---
type: Video Note
title: "Partitionable Devices: Putting the “Dynamic” Back in... Morten Jæger Torkildsen & Jan-Philip Gehrcke"
description: "In this session, Morton Torlson from Google and Yan Phillip from Nvidia discuss the challenges and advancements in dynamic resource allocation for GPUs within Kubernetes, focusing on partitionable devices and the Device Resource Assignment..."
resource: https://www.youtube.com/watch?v=5GIDHxwQGiM
tags: ["kubecon-cloudnativecon-north-america-2025", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

In this session, Morton Torlson from Google and Yan Phillip from Nvidia discuss the challenges and advancements in dynamic resource allocation for GPUs within Kubernetes, focusing on partitionable devices and the Device Resource Assignment (DRA) framework.
They explain that traditional device plug-ins only allow static, full-GPU allocation, which leads to inefficient utilization, especially given the diverse needs of workloads.
Nvidia’s Multi-Instance GPU (MIG) technology enables physical partitioning of GPUs, providing fault isolation and predictable quality of service, but previous approaches required static partitioning.
The new partitionable devices extension in DRA introduces concepts like counter sets and counters, allowing dynamic allocation of GPU fractions based on real-time resource availability, which improves flexibility and utilization.
A demo illustrates that dynamic partitioning with MIG devices completes workloads faster and uses resources more efficiently than static allocation.
The speakers also note that partitionable devices can be applied to other hardware types, such as TPUs and CPUs, and discuss ongoing work to improve scheduling and configuration.
Audience questions address the efficiency of MIG setup and the potential for similar approaches with CPUs, highlighting the need for specialized drivers.
# Main Points

|   # | Main point                                                                                                                                     |
| --: | ---------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Partitionable devices enable dynamic resource allocation in Kubernetes, maximizing GPU utilization.                                            |
|   2 | Traditional device plug-in API only allows assigning full GPUs, leading to inefficiency and static partitioning.                               |
|   3 | NVIDIA MIG (Multi-Instance GPU) technology allows physical partitioning of GPUs, providing fault isolation and predictable quality of service. |
|   4 | MIG partitions assign hardware fractions (e.g., streaming multiprocessors, memory regions) to each instance, ensuring robust isolation.        |
|   5 | Static partitioning is inflexible; if workloads require different memory sizes, static chunks can lead to resource fragmentation.              |
|   6 | DRA (Dynamic Resource Allocation) introduces a resource API for describing devices and their capacities/attributes.                            |
|   7 | DRA allows dynamic MIG partitioning, but core features are insufficient; partitionable devices extension is needed.                            |
|   8 | Partitionable devices introduce counter sets and counters, representing limited resources (e.g., memory, processors).                          |
|   9 | Devices consume counters from counter sets; allocation only occurs if sufficient counters are available.                                       |
|  10 | Partitionable devices feature is alpha in Kubernetes 1.35, targeting beta in 1.36.                                                             |
|  11 | NVIDIA’s DRA driver uses NVML to manage dynamic MIG device creation and destruction at runtime.                                                |
|  12 | The scheduler is informed of all possible MIG devices and their resource consumption via counters and counter sets.                            |
|  13 | When a workload requests a device, MIG mode is enabled if needed, the device is created, and cleaned up after use.                             |
|  14 | User experience for requesting devices remains unchanged; resource claim templates are used as before.                                         |
|  15 | Dynamic partitioning increases GPU utilization and reduces job completion time compared to static partitioning.                                |
|  16 | Partitionable devices can also model topology constraints (e.g., TPUs) and multi-host devices.                                                 |
|  17 | Upcoming work includes improved scoring for better scheduling decisions and mixins for more compact resource slice definitions.                |
|  18 | Partitionable devices may be applicable                                                                                                        |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=5GIDHxwQGiM)