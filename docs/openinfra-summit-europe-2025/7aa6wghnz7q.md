---
layout: default
title: AI Infrastructure at Scale – Unlocking the Power of OpenStack for AI and Machine Learning
nav_order: 49
parent: OpenInfra Summit Europe 2025
type: Video Note
description: "The presentation outlines the critical infrastructure shifts required to support the rapid growth of AI workloads, which are projected to triple by 2030, necessitating a rethinking of traditional c..."
resource: "https://www.youtube.com/watch?v=7aa6Wghnz7Q"
youtube_stats:
  view_count: 153
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

The presentation outlines the critical infrastructure shifts required to support the rapid growth of AI workloads, which are projected to triple by 2030, necessitating a rethinking of traditional cloud foundations for compute, storage, and networking.
It details how OpenStack capabilities, specifically Nova, Cyborg, and Neutron, facilitate AI infrastructure by managing GPU pass-through, accelerator scheduling, and high-speed data connectivity.
The speaker explores eight distinct architectural patterns, ranging from foundational AI launchpads and GPU maximization strategies to advanced implementations like LLM factories, real-time edge computing, and RAG-based data refineries.
These architectures leverage technologies such as NVLink, InfiniBand, and Kubernetes integration to address challenges in massive parallelism, data gravity, and latency sensitivity.
Finally, the talk emphasizes best practices for cost optimization and performance tuning, highlighting that OpenStack’s open-source, vendor-neutral approach allows organizations to achieve significant efficiency gains and maintain data sovereignty compared to fixed cloud services.

# Main Points

|   # | Main point                                                                                                                                                   |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   1 | AI workloads are projected to triple by 2030, driving increased demand for energy and infrastructure.                                                        |
|   2 | AI has transitioned from experimental stages to business-critical production use cases involving large language models and computer vision.                  |
|   3 | Core challenges include massive parallelism, enormous data gravity, the need for accelerated networking, and managing burst versus idle lifecycles.          |
|   4 | Current infrastructure reality requires rethinking computing, storage, and networking fundamentals to support high-density GPUs and petabyte-scale datasets. |
|   5 | OpenStack capabilities for AI include Nova for compute instances, Cyborg for accelerator scheduling, and Neutron for networking integration.                 |
|   6 | GPU pass-through provides direct hardware access for performance, while vGPU allows shared access for multiple tenants.                                      |
|   7 | Cyborg manages the lifecycle and scheduling of GPU availability to optimize resource allocation.                                                             |
|   8 | The Golden Stack combines OpenStack infrastructure services with Kubernetes container services to run AI applications.                                       |
|   9 | Accelerator management approaches include PCI pass-through for raw performance, vGPU for sharing, and MIG for deterministic hardware isolation.              |
|  10 | Data preparation requires high-throughput sequential reads and support for structured and unstructured data formats.                                         |
|  11 | Training phases demand sustained high bandwidth, random access, and checkpointing capabilities for large datasets.                                           |
|  12 | Inference requires low-latency access and concurrent request handling supported by storage and networking layers.                                            |
|  13 | Storage strategies include using Ceph and Swift for block and object storage, and NVMe localStorage for fast caching.                                        |
|  14 | Networking for high-bandwidth GPU interconnect utilizes NVLink and InfiniBand technologies.                                                                  |
|  15 | Emerging architectures include disaggregated infrastructure, AI at the edge, and serverless AI for cost-effective scaling.                                   |
|  16 | The AI Launchpad architecture uses Keystone, Nova, Ceph, and Neutron to provide a foundational environment for machine learning engineers.                   |
|  17 | The GPU Maximize pattern uses Cyborg and Horizon to distribute GPUs across different access modes for sharing or performance.                                |
|  18 | The Assembly Line pattern integrates CI/CD pipelines with Kubernetes via Magnum for MLOps deployment and model versioning.                                   |
|  19 | The LLM Factory pattern utilizes bare metal access, NVLink, and parallel file systems for distributed training of large language models.                     |
|  20 | The Real-Time Edge pattern distributes models to edge devices like autonomous vehicles for millisecond-level decision-making.                                |
|  21 | The Hybrid Burst pattern combines on-premise OpenStack resources with cloud services to handle unexpected demand spikes.                                     |
|  22 | The Shield pattern supports federated learning to maintain data sovereignty and compliance by training models locally and sharing only parameters.           |
|  23 | The Data Refinery pattern implements Retrieval-Augmented Generation using vectorized data stored in Ceph or Kubernetes databases.                            |
|  24 | Real-world deployments of OpenStack for AI have demonstrated approximately 55% cost reduction and improved efficiency.                                       |
|  25 | Best practices include leveraging the open-source community, choosing the right GPU mode, and adopting hybrid or multi-cloud strategies.                     |
|  26 | Optimizing GPU usage involves reservation, scheduling, and performance tuning using tools like vLLM and MUSA.                                                |
|  27 | Autoscaling and monitoring are essential for matching infrastructure capacity to dynamic machine learning demand.                                            |
|  28 | AI at scale requires specialized infrastructure that allows organizations to customize compute, storage, and networking beyond fixed cloud offerings.        |

# Video

[![Video thumbnail](https://img.youtube.com/vi/7aa6Wghnz7Q/hqdefault.jpg)](https://www.youtube.com/watch?v=7aa6Wghnz7Q)

[Watch on YouTube](https://www.youtube.com/watch?v=7aa6Wghnz7Q)
