---
type: Video Note
title: "KubeEdge DeepDive: Extending Kubernetes To the... Tina Tsou, Hongbing Zhang, Huan Wei & Yin Ding"
description: "The video features a deep dive into the KubeEdge project, presented by Technical Steering Committee members Kevin Juan and Ahumb. KubeEdge, which graduated at the end of last year, extends Kubernetes capabilities from data centers to edge e..."
resource: https://www.youtube.com/watch?v=LwIiDmesgtw
tags: ["kubecon-cloudnativecon-north-america-2025", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

The video features a deep dive into the KubeEdge project, presented by Technical Steering Committee members Kevin Juan and Ahumb.
KubeEdge, which graduated at the end of last year, extends Kubernetes capabilities from data centers to edge environments, enabling workloads to run efficiently on diverse and resource-constrained edge nodes with unstable network connections.
The speakers highlight significant real-world deployments, such as smart retail systems, highway tolling, smart vehicles, satellites, and robotics, emphasizing KubeEdge’s lightweight architecture, unified abstraction for heterogeneous hardware, and robust remote management features.
They discuss technical aspects like network communication, device management, edge-to-edge networking, and AI integration, as well as the project’s transparent and sustainable governance model, broad industry adoption, and active community engagement.
The Q&A addresses topics including deployment at scale, security, minimal resource requirements, and the architectural differences between KubeEdge and other edge Kubernetes solutions, underscoring KubeEdge’s focus on lightweight, autonomous edge operations and seamless cloud collaboration.
# Main Points

|   # | Main point                                                                                                                                                        |
| --: | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | CubeEdge is an open-source project focused on extending Kubernetes to edge computing scenarios.                                                                   |
|   2 | The project started in 2018 and graduated at the end of last year.                                                                                                |
|   3 | CubeEdge enables workloads to run outside data centers, supporting deployment in diverse physical locations.                                                      |
|   4 | Notable adoptions include highway tolling systems (2020), smart vehicles (first cloud-native car, 2021), and low earth orbit satellites.                          |
|   5 | CubeEdge addresses challenges like limited edge resources, unstable network connections, and heterogeneous hardware.                                              |
|   6 | The architecture places nodes on the edge, not entire clusters, to minimize footprint and enable collaboration between cloud/data center and edge nodes.          |
|   7 | Communication between control plane and edge nodes uses WebSocket and QUIC protocols.                                                                             |
|   8 | Community work is organized by SIGs (Special Interest Groups), similar to Kubernetes.                                                                             |
|   9 | Improvements include better image downloading, automatic restarting of edge modules, and remote maintenance/upgrading.                                            |
|  10 | Device IoT management is simplified with unified abstraction and device management interface (DMI), supporting multiple programming languages for device plugins. |
|  11 | EdgeMesh subproject provides P2P tunneling, node-local DNS, and seamless workload communication between edge nodes.                                               |
|  12 | SEDA subproject supports AI at the edge, including joint inference and federated learning to optimize resource use and bandwidth.                                 |
|  13 | Robotics support is being developed, including collaboration with the ROS community for robot fleet management.                                                   |
|  14 | Case studies include smart retail (10,000+ stores), express highway tolling (10,000+ gates), and robotics scenarios.                                              |
|  15 | CubeEdge enables autonomous operation at the edge, seamless upgrades, and consistent experience between data center and edge.                                     |
|  16 | Governance is transparent and sustainable, with a Technical Steering Committee, subcommittees, SIGs, and regular meetings.                                        |
|  17 | Partnerships span industry, academia, and research, with mentorship programs and active community engagement.                                                     |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=LwIiDmesgtw)