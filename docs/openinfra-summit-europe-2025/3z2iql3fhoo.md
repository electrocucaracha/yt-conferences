---
layout: default
title: Architecting a Managed Kubernetes Service on OpenStack for Public Cloud Delivery
nav_order: 33
parent: OpenInfra Summit Europe 2025
type: Video Note
description: "The speaker from Kakao Cloud presents the architectural design and operational challenges of their managed Kubernetes service, which was developed to serve as a late entrant in the public cloud mar..."
resource: "https://www.youtube.com/watch?v=3z2IQl3fHoo"
youtube_stats:
  view_count: 207
  like_count: 3
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

The speaker from Kakao Cloud presents the architectural design and operational challenges of their managed Kubernetes service, which was developed to serve as a late entrant in the public cloud market by adopting best practices from global providers.
A primary design goal was to hide the control plane from end users by isolating it in a separate VPC and using custom bootstrapping logic that prevents control plane nodes from joining the cluster as standard nodes, thereby enhancing security and management consistency.
Following a major data center fire in South Korea in 2022, the team prioritized high availability by implementing a multi-AZ architecture that separates ETCD servers from the control plane, allowing for independent scaling and resilience against single-site failures.
To address performance concerns associated with multi-AZ latency, the team utilized high-bandwidth transit gateways and software-level optimizations such as topology-aware scheduling hints and efficient proxy solutions.
The presentation also details a zero-downtime blue-green upgrade strategy using Cluster API templates and resolves specific operational issues, such as file descriptor exhaustion in ETCD, by implementing client caching and server-side connection cleanup mechanisms.

# Main Points

|   # | Main point                                                                                                                                                                   |
| --: | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Kakao Cloud launched in 2023 to enter the public cloud market, leveraging the dominance of the Kakao messenger app in South Korea.                                           |
|   2 | The team developed a managed Kubernetes service with two primary goals: learning global best practices and ensuring multi-AZ availability.                                   |
|   3 | A 2022 data center fire in South Korea served as a critical catalyst for adopting multi-AZ architectures to prevent total service outages.                                   |
|   4 | The infrastructure is Kubernetes-native, using Cluster API and Cluster API Provider OpenStack to manage clusters declaratively.                                              |
|   5 | A "Ring Zero" management cluster acts as the core infrastructure, provisioning and controlling all other Kubernetes clusters automatically.                                  |
|   6 | The architecture separates the control plane into a dedicated management VPC to hide it from end users and enhance security.                                                 |
|   7 | A dedicated router connects the management VPC and user VPC, allowing worker nodes to access the Kubernetes API server via internal endpoints.                               |
|   8 | Control plane nodes are installed in standalone mode rather than joining the cluster as nodes, requiring custom health checks via the API server.                            |
|   9 | Essential static pods and add-ons are managed by lightweight agents that watch cluster state and synchronize components using internal Helm charts.                          |
|  10 | High availability is achieved by distributing control plane nodes and etcd servers across three availability zones.                                                          |
|  11 | Separating etcd from the control plane allows independent scaling and prevents control plane failures from affecting etcd stability.                                         |
|  12 | Network latency concerns in multi-AZ setups were addressed by using high-bandwidth transit gateways and topology-aware scheduling hints.                                     |
|  13 | For large-scale clusters, performance is improved by using eBPF-based proxy solutions like Cilium or Kicole to reduce latency.                                               |
|  14 | Cluster upgrades utilize a blue-green deployment strategy to ensure zero downtime during version transitions.                                                                |
|  15 | The upgrade process sequentially provisions new etcd members, updates control plane nodes one by one, and gracefully transfers leadership before scaling down old resources. |
|  16 | Operational challenges included etcd file descriptor exhaustion caused by creating new gRPC connections for every reconcile loop.                                            |
|  17 | This issue was resolved by implementing an etcd client cache to reuse connections and optimizing gRPC efficiency.                                                            |
|  18 | Server-side issues with lingering TCP connections were addressed by periodically closing idle connections and increasing file descriptor limits.                             |
|  19 | Ongoing work includes developing a custom CNI for cross-VPC pod-to-pod communication and achieving CNCF certification compliance.                                            |

# Video

[![Video thumbnail](https://img.youtube.com/vi/3z2IQl3fHoo/hqdefault.jpg)](https://www.youtube.com/watch?v=3z2IQl3fHoo)

[Watch on YouTube](https://www.youtube.com/watch?v=3z2IQl3fHoo)
