---
type: Video Note
title: "Snapshots Gone Wild: Taming Multi-PVC Chaos with VolumeGroupSna... Shubham Pampattiwar & Scott Seago"
description: "In this talk, Shuan Pampachar and Scott Sego from Red Hat discuss the challenges of backing up multi-volume stateful applications on Kubernetes, highlighting how traditional individual volume snapshots can lead to inconsistent and potential..."
resource: https://www.youtube.com/watch?v=pLmRkRO6O6E
tags: ["kubecon-cloudnativecon-europe-2026", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

In this talk, Shuan Pampachar and Scott Sego from Red Hat discuss the challenges of backing up multi-volume stateful applications on Kubernetes, highlighting how traditional individual volume snapshots can lead to inconsistent and potentially corrupt backups due to non-atomic capture times.
They introduce the Kubernetes Volume Group Snapshot (VGS) API, which enables atomic, crash-consistent snapshots across multiple volumes with a single API call, ensuring all volumes are captured at the same instant.
The speakers explain how VGS support was integrated into the open-source backup tool Velero, allowing users to opt in simply by labeling their Persistent Volume Claims (PVCs), and describe the workflow, design decisions, and lessons learned from testing across different CSI drivers.
They share benchmark results showing that VGS not only improves consistency but also speeds up backups, especially as the number of volumes increases, and provide a practical blueprint for adopting VGS in production environments.
The session concludes with key takeaways: atomic snapshots are essential for multi-volume apps, VGS provides this capability, Velero makes it easy to use, VGS artifacts are transient by design, and thorough testing across storage drivers is crucial.
# Main Points

|   # | Main point                                                                                                                        |
| --: | --------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Multi-volume stateful application backups often fail due to inconsistent snapshots taken at different times.                      |
|   2 | Velero is an open-source Kubernetes backup, restore, and disaster recovery tool supporting multiple backup methods.               |
|   3 | Individual volume snapshots can lead to data inconsistency and application corruption on restore.                                 |
|   4 | Volume Group Snapshot (VGS) API enables atomic, crash-consistent snapshots across multiple volumes with a single API call.        |
|   5 | VGS was introduced via KEP 3476, promoted to beta in Kubernetes 1.32+, and is moving toward GA in 1.36.                           |
|   6 | VGS uses label selectors to group PVCs for atomic snapshotting.                                                                   |
|   7 | Crash consistency is achieved with VGS; application consistency requires coordination with app-specific hooks.                    |
|   8 | Velero integrates VGS as an opt-in feature using PVC labels; existing workflows remain unchanged for unlabelled PVCs.             |
|   9 | Velero’s backup workflow for VGS: group PVCs by label, create VGS via CSI plugin, delete VGS artifacts after snapshots are ready. |
|  10 | VGS in Velero is transient—used only during backup, then removed for portability and lifecycle management.                        |
|  11 | Volume policies are evaluated before grouping to handle PVCs on different storage backends.                                       |
|  12 | CSI driver behaviors vary; testing across multiple drivers is essential.                                                          |
|  13 | VGS provides crash consistency, fewer CSI calls, and all-or-nothing backups, but requires driver support and PVC labeling.        |
|  14 | Performance: VGS is 1.3–1.6x faster than individual snapshots; eliminates inconsistency window.                                   |
|  15 | Prerequisites for VGS: Kubernetes 1.32+, VGS CRDs, compatible CSI driver, default snapshot class, Velero 1.17+.                   |
|  16 | Adoption steps: label PVCs, ensure prerequisites, and use standard Velero CLI.                                                    |
|  17 | Key takeaways: use VGS for multi-volume apps, label PVCs, VGS is transient, test with multiple CSI drivers.                       |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=pLmRkRO6O6E)