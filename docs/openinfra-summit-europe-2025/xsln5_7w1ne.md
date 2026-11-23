---
layout: default
title: "Trusted AI Anywhere: Kata Containers & Confidential Containers at Scale"
nav_order: 37
parent: OpenInfra Summit Europe 2025
type: Video Note
description: "Kaiser from Nvidia presents a technical overview of confidential containers with GPUs, explaining how this technology shifts the threat model from protecting infrastructure against untrusted worklo..."
resource: "https://www.youtube.com/watch?v=XSln5_7w1nE"
youtube_stats:
  view_count: 187
  like_count: 2
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

Kaiser from Nvidia presents a technical overview of confidential containers with GPUs, explaining how this technology shifts the threat model from protecting infrastructure against untrusted workloads to protecting workloads against untrusted infrastructure.
By leveraging Kata Containers and Trusted Execution Environments (TEEs), the solution provides hardware-based isolation and encryption, ensuring that cloud service providers cannot access or inspect sensitive data, unlike standard containerization which relies on weak kernel-level boundaries.
The presentation details the Nvidia enablement stack, which utilizes the Container Device Interface (CDI) and the GPU Operator to seamlessly integrate GPUs into Kubernetes environments, supporting both bare-metal and virtualized deployments without requiring code modifications.
A significant portion of the talk addresses the complexity of PCI Express topology, introducing two modes—flattening and host topology replication—to ensure proper peer-to-peer communication and performance for advanced features like GPU Direct RDMA and MIG.
Finally, the speaker discusses the critical role of attestation in verifying the integrity of the CPU, GPU, and software stack, enabling secure secret key release for AI and ML workloads where data owners, model owners, and infrastructure providers must mutually trust each other within a single encrypted environment.

# Main Points

|   # | Main point                                                                                                                                                                              |
| --: | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Confidential containers serve as an umbrella term for Kata Containers components, shifting the threat model so workloads do not trust the infrastructure.                               |
|   2 | Traditional containers provide weak security boundaries and share the host kernel, making them vulnerable to breakouts that can compromise the entire cluster.                          |
|   3 | Kata Containers offer micro-VM isolation that is fully OCI compliant, allowing untrusted code to run safely without modifying the container runtime.                                    |
|   4 | Trusted Execution Environments (TEEs) like Intel TDX and AMD SEV-SNP enable confidential computing by encrypting VMs so the infrastructure cannot access data.                          |
|   5 | Attestation is the process of proving that a VM is in an expected state, ensuring the hardware and software match reference values before releasing secrets.                            |
|   6 | NVIDIA enables GPUs in containers using the Container Device Interface (CDI) to provide necessary drivers and libraries, ensuring compatibility between user and kernel space.          |
|   7 | In Kubernetes, the GPU Operator manages feature discovery, node labeling, and networking to properly enable GPU workloads within the cluster.                                           |
|   8 | To achieve lift-and-shift capabilities, NVIDIA replicates the bare-metal GPU enablement pattern inside Kata VMs, ensuring consistent behavior across environments.                      |
|   9 | Support for PCIe topology is critical for advanced features like peer-to-peer communication, GPU Direct RDMA, and MIG, which require correct hardware mapping.                          |
|  10 | Two modes exist for handling PCIe topology: flattening the hierarchy with side-channel metadata or replicating the host topology inside the VM for accurate driver behavior.            |
|  11 | Hypervisor resource limits, such as PCI slot constraints, require careful device attachment strategies, potentially using PCI bridges for non-critical devices in the same IOMMU group. |
|  12 | The transition from Kata to confidential containers is seamless, requiring only a change in the runtime class definition while maintaining the same internal mechanics.                 |
|  13 | Composite attestation supports both CPU and GPU verification, enabling secure key release for encrypted storage, model decryption, and data protection.                                 |
|  14 | Future attestation efforts will include DPUs and other devices, addressing timing attacks and ensuring runtime integrity of guest file systems and container images.                    |
|  15 | AI/ML use cases like data clean rooms require protecting data owners, model owners, and infrastructure owners from each other within the same VM.                                       |
|  16 | GPU attestation currently uses bounce buffers for key exchange, but future PCIe Gen 6 with TDISP will provide encrypted and integrity-protected bus communication.                      |
|  17 | Hardware partitioning for confidential compute, known as SME, is under development to provide guaranteed quality of service without sharing contexts.                                   |
|  18 | Design documents for PCIe topology optimization are available in the Kata GitHub repository, with a preference for automated host topology replication.                                 |
|  19 | Performance issues with full device pass-through are being addressed by upstreaming fixes and improving IOMMU group handling to reduce latency.                                         |
|  20 | A proposed launch layer architecture allows running Kubernetes control planes and workers as isolated VMs on L1, avoiding nested virtualization for better security.                    |
|  21 | This architecture enables attesting the entire stack, including the Kubernetes control plane, workers, and pods, with out-of-band roots of trust like DPUs.                             |

# Video

[![Video thumbnail](https://img.youtube.com/vi/XSln5_7w1nE/hqdefault.jpg)](https://www.youtube.com/watch?v=XSln5_7w1nE)

[Watch on YouTube](https://www.youtube.com/watch?v=XSln5_7w1nE)
