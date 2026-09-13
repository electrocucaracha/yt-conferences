---
type: Video Note
title: "Cloud Native Theater | Istio Day: Panel: Horrors and Successes of Running Istio in Production"
description: "The panel, moderated by Yophikova, brought together end users from organizations like Kaisaban Techch, Skyscanner, TomTom, and B to discuss their experiences running Istio in production. Panelists introduced themselves and described their m..."
resource: https://www.youtube.com/watch?v=-Z9zvo6leRY
tags: ["kubecon-cloudnativecon-europe-2026", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

The panel, moderated by Yophikova, brought together end users from organizations like Kaisaban Techch, Skyscanner, TomTom, and B to discuss their experiences running Istio in production.
Panelists introduced themselves and described their motivations for adopting Istio, highlighting needs such as multicluster support, zero trust security, robust traffic management, and strong community backing.
They shared deployment strategies, with most starting in sidecar mode and moving toward ambient mesh and multicluster setups for improved resiliency and efficiency.
The discussion included detailed horror stories about complex upgrades, network policy misconfigurations, certificate issues, and DNS proxy failures, emphasizing the importance of rollback strategies and observability.
Despite challenges, panelists agreed that Istio’s powerful L7 traffic management, extensibility, multicluster routing, and authorization policies have delivered significant value, enabling secure, scalable, and flexible service communication across large, distributed environments.
Audience questions and additional anecdotes further illustrated both the pitfalls and successes of operating Istio at scale.
# Main Points

|   # | Main point                                                                                                                                           |
| --: | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Panelists introduced themselves, sharing their roles, companies, and years of Istio adoption.                                                        |
|   2 | Augustine (Kaisaban Tech): Using Istio since 2022 for zero trust, ingress/egress control, and self-service rule management.                          |
|   3 | Alex (Skyscanner): Using Istio since 2019 for multi-cluster, ingress/east-west gateways, and service-to-service communication.                       |
|   4 | Vladimir (TomTom): Managing hundreds of clusters, consolidating with Istio for multi-cluster and multi-regional support.                             |
|   5 | Roland (B): Adopted Istio in 2020 for multi-cluster, egress gateway, and VM integration.                                                             |
|   6 | Motivations for adopting Istio: multi-cluster support, traffic management, zero trust, strong community, extensibility, and avoiding vendor lock-in. |
|   7 | Alternatives like Linkerd lacked required features (e.g., multi-cluster) at the time of adoption.                                                    |
|   8 | Current deployments:                                                                                                                                 |
|   9 | Augustine: Sidecar mode, moving to multi-cluster.                                                                                                    |
|  10 | Vladimir: Ambient mode, aiming for multi-cluster.                                                                                                    |
|  11 | Alex: Sidecar mode with egress gateway, planning ambient mode.                                                                                       |
|  12 | Roland: Multi-primary, sidecar mode, migrating to ambient.                                                                                           |
|  13 | Horror stories included:                                                                                                                             |
|  14 | Painful upgrades (e.g., 1.4 to 1.16, 1.18 to 1.24), requiring cluster recreations and complex migrations.                                            |
|  15 | Network policy misalignment causing node failures and lack of rollback scripts.                                                                      |
|  16 | Certificate misconfigurations leading to routing issues.                                                                                             |
|  17 | DNS proxying issues causing DNS server floods after disaster recovery tests.                                                                         |
|  18 | Most valuable Istio features:                                                                                                                        |
|  19 | Level 7 traffic management and authorization policies.                                                                                               |
|  20 | Multi-cluster routing and zero trust.                                                                                                                |
|  21 | Extensibility via Envoy filters and CRDs.                                                                                                            |
|  22 | Observability and metrics.                                                                                                                           |
|  23 | Challenges with Istio APIs: Authorization policy compounding, complexity of Envoy filters, and managing load balancer weights.                       |
|  24 | TLS origination and debugging issues discussed.                                                                                                      |
|  25 | Audience shared additional horror stories and praised Istio’s developer abstractions.                                                                |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=-Z9zvo6leRY)