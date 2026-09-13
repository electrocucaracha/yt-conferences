---
type: Video Note
title: "Building the Next Generation of Multi-Cluster with Gateway API - Mike Morris & Alan Grosskurth"
description: "In this talk, Mike from Microsoft and Alan from Google discuss the evolution and challenges of Kubernetes service APIs, particularly in the context of multi-cluster networking and modern workloads such as AI. They highlight the limitations..."
resource: https://www.youtube.com/watch?v=oRbdcHgHPbo
tags: ["kubecon-cloudnativecon-europe-2026", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

In this talk, Mike from Microsoft and Alan from Google discuss the evolution and challenges of Kubernetes service APIs, particularly in the context of multi-cluster networking and modern workloads such as AI.
They highlight the limitations of the existing Service and MCS APIs, including their lack of flexibility, cumbersome design, and inability to efficiently support advanced use cases like heterogeneous GPU workloads and dynamic routing.
The presenters introduce new concepts under development, such as separating service front end and back end components, the cluster IP gateway, endpoint selectors, and composite back ends, which aim to provide more modular, scalable, and future-proof solutions for multi-cluster environments.
They describe experimental implementations that leverage Gateway API and XDS protocols to enable more efficient cross-cluster communication without overloading the Kubernetes API, and emphasize the importance of integrating these innovations with existing Kubernetes patterns rather than creating isolated solutions.
The session concludes with a call for collaboration in working groups to refine and standardize these approaches, ensuring they address both current and emerging needs in the Kubernetes ecosystem.
# Main Points

|   # | Main point                                                                                                                                                                                                                          |
| --: | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Mike (Microsoft) and Alan (Google) presented on Gateway API, data model, and multi-cluster services.                                                                                                                                |
|   2 | Agenda: background and lessons from service history, desirable properties for multi-cluster solutions, solution ideas, experimental implementations, closing thoughts.                                                              |
|   3 | Kubernetes Service API is old, heavily used, and difficult to evolve; patching is unsustainable.                                                                                                                                    |
|   4 | Service has two facets: front end (DNS, FQDN, cluster-local address) and back end (cluster IP, endpoints/pods).                                                                                                                     |
|   5 | Service mesh and Gateway API often only use the back end; front end/back end coupling is cumbersome.                                                                                                                                |
|   6 | Multi-cluster Services API (MCS API) uses CRDs like service import/export; adoption is hindered by code changes and namespace sameness challenges.                                                                                  |
|   7 | MCS API allows flexible network topologies but has implementation complexities (shadow services, cross-cluster resource control, lack of reference implementation).                                                                 |
|   8 | MCS API is stable but insufficient for modern needs (gateways, inference pools, AI workloads, advanced routing).                                                                                                                    |
|   9 | Modern demands: need for spillover, efficient load balancing (e.g., for GPUs), and communicating endpoint capacity.                                                                                                                 |
|  10 | Desire to avoid proliferation of X-import patterns for new resources.                                                                                                                                                               |
|  11 | Desirable properties for future solutions: separate but connect front end/back end, cluster IP gateways, flexible routing, support for non-pod backends, avoid strict network/gateway requirements, inform architectural decisions. |
|  12 | Proposed ideas: cluster IP gateway (front end via gateway, DNS under gw.cluster.local, endpoint selector for back end), composite back end (aggregates back ends across clusters for multi-cluster load balancing).                 |
|  13 | Experimental implementations: prototype cluster IP gateway using CoreDNS plugin, controller, and agent; disintermediate Kubernetes API for multi-cluster via XDS protocol.                                                          |
|  14 | Goal: integrate with existing Kubernetes/Gateway API, make service components atomic/composable, solve high-priority problems quickly via Gateway API experimental channel, a                                                       |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=oRbdcHgHPbo)