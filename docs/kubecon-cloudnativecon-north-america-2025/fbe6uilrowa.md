---
layout: default
title:
  "Project Lightning Talk: Spiderpool: Dynamic Topology-Aware RDMA Allocation
  For GPU... Weizhou Lan"
nav_order: 237
parent: Kubecon Cloudnativecon North America 2025
type: Video Note
description:
  The speaker discusses Sparo, a dynamic topology-aware RDMA allocation
  solution designed for GPU-based AI workloads in multi-tenant inference clusters.
  Efficient GPU and RDMA device allocation is crucial, especially when distributed
  inferenc...
resource: https://www.youtube.com/watch?v=fBE6UiLROWA
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

The speaker discusses Sparo, a dynamic topology-aware RDMA allocation solution designed for GPU-based AI workloads in multi-tenant inference clusters.
Efficient GPU and RDMA device allocation is crucial, especially when distributed inference tasks require fine-grained resource management across nodes.
Traditional device plug-ins for GPUs and RDMA operate separately and do not coordinate allocations based on PCIe affinity, leading to inefficiencies.
Sparo, as a Singi project plug-in, addresses these challenges by enabling underlay networking for containers, detecting PCIe affinity between RDMA devices and GPUs, and providing dedicated RDMA interfaces with independent IP addresses for traceable traffic.
It offers two allocation approaches: predefined resource allocation, which allows administrators to specify resource claims in advance, and adaptive RDMA resource allocation, which automatically assigns RDMA devices based on the PCIe topology of allocated GPUs, improving flexibility and efficiency over traditional methods.

# Main Points

|   # | Main point                                                                                                                          |
| --: | ----------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Discusses dynamic topology-aware RDMA allocation for GPU-based AI workloads in multi-tenant inference clusters                      |
|   2 | Emphasizes the need for efficient GPU resource usage in distributed inference tasks using tensor parallelism and data parallelism   |
|   3 | Highlights two key issues:                                                                                                          |
|   4 | GPU and RDMA device plug-ins are separate and do not coordinate allocation based on PCIe affinity                                   |
|   5 | Each port requires a dedicated RDMA device with its own IP address for traffic identification and observation                       |
|   6 | Introduces Spot as a Singi project and plug-in providing Singi functionality                                                        |
|   7 | Spot enables underlay networking for containers, particularly for RDMA network interfaces                                           |
|   8 | Latest Spot version implements DIA and NI capabilities to better meet AI inference networking requirements                          |
|   9 | Spot can detect PCIe affinity between NICs and GPUs for fine-grained RDMA device allocation                                         |
|  10 | SIOV-based containers can have dedicated RDMA NICs and independent IP addresses, making RDMA traffic traceable per container        |
|  11 | Prefind resource allocation approach:                                                                                               |
|  12 | Resource claim templates predefine how interfaces are assigned from master network interfaces                                       |
|  13 | Users reference resource claims when creating ports, allowing fine-grained RDMA device allocation without considering PCIe topology |
|  14 | Adaptive RDMA resource allocation approach:                                                                                         |
|  15 | Users do not need to specify detailed configurations during NI phase                                                                |
|  16 | Sparot detects PCIe slot of allocated GPU and adaptively assigns RDMA NICs with PCIe affinity                                       |
|  17 | Traditional GPU and RDMA device plug-ins cannot achieve this adaptive allocation                                                    |
|  18 | Spot introduces new features for AI inference, especially with small modules                                                        |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=fBE6UiLROWA)
