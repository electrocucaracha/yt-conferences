---
layout: default
title: etcd 3.6 Updates and 3.7 Roadmap - Arka Saha, Broadcom & Josh Berkus, Red Hat
nav_order: 408
parent: Kubecon Cloudnativecon Europe 2026
type: Video Note
description:
  In this SCD maintainer session, Josh Burkus and Shaha provided updates
  on recent and upcoming developments in the SCD project, a key component of Kubernetes.
  They discussed the recent security release addressing authorization issues with
  SC...
resource: https://www.youtube.com/watch?v=YK2Q0hz962o
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

In this SCD maintainer session, Josh Burkus and Shaha provided updates on recent and upcoming developments in the SCD project, a key component of Kubernetes.
They discussed the recent security release addressing authorization issues with SCD auth, and highlighted the major features of version 3.6, including officially supported downgrade capabilities and the transition from the v2 to v3 data store for improved reliability and performance.
The roadmap for 3.7 includes features like chunked data retrieval (CD range), significant cleanup of gRPC and Protobuff dependencies, and the removal of experimental features, though some proposed performance enhancements may be deferred without additional contributors.
The team is also overhauling documentation for better usability and announced changes to support windows, urging users to upgrade from older versions.
Demonstrations showcased the SCD operator's new capabilities, such as certificate management and cluster upgrades, and the session concluded with a call for new contributors to join various subprojects and a Q&A addressing multi-tenancy and resource limits in Kubernetes environments.

# Main Points

|   # | Main point                                                                                                                                       |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------------ |
|   1 | Introduction of session leaders: Josh Burkus (CD documentation approver) and Shaha (CD operator reviewer).                                       |
|   2 | Agenda: Updates on 3.6 release, 3.7 roadmap, security news, and call for contributors.                                                           |
|   3 | Recent security release addressing authorization issues in CD auth for non-Kubernetes use cases; patches released for all supported versions.    |
|   4 | 3.6 features:                                                                                                                                    |
|   5 | Officially supported downgrade capability (one minor version at a time, e.g., 3.6 to 3.5).                                                       |
|   6 | Downgrade process includes validation, migration, and deactivation of incompatible features.                                                     |
|   7 | Transition from v2 store to v3 store as the source of truth, improving reliability and performance.                                              |
|   8 | Snapshotting improved from every 100,000 writes to every 10,000 writes or on membership change.                                                  |
|   9 | Fixes for upgrade issues (e.g., too many learners, old snapshot data).                                                                           |
|  10 | Adoption of Kubernetes-style feature flags and endpoints (livez, readyz).                                                                        |
|  11 | 3.7 roadmap:                                                                                                                                     |
|  12 | Implementation of CD range for chunked data queries (KEP 5967).                                                                                  |
|  13 | Cleanup of gRPC and Protobuff dependencies; removal of outdated/experimental features.                                                           |
|  14 | Need to implement a new client-side load balancer.                                                                                               |
|  15 | Two performance features investigated (raft async writes, configurable bolt rebalance threshold) but unlikely for 3.7 without more contributors. |
|  16 | Documentation overhaul planned, possibly removing versioned docs.                                                                                |
|  17 | Support window updates:                                                                                                                          |
|  18 | CD 3.4 support ending in two months.                                                                                                             |
|  19 | 3.5 supported until at least next May.                                                                                                           |
|  20 | Plans to publish support timelines and release new versions annually.                                                                            |
|  21 | Adoption of Go workspace; ongoing automation and vulnerability script updates.                                                                   |
|  22 | Official CD images now available on Kubernetes registry (from Kubernetes 1.35+).                                                                 |
|  23 | CD operator updates:                                                                                                                             |
|  24 | 0.2.0 release adds certificate and upgrade support.                                                                                              |
|  25 | Roadmap includes recovery/backup and Helm chart release.                                                                                         |
|  26 | Demo of cluster creation with auto and cert-manager TLS providers.                                                                               |
|  27 | Call for contributors in areas: performance engineering, Protobuff overhaul, raft co                                                             |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=YK2Q0hz962o)
