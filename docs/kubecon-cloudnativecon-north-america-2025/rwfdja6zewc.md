---
type: Video Note
title: "Gateway API: Table Stakes - Shane Utt, Candace Holman, Mike Morris, Lior Lieberman & Kellen Swain"
description: "The video presents an overview and update on the Gateway API, a next-generation Kubernetes routing and load balancing API that has become the effective successor to Ingress since its inception in 2019. The speakers, representing Google, Red..."
resource: https://www.youtube.com/watch?v=RWFDjA6ZeWc
tags: ["kubecon-cloudnativecon-north-america-2025", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

The video presents an overview and update on the Gateway API, a next-generation Kubernetes routing and load balancing API that has become the effective successor to Ingress since its inception in 2019.
The speakers, representing Google, Red Hat, and Microsoft, discuss recent developments, including the release of version 1.4, which graduated backend TLS policy and supported features from experimental to standard, and introduced new experimental features such as mesh resource, default gateways, HTTP external authorization, and enhanced TLS configuration.
They emphasize the API’s role-based design, extensibility, and the importance of selecting an appropriate implementation, as there is no default provided.
The session also highlights ongoing and future work, such as documentation improvements, enhanced CRD provider guidance, expanded support for retries and timeouts, and monthly experimental releases.
Additionally, the talk covers related subprojects like the inference extension and agentic networking, both aimed at supporting AI and agent workloads in Kubernetes, and invites community feedback and participation to guide further development and address user needs, including multicluster and egress scenarios.
# Main Points

|   # | Main point                                                                                                                                                                                                                        |
| --: | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Overview of Gateway API, its recent highlights, finishing touches, table stakes, and future direction                                                                                                                             |
|   2 | Gateway API started in 2019 as the next generation of Kubernetes routing and load balancing APIs, succeeding Ingress                                                                                                              |
|   3 | All new features are now added to Gateway API, not Ingress                                                                                                                                                                        |
|   4 | Gateway API reached v1 GA in 2023 with 30+ implementations                                                                                                                                                                        |
|   5 | No default implementation is provided; users must choose from available implementations                                                                                                                                           |
|   6 | Gateway API is role-oriented, aligning APIs with roles like infrastructure providers, cluster operators, and application developers                                                                                               |
|   7 | Designed to be expressive and extensible, avoiding reliance on annotations                                                                                                                                                        |
|   8 | Core resources: GatewayClass, Gateway, HTTPRoute, gRPCRoute, ReferenceGrant, BackendTLSPolicy                                                                                                                                     |
|   9 | Experimental APIs: TLSRoute, TCPRoute, UDPRoute, ListenerSet, Mesh resource, BackendTrafficPolicy                                                                                                                                 |
|  10 | Version 1.4 (released Oct 6): BackendTLSPolicy and SupportedFeatures graduated from experimental to standard                                                                                                                      |
|  11 | BackendTLSPolicy enhances TLS termination options for HTTPRoutes, supporting secure connections between gateway and backend                                                                                                       |
|  12 | SupportedFeatures provides machine-readable info on features supported by each implementation, aiding discoverability and tooling                                                                                                 |
|  13 | New experimental features: Mesh resource for mesh-wide config, DefaultGateway for easier migration from Ingress, HTTPExternalAuth for external authentication/authorization, improved per-port TLS config for security            |
|  14 | Upcoming work: documentation overhaul, improved CRD provider guidance, standardizing retries and timeouts, ListenerSet for scalable configuration, backend/frontend mTLS, advancing TLSRoute, more frequent experimental releases |
|  15 | Gateway API ecosystem expanding with subprojects: Inference Extension, AI Gateway Working Group, Agentic Networking                                                                                                               |
|  16 | Inference Extension focuses on efficient, self-hosted model serving with L7 routing and integration with broader AI ecosystems                                                                                                    |
|  17 | Agentic Networking aims to provide governance and connectivity for agentic AI workloads, suppor                                                                                                                                   |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=RWFDjA6ZeWc)