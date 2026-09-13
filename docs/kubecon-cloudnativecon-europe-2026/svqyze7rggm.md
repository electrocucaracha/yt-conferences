---
type: Video Note
title: "Longhorn: Intro, Deep Dive and Q&A - David Ko & Divya Mohan, SUSE"
description: "David Co, engineering director at Susa, and Da, the new community manager for Longhorn, provided an update on the Longhorn project during a QCON session. They discussed Longhorn’s architecture as a cloud-native distributed block storage sol..."
resource: https://www.youtube.com/watch?v=sVQyZe7rggM
tags: ["kubecon-cloudnativecon-europe-2026", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

David Co, engineering director at Susa, and Da, the new community manager for Longhorn, provided an update on the Longhorn project during a QCON session.
They discussed Longhorn’s architecture as a cloud-native distributed block storage solution built for Kubernetes, highlighting its high availability, efficiency, and compatibility with various environments and operating systems.
The session covered recent and upcoming releases, including the introduction of a new high-performance data engine (V2) based on SPDK, improvements in replica rebuilding, performance tuning, and enhanced automation and monitoring features.
The team emphasized their commitment to regular release cycles, extensive testing, and feature parity between V1 and V2, with V2 moving towards general availability in version 1.12.
Da also outlined efforts to grow the community, increase non-Susa contributions, and move Longhorn towards CNCF graduation by building a more inclusive governance structure and encouraging user engagement through community meetings, social media, and the adopters file.
The presenters invited further participation and feedback to ensure Longhorn’s continued growth and relevance.
# Main Points

|   # | Main point                                                                                                                                                                                                                         |
| --: | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | David Co, Engineering Director at Susa, provided the annual Longhorn update.                                                                                                                                                       |
|   2 | Da has recently taken over Longhorn community management.                                                                                                                                                                          |
|   3 | Agenda included Longhorn overview, project and release updates, new release cadence, data engines, v2 status, performance, 1.11 features, and 1.12 roadmap.                                                                        |
|   4 | Longhorn is a cloud-native distributed block storage solution, highly available, Kubernetes-native, and deployment-agnostic.                                                                                                       |
|   5 | Architecture includes control plane (local managers), instance manager, engine, and replicas.                                                                                                                                      |
|   6 | Supports CSI spec, user interface, RESTful API, and CR manipulation via kubectl and longhorn CLI.                                                                                                                                  |
|   7 | Project is stable and growing: over 2,000 nodes, 35% yearly node growth, 50% cluster growth, supports multiple OS including immutable systems like Talos.                                                                          |
|   8 | Community contributions managed via GitHub; sprints every two weeks; spring releases for early feedback.                                                                                                                           |
|   9 | Release cadence: minor releases in January, May, September; two months patch support per minor release.                                                                                                                            |
|  10 | Data engine v1 is in-house; v2 is based on SPDK for higher performance, supports NVMe-oF, and aims for resource sharing like v1.                                                                                                   |
|  11 | v2 performance testing shows significant improvements, especially with more CPU cores.                                                                                                                                             |
|  12 | 1.11 release highlights: v2 technical preview, feature catch-up with v1, over 600 end-to-end test cases, improved test coverage.                                                                                                   |
|  13 | Key 1.11 features: adjustable Uro queue size, faster parallel replica rebuilding, improved replica scheduling, storage cluster topology, enhanced monitoring, dedicated storage network, new access mode contributed by community. |
|  14 | 1.12 roadmap: v2 GA, live upgrades, IPv6 support, engine migration, resource cleanup, faster volume creation, resource resize, offline replica rebuild, sharding and erasure coding.                                               |
|  15 | Community update: aiming for CNCF graduation, increasing non-Susa contributors, over 50% non-Susa code in 1.11, monthly community meetings, recordings on YouTube.                                                                 |
|  16 | Encouragement to join meetings, contribute, and add production use to adopters fi                                                                                                                                                  |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=sVQyZe7rggM)