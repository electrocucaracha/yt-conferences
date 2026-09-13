---
type: Video Note
title: "Cloud Native Theater | Istio Day: The Good, The Ugly, and The Bad... Alfonso Ming and Jorge Turrado"
description: "Alonso and Jorge introduce their experiences transitioning from the traditional sidecar service mesh model to the ambient mesh approach in their Kubernetes clusters. They explain that while the sidecar model, which places a proxy alongside..."
resource: https://www.youtube.com/watch?v=ToKv7JntLvY
tags: ["kubecon-cloudnativecon-europe-2026", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

Alonso and Jorge introduce their experiences transitioning from the traditional sidecar service mesh model to the ambient mesh approach in their Kubernetes clusters.
They explain that while the sidecar model, which places a proxy alongside every pod, offers benefits in security, observability, and traffic management, it leads to high resource costs and operational complexity, especially during updates and version drift.
By adopting ambient mesh, where a single proxy (ztunnel) runs per node and waypoints handle Layer 7 traffic, they achieved significant cost reductions (30–60% in proxy resource allocation), simplified version management, and made resource usage more predictable.
However, they note that ambient mesh introduces new complexities, such as more fragmented metrics, increased policy management difficulty, and challenges with observability and certain network scenarios.
Despite these challenges, the team found the operational and cost benefits worthwhile, especially as the infrastructure became simpler for developers, though they caution that some pain points remain, particularly around policy enforcement and integration with existing tools.
# Main Points

|   # | Main point                                                                                           |
| --: | ---------------------------------------------------------------------------------------------------- |
|   1 | Alonso and Jorge introduced themselves and their roles.                                              |
|   2 | The session covers their adoption process of ambient mesh.                                           |
|   3 | Service mesh provides security, observability, and traffic management for microservices.             |
|   4 | Sidecar model uses a proxy per pod, handling all traffic and authentication.                         |
|   5 | Sidecar model issues:                                                                                |
|   6 | High resource and cost overhead due to one proxy per pod.                                            |
|   7 | Operational complexity when updating proxies, leading to version drift.                              |
|   8 | Ambient mesh approach:                                                                               |
|   9 | Uses a per-node proxy (ztunnel) instead of per-pod.                                                  |
|  10 | Communication is managed at the node level, reducing resource usage.                                 |
|  11 | Layer 7 capabilities require a waypoint component.                                                   |
|  12 | Gateway API is recommended for ambient mesh, splitting responsibilities between SREs and developers. |
|  13 | Benefits of ambient mesh:                                                                            |
|  14 | Significant cost reduction (proxy resource allocation reduced by 40-60%).                            |
|  15 | Reduced version drift across clusters.                                                               |
|  16 | Predictable traffic routing costs.                                                                   |
|  17 | Simplified metrics collection due to fewer proxies.                                                  |
|  18 | Downsides of ambient mesh:                                                                           |
|  19 | Added complexity with waypoints and policy management at both layer 4 and layer 7.                   |
|  20 | Metrics and observability are more fragmented and require dashboard/alert updates.                   |
|  21 | If ztunnel fails, all node communication fails.                                                      |
|  22 | Transparent proxying in ztunnel makes excluding ports more complex.                                  |
|  23 | Gateway API adoption requires plugin updates for tools like cert-manager and Argo Rollouts.          |
|  24 | Multicluster installation support is in beta.                                                        |
|  25 | Waypoint proxies:                                                                                    |
|  26 | Can be namespace or cluster scoped.                                                                  |
|  27 | Are shared and autoscalable deployments.                                                             |
|  28 | Adjusting proxy resource requests per workload is operationally costly.                              |
|  29 | For restrictive egress policies, network policies are recommended over sidecar egress annotations.   |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=ToKv7JntLvY)