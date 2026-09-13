---
layout: default
title:
  "Rook: Intro and... Travis Nielsen, Madhu Rajanna, Artem Torubarov, Deepika
  Upadhyay & Sebastien Han"
nav_order: 284
parent: Kubecon Cloudnativecon Europe 2025
type: Video Note
description:
  Rook is an open-source Kubernetes operator that automates self-storage
  management, providing cloud-native management of storage. It uses SE (Sephira) as
  its underlying storage solution, which is a distributed file system with features
  like...
resource: https://www.youtube.com/watch?v=xGywrHPAMms
tags:
  - kubecon-cloudnativecon-europe-2025
  - video
  - learning
status: stable
generated:
  by: process:yt-conferences-okf
  at: 2026-09-12 00:00:00+00:00
---

# Summary

Rook is an open-source Kubernetes operator that automates self-storage management, providing cloud-native management of storage.
It uses SE (Sephira) as its underlying storage solution, which is a distributed file system with features like replication, thin provisioning, and performance optimization.
Rook supports various storage classes, including block storage, shared file systems, S3-like object storage, and more.
The operator allows for flexible deployment options, including cloud provider environments, on-premises data centers, and hybrid multi-cloud environments.
With Rook, users can enjoy scalability, high availability, and performance, while also ensuring data security and protection through features like replication, encryption, and backup capabilities.

# Main Points

|   # | Main point                                                                                                         |
| --: | ------------------------------------------------------------------------------------------------------------------ |
|   1 | Rook is a Kubernetes operator that automates self-storage.                                                         |
|   2 | SE (Sephira) is an open-source distributed storage solution used with Rook.                                        |
|   3 | Rook has three layers: Rook, CSI, and SE.                                                                          |
|   4 | SE provides block storage, shared file systems, S3-like object storage, and more.                                  |
|   5 | Rook supports cloud providers, on-premises data centers, and hybrid environments.                                  |
|   6 | New features in Rook include mirroring, improved object storage, and CSI operator enabled by default.              |
|   7 | CSI driver has three projects: FFS, RBD, and NFS.                                                                  |
|   8 | CSI driver supports thin provisioning, RWX block mode, and more.                                                   |
|   9 | Object store custom resource allows users to create buckets with desired configuration.                            |
|  10 | Performance penalty for running Rook compared to local storage is due to network performance for write operations. |
|  11 | Seph performs better with many clients in a large cluster.                                                         |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=xGywrHPAMms)
