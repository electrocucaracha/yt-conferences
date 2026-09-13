---
layout: default
title:
  Dynamic Multi-Cluster Controllers With Controller-runtime - Marvin Beckers
  & Stefan Schimanski
nav_order: 78
parent: Kubecon Cloudnativecon Europe 2025
type: Video Note
description:
  Marvin Beckers, a team lead at Kubernetic, discusses writing dynamic
  multicluster controllers with controller runtime. He explains that multicluster
  runtime is an extension of controller runtime, adding a provider concept to enable
  reconcil...
resource: https://www.youtube.com/watch?v=Tz8IcMSY7jw
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

Marvin Beckers, a team lead at Kubernetic, discusses writing dynamic multicluster controllers with controller runtime.
He explains that multicluster runtime is an extension of controller runtime, adding a provider concept to enable reconciliation across multiple clusters.
The project aims to provide a generic and integrated solution for managing multiple Kubernetes clusters, allowing users to scale their controllers more efficiently.
Marvin showcases the code and demonstrates how to build a multicluster controller using the new multicluster runtime, highlighting its benefits and potential use cases.

# Main Points

|   # | Main point                                                                                                                        |
| --: | --------------------------------------------------------------------------------------------------------------------------------- |
|   1 | There are different scaling models for controllers:                                                                               |
|   2 | One per cluster                                                                                                                   |
|   3 | One management cluster and dynamic controller launches                                                                            |
|   4 | Host cluster with multiple managers                                                                                               |
|   5 | Multicluster runtime is a friendly extension of controller runtime, not a fork.                                                   |
|   6 | It adds a provider concept to discover and manage clusters.                                                                       |
|   7 | Providers can be implemented in different ways (e.g., kind provider, KCP provider).                                               |
|   8 | The multicluster manager is responsible for managing the providers and reconcilers.                                               |
|   9 | Reconcilers use a builder package to reconcile events from caches.                                                                |
|  10 | Multicluster runtime uses generic types from controller runtime with concrete multicluster-aware types.                           |
|  11 | Providers are responsible for watching changes in the cluster fleet, creating caches, and disengaging clusters when they go away. |
|  12 | The multicluster manager is tightly integrated with the reconcilers and providers.                                                |
|  13 | There are plans to gather feedback from existing code bases and integrate with cluster profile provider on sig multicluster.      |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=Tz8IcMSY7jw)
