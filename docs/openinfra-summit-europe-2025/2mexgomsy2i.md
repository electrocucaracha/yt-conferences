---
layout: default
title: How Ant Group Achieves Data Security in LLM Inference with Kata Based Confidential Computing
nav_order: 77
parent: OpenInfra Summit Europe 2025
type: Video Note
description: "This session presents a comprehensive overview of data security and confidential computing within cloud-native environments, focusing on the evolution of Kata Containers."
resource: "https://www.youtube.com/watch?v=2mEXGOmsY2I"
youtube_stats:
  view_count: 90
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

This session presents a comprehensive overview of data security and confidential computing within cloud-native environments, focusing on the evolution of Kata Containers.
The speakers, Alex and Shang, detail the significant performance and resource optimizations achieved by rewriting the Kata runtime and agent in Rust, which resulted in a tenfold reduction in memory consumption and faster container startup times compared to previous Go-based implementations.
They introduce "rund," a cloud-native system developed by Ant Group and Alibaba Cloud that integrates these Rust-based optimizations with lightweight virtual machine technologies to balance high security with extreme performance.
The discussion further explores the integration of Confidential Containers (CoCo) into this ecosystem, highlighting how the runtime supports essential features such as Trusted Execution Environments (TEE), guest image pulling, and remote attestation to protect data in use.
Additionally, the presentation covers the "Hybrid GPU" solution, a hardware-agnostic approach that leverages Trusted Board Management (TBM) to secure GPU workloads without requiring specific hardware upgrades, thereby reducing costs and expanding the trust model.
Finally, the speakers illustrate a real-world application in the medical industry, where these technologies enable secure processing of sensitive patient data by AI models, ensuring privacy and regulatory compliance through end-to-end encryption and isolated execution environments.

# Main Points

|   # | Main point                                                                                                                                                 |
| --: | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | The session introduces group data security with cloud-based confidential computing, focusing on Kata containers and confidential containers.               |
|   2 | Alex, a software engineer specializing in container infrastructure, and Shang, a security software engineer, present the work.                             |
|   3 | Kata containers are an open-source project under the Open Foundation designed to solve security and isolation deficiencies in traditional containers.      |
|   4 | Kata combines the lightweight nature of containers with the strong isolation of virtual machines to balance performance and security.                      |
|   5 | A core challenge in large-scale Kata adoption was excessive memory consumption by the Go-based Kata agent, limiting scalability and deployment density.    |
|   6 | The Kata agent was rewritten in Rust, reducing RSS anonymous memory from 11 megabytes to 300 kilobytes, a tenfold improvement.                             |
|   7 | The entire Kata containers runtime was rewritten in Rust to further lower memory overhead and improve performance.                                         |
|   8 | A lightweight VM optimized for container scenarios, called Jumbo, was developed and combined with the Rustified runtime to form Rund.                      |
|   9 | Rund is a cloud-native system refined by Ant Group and Alibaba Cloud, later contributed to the Kata community as Kata 3.                                   |
|  10 | The Rund architecture utilizes a single-core, single-process design and integrates optimized components like Jumbo and image service management.           |
|  11 | Rund supports multiple VMs, including QEMU and Cloud Hypervisor, with a flexible VM strategy allowing users to choose based on requirements.               |
|  12 | Performance tests show Rund achieves a faster setup time of around 718 milliseconds and substantially lower memory consumption compared to other runtimes. |
|  13 | Rund demonstrates a 10.9% faster startup and 24% less memory per instance compared to competitors in benchmark tests.                                      |
|  14 | RSS anonymous memory measurements indicate a 3.9-fold improvement in memory efficiency, dropping from 17.5 megabytes to 4.49 megabytes.                    |
|  15 | Confidential Containers (CoCo) is a CNCF sandbox project started in 2022 to protect data in use within cloud-native systems.                               |
|  16 | CoCo extends Kata containers with full-stack hardening technologies, including TEE hardware, end-to-end encryption, and remote attestation.                |
|  17 | Kata provides the runtime base and isolation, while CoCo adds security features to protect against unauthorized access and tampering from the host.        |
|  18 | Key CoCo features supported by Rund include TEE hardware support, guest image pulling, file sharing for Kubernetes, and OPA agent policy.                  |
|  19 | Rund supports trusted state storage, secure boot, and confidential GPU device support with hot plug capabilities via CDI.                                  |
|  20 | Rund is ready for production use, allowing seamless migration of confidential computing applications to the new runtime.                                   |
|  21 | Data security and privacy are critical for AI model providers concerned about leakage of modified models and sensitive user data.                          |
|  22 | Trusted Execution Environments (TEE) are the only viable solution for privacy protection given the computational performance needs of AI models.           |
|  23 | CoCo is an ideal solution for privacy protection as it is built on Kata containers and relies on TEE to protect running workloads.                         |
|  24 | Hybrid GPU (HPU) acts as a TEE backend for Kata-based CoCo solutions, offering different levels of security such as machine and device trust.              |
|  25 | HPU is hardware-agnostic, relying on widely available hardware-assisted personalization without depending on specific CPU or GPU hardware.                 |
|  26 | The trust model of HPU is hosted by a neutral authority, leveraging TEE and HPU to ensure security.                                                        |
|  27 | HPU enables legacy hardware usage, providing cost-effectiveness by avoiding the need for infrastructure upgrades.                                          |
|  28 | HPU uses virtualization extensions to create isolated execution environments, managing the host OS and enforcing physical address control.                 |
|  29 | Memory isolation is ensured by clearing IOMMU and PCI context spaces to defend against boot attacks.                                                       |
|  30 | HPU ensures that only the Confidential Machine (CM) associated with the GPU can control and manage the GPU device for data plane protection.               |
|  31 | A challenge-response mechanism based on GPU path physical and chrome functions is used to gather device fingerprints and attest GPU devices.               |
|  32 | A DP HPU protocol is designed to derive keys based on GPU fingerprints, improving data communication security on the DA bus between CPU and GPU.           |
|  33 | Real-world application scenarios include the medical industry, where strict security and regulatory compliance are required to protect patient privacy.    |
|  34 | In medical applications, encrypted medical records are processed securely in a confidential container platform implemented with Kata and CoCo.             |
|  35 | The solution leverages TEE and CoCo technology to protect data privacy, improve stakeholder security, and enhance AI model accuracy.                       |

# Video

[![Video thumbnail](https://img.youtube.com/vi/2mEXGOmsY2I/hqdefault.jpg)](https://www.youtube.com/watch?v=2mEXGOmsY2I)

[Watch on YouTube](https://www.youtube.com/watch?v=2mEXGOmsY2I)
