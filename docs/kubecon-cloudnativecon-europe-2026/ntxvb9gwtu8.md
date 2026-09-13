---
layout: default
title:
  "Project Lightning Talk: CNCF Sandbox Project K8Up Under The Hood - Aarno Aukia,
  Maintainer"
nav_order: 255
parent: Kubecon Cloudnativecon Europe 2026
type: Video Note
description:
  The speaker, a maintainer of the KUP CNCF sandbox project, discusses
  the evolution of Kubernetes from primarily hosting stateless applications to supporting
  critical workloads with important data, highlighting real-world incidents where
  ina...
resource: https://www.youtube.com/watch?v=NtXvB9gWTu8
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

The speaker, a maintainer of the KUP CNCF sandbox project, discusses the evolution of Kubernetes from primarily hosting stateless applications to supporting critical workloads with important data, highlighting real-world incidents where inadequate data distribution led to significant outages.
To address challenges in backup and restore processes—such as determining what data to back up and how often—the team developed KAP, a backup-as-a-service operator launched in 2018.
Unlike traditional infrastructure-based backup solutions, KAP empowers application users to define their own backup requirements, schedules, and security needs using Kubernetes-native CRDs, with all configurations managed via GitOps practices.
The tool leverages the open-source backup utility restic for encrypted, flexible storage and allows users to both back up and restore stateful applications independently.
The project, introduced at KubeCon Barcelona 2019, invites contributors from various backgrounds to join their efforts toward incubation.

# Main Points

|   # | Main point                                                                                                                                |
| --: | ----------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Maintainer of the KUP CNCF sandbox project                                                                                                |
|   2 | Started using Kubernetes in late 2015, initially for stateless apps                                                                       |
|   3 | Increasing use of Kubernetes for important workloads with critical data                                                                   |
|   4 | Risks exist even with distributed nodes and replicas (e.g., racks stacked together, availability zones misconfigured)                     |
|   5 | Real-world incidents where data loss or downtime occurred due to poor distribution or accidents                                           |
|   6 | Importance of making backups to protect data                                                                                              |
|   7 | Developed KAP, the backup operator, in 2018                                                                                               |
|   8 | Existing backup operators mostly focused on infrastructure-level backups                                                                  |
|   9 | Problems with infrastructure-level backups: operators may not know which data to back up or how often, and must handle restores for users |
|  10 | KAP provides backup as a service, allowing cluster users to define backup needs (what, how often, where, security requirements)           |
|  11 | Application owners best understand their backup requirements                                                                              |
|  12 | Emphasis on GitOps: configuration stored in Git repositories, synced with clusters                                                        |
|  13 | Uses open source backup tool restic for backups and encryption                                                                            |
|  14 | Kubernetes-native approach: backups and restores managed via CRDs and Kubernetes primitives                                               |
|  15 | Users can schedule backups (e.g., nightly, weekly, monthly), define retention and pruning                                                 |
|  16 | Restic supports multiple storage backends (e.g., S3), with credentials managed as secrets                                                 |
|  17 | Supports backup and restore of stateful applications, either inside pods or via new pods/services                                         |
|  18 | Users can list and restore backups themselves using Kubernetes CRDs                                                                       |
|  19 | KAP launched at KubeCon Barcelona 2019                                                                                                    |
|  20 | Project is still in CNCF sandbox, seeking contributors (developers, writers, managers)                                                    |
|  21 | Invitation to connect via Slack or at the project pavilion at KubeCon                                                                     |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=NtXvB9gWTu8)
