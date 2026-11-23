---
layout: default
title: "Trusted AI Anywhere: Kata Containers & Confidential Containers at Scale"
nav_order: 4
parent: OpenInfra Summit Europe 2025
type: Video Note
description: "The speaker presents a solution for running AI pipelines on confidential data at scale, addressing the critical need to protect intellectual property and prevent model leakage in enterprise environ..."
resource: "https://www.youtube.com/watch?v=bdoF5hQojaA"
youtube_stats:
  view_count: 1167
  like_count: 18
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

The speaker presents a solution for running AI pipelines on confidential data at scale, addressing the critical need to protect intellectual property and prevent model leakage in enterprise environments.
By leveraging trusted execution environments and NVIDIA GPUs with confidential compute support, the approach extends trust to the hardware, overcoming the limitations of slower cryptographic methods and standard sandboxing.
The core of this strategy is Kata Containers and Confidential Containers, which enable a "lift and shift" migration of existing Kubernetes workloads into a secure, memory-safe Rust-based stack without requiring code modifications.
This ecosystem integrates seamlessly with Kubernetes through features like runtime classes and peer pods, supporting diverse deployment models from on-premises to hybrid cloud and edge.
The presentation concludes with a call to action for the community to test, contribute to, and deploy these confidential container solutions to secure large-scale AI infrastructure.

# Main Points

|   # | Main point                                                                                                                       |
| --: | -------------------------------------------------------------------------------------------------------------------------------- |
|   1 | The speaker is excited to meet Kata community members in person after four years of remote collaboration.                        |
|   2 | The talk focuses on trusted AI using Kata and confidential containers at scale.                                                  |
|   3 | A major challenge is running AI pipelines on confidential data while preventing model leakage.                                   |
|   4 | A Google study indicates 66% of companies have over 50% of data unused due to trust gaps.                                        |
|   5 | IP leakage of financial models poses an existential risk to companies.                                                           |
|   6 | Enterprises require AI pipelines to run at scale, which is defined by GPU capacity.                                              |
|   7 | Major AI players operate on hundreds of nodes and thousands of GPUs.                                                             |
|   8 | Cryptographic compute methods like homomorphic encryption are powerful but niche and 1,000 times slower for AI tasks.            |
|   9 | Sandbox environments like Firecracker reduce blast radius but still require trust in the host infrastructure.                    |
|  10 | Confidential compute aims to eliminate trust in the infrastructure.                                                              |
|  11 | Trusted Execution Environments like SGX are process-based and do not work for GPUs.                                              |
|  12 | VM-based solutions like SNP and TDX extend trust to GPUs with CC support.                                                        |
|  13 | Future CCA technology will extend trust to edge deployments.                                                                     |
|  14 | Kata containers and confidential containers enable a lift-and-shift strategy for Kubernetes workloads without code modification. |
|  15 | Kubernetes is the primary platform for AI deployments.                                                                           |
|  16 | Work includes patches and enhancement proposals for kubelet, containerd, and CRI-O.                                              |
|  17 | Dynamic Resource Allocation allows for fine-grained resource allocation in Kubernetes.                                           |
|  18 | Runtime classes allow workloads to run on bare metal, Kata, or confidential containers via a single annotation.                  |
|  19 | Peer pods enable running confidential containers on-premises with burst capacity to the cloud.                                   |
|  20 | The complete stack is being rewritten in Rust for memory safety.                                                                 |
|  21 | The Nvidia GPU operator provides a single interface for deploying across bare metal, Kata, and confidential containers.          |
|  22 | Confidential containers provide a tested VM workload that can run in various environments.                                       |
|  23 | Deployment models include on-premises, public cloud VMs, private cloud VMs, and edge or factory settings.                        |
|  24 | The goal is to run the same image and attestation across different deployment postcodes.                                         |
|  25 | Hopper GPUs supported single GPU pass-through for confidential compute.                                                          |
|  26 | Blackwell GPUs support multi-GPU pass-through.                                                                                   |
|  27 | Support is being extended for multi-GPU and multi-node workloads on hundreds of nodes.                                           |
|  28 | Blackwell and future generations support TDISP, which significantly increases performance.                                       |
|  29 | The focus has shifted from hardware to software standards and operations.                                                        |
|  30 | The call to action is to test current setups, deploy them, and share use cases.                                                  |
|  31 | The team runs a simple recommendation pipeline in RCI for testing.                                                               |
|  32 | Contact channels include the Kata select channel, CNCF select channels, and direct email.                                        |
|  33 | A breakout session on confidential containers is scheduled for Sunday around noon.                                               |
|  34 | The speaker thanks the Kata community, OpenFaaS Summit, and collaborators for their contributions.                               |

# Video

[![Video thumbnail](https://img.youtube.com/vi/bdoF5hQojaA/hqdefault.jpg)](https://www.youtube.com/watch?v=bdoF5hQojaA)

[Watch on YouTube](https://www.youtube.com/watch?v=bdoF5hQojaA)
