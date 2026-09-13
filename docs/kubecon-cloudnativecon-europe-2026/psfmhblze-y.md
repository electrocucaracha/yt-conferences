---
layout: default
title:
  "Visualizing GitOps: A Tour of Flux UIs in the Open Source Ecosystem - Stefan
  Prodan, ControlPlane"
nav_order: 388
parent: Kubecon Cloudnativecon Europe 2026
type: Video Note
description:
  The speaker provides an overview of recent developments in the Flux ecosystem,
  highlighting key features introduced in Flux 2.8, such as native Helm v4 support,
  Kubernetes server-side apply integration, improved health checks for custom res...
resource: https://www.youtube.com/watch?v=pSfmhblzE-Y
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

The speaker provides an overview of recent developments in the Flux ecosystem, highlighting key features introduced in Flux 2.8, such as native Helm v4 support, Kubernetes server-side apply integration, improved health checks for custom resources, and enhancements to mean time to recovery and release inventory status.
They explain the rationale behind Flux’s lack of an official UI, emphasizing the project’s commitment to loosely coupled APIs and encouraging community-driven UI solutions.
Several third-party UIs are discussed, including Freelance, Headlamp, Capacitor, and terminal-based options like K9s and Flux9s, each offering different approaches to managing and visualizing Flux resources.
The speaker also demonstrates a lightweight, mobile-first UI built into Flux Operator, which prioritizes security through single sign-on and RBAC alignment, offers fast, scalable cluster views, and supports custom dashboards for all Flux CRDs.
Future plans include enhancing the developer experience and adding dedicated support for Flagger, while maintaining a focus on security and scalability.

# Main Points

|   # | Main point                                                                                                                                                                                         |
| --: | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Flux 2.8 has gone GA, with three releases per year, skipping December.                                                                                                                             |
|   2 | Major feature: Helm v4 support integrated, thanks to collaboration with the Helm team.                                                                                                             |
|   3 | Flux uses the Helm Go SDK natively, not just as a templating tool.                                                                                                                                 |
|   4 | Focus on performance and security: supports upgrading hundreds of Helm releases in parallel, with sealed charts inside the controller.                                                             |
|   5 | Kubernetes server-side apply now available in Helm controller, providing uniform resource management and improved scaling.                                                                         |
|   6 | Helm controller now supports health checks for custom resources inside charts using CEL expressions.                                                                                               |
|   7 | New feature to reduce mean time to recovery: controller can cancel ongoing health checks and start upgrades immediately on new revisions (behind a feature gate, planned default in Q1 next year). |
|   8 | Helm release inventory is now reflected in the custom resource status, simplifying UI integration and debugging.                                                                                   |
|   9 | New controller: source-watcher and custom resource: artifact generator (introduced in 2.7).                                                                                                        |
|  10 | Artifact generator allows decomposition of monorepos and composition from multiple sources, generating internal artifacts compatible with OCI artifacts.                                           |
|  11 | Flux will not have an official UI; APIs are designed to be loosely coupled, enabling community-driven UIs.                                                                                         |
|  12 | Notable UIs:                                                                                                                                                                                       |
|  13 | Freelance: Fast updates, supports all Flux custom resources, adapts quickly to new releases.                                                                                                       |
|  14 | Headlamp: Official Kubernetes dashboard replacement, holistic overview, supports plugins including Flagger.                                                                                        |
|  15 | Capacitor: Desktop app (open source), unique approach, focused on debugging.                                                                                                                       |
|  16 | Terminal UIs: K9s plugin (stable), Flux9s (Rust, beta).                                                                                                                                            |
|  17 | Multicluster read-only options: Grafana dashboards, Backstage plugin.                                                                                                                              |
|  18 | Flux operator UI: lightweight, mobile-first, built-in, uses single sign-on with Dex, impersonates service accounts for RBAC.                                                                       |
|  19 | UI uses controller runtime cache for fast, scalable performance.                                                                                                                                   |
|  20 | Supports all CRDs with custom dashboards, workload views, and safe actions based on Kubernetes RBAC.                                                                                               |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=pSfmhblzE-Y)
