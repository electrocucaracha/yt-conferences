---
layout: default
title:
  "Kubernetes Network Driver Unpacked: Modularity, Tra... Lionel J, Sebastian
  S, Antonio O & Sunyanan C"
nav_order: 193
parent: Kubecon Cloudnativecon Europe 2026
type: Video Note
description:
  In this panel discussion, experts from Google, Red Hat, IBM, and Reddit
  introduce themselves and discuss advancements in Kubernetes network drivers, focusing
  on the Device Resource Assignment (DRA) framework. They explain that DRA addresses...
resource: https://www.youtube.com/watch?v=xJ9R7NNZMyQ
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

In this panel discussion, experts from Google, Red Hat, IBM, and Reddit introduce themselves and discuss advancements in Kubernetes network drivers, focusing on the Device Resource Assignment (DRA) framework.
They explain that DRA addresses limitations in Kubernetes networking, such as topology awareness, bandwidth allocation, and resource scheduling, which were previously difficult to solve, especially for high-performance and AI workloads.
The panelists debate the merits of a single monolithic driver versus a constellation of specialized drivers, ultimately agreeing that multiple interoperable drivers are preferable due to the complexity and diversity of networking needs.
They highlight ongoing projects like the SR-IOV device plugin, the Multus project, and new APIs for secondary networks, emphasizing efforts to ensure backward compatibility and smooth migration for existing users.
The discussion concludes with insights into current and future driver availability, integration challenges, and the importance of standardizing APIs to enhance portability and flexibility across Kubernetes environments.

# Main Points

|   # | Main point                                                                                                                                                                                   |
| --: | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Panel discusses Kubernetes network drivers, focusing on DRA (Device Resource Assignment)                                                                                                     |
|   2 | Panelists: Antonio H. (Google, Kubernetes Steering Committee), Yan (Red Hat, Multinetics, SIG Network), Sebastian (Reddit, Kubernetes network plumbing), Iman (IBM Research, CNI maintainer) |
|   3 | DRA addresses limitations in Kubernetes networking, enabling topology awareness and cluster-wide resource allocation                                                                         |
|   4 | Telco use case: high-performance networking, SR-IOV devices, low latency, NUMA awareness, and bandwidth allocation                                                                           |
|   5 | AI training use case: secondary networks for increased bandwidth, cost optimization, dynamic metrics, and improved scheduling via DRA                                                        |
|   6 | Multinet project aims to make networks first-class citizens in Kubernetes, leveraging DRA for bandwidth allocation and scheduling integration                                                |
|   7 | Debate on ecosystem: single monolithic driver vs. multiple specialized drivers; consensus leans toward multiple drivers for flexibility and composability                                    |
|   8 | Challenges with legacy APIs (e.g., CNI), lack of scheduling integration, and complexity in supporting diverse CNIs                                                                           |
|   9 | Synchronization and resource management across multiple drivers is an ongoing challenge                                                                                                      |
|  10 | DRA enables migration paths: existing workloads can use extended resources, while new workloads can leverage resource claims and advanced scheduling                                         |
|  11 | New KEPs (Kubernetes Enhancement Proposals) for consumable capacity and shared consumable capacity to improve bandwidth allocation modeling                                                  |
|  12 | Projects mentioned: aret (Google, AI workflows, RDMA), SR-IOV device plugin (Intel, production use), C9 driver (experimental), Kubernetes network drivers repo (for experimentation)         |
|  13 | DRA and CNI are separate tracks; DRA adds new functionality without breaking existing CNI-based networking                                                                                   |
|  14 | Discussion on decomposing drivers, potential for separate IPAM drivers, and modeling IP addresses as consumable resources                                                                    |
|  15 | SR-IOV with DRA supports virtualized environments (e.g., OpenStack VMs as Kubernetes nodes)                                                                                                  |
|  16 | Community is working on portabilit                                                                                                                                                           |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=xJ9R7NNZMyQ)
