---
type: Video Note
title: "What's New in gRPC - Kevin Nilson, Google & Israel Shapiro, Broadcom"
description: "The video features a panel of gRPC maintainers and contributors discussing recent developments and features in the gRPC project. They highlight gRPC’s widespread adoption across industries, its language-agnostic design, and its suitability..."
resource: https://www.youtube.com/watch?v=pd_eE6N3iK8
tags: ["kubecon-cloudnativecon-north-america-2025", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

The video features a panel of gRPC maintainers and contributors discussing recent developments and features in the gRPC project.
They highlight gRPC’s widespread adoption across industries, its language-agnostic design, and its suitability for cloud-native and microservices architectures.
Recent improvements include enhanced documentation, new user guides, and expanded video resources, as well as technical advancements such as service mesh features without sidecar proxies, improved observability with OpenTelemetry, and modernization efforts including first-class Rust support.
The team also introduces new features like HTTP CONNECT integration with XDS, support for multiple SPIFFE trust domains, custom backend metrics for load balancing, and experimental protocols for AI model enrichment.
The session concludes with a Q&A addressing best practices for proto file sharing and schema management, emphasizing the benefits of using protocol buffers directly in applications to reduce complexity and errors.
# Main Points

|   # | Main point                                                                                                                  |
| --: | --------------------------------------------------------------------------------------------------------------------------- |
|   1 | Kevin introduced himself as a gRPC steering committee member and highlighted the project's 11+ years of growth.             |
|   2 | Five speakers presented, including maintainers and a Broadcom representative.                                               |
|   3 | gRPC sees high usage: 7.1M weekly Java downloads, 24M Python downloads, and 13M npm downloads.                              |
|   4 | Recent improvements include four new user guides, four new code examples, and 39 new YouTube videos.                        |
|   5 | Feedback from KubeCon led to significant documentation enhancements.                                                        |
|   6 | Community contributions via pull requests and bug reports are encouraged.                                                   |
|   7 | gRPC Conf is an annual conference; the first gRPC Conf India is upcoming, with content available on YouTube.                |
|   8 | John Fog noted gRPC’s rapid adoption by companies like Cisco, Netflix, Spotify, Reddit, and LinkedIn.                       |
|   9 | gRPC is valued for high performance, multi-language support, and suitability for cloud-native, microservices architectures. |
|  10 | Features include load balancing, retries, and support for service mesh patterns.                                            |
|  11 | Proxilus gRPC service mesh eliminates sidecar proxies, reducing complexity and improving efficiency.                        |
|  12 | gRPC is widely used in AI/ML for efficient data streaming and model training/inference (e.g., TensorFlow, Nvidia Triton).   |
|  13 | Three main development pillars: service mesh, observability (OpenTelemetry), and modernization.                             |
|  14 | New features:                                                                                                               |
|  15 | Extroc and Ext for request/response modification and authorization via plugin servers.                                      |
|  16 | Improved serverless integrations, including XDS host rewriting, JWT-based authorization, and MTLS with spiffy identities.   |
|  17 | Israel from Broadcom discussed HTTP CONNECT with XDS integration and support for multiple spiffy trust domains.             |
|  18 | OpenTelemetry metrics expanded for load balancing policies and XDS client, with new non-per-call metrics.                   |
|  19 | Ivy introduced custom backend metrics and WRR load balancing policy, supporting multiple languages.                         |
|  20 | MCP and A2A protocols enhance AI model capabilities; MCP over gRPC is in experimental development.                          |
|  21 | Rust is now an officially supported gRPC language                                                                           |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=pd_eE6N3iK8)