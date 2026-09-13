---
layout: default
title:
  "Project Lightning Talk: CloudNativePG: Running Postgres The Kubernetes Way
  - Gabriele Bartolini"
nav_order: 211
parent: Kubecon Cloudnativecon North America 2025
type: Video Note
description:
  Gabriel, a maintainer of CloudNativePG and a PostgreSQL contributor,
  introduces CloudNativePG at KubeCon, emphasizing its role as a Kubernetes operator
  designed specifically for managing PostgreSQL databases. Unlike generic stateful
  sets, C...
resource: https://www.youtube.com/watch?v=pYwYwehQX3U
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

Gabriel, a maintainer of CloudNativePG and a PostgreSQL contributor, introduces CloudNativePG at KubeCon, emphasizing its role as a Kubernetes operator designed specifically for managing PostgreSQL databases.
Unlike generic stateful sets, CloudNativePG uses a custom controller to provide fine-grained, declarative management of PostgreSQL, enabling features like automated failover, upgrades, backups, and observability, while supporting high-performance, share-nothing architectures within Kubernetes.
Gabriel highlights the project's recent entry into the CNCF sandbox and urges production users to add themselves to the adopters list to help the project progress toward incubation status.
He also outlines upcoming features such as failover quorums and extension container images, and invites the community to contribute across its 15+ projects, reinforcing CloudNativePG’s vendor-neutral and openly governed nature.
Finally, he encourages attendees to join the community and support the project’s growth and CNCF incubation efforts.

# Main Points

|   # | Main point                                                                                                                                                                     |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   1 | Gabriel is a maintainer of CloudNativePG, Data on Kubernetes ambassador, and Postgres contributor with 25 years of experience.                                                 |
|   2 | Audience engagement: asked who has heard of, used, or is using CloudNativePG in production.                                                                                    |
|   3 | Emphasized importance of being on the adopters list on GitHub, especially for production users.                                                                                |
|   4 | CloudNativePG recently joined CNCF sandbox; next goal is CNCF incubation.                                                                                                      |
|   5 | Need to prove project maturity and wide adoption for incubation.                                                                                                               |
|   6 | CloudNativePG addresses the challenge of running stateful databases like Postgres on Kubernetes.                                                                               |
|   7 | Kubernetes is declarative and designed for "cattle," but databases like Postgres are "pets" needing complex operations (failover, backups, upgrades, security, observability). |
|   8 | Default Kubernetes StatefulSet is generic and doesn't understand Postgres-specific features like streaming, synchronous replication, or write-ahead logs.                      |
|   9 | CloudNativePG uses a custom controller, not StatefulSets, for fine-grained management of pods and PVCs.                                                                        |
|  10 | Enables declarative management of Postgres, supporting features like specifying instance count, synchronous replicas, and separate WAL volumes.                                |
|  11 | Supports the "elephant herd" approach: managing stateful Postgres as a group within Kubernetes.                                                                                |
|  12 | Allows logical database placement in the same namespace as microservices, with physical placement on high-performance nodes using Kubernetes features.                         |
|  13 | Supports "share nothing" architecture and bare metal performance.                                                                                                              |
|  14 | Production-ready features: Postgres-native HA, automated failover, automated upgrades, declarative backups, full observability.                                                |
|  15 | Roadmap includes failover quorums for synchronous replication, 4end data management, first-class extension container images, and more.                                         |
|  16 | Features and roadmap support internal database-as-a-service and migration from hyperscalers.                                                                                   |
|  17 | Project is vendor-neutral, openly governed, and seeking contributors for over 15 projects (Helm charts, Grafana dashboards, container images, metrics, etc.).                  |
|  18 | Encourage                                                                                                                                                                      |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=pYwYwehQX3U)
