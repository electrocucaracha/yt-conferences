---
type: Video Note
title: "Cloud Native Theater | KubeVirt Summit: Breaking the Performance Barrier... Jian Li & Yves Weisser"
description: "In this presentation, Jen from SK Telecom and Eve from NetApp discuss advancements in high-performance AI storage virtualization, focusing on overcoming performance barriers using Kubernetes, KubeVirt, and GPU Direct Storage (GDS) technolog..."
resource: https://www.youtube.com/watch?v=HWaaRLDmI8k
tags: ["kubecon-cloudnativecon-europe-2026", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

In this presentation, Jen from SK Telecom and Eve from NetApp discuss advancements in high-performance AI storage virtualization, focusing on overcoming performance barriers using Kubernetes, KubeVirt, and GPU Direct Storage (GDS) technologies.
They explain the complexities of AI data center infrastructure, emphasizing the shift from CPU to GPU-centric architectures and the need for efficient storage virtualization to support demanding AI workloads.
The team describes their solution, which leverages Kubernetes and KubeVirt to manage both virtual machines and containers, and integrates RDMA and GDS to bypass traditional bottlenecks, achieving near-native storage performance even within virtualized environments.
Benchmark results using NetApp’s AFX platform and GDSIO show that enabling GDS in virtual machines delivers comparable throughput and reduced CPU usage to bare metal setups, significantly improving AI inference efficiency.
A real-world use case demonstrates that offloading KV cache to storage via GDS accelerates inference performance, especially with large context sizes, confirming that their approach effectively removes traditional virtualization performance barriers for AI workloads.
# Main Points

|   # | Main point                                                                                                                                          |
| --: | --------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Presentation by Jen (SK Telecom) and Eve (NetApp) on high performance AI storage virtualization using KubeVirt and NetApp.                          |
|   2 | Jen is a principal engineer at SK Telecom, working on AI data center infrastructure virtualization with KubeVirt.                                   |
|   3 | Eve is a solution architect at NetApp, focusing on Kubernetes and storage.                                                                          |
|   4 | Agenda: introduction to AI storage virtualization, deep dive into virtualization with KubeVirt, integration, performance evaluation, key takeaways. |
|   5 | AI data centers are GPU-centric, requiring GPU, TPU, and AI storage virtualization.                                                                 |
|   6 | Focus is on AI storage and fabric virtualization, leveraging Kubernetes and KubeVirt.                                                               |
|   7 | SK Telecom’s in-house solution, Pasa Cloud, virtualizes AI infrastructure using Kubernetes and KubeVirt.                                            |
|   8 | Solution supports running VMs, containers, and managed Kubernetes, enabling AI/ML ops and DevOps services.                                          |
|   9 | AI data pipeline stages require different storage characteristics; training and inference need high bandwidth and IOPS.                             |
|  10 | RDMA (Remote Direct Memory Access) is used to bypass TCP/IP stack for high-performance storage.                                                     |
|  11 | Three virtualization approaches: CSI-based NVMe over TCP (lower performance), bypassing QEMU (better), and RDMA in VM (best performance).           |
|  12 | Adopted RDMA in VM approach, requiring RDMA drivers and configuration for high availability (HA) using VF link aggregation.                         |
|  13 | Implemented GPU Direct Storage (GDS) inside VMs, enabling direct storage-to-GPU memory transfers, bypassing CPU/system memory.                      |
|  14 | Benchmarks used NetApp AFX platform with NFS over RDMA, managed by Kubernetes and KubeVirt.                                                         |
|  15 | NetApp Trident CSI driver provides efficient snapshots, smart clones, and supports multiple storage protocols.                                      |
|  16 | Two integration architectures: traditional CSI with Trident and direct NFS over RDMA attachment.                                                    |
|  17 | Benchmarks with GDSIO tool show near-native performance in VMs compared to bare metal, with ~40% CPU reduction when GDS is enabled.                 |
|  18 | GDS enables efficient KV cache offloading to storage, accelerating AI inference by av                                                               |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=HWaaRLDmI8k)