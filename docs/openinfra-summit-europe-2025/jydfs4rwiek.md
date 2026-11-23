---
layout: default
title: Enabling Confidential Computing Throughout the Virtualization Stack
nav_order: 18
parent: OpenInfra Summit Europe 2025
type: Video Note
description: "This presentation outlines the critical need for confidential computing to protect sensitive data and proprietary code in use, particularly as AI workloads increase the risk of data exposure to ser..."
resource: "https://www.youtube.com/watch?v=jYdFS4RWIEk"
youtube_stats:
  view_count: 334
  like_count: 4
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

This presentation outlines the critical need for confidential computing to protect sensitive data and proprietary code in use, particularly as AI workloads increase the risk of data exposure to service operators.
The speaker explains that while hardware technologies like AMD SEV-SNP and Intel TDX provide a hardware root of trust to increase attack costs, the industry faces a paradox where regulatory interest outpaces software tooling and full verifiability, especially within opaque hyperscaler environments.
To address this, the speaker highlights the advantage of open infrastructure in offering transparency and verifiability, detailing recent efforts to integrate confidential computing support into Proxmox and develop open-source orchestration tools for secure deployment.
The talk further discusses the current state of platform support, noting that while kernel and virtualization layer support are maturing, significant gaps remain in enterprise management solutions and cloud provider attestation processes.
Finally, the speaker issues a call to action for the community to accelerate the development of confidential computing features in OpenStack, arguing that the platform must catch up to meet the demands of critical infrastructure sectors willing to invest in secure, verifiable digital infrastructure.

# Main Points

|   # | Main point                                                                                                                                           |
| --: | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | The presentation focuses on enabling confidential computing throughout the virtualization stack to protect data and code in use.                     |
|   2 | Confidential computing aims to increase the cost of attacks and raise the trustworthiness of infrastructure by exposing a hardware root of trust.    |
|   3 | Workloads are at risk because service operators typically have complete access to sensitive data and proprietary software.                           |
|   4 | The technology protects workloads encrypted at rest, in transit, and in use, facilitating attestation-based policies for deployment.                 |
|   5 | The evolution of the technology includes TPMs, Intel SGX, and a shift toward treating entire virtual machines as trusted execution environments.     |
|   6 | Current platform support includes AMD SEV-SNP, Intel TDX, ARM CCA, and Nvidia confidential compute, with varying levels of open-source tooling.      |
|   7 | Hyperscalers like Azure and GCP offer confidential VMs but face criticism for lacking full verifiability and requiring trust in opaque binaries.     |
|   8 | Transparency and verifiability are identified as core advantages of open infrastructure over proprietary hyperscaler solutions.                      |
|   9 | Implementing confidential computing on-premise requires host and guest kernel support, which is available in recent Linux kernels.                   |
|  10 | Proxmox added support for AMD SEV-SNP in version 8.4, with Intel TDX support currently in progress.                                                  |
|  11 | Performance overhead varies by workload, and independent studies are preferred over vendor benchmarks for accurate assessment.                       |
|  12 | An open-source Terraform module is available for orchestrating confidential VM deployments at scale.                                                 |
|  13 | OpenStack previously added support for older confidential computing standards but has seen slow progress on newer technologies like SEV-SNP and TDX. |
|  14 | The speaker calls for community collaboration to add robust confidential computing support to OpenStack to meet critical infrastructure needs.       |

# Video

[![Video thumbnail](https://img.youtube.com/vi/jYdFS4RWIEk/hqdefault.jpg)](https://www.youtube.com/watch?v=jYdFS4RWIEk)

[Watch on YouTube](https://www.youtube.com/watch?v=jYdFS4RWIEk)
