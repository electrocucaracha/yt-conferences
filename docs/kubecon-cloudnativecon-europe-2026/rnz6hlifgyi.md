---
type: Video Note
title: "Redis on EC2 to Valkey on Kubernetes: A Zero-Downtime Case Study - Joe Heyburn, Braze"
description: "Joe Hayburn, a staff engineer at Braze, describes how his team migrated nearly 300 Redis instances to Kubernetes without downtime and with a rollback path at every step, enabling a seamless later migration to Valkey and achieving up to a 90..."
resource: https://www.youtube.com/watch?v=rNZ6HLiFgYI
tags: ["kubecon-cloudnativecon-europe-2026", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

Joe Hayburn, a staff engineer at Braze, describes how his team migrated nearly 300 Redis instances to Kubernetes without downtime and with a rollback path at every step, enabling a seamless later migration to Valkey and achieving up to a 90% reduction in latency.
Braze, a customer engagement platform handling billions of personalized messages daily, required a highly available, scalable in-memory database solution, using Redis (and later Valkey) for tasks like rate limiting, distributed locks, and message deduplication.
The migration involved overcoming challenges such as maintaining static IPs for Sentinel in Kubernetes, ensuring no downtime or data loss, and managing network routing with AWS Network Load Balancers.
After successfully migrating to Kubernetes, Braze switched to Valkey with minimal configuration changes, migrating 350 shards across 10 clusters in six weeks and seeing significant performance improvements.
Looking ahead, Braze aims to optimize pod distribution, enable dynamic scaling, and is contributing to a community-led Valkey operator for Kubernetes to further streamline database operations.
# Main Points

|   # | Main point                                                                                                                                                |
| --: | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Joe Hayburn, staff engineer at Braze, led migration of nearly 300 Redis instances to Kubernetes in 2022 with no downtime and rollback at every step.      |
|   2 | Migration to Kubernetes enabled a seamless switch to Valkey, resulting in up to 90% latency improvement.                                                  |
|   3 | Braze is a customer engagement platform supporting real-time, personalized messaging across multiple channels.                                            |
|   4 | Braze operates over 600 highly available Redis/Valkey shards, processing 36 million operations per second with 6.5 TB memory.                             |
|   5 | Legacy setup: Redis on EC2 managed by Chef, sharded workloads, cluster-scoped Sentinel for high availability and failover.                                |
|   6 | Kubernetes setup: Each shard as a StatefulSet with three pods (1 primary, 2 replicas), Sentinel as sidecar, per-pod services with stable cluster IPs.     |
|   7 | Migration requirements: zero downtime and ability to roll back without data loss.                                                                         |
|   8 | RDB file copy approach was rejected due to downtime; direct replication approach was rejected due to rollback limitations.                                |
|   9 | Solution: Used AWS Network Load Balancer (NLB) to route traffic from EC2 to Kubernetes pods, enabling replication and failover.                           |
|  10 | Migration process: three phases—setup, migration (with health checks and zone affinity), and final reconfiguration to internal cluster IPs.               |
|  11 | Unexpected challenges: NLB data transfer fees could exceed $100,000/month; split-brain risk mitigated by adding a seventh Sentinel and increasing quorum. |
|  12 | Migration completed Feb 2023–May 2024: nearly 300 shards across seven clusters, no data loss.                                                             |
|  13 | Redis license change prompted Braze to migrate to Valkey; migration required only minor Helm chart changes.                                               |
|  14 | 350 shards migrated to Valkey in six weeks; Valkey is fully backward compatible with Redis config.                                                        |
|  15 | Performance gains: up to 90% P95 latency reduction on busiest clusters; average 15% P95 latency improvement; 5% median improvement at massive scale.      |
|  16 | Current challenges: need for better pod distribution to avoid hot nodes, desire for dynamic scaling with Kubernetes vertical po                           |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=rNZ6HLiFgYI)