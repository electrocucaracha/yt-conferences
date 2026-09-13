---
layout: default
title:
  "SIG-Node: Intro and Deep Dive - Peter Hunt, Red Hat; Sergey Kanzhelev, Google;
  Mrunal Patel, Red Hat"
nav_order: 270
parent: Kubecon Cloudnativecon North America 2025
type: Video Note
description:
  The session, led by Peter from Red Hat and Sergey from Google, provided
  an introduction and deep dive into SIG Node, a key Kubernetes Special Interest Group
  responsible for node-level infrastructure and compute management. The presenters
  de...
resource: https://www.youtube.com/watch?v=CgICiu2d8LI
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

The session, led by Peter from Red Hat and Sergey from Google, provided an introduction and deep dive into SIG Node, a key Kubernetes Special Interest Group responsible for node-level infrastructure and compute management.
The presenters detailed the role of the kubelet, which manages pod lifecycle, resource allocation, and integration with storage and networking plugins, as well as recent advancements such as dynamic resource allocation (DRA), memory swap support, and in-place pod resource updates.
They highlighted the significant productivity of SIG Node, including numerous merged enhancements (KEPs) and the introduction of the "KEP Wrangler" program to streamline proposal processes.
Sergey focused on the evolution of pod and container restart policies, explaining how new features now allow for granular control over individual container restarts—addressing long-standing user requests and supporting complex workloads like AI/ML training and gaming servers.
The session also covered recent deprecations, ongoing working groups (such as node lifecycle and checkpoint/restore), and encouraged community involvement, emphasizing that feedback and participation are vital to SIG Node’s continued progress.

# Main Points

|   # | Main point                                                                                                                                    |
| --: | --------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | SIG Node session led by Peter (Red Hat) and Sergey (Google)                                                                                   |
|   2 | SIG Node is where infrastructure ends and compute begins in Kubernetes                                                                        |
|   3 | Kubelet is the main agent on every Kubernetes node, responsible for:                                                                          |
|   4 | Registering node with API                                                                                                                     |
|   5 | Watching and reconciling pod state                                                                                                            |
|   6 | Creating static pods and pulling pods from API                                                                                                |
|   7 | Connecting to plugins: CSI (storage), DRA (dynamic resource allocation), CRI (container runtime)                                              |
|   8 | Advertising resources, applying limits/quotas, handling admission, allocating/deallocating resources                                          |
|   9 | Monitoring resource usage, collecting metrics, restarting failed processes, collecting logs                                                   |
|  10 | Supporting overprovisioning and evicting pods if necessary                                                                                    |
|  11 | CRI implementation (container runtime) executes kubelet's instructions (pull images, create sandboxes/containers)                             |
|  12 | Node Problem Detector monitors node conditions                                                                                                |
|  13 | SIG Node collaborates with SIG Storage (CSI), SIG Networking (CNI), and device management working groups                                      |
|  14 | Recent achievements:                                                                                                                          |
|  15 | SIG Node has led in merged KEPs (Kubernetes Enhancement Proposals) since v1.30                                                                |
|  16 | 26 KEPs merged in v1.34; highlights include container restart rules, DRA structured parameters, memory swap GA, in-place pod resource updates |
|  17 | v1.35: more KEPs merged, container restart rules to alpha, node declared features, partitionable devices, in-place pod resource update GA     |
|  18 | Keep Wrangler program helps manage KEP process and deadlines                                                                                  |
|  19 | Deprecations:                                                                                                                                 |
|  20 | cgroup v1 deprecated in v1.35 (move to v2)                                                                                                    |
|  21 | containerd 1.x series deprecated; kubelet will not start with these in v1.36                                                                  |
|  22 | Ongoing work:                                                                                                                                 |
|  23 | SIG Node CI meeting for bug triage and CI stabilization                                                                                       |
|  24 | Working groups: node lifecycle (graceful shutdown/eviction), checkpoint/restore (API for checkpointing/restoring pods)                        |
|  25 | Node readiness gates project to taint nodes with not-ready plugins                                                                            |
|  26 | Focus on AI/ML improvements and resource utilization                                                                                          |
|  27 | Pod/container restart policy deep dive:                                                                                                       |
|  28 | Historical limitations with pod-level restart policy                                                                                          |
|  29 | Sideca                                                                                                                                        |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=CgICiu2d8LI)
