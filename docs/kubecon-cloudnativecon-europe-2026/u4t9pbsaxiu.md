---
layout: default
title: "Vitess: More Data, No Problems - Matt Lord & Rohit Nayak, PlanetScale"
nav_order: 389
parent: Kubecon Cloudnativecon Europe 2026
type: Video Note
description:
  In this presentation, Matt and Rohit from PlanetScale discuss Vitess,
  an open-source database clustering system designed to help organizations scale their
  MySQL data layer efficiently as their data grows. Vitess enables users to move from
  a...
resource: https://www.youtube.com/watch?v=u4T9PbsaxIU
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

In this presentation, Matt and Rohit from PlanetScale discuss Vitess, an open-source database clustering system designed to help organizations scale their MySQL data layer efficiently as their data grows.
Vitess enables users to move from a single MySQL server to a sharded, distributed architecture while maintaining the familiar MySQL interface for developers and applications.
The system is widely used by major companies such as Slack, GitHub, Square, and Uber, and is designed to be managed by small teams through extensive automation, resilience, and self-healing features.
Key concepts include keyspaces, shards, Vschema, and Vindexes, which facilitate data partitioning and routing, as well as tools for online migrations, materialized views, and change data capture.
Vitess emphasizes principles of distributed computing such as isolation, redundancy, automated recovery, and zero-downtime upgrades, leveraging MySQL’s reliability and focusing on deliberate design choices to achieve both performance and resilience at scale.

# Main Points

|   # | Main point                                                                                                                                                             |
| --: | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Presentation covers Vitess and its role in scaling data layers.                                                                                                        |
|   2 | Presenters are maintainers of Vitess at PlanetScale.                                                                                                                   |
|   3 | Vitess enables scaling from a single MySQL server to many nodes without changing the user experience.                                                                  |
|   4 | Users and developers interact with Vitess as if it were a single MySQL server.                                                                                         |
|   5 | Vitess is used by major companies like Slack, GitHub, Square, and Uber.                                                                                                |
|   6 | Key concepts: keyspace (logical database across nodes), shards (data partitions managed by MySQL replication groups), Vschema and Vindexes (define data distribution). |
|   7 | Application traffic flows through load balancers to VTGates (stateless MySQL protocol servers).                                                                        |
|   8 | VTGates use Vschema and Vindexes to route queries to the correct shard.                                                                                                |
|   9 | Vitess supports seamless data migrations and sharding without downtime using commands like MoveTables and Reshard.                                                     |
|  10 | VDiff command compares source and target tables during migrations for consistency.                                                                                     |
|  11 | Supports vertical/functional sharding to split tables into separate keyspaces.                                                                                         |
|  12 | Materialized views and reference tables improve query performance and data locality.                                                                                   |
|  13 | VStream API enables change data capture (CDC) for analytics and data warehousing.                                                                                      |
|  14 | Vitess design principles: distributed computing, isolation, redundancy, graceful degradation, circuit breakers, automated recovery, self-healing, and observability.   |
|  15 | Failure domains ("cells") provide isolation; systems can span multiple availability zones or clouds.                                                                   |
|  16 | VTGates are stateless; system continues serving queries even if some components fail briefly.                                                                          |
|  17 | Sharding provides isolation and redundancy; only affected shards impact a subset of users.                                                                             |
|  18 | Query herd reduction and connection pooling optimize resource usage.                                                                                                   |
|  19 | Backpressure and throttling mechanisms manage load and prioritize critical queries.                                                                                    |
|  20 | Automated failover and fast backup/restore processes minimize downtime.                                                                                                |
|  21 | Smaller shard sizes (500GB–2TB) aid in faster recovery and management.                                                                                                 |
|  22 | Zero downtime upgrades for query serving layers and database                                                                                                           |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=u4T9PbsaxIU)
