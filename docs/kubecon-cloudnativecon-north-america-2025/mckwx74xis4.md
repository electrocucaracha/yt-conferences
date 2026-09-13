---
layout: default
title:
  "10 Years of Cilium: Connecting, Securing... Bill Mulligan, Paul Arah, Neha
  Aggarwal, Satish Krishnan"
nav_order: 1
parent: Kubecon Cloudnativecon North America 2025
type: Video Note
description:
  The session began with an update on the Psyllium project, marking its
  10th anniversary alongside the CNCF. Speakers highlighted Psyllium’s evolution from
  a CNI focused on cloud-native networking to a comprehensive suite including observabil...
resource: https://www.youtube.com/watch?v=mCKwX74xIs4
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

The session began with an update on the Psyllium project, marking its 10th anniversary alongside the CNCF.
Speakers highlighted Psyllium’s evolution from a CNI focused on cloud-native networking to a comprehensive suite including observability (Hubble) and security (Tetragon), all powered by eBPF technology.
Recent advancements in version 1.18 include enhanced IPv6 support, a redesigned load balancer control plane, improved policy isolation, and significant reductions in policy latency and CPU usage.
Microsoft shared how it has integrated Psyllium into Azure CNI to meet hyperscale AI workload demands, introducing features like endpoint slicing and dynamic network metrics filtering to improve scalability and observability.
The session also reflected on Psyllium’s growth, its collaborative open-source community, and its ongoing adaptation to support the next era of AI-driven infrastructure, inviting further community participation and contributions.

# Main Points

|   # | Main point                                                                                                                                                           |
| --: | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | CNCF and Psyllium both celebrate 10-year anniversaries.                                                                                                              |
|   2 | Psyllium started as a CNI for cloud-native networking, expanded into observability (Hubble) and security (Tetragon).                                                 |
|   3 | Powered by Linux kernel eBPF technology for safe, secure kernel reprogramming.                                                                                       |
|   4 | Features include CNI, load balancing, gateway API, multicast, service maps, network flow logs, protocol visibility, runtime enforcement, and deep kernel visibility. |
|   5 | Recent 1.18 release highlights: improved IPv6 support, load balancer control plane redesign, multi-pool IPAM, BGP routing aggregation, gateway API v1.3 support.     |
|   6 | Security/observability updates: better cluster mesh policy isolation, Hubble log field support, enhanced policy dashboard.                                           |
|   7 | Operational improvements: 40% reduced policy latency, 43% lower CPU usage, smaller images, HA for API server communications.                                         |
|   8 | Microsoft integrated Psyllium eBPF data plane into Azure CNI, supporting millions of pod IPs and improving performance/scalability.                                  |
|   9 | Introduced Psyllium endpoint slicers to batch endpoint updates, reducing API server load by up to 10x.                                                               |
|  10 | Enhanced observability with dynamic network metrics filtering and network flow aggregation for scalable analytics.                                                   |
|  11 | For hyperscale AI workloads, disabled CRD watchers and endpoint slices to minimize control plane load, providing basic connectivity and observability.               |
|  12 | Microsoft is prototyping a centralized Psyllium control plane to further reduce API server load and agent overhead, showing 20% improvement in policy recomputation. |
|  13 | Strong collaboration among vendors (Microsoft, Google, Datadog, Cisco) and end users ensures project health and growth.                                              |
|  14 | Psyllium now powers major Kubernetes distributions (Azure, Google, AWS).                                                                                             |
|  15 | Project recently surpassed 1,000 contributors.                                                                                                                       |
|  16 | Community events and case studies highlight real-world usage (e.g., energy sciences, supply chain, eBay security).                                                   |
|  17 | Upcoming resources: "Psyllium Up and Running" book, children's book, new eBPF white paper.                                                                           |
|  18 | Active community engagemen                                                                                                                                           |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=mCKwX74xIs4)
