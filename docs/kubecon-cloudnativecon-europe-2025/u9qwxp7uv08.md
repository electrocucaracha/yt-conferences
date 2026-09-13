---
type: Video Note
title: "Kubernetes Backup Legitimized: CSI Changed Block Tracking Has Arrived- M. Lavi, C. Braganza, X. Yang"
description: "Here is a summary of the video transcript in 3-5 sentences."
resource: https://www.youtube.com/watch?v=U9qwxp7Uv08
tags: ["kubecon-cloudnativecon-europe-2025", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

Here is a summary of the video transcript in 3-5 sentences: Mark Lobby from VMware by Broadcom introduces the change block tracking (CBT) feature for Kubernetes, which allows for more efficient backup and recovery processes by identifying changes between two volume snapshots.
CBT is a critical unblocker for Kubernetes adoption, as it addresses the lack of change block tracking in traditional storage systems.
The feature has been implemented in the CSI specification and is now ready to ship with Kubernetes 13.3 alpha APIs, along with a new snapshot metadata service and two new CSI RPCs: Get Metadata Allocated and Get Metadata Delta.
# Main Points

|   # | Main point                                                                                                                                                                                                      |
| --: | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Change block tracking (CBT) is a feature that allows for efficient backup and recovery of data in Kubernetes.                                                                                                   |
|   2 | CBT is motivated by the need to measure RPO and RTO for backups and disaster recovery.                                                                                                                          |
|   3 | The feature is implemented in the CSI specification and is now ready to ship with Kubernetes 1.33 alpha APIs.                                                                                                   |
|   4 | The architecture involves a new snapshot metadata service, two new CSI RPCs (Get metadata allocated and Get metadata delta), and a sidecar that intercepts and protects the CSI driver from Kubernetes clients. |
|   5 | The backup software uses the Kubernetes snapshot metadata API to retrieve snapshot metadata, which is then used to stream data back through the CSI driver.                                                     |
|   6 | The feature supports block volume only, with file volume support out of scope for now.                                                                                                                          |
|   7 | The CSI hostpath driver is used as a test tool to implement and test this feature.                                                                                                                              |
|   8 | A demonstration shows how to create a PVC, mount it in a block device, add data, take a snapshot, and then use the Kubernetes snapshot metadata API to retrieve the allocated blocks or change blocks.          |
|   9 | The iterator package provides a mechanism for backup vendors to use this feature without having to modify their code.                                                                                           |
|  10 | CSI driver vendors need to open a service, generate CI certificates, and implement the CBT spec.                                                                                                                |
|  11 | Snapshots are useful for achieving crash consistency at the lowest level, but may not be sufficient for application-level consistency.                                                                          |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=U9qwxp7Uv08)