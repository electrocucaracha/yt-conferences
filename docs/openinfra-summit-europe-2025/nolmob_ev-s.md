---
layout: default
title: "From Risk to Resilience: Implementing a Robust Data Protection for OpenStack"
nav_order: 104
parent: OpenInfra Summit Europe 2025
type: Video Note
description: "Storeware, a company founded twelve years ago by its current CEO, specializes in enterprise-grade data protection for KVM-based virtualization environments, including OpenStack, which it has suppor..."
resource: "https://www.youtube.com/watch?v=nOlmoB_Ev-s"
youtube_stats:
  view_count: 59
  like_count: 1
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

Storeware, a company founded twelve years ago by its current CEO, specializes in enterprise-grade data protection for KVM-based virtualization environments, including OpenStack, which it has supported since 2019.
The presentation highlights the company’s mission to provide robust backup solutions for open-source communities, differentiating itself from competitors who primarily focus on VMware and Hyper-V.
Two primary backup strategies are demonstrated: a disk attachment method that leverages Storage Element (SE) for high-performance data transfer, and an SSH-based alternative that addresses quota limitations by connecting directly to hosts.
The software offers advanced features such as multi-tenancy via Horizon and Skyline plugins, allowing managed service providers to offer backup-as-a-service with tenant-specific access and billing capabilities.
Additionally, the system supports ZFS for deduplication and compression, achieving high storage efficiency, and includes granular file-level restoration through mounted volumes, ensuring comprehensive disaster recovery and data protection for large-scale OpenStack deployments.

# Main Points

|   # | Main point                                                                                                                                                                                    |
| --: | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Storware is a backup software vendor founded 12 years ago by three people without external investment, now employing approximately 50 people and selling to over 140 countries.               |
|   2 | The company specializes in enterprise-grade data protection for KVM-based virtualization, a niche largely ignored by competitors who focus on VMware and Hyper-V.                             |
|   3 | Storware supports OpenStack, which it has supported since 2019, and views it as a significant market opportunity for both partners and customers.                                             |
|   4 | The company differentiates itself by offering choice in virtualization engines, allowing customers to protect KVM, OpenStack, Oracle, IBM, HP, and VMware environments.                       |
|   5 | Storware integrates with other backup vendors and is available through partners like Dell (as Dell Vprotect) and IBM, though it emphasizes its unique focus on OpenStack.                     |
|   6 | Two primary backup strategies for OpenStack are presented: disk attachment and SSH-based data transfer.                                                                                       |
|   7 | The disk attachment strategy is the most common method, involving the creation of snapshots and connecting volumes to a data mover node.                                                      |
|   8 | Using Storage Engines (SE) behind the scenes allows direct communication with monitors, bypassing the OpenStack API for significantly improved performance in large environments.             |
|   9 | The SSH strategy serves as an alternative for customers who cannot use disk attachment due to quota limitations or security concerns regarding host access.                                   |
|  10 | In large OpenStack environments, Storware recommends scaling data mover nodes based on concurrent jobs, with a best practice of no more than 20 simultaneous jobs per node.                   |
|  11 | A notable implementation involved eight nodes handling 1.1 petabytes of daily backups using incremental strategies and SE integration.                                                        |
|  12 | Storware provides a Horizon plugin that enables tenant-level backup and restoration, allowing end users to manage their own data protection without accessing the central Storware interface. |
|  13 | A Skyline plugin is also available, enabling managed service providers to offer backup-as-a-service with billing mechanisms and tenant-specific dashboards.                                   |
|  14 | Key benefits of using a third-party vendor over native or script-based solutions include file-level restore capabilities, scheduling, and the transfer of responsibility to the vendor.       |
|  15 | The company adheres to the 3-2-1 backup rule, ensuring three copies of data on two different media types with one copy offsite.                                                               |
|  16 | Storware utilizes ZFS as a deduplication and compression target, achieving high ratios such as 29:1, which significantly reduces physical storage requirements.                               |
|  17 | The software supports synthetic full backups, where incremental backups are treated as full backups for restoration, eliminating the need for complex GFS retention chains.                   |
|  18 | Multi-tenancy is handled through OpenStack native features, allowing specific users to be assigned to specific projects or VMs with limited permissions.                                      |
|  19 | File-level restoration is achieved by mounting the full disk image and using guest filesystem tools to browse and recover individual files or folders.                                        |
|  20 | Security features include immutability flags to prevent ransomware attacks, though the company acknowledges that root access could potentially override these settings.                       |
|  21 | The company emphasizes a close, human-touch approach to customer support, distinguishing itself from larger corporate competitors.                                                            |
|  22 | Storware has over 1,000 customers and continues to develop new features specifically for the OpenStack ecosystem.                                                                             |

# Video

[![Video thumbnail](https://img.youtube.com/vi/nOlmoB_Ev-s/hqdefault.jpg)](https://www.youtube.com/watch?v=nOlmoB_Ev-s)

[Watch on YouTube](https://www.youtube.com/watch?v=nOlmoB_Ev-s)
