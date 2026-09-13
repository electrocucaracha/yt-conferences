---
layout: default
title:
  "Discover Cortex: High Scalability Metrics in 2026 - Friedrich Gonzalez & Charlie
  Le, Apple"
nav_order: 93
parent: Kubecon Cloudnativecon Europe 2026
type: Video Note
description:
  Charlie and Frederick, software engineers at Apple and maintainers of
  Cortex, presented an overview of Cortex, an open-source, CNCF project designed for
  scalable, multi-tenant metric storage and querying, compatible with Prometheus and
  Open...
resource: https://www.youtube.com/watch?v=PCeS4YLKTwg
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

Charlie and Frederick, software engineers at Apple and maintainers of Cortex, presented an overview of Cortex, an open-source, CNCF project designed for scalable, multi-tenant metric storage and querying, compatible with Prometheus and OpenTelemetry.
They highlighted new features in the 1.20 release, including experimental support for remote write 2.0, improved ingestion efficiency, enhanced native histogram support, multi-tenant querying, dynamic query splitting for better performance, resource-based query rejection, UTF-8 metric compatibility, and the introduction of the Parquet storage format for more efficient queries.
Frederick discussed further improvements in the 1.21 release candidate, such as enhanced caching, the removal and reintroduction of store gateways for better performance, and the graduation process for Cortex, including a public security review.
They also addressed community contributions, clarified the collaborative relationship between Cortex and Thanos, and explained that while both projects share some features, Cortex emphasizes multi-tenancy and SaaS-like API access, whereas Thanos focuses on sidecar architecture.
The session concluded with a Q&A addressing differences and shared features between Cortex and Thanos.

# Main Points

|   # | Main point                                                                                                                      |
| --: | ------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Charlie and Frederick, software engineers at Apple, presented updates on Cortex.                                                |
|   2 | Cortex allows sending metrics from Prometheus or OpenTelemetry collectors to a backend for long-term storage and querying.      |
|   3 | Supports multi-tenancy, enabling metric separation and isolation per team.                                                      |
|   4 | Horizontally scalable architecture: distributor, ingester, compactor, querier, and ruler components.                            |
|   5 | Metrics are stored in memory, then uploaded as blocks to object storage (S3, Google Cloud, Azure, Rook) for infinite retention. |
|   6 | Compactor optimizes blocks for efficient querying.                                                                              |
|   7 | Supports querying via Grafana or other tools, with tenant-specific headers for multi-tenancy.                                   |
|   8 | Uses gossip ring protocol for component communication and failure handling.                                                     |
|   9 | Caching reduces repeated fetches from object storage.                                                                           |
|  10 | Ruler component manages per-tenant recording rules.                                                                             |
|  11 | Integrates with PagerDuty and Slack via Alertmanager.                                                                           |
|  12 | Cortex is open source (Apache 2), CNCF project, compatible with Prometheus and OpenTelemetry.                                   |
|  13 | New in 1.20:                                                                                                                    |
|  14 | Experimental support for remote write 2.0 (improved reliability).                                                               |
|  15 | Stream-based push for ingestion, improving efficiency.                                                                          |
|  16 | Improved native histogram support, including out-of-order ingestion and observability.                                          |
|  17 | Ingestion rate limits for native histograms.                                                                                    |
|  18 | Ability to query multiple tenants simultaneously using pipe-delimited or regex.                                                 |
|  19 | Dynamic query splitting for more efficient query sharding.                                                                      |
|  20 | Option to reject queries if ingesters exceed CPU/memory thresholds.                                                             |
|  21 | UTF-8 support in metric names and labels, including emojis.                                                                     |
|  22 | Parquet format support for efficient columnar queries and storage.                                                              |
|  23 | In 1.21 (release candidate):                                                                                                    |
|  24 | Removal of store gateways for more efficient querying.                                                                          |
|  25 | Improved caching with store gateways.                                                                                           |
|  26 | Many features moved from experimental to production-ready.                                                                      |
|  27 | Enhanced HA support without etcd, using memberlist.                                                                             |
|  28 | New metrics to track actual query usage.                                                                                        |
|  29 | Expanded OTLP support.                                                                                                          |
|  30 | Overrides API allows users t                                                                                                    |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=PCeS4YLKTwg)
