---
layout: default
title: "Kata Containers   How far are we to run on CSPs?"
nav_order: 52
parent: OpenInfra Summit Europe 2025
type: Video Note
description: "This discussion, led by representatives from Northflank and Nvidia, addresses the significant challenges of running Kata Containers on Cloud Service Providers (CSPs) where hardware-assisted nested ..."
resource: "https://www.youtube.com/watch?v=hPswsCrhsrY"
youtube_stats:
  view_count: 146
  channel_subscriber_count: 46800
tags:
  - openinfra-summit-europe-2025
  - video
  - learning
status: stable
generated:
  by: process:yt-summarizer-okf
  at: 2026-11-22T23:38:50+00:00
---

# Summary

This discussion, led by representatives from Northflank and Nvidia, addresses the significant challenges of running Kata Containers on Cloud Service Providers (CSPs) where hardware-assisted nested virtualization is restricted or unavailable.
The speakers highlight that while Kata Containers provide strong isolation via lightweight virtual machines, CSPs like AWS often prohibit the necessary virtualization access, forcing users into expensive bare-metal instances or suboptimal nested virtualization setups.
To mitigate this, the community is exploring two primary solutions: PVM (Paravirtualized Page-based Virtualization), which aims to replace KVM with a paravirtualized approach to avoid hardware dependencies, and Peer Pods, which offloads container execution to separate cloud VMs.
However, both approaches face substantial hurdles; PVM patches remain unmerged in the mainline kernel due to a lack of production adoption, while Peer Pods suffer from critical integration issues with Container Storage Interface (CSI), unstable network connections, and complex networking constraints.
Additionally, the conversation covers the performance limitations of virtual file systems in AI workloads and introduces VM templating and lazy loading techniques to reduce container startup latency, emphasizing the need for broader community support to mature these technologies and improve the overall multi-tenancy experience on public clouds.

# Main Points

|   # | Main point                                                                                                                                                                        |
| --: | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Kata Containers adds a KVM layer to standard containers to provide enhanced isolation for multi-tenancy and untrusted workloads.                                                  |
|   2 | Running Kata Containers on Cloud Service Providers (CSPs) is challenging because many providers do not support nested virtualization or restrict hardware virtualization access.  |
|   3 | AWS EC2 instances generally do not allow nested virtualization, making it difficult to run Kata Containers without expensive bare-metal instances.                                |
|   4 | The PVM (Paravirtualized Page-based Virtualization) solution aims to replace KVM by using hardware page table utilization to avoid the need for nested virtualization.            |
|   5 | PVM patches have been open-sourced in the kernel repository but have not yet been accepted into the mainline kernel due to a lack of widespread production usage.                 |
|   6 | The PVM approach allows Kata Containers to run on cloud instances that hide or disable hardware virtualization extensions like VT-x.                                              |
|   7 | Peer Pods is an alternative architecture that moves the container runtime and agent to a separate cloud VM, bypassing the need for nested virtualization on the host.             |
|   8 | Peer Pods implementation faces significant issues with Container Storage Interface (CSI) integration, as node-local volume operations do not translate well to remote cloud VMs.  |
|   9 | Network instability in Peer Pods can cause TTRPC connections to break, leading to container termination while the underlying cloud VM continues to incur costs.                   |
|  10 | Container networking in Peer Pods is currently limited to intra-cloud operations within the same virtual network, lacking support for inter-cloud or complex CNI setups.          |
|  11 | CSI drivers face performance and security challenges with Kata Containers because mounting volumes across the host-guest boundary requires virtual file systems or block devices. |
|  12 | Using virtual block devices for CSI in Kata Containers shifts management tasks like volume formatting and resizing to the user, potentially requiring privileged workloads.       |
|  13 | Alibaba Cloud has implemented a CSI direct volume attachment feature that passes device information to the Kata agent via a side channel to improve storage handling.             |
|  14 | Microsoft is also exploring similar CSI improvements for Kata Containers to support their internal use cases and broader adoption.                                                |
|  15 | Startup speed is a critical performance metric, with competitors like Fly.io achieving sub-second container starts, highlighting the need for faster Kata Container boot times.   |
|  16 | A template-based approach using live migration on the same host can accelerate Kata Container startup by preloading VM states and avoiding full memory copies.                    |
|  17 | Lazy loading of container images allows VMs to start before all image data is pulled, improving initial startup latency for functions and serverless workloads.                   |
|  18 | VM templating currently has limitations with virtual file systems due to shared memory constraints, though recent kernel fixes may enable better support.                         |
|  19 | The community is seeking kernel maintainers to review and merge PVM patches to enable broader production adoption across various cloud providers.                                 |

# Video

[![Video thumbnail](https://img.youtube.com/vi/hPswsCrhsrY/hqdefault.jpg)](https://www.youtube.com/watch?v=hPswsCrhsrY)

[Watch on YouTube](https://www.youtube.com/watch?v=hPswsCrhsrY)
