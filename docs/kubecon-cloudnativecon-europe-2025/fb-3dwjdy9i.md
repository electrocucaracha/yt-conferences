---
layout: default
title: "Tutorial: Exploring Multi-Tenant Kubernetes APIs and Controllers With Kcp"
nav_order: 350
parent: Kubecon Cloudnativecon Europe 2025
type: Video Note
description: Here is a summary of the video transcript in 3-5 sentences.
resource: https://www.youtube.com/watch?v=Fb_3dWJdY9I
tags:
  - kubecon-cloudnativecon-europe-2025
  - video
  - learning
status: stable
generated:
  by: process:yt-conferences-okf
  at: 2026-09-12 00:00:00+00:00
---

# Summary

Here is a summary of the video transcript in 3-5 sentences: The workshop tutorial covers exploring multi-tenant Kubernetes APIs and controllers with KCP, a Kubernetes-like control plane that uses Kubernetes-style APIs but is not Kubernetes itself.
The tutorial guides participants through setting up environments, creating workspaces, and binding to API exports to share resources between workspaces.
The workshop also explores the concept of dynamic providers, including API sync agents that connect KCP to Kubernetes clusters and synchronize resources.
Participants can try exercises from the documentation on their own and attend a follow-up talk by MJ and Nabarun on resource models beyond Kubernetes workloads and multicluster runtime.

# Main Points

|   # | Main point                                                                                                              |
| --: | ----------------------------------------------------------------------------------------------------------------------- |
|   1 | The workshop is hands-on and informal, with a focus on exploring multi-tenant Kubernetes APIs and controllers with KCP. |
|   2 | Prerequisites include four shell terminals, Linux, MacBooks, and GitHub code spaces.                                    |
|   3 | The workshop covers setting up environments, installing KCP, and running the control plane.                             |
|   4 | Workspaces are KCP's unit of tenancy, creating a virtual Kubernetes cluster.                                            |
|   5 | API exports allow sharing APIs between workspaces.                                                                      |
|   6 | API bindings enable consumers to access provider APIs.                                                                  |
|   7 | The API sync agent connects KCP workspaces with Kubernetes clusters.                                                    |
|   8 | The workshop covers creating databases, clusters, and secrets in both KCP and Kubernetes.                               |
|   9 | Multicluster runtime is discussed as a future topic.                                                                    |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=Fb_3dWJdY9I)
