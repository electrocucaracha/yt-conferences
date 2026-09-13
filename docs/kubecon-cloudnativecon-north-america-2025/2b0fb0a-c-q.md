---
layout: default
title:
  "Under the Hood of Vitess: Database Engineered for Scale and Resilien... Matt
  Lord & Florent Poinsard"
nav_order: 331
parent: Kubecon Cloudnativecon North America 2025
type: Video Note
description:
  Florent and Matt, maintainers of the Vitess project and software engineers
  at PlanetScale, provide an overview of Vitess, a cloud-native, massively scalable
  database system originally donated to CNCF by YouTube. Vitess offers MySQL compatib...
resource: https://www.youtube.com/watch?v=2B0FB0A_c_Q
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

Florent and Matt, maintainers of the Vitess project and software engineers at PlanetScale, provide an overview of Vitess, a cloud-native, massively scalable database system originally donated to CNCF by YouTube.
Vitess offers MySQL compatibility, high availability, sharding, materialization workflows, cluster management, online schema changes with minimal downtime, backup and recovery, query consolidation, and automatic failure detection and repair.
The architecture includes components such as VTGate, VTTablet, VTAdmin, VTOrc, and a topology server, enabling easy scaling, management, and resilience.
The talk emphasizes the importance of resilience in large-scale systems, discussing principles like isolation, redundancy, automated recovery, observability, and testing, and highlights how Vitess handles failures gracefully to maintain service availability.
Real-world users such as Slack, GitHub, and Square rely on Vitess for high throughput and reliability, and the project continues to evolve with a strong community and robust testing practices.

# Main Points

|   # | Main point                                                                                                                                                                                                                |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Florent and Matt are maintainers of the Vitess project and software engineers at PlanetScale.                                                                                                                             |
|   2 | Vitess is a cloud native, massively scalable database, graduated in 2019, donated to CNCF by YouTube.                                                                                                                     |
|   3 | Highly available, compatible with MySQL 8.0 and 8.4, supports MySQL and gRPC protocols.                                                                                                                                   |
|   4 | Operators can easily scale and manage large databases with small teams.                                                                                                                                                   |
|   5 | Users experience Vitess as a standard MySQL database, using the same tools and connection strings.                                                                                                                        |
|   6 | Supports sharding and resharding, materialization workflows, cluster management, online schema changes with minimal downtime, throttling, backup and recovery (including point-in-time restore), and query consolidation. |
|   7 | Kubernetes operator (Vitess Operator) allows scheduled backups.                                                                                                                                                           |
|   8 | Automatic failure detection and repair via VTOrc; automatic promotion of replicas if primary fails.                                                                                                                       |
|   9 | Key concepts: keyspaces (logical databases), shards (data subsets), vSchema (JSON mapping for data distribution), vindex (index for sharding).                                                                            |
|  10 | Architecture: clients connect via load balancer to VTGate (main entry point), which parses and routes queries to shards; each shard has a primary and replicas managed by VTTablet.                                       |
|  11 | Administration tools: VTAdmin (UI), VTOrc (repair), VTctl (API for cluster operations), topo server (usually etcd).                                                                                                       |
|  12 | Used by organizations like Slack, GitHub, Vinted, Square, and PlanetScale; supports high QPS and large data volumes.                                                                                                      |
|  13 | Community is active and stable; project is 15 years old.                                                                                                                                                                  |
|  14 | Resilience focuses on availability, cost trade-offs, defining and measuring downtime, and business impact.                                                                                                                |
|  15 | Principles: isolation (avoid single points of failure), redundancy, graceful degradation, circuit breakers, automated recovery, observability, and testing.                                                               |
|  16 | Components are spread across availability zones; stateless services (like VTGate) are easily scalable.                                                                                                                    |
|  17 | Topology server is not in the query hot path; sharding and semi-sync writes ensure data durability.                                                                                                                       |
|  18 | Query consolidation and buffering during failove                                                                                                                                                                          |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=2B0FB0A_c_Q)
