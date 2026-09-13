---
layout: default
title:
  "1000 Services, 1 Year, 0 Downtime: Airbnb’s Zonal Cluster Migration - Sunny
  Beatteay, Airbnb"
nav_order: 3
parent: Kubecon Cloudnativecon Europe 2026
type: Video Note
description:
  Sunny B presents a case study on Airbnb’s largest zonal cluster migration,
  detailing the transition of over 1,000 services from a regional to a zonal Kubernetes
  architecture within a year and achieving zero downtime. Initially, Airbnb used...
resource: https://www.youtube.com/watch?v=N3NTyUeSlaA
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

Sunny B presents a case study on Airbnb’s largest zonal cluster migration, detailing the transition of over 1,000 services from a regional to a zonal Kubernetes architecture within a year and achieving zero downtime.
Initially, Airbnb used regional clusters for their simplicity and high availability, but as the system scaled, the need for improved incident recovery and reduced blast radius led to the adoption of zonal clusters.
The migration required significant technical and organizational changes, including refactoring deployment tooling, introducing new abstractions called "cells" and "cell sets," and automating much of the migration process to minimize disruption for app developers.
The team conducted migrations in phases, prioritized communication and support, and addressed unique requirements for critical services, ultimately migrating 95% of compute to cells and successfully performing live zonal traffic shifts.
The project also laid the groundwork for future multi-regional deployments and ongoing improvements in developer tooling and automation.

# Main Points

|   # | Main point                                                                                                                                                               |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   1 | Presenter: Sunny B, presenting Airbnb's largest zonal cluster migration—1,000 services, 1 year, zero downtime.                                                           |
|   2 | Migration was from regional to zonal Kubernetes clusters.                                                                                                                |
|   3 | Regional clusters: one control plane across multiple AZs, easier management, high availability, AWS-recommended.                                                         |
|   4 | Zonal clusters: separate clusters per AZ, more complexity, sharded workloads, multiple control planes.                                                                   |
|   5 | Airbnb originally used regional clusters (2018–2023), scaling to 1,000 services, 5,000 namespaces, 1,200 jobs, 3,500 deployments, 36,000 pods.                           |
|   6 | Invested in incident prevention: Airdev workspaces, canary frameworks, pre-production testing.                                                                           |
|   7 | Main reason for migration: improve incident recovery, reduce blast radius, enable fast zonal failover.                                                                   |
|   8 | Regional clusters: incidents can affect entire region; zonal clusters limit impact to one AZ and allow traffic shifting.                                                 |
|   9 | Migration challenges: technical (deployment system assumptions, OneTouch abstraction, hardcoded contexts), organizational (changing developer workflows, communication). |
|  10 | Introduced new abstractions: "cell" (self-contained unit per AZ) and "cell set" (group of cells in a region).                                                            |
|  11 | Refactored deployment tooling and config language to support cell/cell set, enabling seamless developer experience.                                                      |
|  12 | Automated migration process integrated into CD platform; migration occurs during normal deployments.                                                                     |
|  13 | Migration process: prepare (scale up), deploy to cells, scale down regional, finalize.                                                                                   |
|  14 | Communication: roadshow, documentation, migration schedule, support via Slack threads.                                                                                   |
|  15 | Migration executed in batches; automated PRs for config changes; phased migration (non-prod, canary, prod).                                                              |
|  16 | Special handling for critical/complex services ("omega" migrations), including node pool labeling and resource upgrades.                                                 |
|  17 | By June, 50% migrated; by year-end, 95% of compute in cells, 1,000+ services migrated, 3,000 PRs, zero downtime.                                                         |
|  18 | Successfully performed zonal traffic shift in under 10 minutes.                                                                                                          |
|  19 | Ongoing improvements: better debugging                                                                                                                                   |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=N3NTyUeSlaA)
