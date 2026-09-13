---
layout: default
title: "Drasi: A New Take on Change-driven Architectures - Aman Singh, Microsoft"
nav_order: 65
parent: Kubecon Cloudnativecon North America 2025
type: Video Note
description:
  Aman Singh, maintainer of the CNCF project DRSI, introduces how DRSI
  simplifies building change-driven architectures, particularly for scenarios like
  real-time chat applications powered by retrieval augmented generation (RAG). He
  explains t...
resource: https://www.youtube.com/watch?v=nbLJ_ICpZhc
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

Aman Singh, maintainer of the CNCF project DRSI, introduces how DRSI simplifies building change-driven architectures, particularly for scenarios like real-time chat applications powered by retrieval augmented generation (RAG).
He explains the challenges of keeping AI chat applications up-to-date with private data stored across multiple databases, highlighting the limitations of polling (which is simple but can be stale and costly) and event streaming (which is real-time but operationally complex).
DRSI addresses these issues by allowing users to declaratively define data sources, queries, and reactions using simple YAML files, enabling continuous, real-time synchronization and derived views—such as vector stores for RAG or live dashboards—without custom code or complex infrastructure.
Through live demos, Singh shows how DRSI can connect disparate data sources, maintain up-to-date result sets, and trigger actions like embedding generation or security alerts in response to data changes, all with minimal configuration.
He concludes by emphasizing DRSI’s scalability, support for various data sources, and open-source nature, inviting collaboration and feedback from the community.

# Main Points

|   # | Main point                                                                                                |
| --: | --------------------------------------------------------------------------------------------------------- |
|   1 | Aman Singh introduces DRSI, a new CNCF project.                                                           |
|   2 | Demonstrates two change-driven scenarios using DRSI.                                                      |
|   3 | Discusses building chat applications with LLMs and the challenge of accessing private data.               |
|   4 | Explains Retrieval Augmented Generation (RAG) pattern for combining internal data with LLMs.              |
|   5 | Highlights issues with data staleness when underlying databases change.                                   |
|   6 | Describes polling as a simple but potentially stale and expensive solution.                               |
|   7 | Suggests polling for only data changes to reduce costs but increase complexity.                           |
|   8 | Presents event streaming (Debezium, Kafka, Flink) as a near real-time but operationally complex solution. |
|   9 | Introduces DRSI as a simpler alternative requiring only configuration files.                              |
|  10 | DRSI connects directly to data sources without data migration.                                            |
|  11 | Allows continuous graph queries across multiple sources, maintaining live, up-to-date result sets.        |
|  12 | Supports reactions to live result sets, such as generating embeddings and updating vector stores.         |
|  13 | Demonstrates real-time updates in a chat application as underlying data changes.                          |
|  14 | Defines derived views as materialized, transformed data for specific purposes.                            |
|  15 | DRSI can power other derived view scenarios, like real-time dashboards and CQRS read models.              |
|  16 | Change-driven architectures perform timely actions in response to data changes.                           |
|  17 | Example: Security alerting when risky container images are detected in Kubernetes clusters.               |
|  18 | DRSI simplifies change-driven solutions with YAML configuration for sources, queries, and reactions.      |
|  19 | Supports pre-built reactions (e.g., Slack, Prometheus, PagerDuty) and custom SDKs.                        |
|  20 | DRSI is open source and invites community participation.                                                  |
|  21 | Queries in DRSI act as continuous, stateful processes, updating result sets in real time.                 |
|  22 | Scaling is managed at the source, query, and reaction component level; autoscaling is in development.     |
|  23 | Data access permissions are managed via roles and cloud provider IAM.                                     |
|  24 | Query state is maintained in pluggable stores (in-memory, RocksDB,                                        |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=nbLJ_ICpZhc)
