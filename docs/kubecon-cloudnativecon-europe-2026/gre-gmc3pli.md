---
layout: default
title: Kubernetes Data Protection WG Intro & Deep Dive - Dave Smith-Uchida, Veeam
nav_order: 192
parent: Kubecon Cloudnativecon Europe 2026
type: Video Note
description:
  The Kubernetes Data Protection Working Group session, led by Dave Smith
  and Shingyang, provided an in-depth overview of ongoing efforts to improve backup
  and restore capabilities for stateful workloads in Kubernetes. The group was formed
  to...
resource: https://www.youtube.com/watch?v=grE_GMC3PlI
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

The Kubernetes Data Protection Working Group session, led by Dave Smith and Shingyang, provided an in-depth overview of ongoing efforts to improve backup and restore capabilities for stateful workloads in Kubernetes.
The group was formed to address limitations in day-two operations, such as data protection, and is supported by multiple companies.
Key topics included the backup and restore workflows, the role of the Cozy project in standardizing object storage integration, and new features like consistent group snapshots and change block tracking, both targeting the Kubernetes 1.36 release.
The session also discussed challenges in backing up applications managed by operators, emphasizing the need to understand resource dependencies, standardize quiescing and data protection operations, and handle complex scenarios involving multiple operators.
The group is developing a white paper on best practices and invites community participation to further advance Kubernetes data protection solutions.

# Main Points

|   # | Main point                                                                                                                                                          |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Introduction of speakers: Dave Smith (BH, Kubernetes backup/recovery) and Shingyang (VMware by Broadcom, co-chair of Kubernetes SIG Storage and Data Protection WG) |
|   2 | Agenda: working group background, involved companies, ongoing projects, white paper, and how to get involved                                                        |
|   3 | Kubernetes day one operations for stateful workloads are well supported; day two operations (like data protection) are limited                                      |
|   4 | Working group formed to improve data protection for Kubernetes stateful workloads                                                                                   |
|   5 | Backup workflow requires backing up Kubernetes metadata and persistent volume data                                                                                  |
|   6 | Two backup methods: native data dump (e.g., mysqldump) or controller-coordinated volume snapshot                                                                    |
|   7 | Application should be quiesced before snapshot for consistency                                                                                                      |
|   8 | Both metadata and data exported to a backup repository                                                                                                              |
|   9 | Cozy project provides standard APIs for provisioning object storage buckets as backup repositories                                                                  |
|  10 | Cozy components: controller, sidecar, driver; supports object storage backends                                                                                      |
|  11 | Cozy moving to v1alpha2 in Kubernetes 1.36; supports multiple bucket claims, new access modes, and data types                                                       |
|  12 | Bucket claim = user request; bucket = physical storage; bucket class = admin-defined type; one-to-one binding                                                       |
|  13 | Consistent group snapshot feature allows crash-consistent snapshots of multiple volumes; targeting GA in Kubernetes 1.36                                            |
|  14 | New APIs and gRPC interfaces for volume group snapshot operations                                                                                                   |
|  15 | Change block tracking enables incremental backups by identifying changed blocks between snapshots; targeting beta in Kubernetes 1.36                                |
|  16 | White paper: first edition covers why/when to back up Kubernetes; second edition focuses on best practices for admins and developers                                |
|  17 | Operators manage applications via custom resources; challenges include resource creation order, resource hierarchy, and backup/restore orchestration                |
|  18 | Importance of owner references for resource relationships                                                                                                           |
|  19 | Need for standardized operator quiesce and data protection operations                                                                                               |
|  20 | Complex scenarios with operators calling other opera                                                                                                                |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=grE_GMC3PlI)
