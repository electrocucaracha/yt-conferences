---
type: Video Note
title: "Not Yet Another Envoy Implementation - Exploring Kgateway To Write Your Own GatewayA... Ricardo Katz"
description: "In this talk, Ricardo, a software engineer at Red Hat and Kubernetes Gateway API maintainer, discusses the recent changes in the K Gateway project, including the split of the control plane and the emergence of Agent Gateway, which is orient..."
resource: https://www.youtube.com/watch?v=9VqzQgin6vk
tags: ["kubecon-cloudnativecon-europe-2026", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

In this talk, Ricardo, a software engineer at Red Hat and Kubernetes Gateway API maintainer, discusses the recent changes in the K Gateway project, including the split of the control plane and the emergence of Agent Gateway, which is oriented toward AI workloads and written in Rust.
He explains the motivation for creating custom Gateway API implementations, emphasizing the importance of separating the control plane from the data plane for security and reusability.
Ricardo demonstrates how K Gateway and Agent Gateway simplify the process of building new gateway backends by providing a streamlined model and gRPC-based configuration delivery, making it easier to support different proxies beyond Envoy.
He shares his experience developing a client and a terminal UI to interact with the control plane, as well as a proof-of-concept NGINX proxy integration, highlighting the ease of consuming configuration updates and the potential for broader ecosystem innovation.
The talk concludes with encouragement for others to experiment with these models, noting ongoing improvements and the need for validation when proxies lack support for certain features.
# Main Points

|   # | Main point                                                                                                                               |
| --: | ---------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Talk focuses on exploring Agent Gateway and its relationship to K Gateway and Gateway API.                                               |
|   2 | K Gateway maintainers recently split the control plane, now partly in Agent Gateway.                                                     |
|   3 | Speaker is Ricardo, software engineer at Red Hat, Gateway API maintainer for Kubernetes.                                                 |
|   4 | Motivation: desire for custom Gateway API implementations, not limited to Envoy.                                                         |
|   5 | Avoids data plane accessing Kubernetes API for security reasons.                                                                         |
|   6 | Goal: make gateway implementations easy and reusable for other backends.                                                                 |
|   7 | Creating a Gateway API implementation involves reconciling gateway classes, listeners, HTTP routes, and updating the data plane.         |
|   8 | Most gateway implementations (nginx, HAProxy, Envoy) share similar configuration patterns: listeners, ports, virtual hosts, routes, TLS. |
|   9 | Envoy Gateway reconciles Gateway API resources and generates Envoy configuration, separating control and data planes.                    |
|  10 | Consuming Envoy API is complex, especially for non-Envoy implementations.                                                                |
|  11 | K Gateway and Agent Gateway emerged as alternatives; Agent Gateway is oriented for AI workloads and written in Rust.                     |
|  12 | K Gateway generates a gRPC XDS server with Aggregated Discovery Service (ADS).                                                           |
|  13 | Agent Gateway model is simpler than Envoy’s, focusing on port binding, listeners, routes, and IP definitions.                            |
|  14 | Model can be reused by other implementations; supports listeners, routes, certificates, backend TLS policy.                              |
|  15 | ADS consolidates configuration streams; authentication is based on node ID.                                                              |
|  16 | Speaker wrote a client to connect to K Gateway control plane, discovered and reported a CVE related to weak authentication.              |
|  17 | Developed a terminal UI to visualize control plane messages to the data plane.                                                           |
|  18 | Two main message types: workload address (endpoints) and resource (listeners, routes, etc.).                                             |
|  19 | Implemented a prototype nginx proxy using the client; not production-ready.                                                              |
|  20 | Proxy parses messages and writes configuration files, avoiding Go templates for security.                                                |
|  21 | Implementation is not Gateway API conformance certified; passes                                                                          |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=9VqzQgin6vk)