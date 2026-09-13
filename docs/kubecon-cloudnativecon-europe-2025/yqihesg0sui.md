---
layout: default
title:
  "More Nodes, More Problems: Solving Multi-Host GPU/TPU Scheduli... John Belamaric
  & Morten Torkildsen"
nav_order: 198
parent: Kubecon Cloudnativecon Europe 2025
type: Video Note
description: Here is a summary of the video transcript in 3-5 sentences.
resource: https://www.youtube.com/watch?v=YqIHESG0suI
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

Here is a summary of the video transcript in 3-5 sentences: John Bellame from Google discusses the challenges of managing large-scale workloads with accelerators like TPUs and GPUs, which can lead to failure points across nodes.
To address this, John introduces Dynamic Resource Allocation (DRA), a new API that allows users to request devices and makes them available to pods and containers.
DRA aims to improve compact placement, reduce failures, and provide self-healing capabilities, but still has limitations in handling complex resource relationships.
The technology is being developed by the Kubernetes community, with ongoing work to address issues like tolerations for GPU resources and device capabilities.

# Main Points

|   # | Main point                                                                                                                                                                         |
| --: | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Kubernetes is working on a new feature called Dynamic Resource Allocation (DRA) to manage advanced use cases.                                                                      |
|   2 | DRA allows users to request devices and make them available to pods and containers.                                                                                                |
|   3 | The feature has four parts: API to describe devices, API for letting users request devices, allocation of devices to satisfy claims, and activation of decisions by the scheduler. |
|   4 | DRA can model devices that are accessible across multiple nodes, such as GPUs or TPUs.                                                                                             |
|   5 | The feature includes device taints, which allow devices to be marked as not suitable for certain workloads.                                                                        |
|   6 | DRA is being used in production environments, including Google's Kubernetes cluster and Nvidia's GKE.                                                                              |
|   7 | The feature is still in development and has some limitations, but it is expected to improve the scalability and flexibility of Kubernetes.                                         |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=YqIHESG0suI)
