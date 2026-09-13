---
layout: default
title: "Project Lightning Talk: What's New In Kubernetes Storage - Xing Yang"
nav_order: 242
parent: Kubecon Cloudnativecon North America 2025
type: Video Note
description:
  In this project lightning talk for SIG Storage, Shing Yang from VMware
  by Broadcom highlights recent developments and features. The team addressed the
  issue of recovering from resize failures, which previously left users unable to
  correct m...
resource: https://www.youtube.com/watch?v=JhMwxRfi7Ho
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

In this project lightning talk for SIG Storage, Shing Yang from VMware by Broadcom highlights recent developments and features.
The team addressed the issue of recovering from resize failures, which previously left users unable to correct mistaken volume expansions; this fix, now generally available in Kubernetes 1.34, allows users to adjust the requested size as long as it remains larger than the original.
Another new feature, volume attributes class, enables users to modify certain volume parameters, such as IOPS or throughput, after provisioning—something not possible with immutable storage class parameters; this feature is also now generally available.
Additionally, the team is working on consolidating multiple CSI sidecar containers into a single mono-repo to simplify releases and improve resource utilization, with the initial alpha targeted for Kubernetes 1.36.
The talk concludes with an invitation for community involvement and information about related sessions at KubeCon.

# Main Points

|   # | Main point                                                                                                                      |
| --: | ------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Shing Yang and Sad are co-chairs of SIG Storage; Michelle and Shing are tech leads.                                             |
|   2 | Many contributors are involved in SIG Storage projects.                                                                         |
|   3 | "Recover from resize failure" project addresses issues when volume expansion fails due to incorrect size input.                 |
|   4 | Previously, failed expansions could not be recovered because shrinking volumes was not supported.                               |
|   5 | The fix allows users to recover by entering a new, larger PVC size; shrinking is still not supported.                           |
|   6 | This feature is generally available (GA) in Kubernetes 1.34.                                                                    |
|   7 | "Volume attributes class" feature allows modification of certain volume parameters (e.g., IOPS, throughput) after provisioning. |
|   8 | Storage class parameters remain immutable, but volume attribute class names are mutable post-provisioning.                      |
|   9 | Users can switch between volume attribute classes (e.g., from silver to gold) to change volume options.                         |
|  10 | This feature is now GA.                                                                                                         |
|  11 | CSI sidecars are helper containers for volume operations in Kubernetes.                                                         |
|  12 | Multiple CSI sidecars exist, leading to release and resource utilization challenges.                                            |
|  13 | Plan to consolidate all CSI sidecars into a single mono repo.                                                                   |
|  14 | The consolidation proposal (KEP) was merged and targets alpha in Kubernetes 1.36.                                               |
|  15 | Next steps include implementation of the consolidated sidecar.                                                                  |
|  16 | Community involvement is encouraged; related sessions and events are available at KubeCon.                                      |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=JhMwxRfi7Ho)
