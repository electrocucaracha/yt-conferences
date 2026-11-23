---
layout: default
title: "FlagRelease: Building a Unified Platform for Automated Migrations​"
nav_order: 134
parent: OpenInfra Summit Europe 2025
type: Video Note
description: 'The speaker, a former IBM researcher, presents "FlagOS," an open-source software stack designed to unify AI infrastructure by enabling large models to run across diverse hardware architectures, inc...'
resource: "https://www.youtube.com/watch?v=Eyp02Aiy8mE"
youtube_stats:
  view_count: 29
  like_count: 1
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

The speaker, a former IBM researcher, presents "FlagOS," an open-source software stack designed to unify AI infrastructure by enabling large models to run across diverse hardware architectures, including NVIDIA, AMD, and Huawei chips.
Addressing the fragmentation of the current AI ecosystem, which is heavily dominated by NVIDIA’s CUDA, the initiative aims to lower barriers for developers and reduce costs by providing a unified compiler, operator libraries, and communication frameworks that are compatible with various processors.
The core mechanism involves a semi-automated migration process where open-source models from platforms like Hugging Face are analyzed, migrated to non-CUDA hardware, rigorously tested for accuracy and performance parity, and then released back to the community with Docker environments for easy deployment.
This approach leverages AI agents to assist in code repair and verification, significantly reducing the manual effort required to adapt models for different chipsets.
Ultimately, the goal is to create an "Open Compute for AI" ecosystem that supports both data center and edge devices, allowing users to seamlessly run AI workloads on any compatible hardware without being locked into a single vendor’s proprietary software stack.

# Main Points

|   # | Main point                                                                                                                                                                                                                              |
| --: | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | The speaker, with 17 years of experience at IBM Research, advocates for AI infrastructure that supports diverse hardware beyond NVIDIA GPUs to enable large model training and inference.                                               |
|   2 | The human brain demonstrates significantly higher power efficiency and synaptic scale compared to current AI chips, highlighting the need for continued architectural innovation.                                                       |
|   3 | The primary barrier to deploying non-NVIDIA AI hardware is the fragmented software ecosystem, where most open-source models and developer tools are optimized exclusively for CUDA.                                                     |
|   4 | The "Open Compute for AI" initiative aims to build a unified, open-source software specification that allows AI models to run across different chipsets, edge devices, and cloud servers.                                               |
|   5 | This approach seeks to lower costs for users, provide hardware vendors with a viable ecosystem to justify R&D investments, and enable global access to AI capabilities by utilizing underused data center resources.                    |
|   6 | The "FlagOS" project, developed with universities and open communities, is an open software stack (not an operating system) designed to unify system software for running PyTorch and large models on various AI chipsets.              |
|   7 | FlagOS includes a unified AI compiler, a large operator library written in Triton, and communication libraries, currently supporting NVIDIA, AMD, Huawei, and RISC-V architectures.                                                     |
|   8 | A major challenge is that over 95% of open-source AI models on Hugging Face are CUDA-only, and developers lack the skills to manually migrate models to other architectures.                                                            |
|   9 | The proposed solution is a "semi-automatic migration" process inspired by CPU architecture porting, where models are downloaded, dependencies analyzed, migrated to new hardware, and rigorously evaluated for accuracy before release. |
|  10 | The migration pipeline involves replacing CUDA-specific components with FlagOS equivalents: FlagScale framework, FlagGems operator library, FlexCX communication library, and an enhanced Triton-based compiler.                        |
|  11 | FlagGems, the largest Triton-based operator library, achieves performance comparable to or better than CUDA on NVIDIA hardware and has been integrated into the PyTorch ecosystem.                                                      |
|  12 | The FlagScale framework supports both training and inference, featuring automatic parallelization optimization that outperforms manual expert tuning on large clusters.                                                                 |
|  13 | FlexCX provides a unified communication layer for different chipset vendors and was recently adopted as a new standard at the ITU conference.                                                                                           |
|  14 | An AI agent, "Triton Copilot," assists developers by automatically generating AI operator code, creating test cases, and verifying accuracy and throughput against NVIDIA baselines.                                                    |
|  15 | The project supports cross-platform deployment from data centers to edge devices and robots, addressing the need to adapt models for different instruction sets in embodied AI applications.                                            |
|  16 | The speaker proposes integrating this abstraction layer with OpenStack to expand its role in AI infrastructure, moving beyond Kubernetes to manage multi-chip support at a higher level.                                                |
|  17 | Migrated models are released back to Hugging Face and ModelScope with Docker environments, ensuring users can run them on new hardware with an accuracy gap of less than 1-2% compared to CUDA.                                         |
|  18 | The ultimate goal is to achieve fully automatic migration of AI models across any hardware architecture, reducing barriers for developers, universities, and enterprises.                                                               |

# Video

[![Video thumbnail](https://img.youtube.com/vi/Eyp02Aiy8mE/hqdefault.jpg)](https://www.youtube.com/watch?v=Eyp02Aiy8mE)

[Watch on YouTube](https://www.youtube.com/watch?v=Eyp02Aiy8mE)
