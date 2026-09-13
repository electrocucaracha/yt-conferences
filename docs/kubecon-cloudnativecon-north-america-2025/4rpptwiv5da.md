---
layout: default
title:
  "Project Lightning Talk: Introducing k8gb: Kubernetes Native Global Load Balancing
  Mad... Yury Tsarev"
nav_order: 219
parent: Kubecon Cloudnativecon North America 2025
type: Video Note
description:
  Yuri, the founder and maintainer of KGB (Kubernetes Global Balancer),
  introduces the project as a solution for seamless, reliable, and declarative global
  traffic management across distributed Kubernetes clusters. KGB enables workload
  resili...
resource: https://www.youtube.com/watch?v=4rpPTWIV5DA
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

Yuri, the founder and maintainer of KGB (Kubernetes Global Balancer), introduces the project as a solution for seamless, reliable, and declarative global traffic management across distributed Kubernetes clusters.
KGB enables workload resilience by supporting multiple global load balancing strategies, such as round robin, weighted, failover, and geographical proximity, all without a single point of failure.
The system integrates components like embedded CoreDNS, ExternalDNS, and a KGB controller, and is managed through a simple custom resource, supporting various workload types and environments, including on-premises, cloud, and hybrid setups.
KGB offers automated DNS zone delegation, supports major cloud providers, and has recently expanded to handle both L7 and L4 workloads.
The project is currently in the CNCF sandbox, has growing community adoption, and invites users to participate, contribute, and join upcoming events and demos.

# Main Points

|   # | Main point                                                                                                         |
| --: | ------------------------------------------------------------------------------------------------------------------ |
|   1 | KGB stands for Kubernetes Global Balancer.                                                                         |
|   2 | Enables global traffic management across distributed Kubernetes clusters.                                          |
|   3 | Provides seamless, reliable, and declarative workload resilience across regions, clouds, and failure domains.      |
|   4 | No single point of failure; no central control cluster.                                                            |
|   5 | Everything is distributed and managed via a single custom resource.                                                |
|   6 | Adopted by several enterprises and has strong community adoption.                                                  |
|   7 | Supports multiple global load balancing strategies:                                                                |
|   8 | Round robin: spreads traffic equally across clusters.                                                              |
|   9 | Weighted: controls traffic percentages per location.                                                               |
|  10 | Failover: steers traffic automatically to healthy clusters during failures.                                        |
|  11 | GeoIP: routes clients to the geographically closest cluster.                                                       |
|  12 | Core components:                                                                                                   |
|  13 | Embedded CoreDNS: serves DNS requests and crafts dynamic responses.                                                |
|  14 | External DNS: handles zone delegation and integration with upstream DNS.                                           |
|  15 | KGB Controller: encapsulates logic, applies GSLB strategy, and monitors application health.                        |
|  16 | Supports two or more clusters.                                                                                     |
|  17 | Deploys next to workloads; integrates with classic ingress and virtual services (e.g., Istio).                     |
|  18 | Works with any CNCF-conformant cluster, on-prem, cloud, multi-cloud, or hybrid environments.                       |
|  19 | Provides full zone delegation automation and integration with many DNS solutions.                                  |
|  20 | Version 0.6 adds full GCP Cloud DNS support and L4 global load balancing.                                          |
|  21 | Project status: CNCF sandbox, in process of incubation, due diligence assigned post-KubeCon.                       |
|  22 | Seven public adopters; two-time CNCF Security Slam finalist; perfect SLSA score.                                   |
|  23 | Maintainers and contributors from multiple companies; over 1,000 GitHub stars, 37 contributors, 37 releases.       |
|  24 | Quarterly release cadence.                                                                                         |
|  25 | Community engagement: website, GitHub, CNCF Slack, bi-weekly meetings, KubeCon kiosks, and contribution workshops. |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=4rpPTWIV5DA)
