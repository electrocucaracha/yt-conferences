---
layout: default
title: "Longhorn: Intro, Deep Dive and Q&A - Shuo Wu, SUSE"
nav_order: 157
parent: Kubecon Cloudnativecon North America 2025
type: Video Note
description: Here is a summary of the video transcript in 3-5 sentences.
resource: https://www.youtube.com/watch?v=NhllqYL0eBg
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

Here is a summary of the video transcript in 3-5 sentences: Longhorn is a cloud-native distributed block storage solution for Kubernetes that has been adopted by the community over the past six years.
The project has recently released version 2 (V2) of its data engine, which offers improved performance and scalability compared to the previous version.
V2 also introduces features such as incremental backup, disaster recovery, and support for NVMe over fabric protocol, making it a more powerful storage solution for Kubernetes clusters.
Longhorn's architecture is designed with reliability, usability, and maintainability in mind, and the project continues to evolve with new features and improvements.
The team plans to release additional features in upcoming versions, including support for file systems and improved snapshot management.

# Main Points

|   # | Main point                                                                                                                 |
| --: | -------------------------------------------------------------------------------------------------------------------------- |
|   1 | Longhorn is a cloud-native distributed block storage for Kubernetes.                                                       |
|   2 | It's an open-source project owned by CNCF.                                                                                 |
|   3 | Longhorn supports multiple operating systems and use cases (AI, telecommunication, data visualization, observability).     |
|   4 | The project has a stable release cadence with four months of feature releases and two months of patch releases.            |
|   5 | Quality assurance mechanisms include regular end-to-end tests, negative tests, and scanning for CVE issues.                |
|   6 | Longhorn's design principles are reliability, usability, and maintainability.                                              |
|   7 | The control plane architecture consists of a Kubernetes CSI plug-in, Longhorn manager, and underlying components.          |
|   8 | Data plane architecture involves block devices, SPK, and TGD.                                                              |
|   9 | Longhorn supports multiple storage topologies and has data protection features (replication, encryption, snapshot backup). |
|  10 | V2 data engine is a next-generation data engine based on SPK, with improved IO performance and latency reduction.          |
|  11 | Longhorn can export volumes to external storage systems using the CSI interface.                                           |
|  12 | Snapshots are supported, but excessive use can lead to space issues; periodic clean-up is recommended.                     |
|  13 | Read-write mini feature has stability improvements planned, including NFSA stability.                                      |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=NhllqYL0eBg)
