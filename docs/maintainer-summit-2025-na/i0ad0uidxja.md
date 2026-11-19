---
layout: default
title: "State of the Union on Disaster Recovery - Raffaele Spazzoli & Rafael Brito"
nav_order: 20
parent: "Maintainer Summit 2025 - NA"
type: Video Note
description: "This presentation by Rafael Espi and Rafael from the CNCF Operational Resilience Tag outlines the state of disaster recovery (DR) in cloud-native environments, emphasizing that DR is an application..."
resource: "https://www.youtube.com/watch?v=I0AD0uIdXJA"
tags:
  - maintainer-summit-2025-na
  - video
  - learning
status: stable
generated:
  by: process:yt-summarizer-okf
  at: 2026-11-16T17:23:58+00:00
---

# Summary

This presentation by Rafael Espi and Rafael from the CNCF Operational Resilience Tag outlines the state of disaster recovery (DR) in cloud-native environments, emphasizing that DR is an application-level discipline rather than solely a cluster concern.
The speakers define two critical metrics, Recovery Time Objective (RTO) and Recovery Point Objective (RPO), to categorize four primary DR archetypes: backup and restore, volume replication, transaction replication, and distributed stateful workloads.
While backup and restore rely on storage capabilities, the latter approaches require robust east-west network communication between clusters, necessitating standardized solutions for global load balancing and inter-cluster connectivity.
The talk highlights significant gaps in the CNCF landscape, noting that while projects like KubeGateway exist for DNS-based load balancing, there is a lack of standardization for anycast-based global load balancers and a unified CSI specification for volume replication, which currently forces reliance on proprietary vendor extensions.
To address these challenges, the presenters issue calls to action for the community to adopt change block tracking in CSI, standardize volume replication interfaces, and develop middleware-agnostic orchestrators to enable scalable, storage-agnostic disaster recovery strategies across diverse workloads.

# Main Points

|   # | Main point                                                                                                                                                                                           |
| --: | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Disaster recovery is a discipline focused on restoring applications, requiring attention from developers and architects rather than just platform engineering.                                       |
|   2 | Key metrics include Recovery Time Objective (RTO), which measures downtime tolerance, and Recovery Point Objective (RPO), which measures acceptable data loss.                                       |
|   3 | Lower RTO and RPO values require more expensive solutions, involving higher cognitive, cloud, or operational costs.                                                                                  |
|   4 | One size does not fit all; different applications require different disaster recovery strategies based on their specific SLOs.                                                                       |
|   5 | Backup and restore is an active-passive approach where RPO depends on backup frequency and RTO can take hours depending on data size.                                                                |
|   6 | Volume replication relies on the storage subsystem for data synchronization, offering zero RPO for synchronous replication and variable RPO for asynchronous.                                        |
|   7 | Transaction replication uses messaging buses or middleware to replicate transactions, achieving zero RPO with RTO measured in minutes.                                                               |
|   8 | Distributed stateful workloads enable true active-active architectures with strong consistency, eliminating the need for traditional failover procedures.                                            |
|   9 | Storage-oriented approaches like backup and volume replication require specific storage capabilities, while networking-oriented approaches require east-west communication between clusters.         |
|  10 | A global load balancer is essential for all approaches to direct traffic to the active or passive cluster based on health checks and policies.                                                       |
|  11 | Current CNCF projects like KubeGateway support DNS-based global load balancing, but there is a gap in projects supporting IPv4 or IPv6 anycast-based load balancing.                                 |
|  12 | East-west network paths lack standardization in the CNI specification, forcing reliance on specific CNI implementations like Cilium or Calico for multi-cluster connectivity.                        |
|  13 | Change block tracking is now part of the CSI specification to enable scalable backups by transferring only differential data, but adoption by CSI implementers remains low.                          |
|  14 | Volume replication for workloads like virtual machines lacks a standard CSI specification, leading to proprietary vendor extensions that prevent storage-agnostic disaster recovery orchestration.   |
|  15 | Database operators for primary-secondary replication exist but use different syntaxes, creating a need for a standardized subresource to define active or passive states across different databases. |
|  16 | Highly available distributed workloads can self-reorganize during failures, acting as high availability events rather than requiring manual disaster recovery procedures.                            |
|  17 | The CNCF Tag Operational Resilience encourages contributions to projects like KubeGateway, CSI extensions for volume replication, and middleware-agnostic orchestrators.                             |
|  18 | Volume snapshots can provide an RPO of approximately 15 minutes but are generally too slow for workloads requiring faster recovery times.                                                            |
|  19 | The community needs to increase awareness and adoption of existing CNCF projects to improve disaster recovery capabilities across the cloud native landscape.                                        |

# Video

[![Video thumbnail](https://img.youtube.com/vi/I0AD0uIdXJA/hqdefault.jpg)](https://www.youtube.com/watch?v=I0AD0uIdXJA)

[Watch on YouTube](https://www.youtube.com/watch?v=I0AD0uIdXJA)
