---
layout: default
title: Leveraging Ceph Rados Gateway for Scalable and Resilient Object Storage
nav_order: 57
parent: OpenInfra Summit Europe 2025
type: Video Note
description: "Kalpesh from the IBM SE RGW team presents an overview of leveraging the Ceph Redos Gateway (RGW) for scalable and resilient object storage, highlighting its capabilities as a unified, S3-compatible..."
resource: "https://www.youtube.com/watch?v=xM37evX7BCs"
youtube_stats:
  view_count: 138
  like_count: 1
  channel_subscriber_count: 46800
tags:
  - openinfra-summit-europe-2025
  - video
  - learning
status: stable
generated:
  by: process:yt-summarizer-okf
  at: 2026-11-22T23:38:50+00:00
---

# Summary

Kalpesh from the IBM SE RGW team presents an overview of leveraging the Ceph Redos Gateway (RGW) for scalable and resilient object storage, highlighting its capabilities as a unified, S3-compatible platform that supports object, block, and file storage.
The presentation details key characteristics such as horizontal scalability to petabyte levels, cost efficiency through tiered storage and commodity hardware, and high availability via multi-site asynchronous replication and archive zones, which provide near-real-time data resilience and immutable backups.
Key components discussed include D3N for accelerating data access through local caching, bucket notifications for event-driven workflows like AI/ML pipelines, and security features such as STS, IAM, and lifecycle management.
Future enhancements planned for the RGW include D4N distributed caching, per-bucket logging and usage metrics, data deduplication, and external bucket indexing to improve performance and scalability.
The session concludes with a Q&A addressing monitoring synchronization in multi-site setups, listing performance optimizations through dynamic sharding, and potential integrations with OpenStack Keystone.

# Main Points

|   # | Main point                                                                                                                                                                 |
| --: | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Ceph is an open-source, distributed, software-defined storage solution offering a unified platform for object, block, and file storage.                                    |
|   2 | Ceph RGW provides a robust, scalable S3 endpoint with low latency, high performance, and full support for the Amazon S3 and IM dialects.                                   |
|   3 | Security compliance features include encryption, STS, public access blocks, MFA delete, and IAM policies for buckets, users, and roles.                                    |
|   4 | The system supports horizontal scaling to petabyte and exabyte levels with no single point of failure and a distributed architecture without central controllers.          |
|   5 | Data redundancy and availability are ensured through automatic data placement, replication, and the ability to add storage nodes without downtime.                         |
|   6 | Cost efficiency is achieved via a pay-as-you-grow model, hot/warm/cold tiering, and the use of commodity hardware to reduce total cost of ownership.                       |
|   7 | Accessibility is enhanced through S3 API compatibility, RESTful APIs, and multi-region replication for a consistent user experience.                                       |
|   8 | High availability and durability are maintained using replication, erasure coding, and multi-region replication for geo-resilience and disaster recovery.                  |
|   9 | Archive zones function as read-only or immutable replicated zones to reduce data copies and provide near-real-time resilience.                                             |
|  10 | Security and compliance are further supported by bucket policies, role-based policies, and metadata and lifecycle management for advanced search and analytics.            |
|  11 | Lifecycle policies automate data retention, archival, and deletion, allowing data retrieval from cloud or S3 tape endpoints.                                               |
|  12 | Operational efficiency is improved through a user-friendly UI that facilitates fast deployments.                                                                           |
|  13 | D3N (Data Center Data Delivery Network) accelerates data access for large datasets using local caching layers like RAM or NVMe at the edge.                                |
|  14 | Bucket notifications enable users to receive alerts for object addition, deletion, or modification events within the storage environment.                                  |
|  15 | Multi-site asynchronous replication allows data to be replicated between zones, with a global load balancer ensuring high availability.                                    |
|  16 | Archive zones reduce the number of object copies across a zone group by enabling versioning exclusively in the archive zone, eliminating the need for scheduled backups.   |
|  17 | An example use case involves an X-ray pneumonia detection pipeline where bucket notifications trigger event-driven functions to analyze and anonymize images.              |
|  18 | Another use case demonstrates an e-commerce data pipeline where S3 Select filters malicious IPs, routing data to raw and staging zones for enrichment via Spark or Presto. |
|  19 | The curated zone stores data in Iceberg table format for business intelligence consumption, completing the ingest-to-consume workflow.                                     |
|  20 | RGW scalability features include handling millions of objects per cluster, dynamic sharding of bucket indexing, and hierarchical data placement.                           |
|  21 | Future plans include D4N caching, an intelligent distributed cache with read/write capabilities to increase overall performance.                                           |
|  22 | Bucket logging will provide granular auditing and monitoring of all bucket-level activities to enhance security and operational visibility.                                |
|  23 | Per-bucket and per-user usage metrics will be introduced to track quota details and specific request bytes sent and received.                                              |
|  24 | A deduplication prototype aims to identify identical objects and replace them with references to a single unique copy for space optimization.                              |
|  25 | Distributed RGW standalone will allow RGW to run on a local POSIX file system without other Ceph components, serving as a direct S3 service.                               |
|  26 | External bucket indexing will leverage data structures like B-trees to enhance performance and scalability for faster lookups and query operations.                        |
|  27 | Multi-site replication consistency can be monitored using Ceph dashboards, CLI bucket stats, and Prometheus performance counters.                                          |
|  28 | Listing performance for high-volume buckets can be improved through dynamic resharding of bucket indices.                                                                  |
|  29 | Integration with OpenStack Keystone is currently limited, with no immediate plans for multiple key pairs per project to separate bucket access.                            |
|  30 | Archive zones are supported in both single-site and multi-site setups, requiring admin access to delete objects from the archive zone.                                     |
|  31 | Accounting for data movement between cold and hot storage classes is currently in planning stages.                                                                         |

# Video

[![Video thumbnail](https://img.youtube.com/vi/xM37evX7BCs/hqdefault.jpg)](https://www.youtube.com/watch?v=xM37evX7BCs)

[Watch on YouTube](https://www.youtube.com/watch?v=xM37evX7BCs)
