---
layout: default
title: "The Need for Speed: Accelerating OpenStack with NVMe-oF & Ceph"
nav_order: 24
parent: OpenInfra Summit Europe 2025
type: Video Note
description: The transcript presents a technical overview of integrating Ceph Storage (Ceph) with NVMe over TCP (NVMe/TCP) to address storage bottlenecks in AI and machine learning workloads.
resource: "https://www.youtube.com/watch?v=EigHsQYIi0A"
youtube_stats:
  view_count: 263
  like_count: 5
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

The transcript presents a technical overview of integrating Ceph Storage (Ceph) with NVMe over TCP (NVMe/TCP) to address storage bottlenecks in AI and machine learning workloads.
The speaker explains that as AI evolves from traditional algorithms to Large Language Models (LLMs) and physical AI, data volumes are expanding from megabytes to exabytes, creating a critical need for high-performance storage that prevents GPUs from sitting idle due to slow I/O.
A basic ML pipeline is outlined, recommending object storage for unstructured data, file systems for processing and training, and low-latency solutions for vector databases and model inference.
The core of the presentation focuses on NVMe/TCP, a protocol that allows NVMe commands to be sent over standard IP networks, offering low latency and high throughput by bypassing the kernel, and introduces the NVMe-oF Gateway as a service that exposes Ceph RBD images as NVMe devices.
The speaker demonstrates a custom integration with OpenStack, detailing how volume creation requests trigger the configuration of NVMe subsystems and namespaces via gRPC, allowing virtual machines to attach to these high-performance block devices.
Performance testing using the fio tool confirms that a single block device can scale to handle high I/O operations, and the architecture supports high availability through multipath connections via multiple gateways.
Finally, the speaker discusses specific use cases, such as RAG pipelines and vector databases, where low latency is essential, and clarifies that while the current gateway implementation supports TCP, it does not natively support RDMA, which remains a separate protocol within the broader NVMe specification.

# Main Points

|   # | Main point                                                                                                                                |
| --: | ----------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | The speaker is a certified architect and artist who specializes in integrating multiple technologies and calligraphy.                     |
|   2 | The presentation covers storage concepts in data pipelines, the role of Ceph (SE), NVMe over TCP architecture, and OpenStack integration. |
|   3 | AI workloads require high compute power, but storage often lags behind, causing GPUs to sit idle due to I/O bottlenecks.                  |
|   4 | Data consumption is evolving from megabytes in traditional algorithms to petabytes in Large Language Models and exabytes in physical AI.  |
|   5 | A basic ML pipeline includes unstructured data storage, data processing, model training, checkpointing, deployment, and monitoring.       |
|   6 | Object storage or data lakes are recommended for unstructured data, while file storage is preferred for processing and training.          |
|   7 | Model checkpointing and serving can utilize file systems or object storage, with vector databases requiring low-latency access.           |
|   8 | Key storage challenges include capacity, I/O performance bottlenecks, cost scalability trade-offs, and data accessibility.                |
|   9 | Ceph is a software-defined storage solution that is massively scalable, self-healing, and supports block, file, and object protocols.     |
|  10 | NVMe over TCP uses NVMe commands over the internet, bypassing the kernel for low latency and high throughput.                             |
|  11 | The NVMe-oF gateway provides block-level access to Ceph and allows for dynamic configuration and scalability tuning.                      |
|  12 | NVMe terminology includes namespaces (mapped to RBD images), subsystems (groups of namespaces), controllers, and listeners.               |
|  13 | Gateway groups enable high availability by grouping multiple gateways to provide multipath access to the initiator.                       |
|  14 | Performance testing using the fio tool demonstrates that a single block device can scale to handle a high number of I/O operations.       |
|  15 | The speaker designed code to integrate OpenStack with Ceph via the NVMe-oF gateway, consisting of approximately 315 lines.                |
|  16 | The integration involves creating RBD images, configuring NVMe subsystems via gRPC, and mapping devices to Nova servers.                  |
|  17 | Upon volume attachment, the system creates an NVMe subsystem and exposes the RBD image to the client.                                     |
|  18 | Upon volume detachment, the namespace is removed to allow remapping to other servers, while the subsystem may persist for reuse.          |
|  19 | Deleting the volume destroys the namespace because the RBD image is mapped to it, ensuring resource cleanup.                              |
|  20 | The demo shows creating an NVMe volume type in OpenStack, attaching it to a VM, and verifying the device mapping.                         |
|  21 | Primary use cases include vector databases for RAG pipelines and database applications requiring low latency.                             |
|  22 | The NVMe gateway can handle small data requests locally, reducing load on the Ceph cluster for better performance.                        |
|  23 | High availability is achieved through multipath connections where two controllers provide separate data paths to the client.              |
|  24 | The gateway currently supports the TCP protocol for NVMe-oF but does not natively support RDMA in this implementation.                    |
|  25 | Ceph supports various backend devices, including SSDs and HDDs, though HDDs may introduce performance bottlenecks.                        |
|  26 | The solution allows for flexible deployment using standard IP networks without requiring specific infrastructure like Fiber Channel.      |

# Video

[![Video thumbnail](https://img.youtube.com/vi/EigHsQYIi0A/hqdefault.jpg)](https://www.youtube.com/watch?v=EigHsQYIi0A)

[Watch on YouTube](https://www.youtube.com/watch?v=EigHsQYIi0A)
