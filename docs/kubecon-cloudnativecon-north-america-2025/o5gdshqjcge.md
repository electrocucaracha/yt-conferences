---
type: Video Note
title: "Retrofitting OTEL Collectors & Prometheus - How To Overcome Scale... Vijay Samuel & Sandeep Raveesh"
description: "In this presentation, Vijay Samuel and Sep from eBay’s reliability engineering team discuss how they have adapted open telemetry collectors and Prometheus to meet the demands of eBay’s large-scale infrastructure. They describe three main us..."
resource: https://www.youtube.com/watch?v=O5GdShQJCgE
tags: ["kubecon-cloudnativecon-north-america-2025", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

In this presentation, Vijay Samuel and Sep from eBay’s reliability engineering team discuss how they have adapted open telemetry collectors and Prometheus to meet the demands of eBay’s large-scale infrastructure.
They describe three main use cases: first, optimizing the service graph connector by pulling completed traces from ClickHouse storage, which reduces memory requirements and accommodates cross-cluster communication; second, extending Prometheus exemplars retention by streaming them into ClickHouse and exposing a compatible API for UI queries, enabling weeks-long retention and efficient triage without modifying Prometheus itself; and third, scaling Prometheus through sharding, replication, and multi-tenancy, while introducing an index store inspired by Google Monarch to direct queries only to relevant shards, thus improving scalability and efficiency.
The team also addresses questions about their custom ingest gateway, indexer TTL management, use of spanmetric connector, and differences from open-source HA Prometheus solutions, emphasizing their non-intrusive, horizontally scalable, and resilient architecture.
# Main Points

|   # | Main point                                                                                                                                                         |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   1 | eBay retrofitted OpenTelemetry Collectors and Prometheus to handle large-scale operations and overcome design limitations.                                         |
|   2 | Three main use cases discussed: Service Graph Connector, Prometheus Exemplars, and Prometheus Clustering.                                                          |
|   3 | Service Graph Connector:                                                                                                                                           |
|   4 | Used to construct service graphs for distributed traces.                                                                                                           |
|   5 | At eBay’s scale (10 million spans/sec, 4,000 microservices, cross-cluster communication), holding traces in memory is impractical.                                 |
|   6 | Solution: Store completed traces in ClickHouse; periodically pull traces with a custom OpenTelemetry receiver; construct service graphs without high memory usage. |
|   7 | Approach avoids global routing and in-memory holding; can be applied to tail sampling.                                                                             |
|   8 | Prometheus Exemplars:                                                                                                                                              |
|   9 | Exemplars are point-in-time events within time series, useful for triage and drill-down.                                                                           |
|  10 | Prometheus stores exemplars in a circular in-memory buffer, limiting retention (minutes to hours).                                                                 |
|  11 | eBay streams exemplars to ClickHouse for two-week retention; exposes a Prometheus-compatible API for UI queries.                                                   |
|  12 | Query optimizations: use dictionaries for metric names, uniform sampling, denormalized schema for performance.                                                     |
|  13 | Approach is non-intrusive; Prometheus remains unmodified.                                                                                                          |
|  14 | Exemplars also used for tail sampling to retain important traces.                                                                                                  |
|  15 | Prometheus Clustering:                                                                                                                                             |
|  16 | Single TSDB node scales vertically; sharding enables horizontal scaling.                                                                                           |
|  17 | Ingester hashes time series and writes to appropriate shards; shards discovered via Kubernetes API.                                                                |
|  18 | Replication across regions for high availability.                                                                                                                  |
|  19 | Multi-tenancy achieved by pinning tenants to specific clusters for isolation and custom retention.                                                                 |
|  20 | Data kept close to source to reduce latency, cost, and single points of failure; replicated across availability zones.                                             |
|  21 | Query layer uses an index store (inspired by Google Monarch) to locate data efficiently, avoiding expensive fan-out.                                               |
|  22 | Index store uses fingerprints and n-grams from time series labels.                                                                                                 |
|  23 | System supports hori                                                                                                                                               |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=O5GdShQJCgE)