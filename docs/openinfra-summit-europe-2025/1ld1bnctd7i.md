---
layout: default
title: "Next Generation Edge: Edge Computing Architectures for AI/ML Use Cases"
nav_order: 72
parent: OpenInfra Summit Europe 2025
type: Video Note
description: "Eli Kovancha and Beth present a session on edge AI, emphasizing that data is a critical yet often overlooked component of successful edge infrastructure."
resource: "https://www.youtube.com/watch?v=1ld1BNcTd7I"
youtube_stats:
  view_count: 102
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

Eli Kovancha and Beth present a session on edge AI, emphasizing that data is a critical yet often overlooked component of successful edge infrastructure.
They define edge computing as deploying resources closer to end users to handle workloads in constrained environments, distinguishing between centralized control plane architectures and fully distributed models.
The speakers highlight the unique challenges of edge AI, including limited hardware resources, high network latency, and the need for robust security in physically accessible locations like oil rigs or grain silos.
Specific use cases discussed include automotive federated learning, where partial training occurs on vehicles to save costs, and real-time surgical robotics, which requires sub-100-millisecond latency and strict data privacy.
The presentation concludes by advocating for open-source solutions and community collaboration through the OpenInfra Foundation’s Edge Computing Group to address these complex infrastructure and data standardization challenges.

# Main Points

|   # | Main point                                                                                                                                                           |
| --: | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | The Open Infrastructure Foundation Edge Computing Group was established in 2017 to explore edge computing infrastructure and reference architectures.                |
|   2 | Edge computing is defined as deploying hardware and software resources closer to end users to handle workloads locally, often in geographically distributed systems. |
|   3 | Two primary architecture models exist: centralized control planes with edge sites attached, and fully distributed decentralized models with high edge autonomy.      |
|   4 | Data is a critical but often overlooked component of edge AI, requiring infrastructure-level consideration beyond just dataset bias.                                 |
|   5 | Data types range from highly structured (e.g., IP packets) to unstructured (e.g., images) and semi-structured, each presenting different processing challenges.      |
|   6 | Remotely generated data from IoT, drones, and cameras poses unique challenges due to high volume and distributed generation points.                                  |
|   7 | Network constraints at the edge, such as reliance on expensive satellite links in remote areas like oil fields, limit data transmission capabilities.                |
|   8 | Data sovereignty and retention policies vary significantly, with some data useful for only seconds while other data requires permanent storage.                      |
|   9 | Edge hardware must be ruggedized, lightweight, and energy-efficient to operate in harsh environments like grain silos or outdoor 5G antennas.                        |
|  10 | Software at the edge must be self-managing and capable of operating autonomously during network outages to minimize costly physical maintenance.                     |
|  11 | Security is a major concern because edge devices are often physically accessible, increasing risks of data theft or sabotage.                                        |
|  12 | Centralized architectures may fail for use cases requiring ultra-low latency, such as robotic surgery, where data cannot be sent to the cloud.                       |
|  13 | Federated learning in automotive use cases allows cars to perform partial training locally to save costs and handle limited hardware space.                          |
|  14 | Healthcare applications like smart aging devices keep sensitive raw data on-premises to comply with privacy regulations and prevent data breaches.                   |
|  15 | Real-time surgical imaging requires sub-100 millisecond latency, necessitating local processing and efficient power management.                                      |
|  16 | Return on investment remains a significant challenge for companies deploying AI at the edge, especially given the high costs of specialized hardware.                |
|  17 | The rapid evolution of AI technology makes it difficult to build long-term architectures, requiring a balance between cost and capability.                           |
|  18 | Open-source projects under the Linux Foundation and Open Infrastructure Foundation provide essential infrastructure components for edge AI.                          |
|  19 | Standardization of data formats across different devices and telecom networks remains a significant unresolved challenge for edge analytics.                         |
|  20 | The Edge Computing Group plans to develop detailed reference architectures and invites community participation through weekly meetings and mailing lists.            |

# Video

[![Video thumbnail](https://img.youtube.com/vi/1ld1BNcTd7I/hqdefault.jpg)](https://www.youtube.com/watch?v=1ld1BNcTd7I)

[Watch on YouTube](https://www.youtube.com/watch?v=1ld1BNcTd7I)
