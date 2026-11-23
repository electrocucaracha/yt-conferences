---
layout: default
title: Engineering Reliable OpenStack Backups at Scale
nav_order: 39
parent: OpenInfra Summit Europe 2025
type: Video Note
description: Alejandro Garcia from Weissaff presents a case study on optimizing OpenStack backup performance for large virtual machines migrating from VMware.
resource: "https://www.youtube.com/watch?v=cF3LkF_ju3c"
youtube_stats:
  view_count: 186
  like_count: 6
  channel_subscriber_count: 46800
tags:
  - openinfra-summit-europe-2025
  - video
  - learning
status: stable
generated:
  by: process:yt-summarizer-okf
  at: 2026-11-22T23:38:50+00:00
---

# Summary

Alejandro Garcia from Weissaff presents a case study on optimizing OpenStack backup performance for large virtual machines migrating from VMware.
The team addressed significant delays in Cinder backup operations caused by inefficient default compression and hashing algorithms.
By replacing the slow zlib compression with the faster zstd algorithm and substituting MD5 and SHA-256 hashing with the high-speed xxHash algorithm, they achieved a three to seven-fold increase in backup speed, reducing a 200 GB backup from over an hour to under 25 minutes.
Additionally, the presentation details various technical challenges resolved during deployment, including fixing Glance S3 upload bugs, implementing custom certificate support, and addressing missing dependencies in Colansible containerized deployments.
These optimizations allowed the company to efficiently handle large-scale backups and incremental restores in production environments, ensuring a user experience comparable to traditional hypervisor-based backup solutions.

# Main Points

|   # | Main point                                                                                                                                                                |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | The presentation covers a real-world backup story for OpenStack virtual machines from a user perspective, focusing on customer expectations during migration from VMware. |
|   2 | The team addressed scenarios involving large virtual machines with hundreds of gigabytes to terabytes of data, using both Cinder volumes and Glance ephemeral disks.      |
|   3 | Cinder backup operations involve transferring data from a volume backend to a separate backup backend, such as S3 or NFS, using the Cinder backup service.                |
|   4 | Incremental backups rely on chunk-based comparison logic where the driver hashes chunks to determine if data has changed since the last backup.                           |
|   5 | Glance does not natively support backups, so the team implemented a workaround using server snapshots to create temporary copies of ephemeral disks for transfer.         |
|   6 | Performance bottlenecks were identified in the default compression and hashing algorithms used by Cinder backup, specifically zlib and MD5/SHA-256.                       |
|   7 | The team replaced the default zlib compression with the faster zstd algorithm by updating the Cinder backup configuration.                                                |
|   8 | Custom code was contributed to Cinder to replace the default MD5 and SHA-256 hashing algorithms with the faster xxHash algorithm.                                         |
|   9 | These algorithm changes resulted in a backup speed boost of three to seven times, reducing a 200 GB backup from over an hour to approximately 23 minutes.                 |
|  10 | The team used Colasoft for deployment, which required adding missing S3 configurations and dependencies to container images.                                              |
|  11 | A Glance bug was fixed where the file size was not correctly set during multi-part uploads to S3, causing failures for large files.                                       |
|  12 | Support for custom SSL certificates in Glance was implemented to allow connections to private S3 backends using self-signed certificates.                                 |
|  13 | A deadlock issue in the Cinder backup library was backported to the production environment to resolve hanging backup processes.                                           |
|  14 | Compatibility issues with Huawei storage required changing a specific command flag to enable successful backups.                                                          |
|  15 | The team implemented an external agent to automate backup policies, such as full backups on Sundays and incremental backups daily.                                        |
|  16 | Recovery speed was also improved proportionally to backup speed by using the same optimized compression and hashing algorithms.                                           |
|  17 | The solution allows for partial restores of specific volumes but does not currently support listing contents within a backup for file-level recovery.                     |
|  18 | The team discovered that the chunk-based driver did not actually use the calculated MD5 hashes for change detection, which justified the algorithm replacement.           |
|  19 | Incremental backups with certain third-party storage solutions, such as Huawei, may still perform full scans due to limitations in change block tracking.                 |
|  20 | The changes are self-contained within Cinder and Glance and do not affect other OpenStack tools like Freezer.                                                             |

# Video

[![Video thumbnail](https://img.youtube.com/vi/cF3LkF_ju3c/hqdefault.jpg)](https://www.youtube.com/watch?v=cF3LkF_ju3c)

[Watch on YouTube](https://www.youtube.com/watch?v=cF3LkF_ju3c)
