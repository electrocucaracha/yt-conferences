---
layout: default
title: "VM Migration Lightning Demo: Seamless VMware Migration to ZIASTACK"
nav_order: 132
parent: OpenInfra Summit Europe 2025
type: Video Note
description: "ZConverter presented a live demonstration of its hypervisor-agnostic migration technology, designed to simplify the complex process of moving workloads from VMware to OpenStack by eliminating vendo..."
resource: "https://www.youtube.com/watch?v=Dk6CvpxTtHY"
youtube_stats:
  view_count: 32
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

ZConverter presented a live demonstration of its hypervisor-agnostic migration technology, designed to simplify the complex process of moving workloads from VMware to OpenStack by eliminating vendor lock-in.
The solution utilizes a unified backup format to reduce the thousands of potential migration scenarios into a single, standardized "backup and recovery" workflow, thereby guaranteeing a 99.9% success rate.
During the demo, the team showcased both full and incremental virtual machine migrations, illustrating how the system captures VM images and replicates them to an OpenStack environment with minimal downtime.
The presentation highlighted that this approach not only facilitates seamless cross-platform migration but also provides integrated capabilities for disaster recovery and automated scheduling, allowing organizations to manage large-scale workload transfers efficiently.

# Main Points

|   # | Main point                                                                                                                                             |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   1 | ZConverter presents a virtual machine migration demo led by DJ Min, focusing on workloads running in VMware.                                           |
|   2 | Over 80% of workloads in OpenStack environments are virtual machines, necessitating full and incremental migration strategies.                         |
|   3 | GStack is an OpenStack distribution designed to enable flexible move-in and move-out capabilities for virtual machines and containers.                 |
|   4 | The solution aims to eliminate vendor lock-in and support seamless migration from VMware to OpenStack.                                                 |
|   5 | Cloud migration complexity arises from heterogeneity between VMware and OpenStack, involving different cloud platforms, hypervisors, and disk formats. |
|   6 | The number of potential migration scenarios is vast, with over 30 components per platform contributing to heterogeneity issues.                        |
|   7 | GConverter utilizes hypervisor-agnostic migration technology to eliminate heterogeneity and simplify the process.                                      |
|   8 | The migration process involves capturing VMs in a GBackup format, converting all scenarios into a single Z-to-OpenStack test case.                     |
|   9 | This approach guarantees a 99.9% migration success rate by reducing the need to test thousands of individual cases.                                    |
|  10 | The technology supports migration from AWS, Azure, GCP, and bare metal machines to OpenStack using a backup and recovery model.                        |
|  11 | A single backup technology provides three capabilities: backup, cross-hypervisor migration, and disaster recovery.                                     |
|  12 | The live demo showcases a video streaming service running on VMware being migrated to OpenStack.                                                       |
|  13 | The migration UI allows for both manual and script-based automation for large-scale migrations of thousands of machines.                               |
|  14 | A full backup capture takes approximately five minutes, while the recovery process to OpenStack takes about three minutes.                             |
|  15 | During the full migration demo, the video streaming file was replaced on the source to demonstrate incremental migration capabilities.                 |
|  16 | GConverter released new OpenStack distributions to address high costs and long durations associated with VM-to-container migrations.                   |
|  17 | The solution enables flexible move-in and move-out capabilities for virtual machines within the OpenStack environment.                                 |
|  18 | Incremental migration involves capturing only changed data, such as a replaced video file, to minimize service downtime.                               |
|  19 | The recommended strategy for massive workload migrations is to perform a full backup first, followed by incremental backups.                           |
|  20 | Automated scripts can be used to eliminate human errors and streamline the backup and recovery processes.                                              |
|  21 | The migration process is described as a lift-and-shift or copy-and-paste operation between VMware and OpenStack.                                       |

# Video

[![Video thumbnail](https://img.youtube.com/vi/Dk6CvpxTtHY/hqdefault.jpg)](https://www.youtube.com/watch?v=Dk6CvpxTtHY)

[Watch on YouTube](https://www.youtube.com/watch?v=Dk6CvpxTtHY)
