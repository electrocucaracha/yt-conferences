---
layout: default
title: Kubernetes Data Protection WG Intro & Deep Dive - Dave Smith-Uchida, Veeam
nav_order: 138
parent: Kubecon Cloudnativecon North America 2025
type: Video Note
description:
  The session, led by Shing Yang and Dave Smith, provided an update on
  the Kubernetes Data Protection Working Group, detailing its motivation, current
  projects, and ongoing white paper. The group, sponsored by SIG Storage and SIG Apps,
  address.
resource: https://www.youtube.com/watch?v=dKl_OaNlpOA
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

The session, led by Shing Yang and Dave Smith, provided an update on the Kubernetes Data Protection Working Group, detailing its motivation, current projects, and ongoing white paper.
The group, sponsored by SIG Storage and SIG Apps, addresses the gap in Kubernetes’ support for day two operations like data protection, focusing on backing up both Kubernetes metadata and persistent volume data.
Recent advancements include features such as consistent group snapshots, change block tracking (CBT) for incremental backups, and a new snapshot metadata service, all aimed at improving backup and restore workflows.
The forthcoming white paper outlines best practices for data protection, discussing strategies like backup and restore, replication (cold and hot copies), and the importance of balancing recovery objectives (RTO/RPO) with cost and application impact.
Special attention is given to consistency strategies and the unique challenges posed by Kubernetes operators, emphasizing the need for better APIs and practices to ensure reliable backups and restores in complex environments.
The group encourages community involvement through meetings, mailing lists, and contributions to the white paper.

# Main Points

|   # | Main point                                                                                                                                                                                 |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   1 | Session on the Data Protection Working Group in Kubernetes, led by Shing Yang and Dave Smith                                                                                               |
|   2 | Agenda: working group update, involved parties, motivation, ongoing projects, white paper, and how to get involved                                                                         |
|   3 | White paper on data protection workflows in Kubernetes created; links to previous talks provided                                                                                           |
|   4 | Companies supporting the working group listed                                                                                                                                              |
|   5 | Kubernetes supports day one operations for stable workloads (persistent volumes, workload APIs)                                                                                            |
|   6 | Day two operations like data protection are limited; GitOps has limitations for stateful workloads                                                                                         |
|   7 | Data protection working group formed to address these gaps; sponsored by SIG Storage and SIG Apps                                                                                          |
|   8 | Backup workflow requires backing up Kubernetes metadata and persistent volume data                                                                                                         |
|   9 | Two volume backup approaches: native data dump (e.g., MySQL dump) or controller-coordinated snapshot                                                                                       |
|  10 | Application consistency requires quiescing before snapshot and unquiescing after                                                                                                           |
|  11 | Backup repository stores data and metadata                                                                                                                                                 |
|  12 | Existing Kubernetes components: Application CRD, VolumeSnapshot, volume mode conversion, consistent group snapshot, Container Object Storage Interface (COSI), change block tracking (CBT) |
|  13 | Restore workflow: import backup, restore metadata, restore PVC/PV, restore from native dump or snapshot, use volume populator                                                              |
|  14 | Change Block Tracking (CBT) feature introduced: APIs to identify changed blocks between snapshots, supports incremental backup, decouples backup from storage system                       |
|  15 | CBT uses snapshot metadata service, new CSI RPCs, and Kubernetes gRPC APIs                                                                                                                 |
|  16 | Recent CBT API change: base snapshot name replaced with base snapshot ID to avoid long-term retention                                                                                      |
|  17 | CBT project is alpha since Kubernetes 1.33; moving toward beta                                                                                                                             |
|  18 | White paper under construction on best practices for data protection; contributors needed                                                                                                  |
|  19 | Key terms: RTO (Recovery Time Objective), RPO (Recovery Point Objective)                                                                                                                   |
|  20 | Data protection strategies: stateless (low cost/impact), backup/restore (medium), replication with cold copy (low RTO, higher c                                                            |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=dKl_OaNlpOA)
