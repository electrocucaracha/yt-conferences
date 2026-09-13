---
layout: default
title: "Linkerd: Reliable Production in an AI/MCP World - William Morgan, Buoyant"
nav_order: 212
parent: Kubecon Cloudnativecon Europe 2026
type: Video Note
description:
  William Morgan, director of the Linkerd project, opens his talk by introducing
  Linkerd as a service mesh designed to provide secure, reliable, and observable networking
  for Kubernetes environments, emphasizing simplicity, minimal configurat...
resource: https://www.youtube.com/watch?v=jPWsMZFpihA
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

William Morgan, director of the Linkerd project, opens his talk by introducing Linkerd as a service mesh designed to provide secure, reliable, and observable networking for Kubernetes environments, emphasizing simplicity, minimal configuration, and operational transparency.
He highlights Linkerd’s unique architecture, notably its use of lightweight Rust-based microproxies instead of Envoy, and discusses the project’s sustainable funding model through Buoyant, which employs full-time maintainers and supports the open-source community.
Morgan reviews recent updates, including post-quantum-ready TLS libraries, protocol declarations to improve reliability under load, GitOps-compatible multicluster linking, and decoupling from the Gateway API.
Addressing the impact of AI and MCP (Model Control Protocol) workloads, he notes that while core platform requirements remain unchanged, Linkerd is actively prototyping features to support new AI-driven use cases, such as MCP protocol parsing and enhanced gateway capabilities.
He concludes by inviting feedback from users facing AI challenges, promoting educational resources, and answering audience questions about technical implementation and future directions.

# Main Points

|   # | Main point                                                                                                                                                        |
| --: | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | William Morgan, director on the Linkerd project, presented on reliable production in AI and MCP world.                                                            |
|   2 | Audience included newcomers and experienced Linkerd users; Linkerd has been in production for 9 years.                                                            |
|   3 | Linkerd is a service mesh for Kubernetes, handling networking between services to make it reliable, secure, and observable.                                       |
|   4 | Linkerd was the fifth project to join CNCF and the first service mesh to achieve graduated status.                                                                |
|   5 | Linkerd's design philosophy emphasizes simplicity, minimal configuration, small resource footprint, understandability, and easy security (mutual TLS by default). |
|   6 | Linkerd is unique among popular service meshes for not using Envoy; instead, it uses lightweight Rust-based microproxies.                                         |
|   7 | Early adopter of Rust in cloud native space; contributed to libraries like Tokio, Tower, and H2.                                                                  |
|   8 | Operational goal: proxies should be an implementation detail, requiring minimal tuning.                                                                           |
|   9 | Linkerd is a sustainable project funded by Buoyant, which employs all maintainers and sells an enterprise version.                                                |
|  10 | Release process: frequent "edge" releases with latest code and bugfixes; major versions are bundled periodically.                                                 |
|  11 | Recent features/changes:                                                                                                                                          |
|  12 | Default TLS libraries updated to be post-quantum ready (moved from ring to AWS LC).                                                                               |
|  13 | Added observability for cipher suite and key exchange in metrics.                                                                                                 |
|  14 | Introduced protocol declarations to avoid protocol detection issues under load.                                                                                   |
|  15 | GitOps-compatible multicluster linking now available.                                                                                                             |
|  16 | Decoupled from Gateway API CRDs; users must now manage these dependencies.                                                                                        |
|  17 | No plans to add AI to Linkerd; focus remains on speed, lightweight, and predictability.                                                                           |
|  18 | Platform requirements (reliability, security, observability) remain unchanged despite generative AI trends.                                                       |
|  19 | Linkerd is experimenting with MCP protocol parsing and gateway features for AI-related workloads.                                                                 |
|  20 | Free online courses and guides available; escape room party event announced.                                                                                      |
|  21 | Windows support is available behind a paywall.                                                                                                                    |
|  22 | MCP integration                                                                                                                                                   |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=jPWsMZFpihA)
