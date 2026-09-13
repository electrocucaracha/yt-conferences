---
layout: default
title:
  "An Open Source AI Compute Stack: Kubernetes + Ray + PyTorch + VLLM - Robert
  Nishihara, Anyscale"
nav_order: 17
parent: Kubecon Cloudnativecon North America 2025
type: Video Note
description:
  Robert presents an overview of Ray, an open-source project developed
  to address the growing complexity of modern AI workloads, particularly in reinforcement
  learning and large-scale data processing. He explains how Ray, in combination with...
resource: https://www.youtube.com/watch?v=4o2amJxMHUc
tags:
  - kubecon-cloudnativecon-north-america-2025
  - video
  - learning
status: stable
generated:
  by: process:yt-conferences-okf
  at: 2026-09-12 00:00:00+00:00
---

# Summary

Robert presents an overview of Ray, an open-source project developed to address the growing complexity of modern AI workloads, particularly in reinforcement learning and large-scale data processing.
He explains how Ray, in combination with Kubernetes, PyTorch, and frameworks like VLM, forms an emerging software stack that enables organizations to efficiently process multimodal data, train and serve increasingly complex models, and manage distributed systems challenges such as resource allocation, failure handling, and autoscaling.
Ray’s actor abstraction allows users to easily scale Python classes and functions across clusters, supporting diverse workloads from data processing to reinforcement learning, and recent enhancements include native GPU-to-GPU data transfer.
Robert highlights the importance of collaboration between Ray and other open-source communities, the integration with the PyTorch and Linux Foundations, and the development of a rich ecosystem of libraries on top of Ray.
He also clarifies the complementary roles of Ray and Kubernetes, emphasizing that Ray manages process-level orchestration within workloads while Kubernetes handles container-level management, and discusses ongoing efforts to improve support for AI workloads in both systems.

# Main Points

|   # | Main point                                                                                                                            |
| --: | ------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Robert introduces himself and the open-source project Ray.                                                                            |
|   2 | Focus of talk: emerging open-source software stack for AI workloads—Kubernetes, Ray, PyTorch, VLM.                                    |
|   3 | AI workloads have become more complex compared to 5–10 years ago.                                                                     |
|   4 | Ray was created at Berkeley to address limitations in existing distributed systems for reinforcement learning and large-scale AI.     |
|   5 | Ray’s actor abstraction allows Python classes to be distributed as actors across a cluster.                                           |
|   6 | Ray supports scaling from one to thousands of actors, enabling complex distributed applications.                                      |
|   7 | Recent Ray development: native RDMA support for efficient GPU-to-GPU weight transfer.                                                 |
|   8 | Ray provides low-level APIs for actors and tasks, making it general-purpose for data processing, model training, and serving.         |
|   9 | Many open-source RL post-training frameworks for LLMs are built on Ray.                                                               |
|  10 | AI data processing is shifting from tabular data to multimodal data (video, PDFs, images, etc.), requiring inference on GPUs.         |
|  11 | Reinforcement learning workloads involve complex coordination between training, data generation, and environment simulation.          |
|  12 | The modern AI software stack:                                                                                                         |
|  13 | Top: Training/inference frameworks (e.g., PyTorch, transformers)                                                                      |
|  14 | Middle: Distributed compute engine (Ray)                                                                                              |
|  15 | Bottom: Container orchestrator (Kubernetes)                                                                                           |
|  16 | Ray and Kubernetes operate at different levels: Ray manages processes inside workloads; Kubernetes manages containers and jobs.       |
|  17 | Ray and Kubernetes complement each other for autoscaling, failure handling, and resource allocation.                                  |
|  18 | Ray joined the PyTorch and Linux Foundation to foster open-source collaboration and adoption.                                         |
|  19 | Ray consists of a core API and a growing ecosystem of third-party libraries for RL, data curation, distributed inference, and agents. |
|  20 | AnyScale was founded to commercialize Ray and provide production features like multi-cloud deployment and observability.              |
|  21 | Kubernetes support for AI workloads is improving, including better accelerator support and topology-aware scheduling                  |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=4o2amJxMHUc)
