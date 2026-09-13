---
type: Video Note
title: "Virtualizing Large Scale GPU Cluster for Sovereign AI: Petasus AI Cloud Journey with Kube... Jian Li"
description: "In this talk, Jen, a principal engineer at SK Telecom, presents their in-house solution, Pedestria Cloud, for virtualizing large-scale GPU clusters to support AI workloads in South Korea. The HANE cluster, built with over 1,000 Blackwell GP..."
resource: https://www.youtube.com/watch?v=m1buNUEmXTg
tags: ["kubecon-cloudnativecon-europe-2026", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

In this talk, Jen, a principal engineer at SK Telecom, presents their in-house solution, Pedestria Cloud, for virtualizing large-scale GPU clusters to support AI workloads in South Korea.
The HANE cluster, built with over 1,000 Blackwell GPUs and partners like Penguin Solutions and Super Micro, leverages Kubernetes and containerized VMs to address challenges such as GPU resource fragmentation, provisioning delays, security risks, and operational overhead.
Key technical optimizations include MVLink and RDMA virtualization, PCI topology alignment, and automated partition management to ensure high performance and hard multi-tenancy isolation, with benchmarks showing less than 1% performance degradation compared to bare metal.
The system also features automated observability and monitoring using CNCF projects, providing near bare-metal performance and robust management for AI infrastructure.
Overall, SK Telecom’s solution demonstrates that large-scale GPU virtualization can be achieved efficiently, securely, and with minimal performance loss, supporting Korea’s sovereign AI infrastructure goals.
# Main Points

|   # | Main point                                                                                                                                                                 |
| --: | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | SK Telecom developed an in-house GPU virtualization solution called Pedestria Cloud, built on Kubernetes.                                                                  |
|   2 | Over 1,000 Blackwell GPUs are managed in the HANE cluster, designed with partners Penguin Solutions and Super Micro.                                                       |
|   3 | The cluster uses HGX-type GPU servers and fully virtualizes the AI infrastructure.                                                                                         |
|   4 | Two end customers currently use the solution for RLM model training.                                                                                                       |
|   5 | Key challenges addressed: GPU resource fragmentation and waste, AI environment provisioning delays, security risks (multi-tenancy), scalability, and operational overhead. |
|   6 | Virtualization minimizes GPU underutilization and enables dynamic allocation.                                                                                              |
|   7 | AI environment provisioning is automated to reduce deployment delays.                                                                                                      |
|   8 | Hard multi-tenancy is enforced for security, isolating infrastructure between users.                                                                                       |
|   9 | Operational overhead is reduced through systematic GPU failure detection and automated management.                                                                         |
|  10 | Virtualization stack includes GPU node virtualization, MVLink, GPU fabric, and storage fabric.                                                                             |
|  11 | Container-based virtualization is used for flexibility and performance; containerized VMs (via KubeVirt) are used for security and extensibility.                          |
|  12 | SKT optimized KubeVirt for AI workloads, including PCI topology alignment and MVLink/GDR virtualization.                                                                   |
|  13 | MVLink and GDR (GPU Direct RDMA) are virtualized to maintain high inter-GPU and inter-node bandwidth.                                                                      |
|  14 | PCI topology is carefully managed to match bare metal for optimal performance.                                                                                             |
|  15 | SKT developed a PCI topology sidecar container to rearrange VM PCI topology.                                                                                               |
|  16 | Benchmarks show less than 1% performance degradation compared to bare metal for MVLink and NCCL tests.                                                                     |
|  17 | GPU fabric isolation is achieved using partition keys for InfiniBand and VLAN/VXLAN for Ethernet.                                                                          |
|  18 | Kubernetes operators automate GPU fabric partitioning and management.                                                                                                      |
|  19 | Scalability tests with over 1,000 GPUs show minimal performance loss.                                                                                                      |
|  20 | Observability stack uses Prometheus, node exporter, and DCGM exporter for monitoring and alerting.                                                                         |
|  21 | Near bare-metal performance is achie                                                                                                                                       |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=m1buNUEmXTg)