---
type: Video Note
title: "A Unified Management and Control Plane for Cloud Native Robots Wi... Sitong Mao, Huan Wei & Yin Ding"
description: "In this presentation at KubeCon Europe 2026, Juan and Ding, both KubeEdge TSC members, introduce a unified management and control plane for cloud-native robots using KubeEdge. They explain that as robotics evolves toward multi-robot collabo..."
resource: https://www.youtube.com/watch?v=e1x5R6dZ-sE
tags: ["kubecon-cloudnativecon-europe-2026", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

In this presentation at KubeCon Europe 2026, Juan and Ding, both KubeEdge TSC members, introduce a unified management and control plane for cloud-native robots using KubeEdge.
They explain that as robotics evolves toward multi-robot collaboration, remote operation, and AI-driven upgrades, there is a need for a platform that supports both real-time edge autonomy and scalable cloud management.
KubeEdge extends Kubernetes to the edge, enabling centralized resource management, dynamic workload shifting, and seamless integration of edge devices within a single cluster, which reduces infrastructure overhead and accelerates development cycles.
The speakers detail how KubeEdge leverages Kubernetes concepts like CRDs and controllers to manage robot registration, task assignment, and synchronization between cloud and edge, and demonstrate a live example where natural language processing in the cloud assigns tasks to multiple robots, optimizing operations and reducing onboarding time for new robots.
The session concludes with a discussion on the technical architecture, real-world deployment benefits such as increased efficiency and rapid robot integration, and answers to audience questions about orchestration, communication protocols, and practical use cases.
# Main Points

|   # | Main point                                                                                                                                                           |
| --: | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Presentation on unified management and control plane for cloud native robots with KubeEdge                                                                           |
|   2 | Robotics field moving from isolated control to multi-robot collaboration, remote operation, continuous upgrades, and AI enhancement                                  |
|   3 | Need for a platform handling both site-level real-time behavior and cloud-scale governance                                                                           |
|   4 | KubeEdge provides edge autonomy for real-time operation and cloud native engineering for scalable, reliable systems                                                  |
|   5 | Benefits include smarter robots, centralized cloud resources (AI models, maps, policies), local edge sensing and control, and collaborative cloud-edge intent agents |
|   6 | Economical development by reusing Kubernetes ecosystem (logging, monitoring, multi-site operation)                                                                   |
|   7 | No need to build separate platforms for each robot type or project                                                                                                   |
|   8 | Compute workloads can dynamically shift between cloud and edge                                                                                                       |
|   9 | Lightweight solution by reducing Kubernetes APIs and control plane patterns; all edge applications and devices in one cluster                                        |
|  10 | Reduces overhead for scheduling, configuration, measurement, and updates                                                                                             |
|  11 | Faster development iteration with unified CI/CD workflow, OTA updates, and standardized version release                                                              |
|  12 | KubeEdge is the first open source project for edge computing with cloud native principles, enabling consistent lifecycle management across cloud and edge            |
|  13 | Over 8,400 GitHub stars, 2,400 forks, 1,600 contributors from 100+ organizations                                                                                     |
|  14 | KubeEdge extends Kubernetes control plane to the edge; cloud core runs in cloud, edge core on each edge node                                                         |
|  15 | Enables management of edge using familiar Kubernetes APIs in a single cluster                                                                                        |
|  16 | Supports reliable offline operations and efficient data transmission                                                                                                 |
|  17 | Edge autonomy: local database (SQLite) stores latest watch info, enabling smooth operation even if cloud connection is lost                                          |
|  18 | Cloud-edge collaboration: manage resources and devices across cloud and edge; mapper framework connects various devices                                              |
|  19 | Design layers cloud-native orchestration over legacy systems; unified control plane for cloud manage                                                                 |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=e1x5R6dZ-sE)