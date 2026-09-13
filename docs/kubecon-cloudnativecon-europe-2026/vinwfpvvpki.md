---
layout: default
title:
  "Multi-Network Step-by-Step: Enabling SR-IOV Support From Kubernetes... Masaharu
  Kanda & Lionel Jouin"
nav_order: 220
parent: Kubecon Cloudnativecon Europe 2026
type: Video Note
description:
  The presentation discusses the integration of SR-IOV (Single Root I/O
  Virtualization) in Kubernetes using the new model Kubernetes network driver, focusing
  on enabling multi-network support and advanced hardware-level networking features.
  S...
resource: https://www.youtube.com/watch?v=vINwfpvvpKI
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

The presentation discusses the integration of SR-IOV (Single Root I/O Virtualization) in Kubernetes using the new model Kubernetes network driver, focusing on enabling multi-network support and advanced hardware-level networking features.
SR-IOV allows a single physical network card to expose multiple virtual functions (VFs), providing hardware-level virtualization for high-performance workloads such as telco, HPC, and AI/ML.
The speakers detail how Kubernetes is evolving to treat networking as a first-class resource, leveraging Dynamic Resource Allocation (DRA) and new APIs like consumable capacity and partitionable devices to manage and allocate network bandwidth and VFs more flexibly.
A live demo illustrates configuring and allocating VFs with specific bandwidths to pods, highlighting current limitations and the need for further enhancements, such as dynamic bandwidth requests at deployment time.
The talk concludes with an overview of ongoing community efforts, available drivers, and upcoming Kubernetes enhancements aimed at making network resource management as flexible and integrated as CPU and memory, inviting contributions and questions from the audience.

# Main Points

|   # | Main point                                                                                                                                                       |
| --: | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Introduction of speakers: Lo (Red Hat, multi network project lead, CNI maintainer) and Masar (NTT, disaggregated computing infrastructure controller developer). |
|   2 | SR-IOV (SRV) is a PCI Express standard enabling a single physical NIC to expose multiple virtual functions (VFs).                                                |
|   3 | SRV provides hardware-level virtualization, requiring hardware support and limiting the number of VFs by hardware.                                               |
|   4 | Each VF appears as an independent PCI device but shares the underlying physical NIC resources (e.g., bandwidth).                                                 |
|   5 | SRV is used for high-end NICs with advanced features (RDMA, traffic steering, encryption offload).                                                               |
|   6 | Use cases include telco (CNF), HPC, large-scale simulation, AI/ML training, and inference.                                                                       |
|   7 | Real-world example: Video inference pipeline at Osaka Expo using RDMA and Nvidia ConnectX with SRV VFs.                                                          |
|   8 | Multi network support in Kubernetes is being developed under the SIG Network subproject.                                                                         |
|   9 | CAP 3698 (multi network) is closed, but objectives continue via other initiatives.                                                                               |
|  10 | Two main user stories: VF feature and bandwidth guarantee.                                                                                                       |
|  11 | Dynamic Resource Allocation (DRA) enables flexible management of hardware/virtual devices in Kubernetes.                                                         |
|  12 | Relevant KEPs: 5075 (consumable capacity), 4817 (device status), 5941 (extended consumable capacity).                                                            |
|  13 | New Kubernetes network driver model bridges CNI and device plugin concepts, leveraging DRA for scheduling and NRI for configuration.                             |
|  14 | Networking is treated as a first-class resource; drivers are independent and composable.                                                                         |
|  15 | Demo: Bandwidth allocation to VFs using config maps and resource APIs; VFs advertised as individual devices.                                                     |
|  16 | Limitations: Cluster admins must preconfigure VFs; users can't request arbitrary bandwidth at deploy time.                                                       |
|  17 | CAP 5941 proposes dynamic bandwidth requests and shared capacity among devices.                                                                                  |
|  18 | Multiple drivers exist: Kubernetes network drivers, JNET, syn driver, SRV DR driver.                                                                             |
|  19 | Device attributes (e.g., PCI address) can be accessed via the donor API.                                                                                         |
|  20 | Q&A:                                                                                                                                                             |
|  21 | CI driver calls CNI; can use any CNI.                                                                                                                            |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=vINwfpvvpKI)
