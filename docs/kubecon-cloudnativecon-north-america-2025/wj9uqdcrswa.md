---
layout: default
title:
  "Kubernetes and etcd: Common Pitfalls and How To Avoid Them - Arka Saha & Nabarun
  Pal, Broadcom"
nav_order: 143
parent: Kubecon Cloudnativecon North America 2025
type: Video Note
description:
  The session focused on common pitfalls and best practices for managing
  etcd within Kubernetes, particularly at large scale. The speakers emphasized the
  critical role of etcd as Kubernetes’ core data store and discussed issues such as
  databa...
resource: https://www.youtube.com/watch?v=wj9UQDcRSWA
tags:
  - kubecon-cloudnativecon-north-america-2025
  - video
  - learning
status: stable
generated:
  by: process:yt-conferences-okf
  at: 2026-09-12 00:00:00+00:00
---

# Summary

The session focused on common pitfalls and best practices for managing etcd within Kubernetes, particularly at large scale.
The speakers emphasized the critical role of etcd as Kubernetes’ core data store and discussed issues such as database size limits, compaction, defragmentation, upgrade challenges, and the impact of disk and network performance on cluster health.
They highlighted the importance of monitoring key metrics—like leader changes, slow applies, slow read indices, and heartbeat failures—using Prometheus to detect performance problems.
The discussion also covered strategies like separating high-churn resources (e.g., events) into dedicated etcd clusters to maintain overall performance, and the necessity of adhering to recommended disk IOPS and network throughput for stability.
Attendees were encouraged to consult the official etcd operational guide and use diagnostic tools for proactive cluster health management, while questions from the audience addressed real-world scenarios, performance tuning, and the rationale behind architectural decisions.

# Main Points

|   # | Main point                                                                                                                                |
| --: | ----------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Session covers Kubernetes and etcd common pitfalls, especially for large-scale users.                                                     |
|   2 | etcd is a critical component of Kubernetes; if etcd fails, the cluster becomes read-only and API requests fail.                           |
|   3 | Default etcd database size is 2GB; recommended to increase to 8GB using quota-backend-bytes.                                              |
|   4 | Exceeding space quota leads to "MVCC database space exceeded" errors; manage with auto-compaction and defragmentation.                    |
|   5 | Defragmentation is resource-intensive and must be done per etcd member, one at a time.                                                    |
|   6 | Upgrading from etcd 3.5 to 3.6 can cause "too many learner" errors due to V2/V3 data store changes; fixed in 3.5.24+.                     |
|   7 | Rolling upgrades from older 3.5.x versions can reintroduce learner issues if old snapshots are used.                                      |
|   8 | Network latency and disk write latency can cause cluster performance issues; minimum 50 sequential IOPS for typical, 500 for large-scale. |
|   9 | etcd recommends 1Gbps network for typical, 10Gbps for high-scale clusters.                                                                |
|  10 | Monitor etcd space quota metrics: actual size in use and total size in use.                                                               |
|  11 | High-churn Kubernetes objects (e.g., events, leases) can overwhelm etcd; use etcd server overrides to separate workloads.                 |
|  12 | Large list queries can cause memory spikes; streaming encoding helps, but stream ranges are being developed for further mitigation.       |
|  13 | Use etcd-diagnosis tool for comprehensive health checks and metrics.                                                                      |
|  14 | Key Prometheus metrics to monitor: leader changes, slow applies, slow read index, heartbeat failures.                                     |
|  15 | Frequent leader changes or failed heartbeats indicate cluster instability.                                                                |
|  16 | Creating separate etcd clusters for high-churn resources (like events) isolates performance impact.                                       |
|  17 | Security pitfalls (PKI, RBAC) were not discussed; etcd uses certificate-based authentication.                                             |
|  18 | Large numbers of watches/subscriptions can impact performance; compaction and defrag operations may take longer with large data sizes.    |
|  19 | Refer to the etcd operational guide for detailed best practices.                                                                          |
|  20 | Join the sig-etcd Slack channel and check the etcd-diagnosis                                                                              |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=wj9UQDcRSWA)
