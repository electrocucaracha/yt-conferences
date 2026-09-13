---
layout: default
title: OpenCost - Cost and Resource Management Deep Dive - Rajith Attapattu, Randoli
nav_order: 230
parent: Kubecon Cloudnativecon Europe 2026
type: Video Note
description:
  Rajit Tatawatu, founder and CTO of Randoli and maintainer of the OpenCost
  project, introduces OpenCost, an open-source, vendor-neutral CNCF project for Kubernetes
  cost monitoring. He explains that OpenCost provides detailed cost visibility...
resource: https://www.youtube.com/watch?v=QL3bpkNJRec
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

Rajit Tatawatu, founder and CTO of Randoli and maintainer of the OpenCost project, introduces OpenCost, an open-source, vendor-neutral CNCF project for Kubernetes cost monitoring.
He explains that OpenCost provides detailed cost visibility and efficiency metrics for Kubernetes workloads, supporting multi-cluster and multi-cloud environments, and allows users to break down costs by pods, containers, deployments, and namespaces.
The architecture relies on Prometheus for usage metrics and cloud API pricing, with recent developments including improved integration testing, an experimental Prom-less mode for large clusters, and the introduction of the kube model to better separate usage and pricing data for more accurate cost calculations.
OpenCost features a plugin system for extensibility, though the UI is basic, and the project's value lies in its robust APIs and data model.
Rajit encourages community contributions, highlighting areas such as plugin development, testing, and roadmap input, and addresses questions about cost calculation, data export, and future support for infrastructure outside Kubernetes.

# Main Points

|   # | Main point                                                                                                                                                     |
| --: | -------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | High interest in Kubernetes cost management; session focused on OpenCost.                                                                                      |
|   2 | Presenter: Rajit Tatawatu, founder/CTO of Randoli, OpenCost maintainer.                                                                                        |
|   3 | OpenCost: open source, vendor-neutral CNCF project (incubating stage).                                                                                         |
|   4 | Provides Kubernetes cost model: resource efficiency and resource cost.                                                                                         |
|   5 | Supports multi-cluster, multi-cloud (AWS, Azure, GCP, on-prem with custom pricing).                                                                            |
|   6 | Straightforward integration and flexible deployment.                                                                                                           |
|   7 | Essential for Kubernetes day-two operations and cost visibility.                                                                                               |
|   8 | Offers granular cost breakdown: pod, container, deployment, namespace.                                                                                         |
|   9 | Enables tracking spend, cost alerts, budgets, chargeback, and efficiency metrics.                                                                              |
|  10 | Cluster cost zones: overhead (control plane, licensing), resource allocation (CPU, GPU, memory, disk), resource usage (network, egress).                       |
|  11 | OpenCost calculates cost as request or usage, whichever is higher.                                                                                             |
|  12 | Highlights inefficiencies and oversized pods.                                                                                                                  |
|  13 | Aggregates costs from container up to business units.                                                                                                          |
|  14 | Difference between OpenCost and Kubecost: Kubecost donated OpenCost; OpenCost is vendor-neutral standard, vendors build on top.                                |
|  15 | Architecture: relies on Prometheus, kube-state-metrics, cloud API pricing; exposes APIs for data aggregation.                                                  |
|  16 | Plugin architecture allows integration with tools like Datadog, Snowflake, OpenAI.                                                                             |
|  17 | Recent updates: improved integration/release testing, experimental "promless" mode (no Prometheus), MCP server, and "kubemodel" for better pricing separation. |
|  18 | Promless mode improves performance for large clusters.                                                                                                         |
|  19 | Kubemodel separates usage from pricing for more accurate calculations.                                                                                         |
|  20 | UI is basic; main value is in APIs and data model.                                                                                                             |
|  21 | Focus on supply chain security: CI scanning, SBOM generation.                                                                                                  |
|  22 | Community invites contributions: plugins, promless mode, kubemodel, UI revamp.                                                                                 |
|  23 | Bi-weekly community meetings scheduled for global participation.                                                                                               |
|  24 | Ongoing discussions: LLM token cost, OpenTelemetry integration.                                                                                                |
|  25 | OpenCost uses public pricing by default; vendors can override; kubemodel aim                                                                                   |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=QL3bpkNJRec)
