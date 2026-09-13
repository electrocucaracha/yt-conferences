---
type: Video Note
title: "Kubernetes SIG Storage: Intro & Deep Dive - Xing Yang, VMware by Broadcom & Jan Šafránek, Red Hat"
description: "The Kubernetes SIG Storage session, led by Shinang and Yan, provided an overview of the group's responsibilities, including maintaining storage-related APIs, volume plugins, and the Container Storage Interface (CSI). The presenters detailed..."
resource: https://www.youtube.com/watch?v=p17X_VnlpiY
tags: ["kubecon-cloudnativecon-europe-2026", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

The Kubernetes SIG Storage session, led by Shinang and Yan, provided an overview of the group's responsibilities, including maintaining storage-related APIs, volume plugins, and the Container Storage Interface (CSI).
The presenters detailed key features introduced in Kubernetes 1.35, such as improved handling of service account tokens for CSI drivers, mutable volume attach limits, mutable persistent volume node affinity, and integration of volume attach limits with the cluster autoscaler.
For the upcoming 1.36 release, they highlighted the graduation of features like service account tokens for secrets, mutable volume attach limits, and volume group snapshots, as well as changes to SELinux labeling and the introduction of change block tracking for incremental backups.
Additional updates include the removal of the legacy gitRepo volume plugin, enhancements to the Container Object Storage Interface, and a new feature to report when a persistent volume claim was last used.
The session concluded with information on ongoing design efforts, such as expanding volumes in StatefulSets, consolidating CSI sidecars, and improving volume health reporting, along with guidance on how to participate in SIG Storage activities.
# Main Points

|   # | Main point                                                                                                               |
| --: | ------------------------------------------------------------------------------------------------------------------------ |
|   1 | Introduction by Shinang (VMware by Broadcom, co-chair) and Yan Shafa Franek (Red Hat, co-tech lead) of SIG Storage       |
|   2 | SIG Storage maintains Kubernetes storage APIs (persistent volumes, claims, storage classes, volume snapshots)            |
|   3 | Maintains code for dynamic provisioning, volume plugins (e.g., NFS, iSCSI), projected volumes (secrets, config maps)     |
|   4 | Designed Container Storage Interface (CSI) for storage vendors to integrate with Kubernetes                              |
|   5 | Maintains CSI sidecars and Container Object Storage Interface (COSI)                                                     |
|   6 | Kubernetes 1.35 release:                                                                                                 |
|   7 | Introduced feature for CSI drivers to opt-in for service account tokens in secrets field (beta)                          |
|   8 | Enabled mutable volume attach limits by default (beta)                                                                   |
|   9 | Introduced alpha feature: mutable persistent volume node affinity                                                        |
|  10 | Integrated CSI volume attach limits with cluster autoscaler (alpha)                                                      |
|  11 | Kubernetes 1.36 release:                                                                                                 |
|  12 | Graduating service account tokens for secrets and mutable volume attach limits to GA                                     |
|  13 | Volume group snapshots graduating to GA (crash-consistent snapshots of multiple PVCs)                                    |
|  14 | SELinux labeling with mount options: improves efficiency, breaks privileged/unprivileged pod sharing (opt-out available) |
|  15 | Graduating change block tracking to beta (enables incremental backup, new external snapshot metadata sidecar)            |
|  16 | Removing gitRepo volume plugin (disabled in 1.36)                                                                        |
|  17 | Evolving COSI to v1alpha2 (multiple buckets, simplified RBAC)                                                            |
|  18 | Reporting last-used timestamp for PVCs (better UI/UX)                                                                    |
|  19 | Ongoing design/prototyping:                                                                                              |
|  20 | Expanding volumes in StatefulSets                                                                                        |
|  21 | Combining CSI sidecars into one repository/binary                                                                        |
|  22 | Improving volume health reporting and APIs                                                                               |
|  23 | How to get involved:                                                                                                     |
|  24 | SIG Storage landing page, bi-weekly meetings, subproject meetings, mailing list, Slack channels                          |
|  25 | Slides and materials will be uploaded after the session                                                                  |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=p17X_VnlpiY)