---
type: Video Note
title: "Project Lightning Talk: Vitess: Unlimited Database Scalability - Matt Lord, Maintainer"
description: "In this talk, Matt Lord introduces Vitess, a CNCF project designed as a cloud-native, massively scalable, and highly available database solution that is MySQL compatible. Vitess enables organizations to scale both their data storage and ope..."
resource: https://www.youtube.com/watch?v=CSSnY3MFhPI
tags: ["kubecon-cloudnativecon-north-america-2025", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

In this talk, Matt Lord introduces Vitess, a CNCF project designed as a cloud-native, massively scalable, and highly available database solution that is MySQL compatible.
Vitess enables organizations to scale both their data storage and operations teams by providing a familiar MySQL user experience, even as data is sharded and managed across large distributed clusters.
Key features include seamless sharding and resharding, materialized views, online schema changes with controlled cutovers, robust backup and recovery options, and strong observability.
Vitess employs a shared-nothing architecture for isolation and resilience, supports consolidation and pooling to handle high-traffic events, and incorporates mechanisms for graceful degradation, load shedding, and circuit breaking to maintain system health.
Major companies like Slack, Square, Shopify, and GitHub use Vitess in production, demonstrating its reliability and scalability for large-scale applications.
# Main Points

|   # | Main point                                                                                                                      |
| --: | ------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Vitess is a CNCF project aimed at providing a cloud-native, massively scalable, and highly available MySQL-compatible database. |
|   2 | The project includes a Kubernetes operator as a key component.                                                                  |
|   3 | Vitess enables virtually unlimited scaling of the data storage layer and helps scale operations teams.                          |
|   4 | Users experience the same interface as a single MySQL instance, both for development and production.                            |
|   5 | Key features include sharding and resharding data, allowing partitioning and management of large datasets.                      |
|   6 | Supports materialized views across distributed data sets.                                                                       |
|   7 | Provides online schema changes with controlled cutovers, such as scheduling changes during low-traffic periods.                 |
|   8 | Offers robust backup and recovery options.                                                                                      |
|   9 | Used in production by companies like Slack, Square, Shopify, and GitHub.                                                        |
|  10 | Many people interact with Vitess daily through these platforms without realizing it.                                            |
|  11 | Employs a shared-nothing architecture; each shard is managed by a MySQL replica set with a primary and multiple replicas.       |
|  12 | Replicas can serve reads and take over writes in case of primary failure, providing isolation and protection from failures.     |
|  13 | Supports consolidation and pooling to efficiently handle high-traffic events by sharing database responses among many clients.  |
|  14 | Implements graceful degradation during failures, promoting replicas and pausing traffic briefly to avoid client errors.         |
|  15 | Includes mechanisms for throttling, back pressure, load shedding, and circuit breakers to maintain system health.               |
|  16 | Highly observable, supporting large-scale operations.                                                                           |
|  17 | Project maintainers are available at the project booth and more information can be found at vitess.io.                          |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=CSSnY3MFhPI)