---
layout: default
title:
  "Beyond the Edge: Cloud Native Application Management Under Ex... Tobias Nöthlich
  & Maximilian Nitsch"
nav_order: 28
parent: Kubecon Cloudnativecon Europe 2026
type: Video Note
description:
  In this presentation, Tubius and Maximan, R&D engineers from a Dston-based
  company, discuss their efforts to enable cloud-native application management in
  space and other extreme network environments. They outline the unique challenges
  of d...
resource: https://www.youtube.com/watch?v=9YjpYZVz6_4
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

In this presentation, Tubius and Maximan, R&D engineers from a Dston-based company, discuss their efforts to enable cloud-native application management in space and other extreme network environments.
They outline the unique challenges of deploying such applications in space, including high latency, frequent disruptions, lack of standardized execution environments, insufficient tenant separation, and complex software deployment processes.
To address these, they leverage Delay and Disruption Tolerant Networking (DTN) and introduce their research project, Dark Soul, which aims to build a DTN-based cloud infrastructure for space operations.
Their solution involves extending Kubernetes and Helm with a custom plugin, "helm dtn," and using their DTN protocol implementation, "microdtn," to package and transfer all necessary application dependencies as a single archive to remote clusters, overcoming connectivity issues.
Additionally, they developed a custom resource definition, "Dgate," to manage ingress and egress of application data over DTN links, enabling reliable communication between space and Earth-based clusters.
The presentation concludes with key takeaways about the importance of DTN for space networking, current limitations, and future work, including autonomous deployment, improved security, and practical testing with satellites.

# Main Points

|   # | Main point                                                                                                                                                         |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   1 | Presenters: Tubius and Maximan, R&D engineers at a Dston-based company.                                                                                            |
|   2 | Goal: Bring cloud-native application management to space and extreme network environments.                                                                         |
|   3 | Motivation:                                                                                                                                                        |
|   4 | Deep space links are discontinuous, delayed, low bandwidth, and frequently disrupted.                                                                              |
|   5 | No flexible, easy-to-use cloud-native execution environments for space agencies.                                                                                   |
|   6 | Insufficient tenant separation for space hardware/software platforms.                                                                                              |
|   7 | Deploying new software to satellites/rovers requires dedicated, non-public toolchains.                                                                             |
|   8 | Standard Kubernetes is unsuitable for space due to reliance on stable, low-latency networks.                                                                       |
|   9 | Solution: Use Delay and Disruption Tolerant Networking (DTN) as an overlay network with hop-by-hop data transfer and persistent storage.                           |
|  10 | Project: Dark Soul (DTN architectures for space operations and cloud lifecycle management), in collaboration with T University of Technology and Cyrus Technology. |
|  11 | Approach:                                                                                                                                                          |
|  12 | Build DTN-tolerant cloud infrastructure.                                                                                                                           |
|  13 | Apply secure separation for multi-tenant operations.                                                                                                               |
|  14 | Enable DTN-tolerant application operations.                                                                                                                        |
|  15 | Cluster Design:                                                                                                                                                    |
|  16 | Multiple clusters (Earth, satellites, Mars, ground stations) connected via DTN.                                                                                    |
|  17 | Management node runs control plane; worker nodes run workloads.                                                                                                    |
|  18 | Clusters can be traditional, LEO satellite constellations, or isolated autonomous clusters.                                                                        |
|  19 | Deployment Challenge:                                                                                                                                              |
|  20 | Helm/Kubernetes workflows require stable connections for image pulls and API calls, which are impractical in space.                                                |
|  21 | Solution Developed:                                                                                                                                                |
|  22 | Helm DTN plugin: Preloads all dependencies and images, updates references to local registry, packages everything into a tar archive.                               |
|  23 | Uses microdtn (DTN protocol implementation) to transfer the archive between Earth and space clusters.                                                              |
|  24 | Application lifecycle management engine on the remote cluster unpacks and deploys the application.                                                                 |
|  25 | Communication Challenge:                                                                                                                                           |
|  26 | Need delay-tolerant ingress/egress for application data between clusters.                                                                                          |
|  27 | Attempted Solutions:                                                                                                                                               |
|  28 | Gatew                                                                                                                                                              |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=9YjpYZVz6_4)
