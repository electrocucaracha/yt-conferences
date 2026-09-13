---
type: Video Note
title: "Scaling Valkey the Right Way: Kubernetes at XL Scale - Sarthak Aggarwal & Madelyn Olson, AWS"
description: "Maline Olsen and Sarthik from Amazon Elasticache discuss Valky, an open-source, horizontally scalable caching system forked from Redis, focusing on its deployment and scaling in Kubernetes environments. They share lessons learned from manag..."
resource: https://www.youtube.com/watch?v=t0qax1qQm14
tags: ["kubecon-cloudnativecon-europe-2026", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

Maline Olsen and Sarthik from Amazon Elasticache discuss Valky, an open-source, horizontally scalable caching system forked from Redis, focusing on its deployment and scaling in Kubernetes environments.
They share lessons learned from managing large clusters, referencing real-world scenarios like Pokémon Go’s unexpected traffic surge, and explain Valky’s architecture, including sharding, cluster bus communication, and failover mechanisms.
The talk covers best practices for cluster management, such as distributing primaries and replicas across availability zones, using direct IP connections, and employing connection pooling to avoid node overload.
They detail extensive scalability testing—demonstrating Valky’s ability to handle up to 2,000 nodes and 1 billion requests per second—while addressing challenges like connection storms, failover vote splits, and optimizing pub/sub message overhead.
Recent improvements include smarter connection throttling, more efficient failure detection, and a lightweight pub/sub protocol, with ongoing development of a Valky operator to further automate and simplify cluster management.
The session concludes by encouraging community involvement and highlighting Valky’s suitability as a Redis alternative for large-scale, cloud-native caching needs.
# Main Points

|   # | Main point                                                                                                                                                                                                                 |
| --: | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Maline Olsen and Sarthik are principal engineers at Amazon Elastic and contributors to the open source Valky project.                                                                                                      |
|   2 | The talk focuses on scaling large Valky clusters, sharing lessons from Amazon Elasticache.                                                                                                                                 |
|   3 | Valky is a Linux Foundation project, forked from Redis open source 7.2, and is API compatible with Redis.                                                                                                                  |
|   4 | Valky can be deployed in two modes: standalone (single instance, stateless set) and cluster (horizontally scalable).                                                                                                       |
|   5 | Valky cluster uses sharding: each shard has a primary and replicas; adding shards increases capacity.                                                                                                                      |
|   6 | Nodes communicate in a full mesh via the cluster bus; scaling limits appear around 2,000 nodes.                                                                                                                            |
|   7 | Automatic node failure detection and failover are built-in; replicas can promote themselves to primary.                                                                                                                    |
|   8 | Proper distribution of primaries and replicas across availability zones is crucial for failover and data safety.                                                                                                           |
|   9 | Valky clients connect directly to nodes, retrieve cluster topology, and map keys to slots (16,000 slots per cluster).                                                                                                      |
|  10 | Direct IP connections are recommended over DNS for lower latency.                                                                                                                                                          |
|  11 | Modern Valky clients support zonal local reads for performance.                                                                                                                                                            |
|  12 | Best practices: use connection pooling, limit connection retries, and avoid excessive topology refreshes.                                                                                                                  |
|  13 | Valky Glide is a new client that optimizes topology refreshes.                                                                                                                                                             |
|  14 | Observability improvements include cluster slot stats for identifying bottlenecks (network, CPU, memory).                                                                                                                  |
|  15 | For resharding, move the second hottest slot first, not the hottest.                                                                                                                                                       |
|  16 | Kubernetes can be used to collocate memory-heavy caches with CPU-heavy workloads for better utilization.                                                                                                                   |
|  17 | Recent improvements allow transparent data migration between shards.                                                                                                                                                       |
|  18 | Valky clusters have been tested up to 2,000 nodes and 1 billion RPS.                                                                                                                                                       |
|  19 | Issues encountered: excessive reconnection attempts after node failures, resolved with connection throttling; optimized failure report processing with radix trees; solved shard vote split with lexicographical ordering. |
|  20 | Pubsub message overhead reduced from 2KB to 16 bytes with l                                                                                                                                                                |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=t0qax1qQm14)