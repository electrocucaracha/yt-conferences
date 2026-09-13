---
type: Video Note
title: "From NLB Sprawl To Mesh Efficiency: How Skyscanner Handles 60M Reque... John Clark & Steven Thwaites"
description: "In this presentation, John from Skyscanner and Steven from Solo describe Skyscanner’s journey to improve the efficiency of their service mesh architecture. Initially, Skyscanner operated with multiple AWS clusters connected via Istio, using..."
resource: https://www.youtube.com/watch?v=2ZvvGdHfknM
tags: ["kubecon-cloudnativecon-europe-2026", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

In this presentation, John from Skyscanner and Steven from Solo describe Skyscanner’s journey to improve the efficiency of their service mesh architecture.
Initially, Skyscanner operated with multiple AWS clusters connected via Istio, using network load balancers (NLBs) and sidecar proxies, which provided security, observability, and failover but eventually led to high infrastructure costs and complexity.
To address this, they transitioned to a multicluster setup using egress gateways, reducing NLB costs by 10% of their cloud bill, and later began migrating to Istio’s ambient mesh, which eliminates sidecars in favor of node-level Z tunnels and shared waypoint proxies, further simplifying management and reducing resource usage.
The migration required adapting telemetry collection and multicluster routing, but was achieved without requiring changes from developers or service owners.
Throughout, Skyscanner emphasized gradual rollouts, custom solutions where necessary, and the use of tools like Argo CD for orchestrating upgrades, finding that the trade-offs in complexity were outweighed by the operational and cost benefits.
# Main Points

|   # | Main point                                                                                                                                             |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   1 | Skyscanner improved mesh efficiency by moving from load balancers to multicluster and then to ambient mesh.                                            |
|   2 | Skyscanner operates across four production regions, each with six AWS clusters, serving 600 services, 35,000 pods, and 60 million requests per minute. |
|   3 | In 2019, Skyscanner split large clusters into smaller, single-AZ clusters to reduce blast radius and enable phased upgrades.                           |
|   4 | Istio was chosen for service connectivity, MTLS, DNS abstraction, and telemetry.                                                                       |
|   5 | Sidecar proxies are injected into each pod for security and observability.                                                                             |
|   6 | Skyscanner provides developers with seamless service discovery via DNS, MTLS, metrics, and automatic failover.                                         |
|   7 | Each cluster exposes a single IP behind a gateway; virtual services and destination rules manage retries and failover.                                 |
|   8 | Initial mesh used default gateways with NLBs, but costs rose to 10% of the cloud bill as usage increased.                                              |
|   9 | Transitioned to multicluster by deploying egress gateways in each cluster, reducing NLB costs significantly.                                           |
|  10 | Multicluster setup increased Istiod scaling by 10x but was offset by cost savings.                                                                     |
|  11 | Ambient mesh removes sidecars, using Z tunnel daemonsets per node for L4, and optional waypoint proxies for L7.                                        |
|  12 | Ambient mesh reduces infrastructure and management complexity, and upgrades no longer require pod restarts.                                            |
|  13 | Skyscanner uses Solo’s XDS peering and workload entries to enable single-IP access to remote clusters without egress gateways.                         |
|  14 | Telemetry challenges addressed by moving client-side spans to waypoints and using default gateways for server-side spans.                              |
|  15 | Migration to ambient mesh required custom solutions and gradual rollout; new clusters use ambient, existing clusters migrate slowly.                   |
|  16 | Argo CD and Argo Workflows are used for orchestrating rollouts across clusters in defined channels (dev, alpha, beta, prod).                           |
|  17 | No significant latency or resource issues observed with Z tunnel; CPU usage scales horizontally with Istiod pods.                                      |
|  18 | Ingress gateways and envoy filters remain supported; Lu                                                                                                |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=2ZvvGdHfknM)