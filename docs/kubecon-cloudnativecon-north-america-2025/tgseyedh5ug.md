---
layout: default
title:
  "Kubernetes SIG Storage: Intro & Deep Dive - Xing Yang, Michelle Au, Hemant
  Kumar"
nav_order: 141
parent: Kubecon Cloudnativecon North America 2025
type: Video Note
description:
  The session, led by members of SIG Storage from organizations like VMware,
  Google, and Red Hat, provided an overview of SIG Storage’s responsibilities in Kubernetes,
  including maintaining storage-related APIs, dynamic provisioning, volume p...
resource: https://www.youtube.com/watch?v=tGSEyEdh5ug
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

The session, led by members of SIG Storage from organizations like VMware, Google, and Red Hat, provided an overview of SIG Storage’s responsibilities in Kubernetes, including maintaining storage-related APIs, dynamic provisioning, volume plugins, and the Container Storage Interface (CSI).
The team highlighted key features introduced in Kubernetes releases 1.33 and 1.34, such as generic data populators for persistent volumes, improvements to volume expansion and resizing, volume attribute classes for easier modification of storage parameters, mutable volume attach limits, and enhancements to group snapshot capabilities.
Upcoming work in 1.35 and beyond includes security improvements for CSI drivers, further development of the Container Object Storage Interface (COSI), integration with cluster autoscaler for volume node limits, and the ability to mutate persistent volume node affinity.
The discussion also addressed ongoing efforts around volume health reporting, disaster recovery, replication, and automatic volume expansion, as well as community engagement opportunities.
Attendees asked questions about advanced CSI driver use cases, storage class recommendations for testing, data protection workflows, disaster recovery across clusters, and technical challenges with storage affinity and FUSE-based file systems, with SIG Storage encouraging participation and feedback through meetings and communication channels.

# Main Points

|   # | Main point                                                                                                                                |
| --: | ----------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | SIG Storage maintains Kubernetes storage APIs (PVCs, PVs, StorageClasses, VolumeSnapshots) and related code.                              |
|   2 | Maintains volume plugins (NFS, iSCSI), projected volumes (secrets, configmaps), and co-owns CSI and COI (Cozy) interfaces.                |
|   3 | CSI enables storage vendors to write drivers for Kubernetes; SIG Storage maintains CSI sidecars.                                          |
|   4 | COI (Cozy) provides APIs for object bucket provisioning similar to PVCs.                                                                  |
|   5 | Kubernetes 1.33:                                                                                                                          |
|   6 | Volume Populators feature went GA, allowing PVCs to be created from any data source via a new dataSourceRef field.                        |
|   7 | Always Honor PV Reclaim Policy moved to GA, preventing leaked volumes.                                                                    |
|   8 | Portworx CSI migration moved to GA.                                                                                                       |
|   9 | Secure Linux labeling for non-RWO pod volumes moved to beta.                                                                              |
|  10 | Mutable Volume Attach Limits introduced.                                                                                                  |
|  11 | Change Block Tracking (alpha) enables incremental backups.                                                                                |
|  12 | Storage Capacity Scoring (alpha) supports dynamic provisioning and replaces Volume Capacity Priority.                                     |
|  13 | GitRepo entry plugin disabled by default; removal planned for 1.39.                                                                       |
|  14 | Kubernetes 1.34:                                                                                                                          |
|  15 | Volume expansion failures can now be retried by reducing PVC size.                                                                        |
|  16 | Improved PVC resizing status reporting and bug fixes.                                                                                     |
|  17 | Volume Attribute Class (beta) allows changing volume attributes post-provisioning.                                                        |
|  18 | Mutable Volume Attach Limits (beta) enables dynamic attach limit reporting.                                                               |
|  19 | Volume Group Snapshot (beta2) supports consistent snapshots across multiple volumes.                                                      |
|  20 | Kubernetes 1.35 and beyond:                                                                                                               |
|  21 | Beta: CSI drivers can receive pod service account tokens via secrets field for improved security.                                         |
|  22 | Beta: Mutable Volume Attach Limits enabled by default.                                                                                    |
|  23 | Alpha: Cozy v1alpha2 adds RW access modes, multi-bucket support, and improved sidecar/controller security.                                |
|  24 | Alpha: CSI volume node limit support for cluster autoscaler.                                                                              |
|  25 | Alpha: Mutating PV node affinity for non-disruptive topology changes.                                                                     |
|  26 | Planned: Volume expansion via StatefulSet templates, consolidating CSI sidecars, improving volume health reporting, and discussing automa |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=tGSEyEdh5ug)
