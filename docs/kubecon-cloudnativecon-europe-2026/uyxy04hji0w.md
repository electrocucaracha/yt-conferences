---
layout: default
title:
  "Solving Industrial Challenges With KubeEdge: A Post-Graduation... Yue Bao,
  Hongbing Zhang & Yin Ding"
nav_order: 337
parent: Kubecon Cloudnativecon Europe 2026
type: Video Note
description:
  The video presents an overview of the Kubedge project, which addresses
  industry challenges in cloud-edge coordination using Kubernetes. The speakers, Inding
  and Honging, describe Kubedge’s decade-long journey from its inception in 2018,
  thr...
resource: https://www.youtube.com/watch?v=uYxY04HJI0w
tags:
  - kubecon-cloudnativecon-europe-2026
  - video
  - learning
status: stable
generated:
  by: process:yt-conferences-okf
  at: 2026-09-12 00:00:00+00:00
---

# Summary

The video presents an overview of the Kubedge project, which addresses industry challenges in cloud-edge coordination using Kubernetes.
The speakers, Inding and Honging, describe Kubedge’s decade-long journey from its inception in 2018, through its graduation as the first cloud-native edge project under the CNCF in 2024.
Kubedge enables deployment of Kubernetes control planes in the cloud while managing edge nodes remotely, solving issues like unreliable connections, data privacy, and latency.
The project supports mainstream AI frameworks and advanced features such as federated learning and joint inference, allowing sensitive data to remain at the edge and leveraging both edge and cloud resources for AI tasks.
Several real-world case studies are highlighted, including satellite data processing, large-scale expressway toll systems, new energy vehicles, smart retail, and collaborative robotics, demonstrating Kubedge’s versatility across industries.
The speakers also emphasize the importance of open governance, industry-academic partnerships, community engagement, and mentorship in building a thriving open-source ecosystem for Kubedge.

# Main Points

|   # | Main point                                                                                                                                                       |
| --: | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Presentation focuses on solving industry challenges with KubeEdge.                                                                                               |
|   2 | KubeEdge project started about 10 years ago, graduated in October 2024 at KubeCon Chicago.                                                                       |
|   3 | First cloud native edge project to graduate under CNCF; no other edge project has graduated.                                                                     |
|   4 | KubeEdge uses Kubernetes control plane to solve cloud-edge coordination problems, addressing issues like long latency, unreliable connections, and data privacy. |
|   5 | Control plane is deployed in the cloud; worker nodes are deployed at the edge.                                                                                   |
|   6 | Implements secure, duplex communication channels between cloud and edge.                                                                                         |
|   7 | If edge connection is interrupted, the control plane restores the edge node to the desired state.                                                                |
|   8 | KubeEdge has over 8,000 GitHub stars, 2,000+ forks, and 1,600 contributors from 100+ organizations.                                                              |
|   9 | KubeEdge supports multiple SIGs, including networking, AI, and robotics.                                                                                         |
|  10 | Supports mainstream AI frameworks (TensorFlow, PyTorch, PaddlePaddle, MindSpore).                                                                                |
|  11 | Enables federated learning: data remains at the edge for privacy; only intermediate results are aggregated in the cloud.                                         |
|  12 | Supports joint inference: small models run on edge, large models on cloud; edge handles quick inference, cloud handles complex cases.                            |
|  13 | Case studies:                                                                                                                                                    |
|  14 | Satellite edge computing: satellites as edge nodes process data locally, only results sent to ground stations.                                                   |
|  15 | Expressway toll system in China: manages 100,000+ heterogeneous edge nodes, enables easy firmware/app upgrades, and video surveillance management.               |
|  16 | New energy vehicles: each car as an edge device, AI models predict battery lifecycle, data processed at edge and cloud for continuous model improvement.         |
|  17 | Smart retail: edge servers in stores process customer interactions, cloud broadcasts targeted video streams.                                                     |
|  18 | Collaborative robots: natural language commands processed in cloud, edge devices control robot groups.                                                           |
|  19 | Community building:                                                                                                                                              |
|  20 | Open governance structure with distributed leadership.                                                                                                           |
|  21 | Partnerships with industry, academia, and research.                                                                                                              |
|  22 | Eng                                                                                                                                                              |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=uYxY04HJI0w)
