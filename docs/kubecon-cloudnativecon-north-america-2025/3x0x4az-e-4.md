---
type: Video Note
title: "QEMU in the Fast Lane: Accelerating KubeVirt Networking With... Daniel Borkmann & Anton Protopopov"
description: "The talk discusses accelerating virtual machine (VM) networking in Kubernetes using eBPF, focusing on the integration of KubeVirt, Cilium, and the Netkit device driver. The speaker explains how traditional VM and container infrastructures c..."
resource: https://www.youtube.com/watch?v=3X0X4az_E_4
tags: ["kubecon-cloudnativecon-north-america-2025", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

The talk discusses accelerating virtual machine (VM) networking in Kubernetes using eBPF, focusing on the integration of KubeVirt, Cilium, and the Netkit device driver.
The speaker explains how traditional VM and container infrastructures can be unified within Kubernetes, reducing complexity and improving performance by replacing legacy networking components like veth devices with Netkit, which leverages eBPF for efficient packet processing.
Benchmarks show significant improvements in throughput and latency for both container and VM workloads, especially when using advanced kernel features such as AF_XDP for zero-copy networking.
The team demonstrates a prototype where Netkit and AF_XDP are used to connect VMs directly to physical NIC queues, further boosting performance and reducing overhead.
The session concludes with a live demo, discussion of ongoing kernel development, and answers to audience questions about configuration, feature support, and future enhancements.
# Main Points

|   # | Main point                                                                                                                                                         |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   1 | The talk discusses accelerating KubeVirt networking using eBPF, in collaboration with Anton Yusi.                                                                  |
|   2 | Enterprises are reconsidering virtualization stacks, with KubeVirt and Cilium as viable OSS solutions for migrating VM infrastructure to Kubernetes.               |
|   3 | Combining Kubernetes and KubeVirt unifies infrastructure for both VM and container workloads, simplifying monitoring and logging.                                  |
|   4 | Standard Kubernetes pod networking involves veth devices, bridges, and tap devices, introducing overhead and latency.                                              |
|   5 | Cilium improved container networking by implementing kube-proxy in BPF, enabling fast redirects, and introducing the Netkit device driver to replace veth devices. |
|   6 | Netkit removes internal queuing and overhead, supports both L2 and L3 devices, and allows BPF attachment for control from the host namespace.                      |
|   7 | Performance benchmarks show Netkit achieves host-level throughput and latency, with real-world adoption by ByteDance and Meta yielding significant improvements.   |
|   8 | Applying Netkit to KubeVirt VM networking yields 13% better throughput and 12% lower latency compared to standard setups.                                          |
|   9 | Remaining overhead includes bridge and tap devices; alternatives like SR-IOV offer speed but lack observability and unified experience.                            |
|  10 | AFXDP (AF_XDP) is introduced as a zero-copy, high-performance networking technology in the Linux kernel, enabling BPF at the driver level.                         |
|  11 | Netkit is extended to support queue binding, allowing dedicated RX/TX queues for VMs and enabling AFXDP, IO_uring, and DPUF zero-copy.                             |
|  12 | Prototype benchmarks with AFXDP backend in KubeVirt show 37% better throughput and 30-35% lower latency.                                                           |
|  13 | Planned kernel improvements include multi-program XDP support and AFXDP TX hooks for policy enforcement and observability.                                         |
|  14 | Demo shows successful deployment of KubeVirt VM using Netkit queue binding and AFXDP backend.                                                                      |
|  15 | Netkit for Cilium must be enabled manually; future versions may auto-detect support.                                                                               |
|  16 | VLANs, jumbo frames, and multiple VM interfaces are supported with a                                                                                               |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=3X0X4az_E_4)