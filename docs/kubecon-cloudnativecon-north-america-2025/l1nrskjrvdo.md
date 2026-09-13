---
type: Video Note
title: "Share With Care: Efficient Device Sharing With Guaranteed... Sunyanan Choochotkaew & John Belamaric"
description: 'John Bellame and Syan introduce a new alpha feature in Kubernetes called "consumable capacity," developed as part of the Dynamic Resource Allocation (DRA) framework. They explain that traditional methods for allocating network bandwidth to...'
resource: https://www.youtube.com/watch?v=L1NRskjrvDo
tags: ["kubecon-cloudnativecon-north-america-2025", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

John Bellame and Syan introduce a new alpha feature in Kubernetes called "consumable capacity," developed as part of the Dynamic Resource Allocation (DRA) framework.
They explain that traditional methods for allocating network bandwidth to pods are limited, as the Kubernetes scheduler lacks visibility into bandwidth annotations, leading to potential overallocation and degraded user experience.
The new consumable capacity feature allows multiple resource claims to share a single device, such as a network interface card (NIC), while the scheduler tracks and enforces aggregate resource limits to prevent overcommitment.
This is achieved through enhancements to the DRA APIs, including new fields for multi-allocation and distinct device selection, enabling more flexible and scalable resource management for networking and other hardware types.
A live demo illustrates how these features work in practice, and the presenters note that while the feature is currently in alpha, it is expected to reach beta in a future Kubernetes release, with ongoing work to expand its capabilities and use cases.
# Main Points

|   # | Main point                                                                                                                                                                  |
| --: | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Introduction of speakers: John Bellame (upstream Kubernetes) and Syan (IBM Research, networking performance optimizations, first Kubernetes contribution)                   |
|   2 | Presentation focuses on an alpha feature for managing network bandwidth in Kubernetes using DRA (Dynamic Resource Allocation)                                               |
|   3 | Current Kubernetes approach uses CNI and pod annotations for bandwidth allocation, but scheduler lacks visibility, leading to possible bandwidth over-allocation            |
|   4 | Extended resources allow bandwidth to be modeled as a resource, but only work well with a single NIC per node; multiple NICs require complex, bespoke configurations        |
|   5 | DRA (Dynamic Resource Allocation) is a general-purpose resource modeling and requesting framework, not limited to GPUs                                                      |
|   6 | DRA introduces two new APIs: resource slice (for hardware vendors to describe devices) and resource claim (for users to request hardware)                                   |
|   7 | DRA supports device sharing and partitioning, but previous sharing models (e.g., for GPUs) do not work for network interfaces                                               |
|   8 | New alpha feature: consumable capacity, allowing multiple claims to reference the same device, with the platform regulating resource consumption to prevent over-allocation |
|   9 | Consumable capacity enables bandwidth to be divided among multiple pods using sub-interfaces, with the scheduler tracking allocations                                       |
|  10 | API changes include:                                                                                                                                                        |
|  11 | Allowing devices to be allocated multiple times (boolean field)                                                                                                             |
|  12 | Introducing share ID for each allocation                                                                                                                                    |
|  13 | Adding constraints to ensure distinct devices for redundancy                                                                                                                |
|  14 | Ensuring total allocated capacity does not exceed device limits                                                                                                             |
|  15 | Demo showed practical use: multiple network interfaces with different bandwidths, prioritized allocation, and enforcement of capacity limits                                |
|  16 | Device vendors/cluster admins can define request policies (default, minimum, maximum, chunk size) for capacity consumption                                                  |
|  17 | Consumable capacity feature is applicable beyond networking, e.g., virtual GPU memory partitioning, storage, CPUs                                                           |
|  18 | Scheduler handles accounting fo                                                                                                                                             |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=L1NRskjrvDo)