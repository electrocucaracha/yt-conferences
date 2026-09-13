---
type: Video Note
title: "What's New in gRPC - Kevin Nilson & John Feig, Google"
description: "The presenters provided an overview of recent developments in gRPC, highlighting its decade-long growth, stability, and widespread adoption across various programming languages and platforms. They discussed significant improvements in docum..."
resource: https://www.youtube.com/watch?v=P1YhVS4dhVk
tags: ["kubecon-cloudnativecon-europe-2026", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

The presenters provided an overview of recent developments in gRPC, highlighting its decade-long growth, stability, and widespread adoption across various programming languages and platforms.
They discussed significant improvements in documentation and user resources, including new guides and video content, and announced upcoming gRPC conferences in the Bay Area and Bangalore.
Key technical updates include enhanced proxyless service mesh features, improved observability through OpenTelemetry, modernization efforts such as expanded language support (notably Rust), and first-class integration with serverless platforms.
The team also emphasized gRPC’s growing role in AI and ML workflows, support for protocols like MCP and A2A, and new features like custom backend metrics and advanced load balancing policies.
Audience questions addressed topics such as replication, load balancing, and gateway API support, with the team encouraging community feedback and participation to guide future development.
# Main Points

|   # | Main point                                                                                                                       |
| --: | -------------------------------------------------------------------------------------------------------------------------------- |
|   1 | gRPC has been around for 10 years, is stable, and continues to grow.                                                             |
|   2 | Significant usage: 7 million weekly Maven Central (Java), 304 million monthly Python downloads, 29 million weekly NPM downloads. |
|   3 | Community contributions from companies like Netflix, DataDog, Broadcom, and LinkedIn.                                            |
|   4 | Investments made in improving documentation, adding new user guides, and producing more video content.                           |
|   5 | gRPC comp conferences held in the Bay Area and Bangalore.                                                                        |
|   6 | gRPC is well-suited for cloud-native architectures, microservices, and is language-agnostic.                                     |
|   7 | Enables efficient communication using protocol buffers and HTTP/2.                                                               |
|   8 | Provides features like load balancing, retries, and supports developer velocity.                                                 |
|   9 | Proxyless gRPC service mesh reduces operational overhead and complexity.                                                         |
|  10 | Widely used in Google CD, containerd, Kubernetes, and other Google Cloud projects.                                               |
|  11 | gRPC is increasingly used in AI/ML for efficient data streaming and model training/inference (e.g., TensorFlow, Nvidia Triton).  |
|  12 | Three main pillars: Service Mesh, Observability, Modernization.                                                                  |
|  13 | New proxyless service mesh features: Extroproc (request/response modification) and Ext (authorization), using a plugin model.    |
|  14 | Improved serverless integrations: XDS host rewriting, JWT-based authorization, and MTLS with Spiffy identities.                  |
|  15 | HTTP CONNECT tunneling now easier to configure and integrates with XDS.                                                          |
|  16 | Added support for multiple Spiffy trust domains via trust bundles.                                                               |
|  17 | Enhanced observability: open telemetry metrics for load balancing policies and XDS client, non-protocol metrics framework.       |
|  18 | Custom backend metrics for load balancing now available, supporting weighted round robin (WRR) policy.                           |
|  19 | AI protocols MCP and A2A now support gRPC; experimental MCP Python SDK with gRPC transport released.                             |
|  20 | Official gRPC Rust support in development, building on Tonic, with XDS and service mesh compatibility.                           |
|  21 | Ongoing community engagement via documentation, YouTube, meetups, mailing list, and social media.                                |
|  22 | No current roadma                                                                                                                |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=P1YhVS4dhVk)