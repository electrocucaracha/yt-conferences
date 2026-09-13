---
type: Video Note
title: "Authenticating and Authorizing Every Connection at Uber - Yangmin Zhu & Matt Mathew, Uber"
description: "In this presentation, Uber’s engineering security team discusses their journey to authenticate and authorize every service-to-service connection across their vast, heterogeneous microservices architecture. Initially, they implemented a libr..."
resource: https://www.youtube.com/watch?v=GYVNg0_FpwQ
tags: ["kubecon-cloudnativecon-north-america-2025", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

In this presentation, Uber’s engineering security team discusses their journey to authenticate and authorize every service-to-service connection across their vast, heterogeneous microservices architecture.
Initially, they implemented a library-based solution requiring service owners to integrate authentication libraries, but this approach faced low adoption, high operational burden, and technical constraints due to language diversity and open-source system limitations.
To address these challenges, they transitioned to a service mesh solution using Envoy as an on-host proxy, which transparently handles authentication, authorization, and encryption without requiring code changes from service owners.
The team developed supporting systems for observability, automated policy generation, and safe, gradual rollout, enabling them to authorize over 2 million connections per second.
Key lessons learned include the importance of leadership support, optimizing developer experience, handling technical edge cases, and the need for centralized, frictionless security solutions in large-scale, legacy environments.
# Main Points

|   # | Main point                                                                                                                                                  |
| --: | ----------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Uber operates over 7,000 microservices, 7,000 databases, and nearly half a million data jobs, using multiple RPC frameworks and five programming languages. |
|   2 | Uber’s tech stack is highly heterogeneous, leveraging both open source and in-house container orchestration systems.                                        |
|   3 | Security and compliance requirements necessitate authenticating and authorizing every service call.                                                         |
|   4 | Initial solution (2019-2020): library-based approach requiring service owners to adopt a library for authentication and authorization.                      |
|   5 | Library-based approach issues:                                                                                                                              |
|   6 | Low adoption (~10%) due to operational burden on 6,600 engineers.                                                                                           |
|   7 | High maintenance burden for updates and security fixes.                                                                                                     |
|   8 | Inconsistent support across languages (only Golang and Java).                                                                                               |
|   9 | Technical constraints with integrating into some open source systems.                                                                                       |
|  10 | Transitioned to a service mesh solution using Envoy as an on-host proxy, removing the need for per-service libraries.                                       |
|  11 | Envoy handles authentication, authorization, and MTLS encryption transparently at the network layer.                                                        |
|  12 | Adoption, maintenance, and technical constraint issues resolved by centralizing logic in Envoy.                                                             |
|  13 | Technical architecture:                                                                                                                                     |
|  14 | Envoy Manager (homebuilt in Go) manages Envoy lifecycle and configuration.                                                                                  |
|  15 | Traffic redirection layer (using eBPF) transparently routes service traffic to Envoy.                                                                       |
|  16 | Outbound: Injects identity using network class ID and SO_MARK.                                                                                              |
|  17 | Inbound: Enforces authorization policies based on pre-allocated container ports.                                                                            |
|  18 | Adoption strategy:                                                                                                                                          |
|  19 | Built end-to-end observability for monitoring and troubleshooting.                                                                                          |
|  20 | Automated policy generation using observability metrics and RBAC shadow mode.                                                                               |
|  21 | Gradual, safe rollout prioritizing business-critical and stateless services.                                                                                |
|  22 | Tools for policy simulation, impact analysis, and emergency rollback.                                                                                       |
|  23 | Lessons learned:                                                                                                                                            |
|  24 | Certificate distribution latency fixed by using Kubernetes secrets.                                                                                         |
|  25 | Added delay before closing TCP connections on authorization denial to prevent client retr                                                                   |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=GYVNg0_FpwQ)