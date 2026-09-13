---
layout: default
title:
  "Cutting Metrics Traffic, Cutting Costs: The AZ-Aware Observ... Iris Dyrmishi
  & Rodrigo Fior Kuntzer"
nav_order: 81
parent: Kubecon Cloudnativecon Europe 2026
type: Video Note
description:
  Rodrigo and Iris, engineers at Miro, discuss their experience optimizing
  observability costs, particularly focusing on the high expenses associated with
  intra-region data transfer in multi-availability zone (multi-AZ) Kubernetes environment...
resource: https://www.youtube.com/watch?v=ycnDgULCHTA
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

Rodrigo and Iris, engineers at Miro, discuss their experience optimizing observability costs, particularly focusing on the high expenses associated with intra-region data transfer in multi-availability zone (multi-AZ) Kubernetes environments.
They explain that observability components, such as metrics collectors, can generate significant cross-AZ network traffic, often surpassing compute costs, due to default configurations that lack zone awareness.
To address this, Miro implemented a phased approach: first, they modified their metrics collection so that agents only scrape targets within the same AZ, using Kubernetes topology metadata and relabeling techniques, which resulted in substantial cost savings without impacting reliability or user experience.
They emphasize the importance of maintaining centralized alerting and querying, highlight the increased architectural complexity, and note that while their optimizations yielded six-figure savings, some cross-AZ traffic remains unavoidable, especially for certain external services and during query operations.
The team provides a blueprint and resources for others to evaluate and implement similar strategies based on their own needs and environments.

# Main Points

|   # | Main point                                                                                                                                                                                                                                                                             |
| --: | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Speakers: Rodrigo (Staff SR Engineer at Miro) and Iris Durishi (Senior Observability Engineer at Miro, CNCF Ambassador)                                                                                                                                                                |
|   2 | Topic: Cutting metric traffic and costs in observability systems                                                                                                                                                                                                                       |
|   3 | Observability costs are often underestimated, with hidden expenses, especially in cloud environments                                                                                                                                                                                   |
|   4 | At Miro, storage and database costs are significant, but intra-region data transfer costs (especially for observability components) were growing rapidly                                                                                                                               |
|   5 | Up to 60-65% of intra-region data transfer costs came from observability nodes; sometimes network costs exceeded compute costs                                                                                                                                                         |
|   6 | Industry-wide issue: mature companies also struggle with observability network costs; blame often shifts between observability and network teams                                                                                                                                       |
|   7 | Multi-AZ (Availability Zone) setups are often required for fault tolerance and capacity constraints                                                                                                                                                                                    |
|   8 | Cloud providers charge differently for intra-region data transfer: AWS (2 cents/GB), GCP (1 cent/GB egress), Azure (free since 2024)                                                                                                                                                   |
|   9 | Observability is a major source of cross-AZ traffic due to agents scraping targets across zones by default                                                                                                                                                                             |
|  10 | Miro’s environment: ~140 million time series/day, 13,000+ targets, 12-19GB per scrape, 25TB metrics/day                                                                                                                                                                                |
|  11 | Optimization prerequisites: maintain compute resources, no extra architecture spending, preserve availability/reliability/metrics quality, ensure scalability, centralized alerting/querying                                                                                           |
|  12 | Optimization done in two phases: 1. Phase 1: Make metric agents (e.g., VM agent, Prometheus) scrape only targets in the same AZ—quick win, low risk 2. Phase 2 (planned): Fully AZ-aware ingestion and querying with federated multi-level query layer                                 |
|  13 | Technical implementation: use Kubernetes topology metadata to make scraping AZ-aware; three options: 1. Kubernetes 1.35+ (topology labels on pods by default) 2. Mutating webhook to copy node labels to pods (older versions) 3. Prometheus native: attach node metadata in SD config |
|  14 | Use relabeling in scrape configs to filter targets by AZ                                                                                                                                                                                                                               |
|  15 | For targets without AZ metadata (                                                                                                                                                                                                                                                      |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=ycnDgULCHTA)
