---
layout: default
title: "Taming the Kraken:  Experiences with Open Storage in the field"
nav_order: 119
parent: OpenInfra Summit Europe 2025
type: Video Note
description: "Christian, a services director at Morantis, presents a comprehensive overview of Ceph, a software-defined storage solution that runs on standard x86_64 and increasingly ARM-based hardware."
resource: "https://www.youtube.com/watch?v=42XWjEMSsi4"
youtube_stats:
  view_count: 49
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

Christian, a services director at Morantis, presents a comprehensive overview of Ceph, a software-defined storage solution that runs on standard x86_64 and increasingly ARM-based hardware.
He emphasizes that Ceph is highly reliable and resilient, capable of surviving outages without data corruption, and integrates deeply with OpenStack and Kubernetes environments.
A critical lesson from his field experience is that hard disk drives are obsolete for cloud workloads due to latency and seek time limitations; he strongly recommends using flash storage (NVMe) for performance, noting that modern flash is now more cost-effective and reliable than hard drives.
Regarding cluster sizing, he advises a minimum of six nodes to ensure proper data distribution and self-healing capabilities, warning that smaller clusters or disabling replication flags can lead to catastrophic data loss.
Additionally, he highlights best practices for performance, such as using single-CPU systems to avoid NUMA latency issues, allocating sufficient memory per OSD, and implementing encryption at the OpenStack layer (Cinder) rather than within Ceph itself.
Finally, he notes that Ceph’s usability has improved significantly, making it a production-ready, cost-efficient alternative to commercial storage systems, and introduces "Pelagia," an open-source tool developed by his team to simplify Ceph management.

# Main Points

|   # | Main point                                                                                                                                                                            |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Ceph is software-defined storage running on standard x86_64 or ARM64 hardware, with a future trend toward multi-CPU architectures.                                                    |
|   2 | The system is distributed across multiple nodes, highly reliable, and resilient to failure, often surviving outages without data damage.                                              |
|   3 | Ceph integrates deeply with OpenStack, serving as a superior backend for Glance compared to Cinder, and functions as a Swiss army knife for object, file, and block storage.          |
|   4 | Data distribution is elastic across storage classes, but nodes may not be perfectly balanced, so running the cluster near full capacity is discouraged.                               |
|   5 | Replication is the default protection method, while erasure coding offers different protection levels but suffers from poor write performance with small I/O operations.              |
|   6 | Early versions of Ceph were difficult to manage, but modern releases are significantly more stable and user-friendly.                                                                 |
|   7 | A minimum of six nodes is recommended for dedicated Ceph clusters to ensure self-repair capability after node failures and to distribute performance bottlenecks.                     |
|   8 | Running Ceph on fewer than six nodes risks incomplete replication and higher likelihood of network bottlenecks, especially with high-speed NVMe storage.                              |
|   9 | Converged deployments are suitable for small environments, but running Ceph in Kubernetes is preferred over bare metal for easier troubleshooting despite minor performance loss.     |
|  10 | Hard disks are obsolete for cloud workloads due to physical seek latency limitations, which drastically reduce IOPS performance compared to flash storage.                            |
|  11 | Flash storage is now cost-competitive with hard disks, offering superior speed, reliability, and parallel access capabilities for modern workloads.                                   |
|  12 | Using hard disks with flash journals creates operational nightmares and data loss risks if the journal device fails, making all-flash clusters the standard recommendation.           |
|  13 | Operators should avoid permanently disabling Ceph self-repair flags, as this can lead to catastrophic data loss if additional failures occur.                                         |
|  14 | Encryption at rest in Ceph is often unnecessary if encryption is handled at the OpenStack layer in Cinder and Nova, which provides better protection against specific attack vectors. |
|  15 | Performance optimization requires using single-CPU systems to avoid NUMA latency issues, allocating approximately 10 GB of memory per OSD, and ensuring fast network connectivity.    |
|  16 | Two to three CPU cores per NVMe device is recommended, as additional cores yield diminishing returns for normal operations.                                                           |
|  17 | The Pelagia open-source project abstracts Rook objects to simplify the management of Ceph clusters in production environments.                                                        |
|  18 | Ceph integrates well with Kubernetes and other storage subsystems, allowing for hybrid architectures that combine commercial storage with Ceph for specific workloads.                |
|  19 | Flash storage prices continue to drop, making Ceph considerably cheaper than many commercial storage solutions while maintaining high performance.                                    |
|  20 | Failure domains should be defined by racks rather than individual hosts to ensure proper data distribution and resilience.                                                            |
|  21 | Ceph is production-ready and highly reliable, making it a strong recommendation for cloud and container environments.                                                                 |

# Video

[![Video thumbnail](https://img.youtube.com/vi/42XWjEMSsi4/hqdefault.jpg)](https://www.youtube.com/watch?v=42XWjEMSsi4)

[Watch on YouTube](https://www.youtube.com/watch?v=42XWjEMSsi4)
