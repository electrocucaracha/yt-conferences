---
layout: default
title: Slicing Supercomputers for Trusted Research Environments
nav_order: 68
parent: OpenInfra Summit Europe 2025
type: Video Note
description: John from StackHPC and Tundday from Cambridge University presented a project focused on slicing supercomputers to create trusted research environments (TREs) for sensitive data.
resource: "https://www.youtube.com/watch?v=zbIIPjRLw9M"
youtube_stats:
  view_count: 103
  like_count: 3
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

John from StackHPC and Tundday from Cambridge University presented a project focused on slicing supercomputers to create trusted research environments (TREs) for sensitive data.
They discussed the "Fridge" project, which aims to extend existing TREs into high-performance computing infrastructure, specifically targeting the Dawn supercomputer at Cambridge and Isambard AI at Bristol, to enable AI-driven research on sensitive medical data.
The presentation highlighted the use of OpenStack and Azimuth to provide self-service Kubernetes clusters with GPU support, while addressing security concerns like container escape by isolating workloads within virtual machines.
Tundday detailed Dawn’s hardware capabilities, including Intel Xeon CPUs and GPUs, and its integration into the UK’s AI research resource federation, emphasizing the need for secure, federated access.
Additionally, they explained the role of Waldor in managing user authentication, project allocation, and resource provisioning, ensuring compliance and a single pane of glass for infrastructure management.

# Main Points

|   # | Main point                                                                                                                                                                                           |
| --: | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Trusted Research Environments (TREs) enable researchers to work with sensitive data like patient records under strict controls defined by frameworks such as the UK's Five Safe model.               |
|   2 | The Five Safe framework requires managing data classification, approved projects, trained personnel, secure settings like VDI without copypaste, and controlled outputs.                             |
|   3 | StackHPC and Cambridge University are collaborating to slice supercomputers into flexible resources to maximize scientific output beyond single-purpose batch clusters.                              |
|   4 | The approach involves building a cloud foundation using OpenStack APIs to create reproducible, high-performance, and self-service environments.                                                      |
|   5 | Hardware resources are dynamically allocated to different workloads, including Slurm batch clusters, bare-metal Kubernetes, and hypervisor-based virtual machines.                                   |
|   6 | The Fridge project aims to extend existing TREs into HPC infrastructure, specifically targeting the Dawn and Isambard-AI supercomputers in the UK.                                                   |
|   7 | Azimuth is used as a self-service interface to provision Kubernetes clusters with Intel GPUs, simplifying the setup for AI-driven research workloads.                                                |
|   8 | OpenStack Blazar is integrated to manage resource reservations, providing definitive feedback on availability and preventing over-allocation of contested resources like GPUs.                       |
|   9 | Security concerns regarding untrusted workloads in TREs are addressed by running workloads inside virtual machines with isolated networks to prevent container escapes.                              |
|  10 | The Dawn supercomputer features PowerEdge XE946 nodes with Intel Xeon CPUs, Intel Pontevecchio GPUs, and high-speed HDR networking.                                                                  |
|  11 | Dawn achieved a Top 500 ranking of 41 in 2023 with 243 nodes, demonstrating its capability for high-density CPU and GPU workloads.                                                                   |
|  12 | The AI Research Resource (AIR) federation provides federated access to national AI and HPC infrastructure, lowering barriers for researchers while maintaining cybersecurity.                        |
|  13 | Waldo serves as a central access and interface management system, integrating authentication, project management, and service offering for the AIR federation.                                       |
|  14 | Waldo integrates with MyAccessID for secure federated access and Jira Service Desk for resource allocation and user onboarding.                                                                      |
|  15 | Storage encryption is automated using Linux Unified Key Setup (LUKS) and Kubernetes Custom Resource Definitions to ensure compliance with regulations like GDPR.                                     |
|  16 | Network isolation in the Fridge project utilizes VXLAN within the standard OVS ML2 stack to isolate virtual machines, avoiding the need for complex InfiniBand configurations in this specific case. |
|  17 | Waldo automates the provisioning of Slurm accounts and SSH identities, providing a single pane of glass for resource allocation across the federation.                                               |
|  18 | The project emphasizes splitting responsibilities between infrastructure providers and TRE providers to ensure appropriate assurance levels for sensitive medical data.                              |
|  19 | Future work includes exploring confidential containers and Trusted Execution Environments (TEEs) to reduce reliance on trusting the infrastructure provider.                                         |

# Video

[![Video thumbnail](https://img.youtube.com/vi/zbIIPjRLw9M/hqdefault.jpg)](https://www.youtube.com/watch?v=zbIIPjRLw9M)

[Watch on YouTube](https://www.youtube.com/watch?v=zbIIPjRLw9M)
