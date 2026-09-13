---
layout: default
title:
  "Cloud Native Theater | Istio Day: Zero-Downtime Migration from ingress-nginx
  to Isti... Joe Abellard"
nav_order: 68
parent: Kubecon Cloudnativecon Europe 2026
type: Video Note
description:
  Joe, a senior software engineer at Bloomberg, presents on executing a
  zero-downtime migration from the now-retired Ingress NGINX to a multicluster platform
  built atop the CNCF Kamada project. He explains the necessity of multicluster orches...
resource: https://www.youtube.com/watch?v=wix_PfQ61jY
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

Joe, a senior software engineer at Bloomberg, presents on executing a zero-downtime migration from the now-retired Ingress NGINX to a multicluster platform built atop the CNCF Kamada project.
He explains the necessity of multicluster orchestration for data center redundancy and describes how Bloomberg built a fully managed service on Kamada to streamline multicluster management for multiple teams.
The architecture involves host clusters across data centers, with high availability ensured by stretching control planes and integrating with DNS-based service discovery for unified ingress endpoints.
Joe details the handling of ingress traffic, observability challenges, and the migration strategies considered, ultimately settling on a phased rollout by data center to replace NGINX with Envoy without service interruption.
He concludes by discussing future plans to adopt the now-stable Gateway API for improved traffic routing and invites further discussion at the Kamada project booth.

# Main Points

|   # | Main point                                                                                                                                                               |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   1 | Joe, Senior Software Engineer at Bloomberg, presents on executing a zero downtime migration from Ingress NGINX to a multicluster platform built on Kamada.               |
|   2 | The Ingress NGINX repo was archived and is now officially retired.                                                                                                       |
|   3 | Multicluster orchestration is essential at Bloomberg for data center redundancy and service continuity during disasters.                                                 |
|   4 | Multicluster orchestration involves building multiple clusters across data centers and using an orchestrator to make placement decisions.                                |
|   5 | Bloomberg uses the CNCF Kamada project as its multicluster orchestrator.                                                                                                 |
|   6 | Kamada provides Kubernetes-native multicluster management, with a control plane joined to clusters instead of worker nodes.                                              |
|   7 | The Kamada API server enables integration with Kubernetes tools; Kamada scheduler handles intelligent placement decisions.                                               |
|   8 | Bloomberg built a fully managed service on top of Kamada to avoid each team setting up multicluster infrastructure individually.                                         |
|   9 | The managed platform uses a host/management cluster with the Kamada operator and a custom managed Kamada operator for automating cluster registration and ingress setup. |
|  10 | In the HA topology, multiple host clusters span data centers, and Kamada instances are stretched across them for high availability.                                      |
|  11 | DNS-based service discovery provides a unified ingress endpoint; the same CA is used for provisioning across clusters.                                                   |
|  12 | Ingress traffic can enter directly via a host cluster or through the unified ingress endpoint, with DNS load balancing across worker nodes.                              |
|  13 | Observability is achieved by scraping metrics from control plane components, including protected endpoints, using Prometheus and NGINX metrics proxies.                  |
|  14 | Migration strategies explored included a side-by-side approach with port changes and a phased rollout by data center.                                                    |
|  15 | The phased rollout involved replacing NGINX with Envoy on host port 443 in each data center sequentially, maintaining service via the unified ingress endpoint.          |
|  16 | Routing semantics were preserved by configuring                                                                                                                          |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=wix_PfQ61jY)
