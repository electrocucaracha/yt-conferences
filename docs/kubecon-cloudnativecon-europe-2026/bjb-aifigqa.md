---
layout: default
title:
  "Project Lightning Talk: Get To Where You're Going With Kgateway - David Jumani,
  Maintainer"
nav_order: 266
parent: Kubecon Cloudnativecon Europe 2026
type: Video Note
description:
  David, an engineer at Solo and maintainer of the K Gateway project, presents
  recent updates and features of K Gateway, an Envoy-based Kubernetes gateway API
  that integrates with service meshes and hyperscalers for hybrid connectivity. Major...
resource: https://www.youtube.com/watch?v=BjB-AIFiGqA
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

David, an engineer at Solo and maintainer of the K Gateway project, presents recent updates and features of K Gateway, an Envoy-based Kubernetes gateway API that integrates with service meshes and hyperscalers for hybrid connectivity.
Major updates include the introduction of overlays, which allow users to customize Kubernetes resources beyond standard Helm configurations, and expanded hyperscaler integrations, such as support for GCP and AWS Lambda backends, with EC2 support forthcoming.
The project also addresses the deprecation of ingress-nginx by facilitating migration through the ingress-to-gateway tool, mapping common annotations, and providing a detailed migration guide.
Additional enhancements include per-hostname MTLS CA validation for multi-tenant scenarios, full support for Gateway API 1.5.1, integration with Istio as a waypoint, and the introduction of Envoy dynamic modules for greater flexibility.
The project has seen significant growth, with over 170,000 downloads in the past month, and encourages community involvement through events and online channels.

# Main Points

|   # | Main point                                                                                                             |
| --: | ---------------------------------------------------------------------------------------------------------------------- |
|   1 | David is an engineer at Solo and maintainer of the K Gateway project.                                                  |
|   2 | The talk covers major updates, use cases, and production readiness for K Gateway.                                      |
|   3 | K Gateway is an Envoy-based Kubernetes gateway API implementation.                                                     |
|   4 | Integrates with service mesh and hyperscalers, providing hybrid connectivity.                                          |
|   5 | K Gateway has seen over 170,000 downloads in the last month.                                                           |
|   6 | Major update: Overlays feature allows users to override and customize all Kubernetes resources deployed via K Gateway. |
|   7 | Overlays use strategic merge patch to enable niche configuration changes not exposed via Helm.                         |
|   8 | Hyperscaler integrations include GCP and AWS Lambda, with EC2 support being added.                                     |
|   9 | Users can route backends to GCP or AWS Lambda with specific configurations.                                            |
|  10 | Ingress NGINX deprecation: K Gateway provides migration support using the ingress-to-gateway project.                  |
|  11 | 70-80% of common ingress annotations (e.g., session affinity, rate limiting) are mapped and supported.                 |
|  12 | Downstream fork and in-depth migration guide with examples are available for migration.                                |
|  13 | Per-listener or hostname-based MTLS CA validation is now supported, allowing certificate validation per hostname.      |
|  14 | This feature is useful for multi-tenant scenarios and is planned for upstream contribution.                            |
|  15 | K Gateway now implements Gateway API 1.5.1 and has set its conformance report.                                         |
|  16 | Listener sets are supported after collaboration with Gateway API maintainers.                                          |
|  17 | Integrates with Istio as a waypoint, supporting east-west traffic.                                                     |
|  18 | Envoy dynamic modules provide additional flexibility.                                                                  |
|  19 | Agent Gateway is now an independent project with the data plane.                                                       |
|  20 | Recent release: 2.3.0 beta 3.                                                                                          |
|  21 | Community engagement: contract fest, kiosk, website, Slack, and community meetings.                                    |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=BjB-AIFiGqA)
