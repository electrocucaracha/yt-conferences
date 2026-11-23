---
layout: default
title: NVMeoF storage at OVHCloud Public Cloud
nav_order: 54
parent: OpenInfra Summit Europe 2025
type: Video Note
description: Dr.
resource: "https://www.youtube.com/watch?v=mo848fh2Nhg"
youtube_stats:
  view_count: 145
  like_count: 3
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

Dr.
Siga from OVH Cloud details the implementation of NVMe over Fabrics (NVMe-oF) storage for their public cloud services, replacing parts of their existing Ceph infrastructure to achieve lower latency and predictable performance.
The solution leverages the Xen Technologies software-defined storage acquired by OVH, which offers high availability through native Linux kernel multipathing and supports both TCP and RDMA modes, with the latter providing superior speed via reduced protocol overhead.
To integrate this into OpenStack, the team developed a custom Cinder volume driver and a simplified Nova connector that relies on native multipathing, avoiding the complex local replication logic found in older upstream versions.
A critical technical challenge involved managing device naming and attachment safety; the team utilized udev rules to rename NVMe devices based on their unique NQN identifiers, preventing race conditions where device paths could be reused and causing incorrect volume attachments.
Additionally, they implemented specific filter and goodness functions in Cinder to gradually migrate workloads to the new storage backend, ensuring stability while addressing edge cases such as stale data paths and kernel-level device persistence that differ from traditional user-space Ceph operations.

# Main Points

|   # | Main point                                                                                                                                                   |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   1 | Dr. Siga from OVHcloud presented the implementation of NVMe over Fabrics storage for public cloud services.                                                  |
|   2 | OVHcloud operates approximately 430 Ceph clusters, with 260 dedicated to public cloud block storage.                                                         |
|   3 | The team provides Ceph as a Service, handling maintenance, hardware replacement, and cluster delivery for internal and external customers.                   |
|   4 | Multiple Ceph clusters per OpenStack region are used to limit the blast radius during upgrades or hardware failures.                                         |
|   5 | NVMe over Fabrics was adopted to achieve lower latency, predictable performance, and a simpler data path compared to Ceph.                                   |
|   6 | Unlike Ceph, NVMe over Fabrics is an industry standard with native Linux kernel support and backing from major technology companies.                         |
|   7 | OVHcloud acquired Xen Technologies in 2020 to develop software-defined storage with NVMe over Fabrics access.                                                |
|   8 | The first production cluster was deployed in 2023, and approximately 10 clusters now power public cloud block storage.                                       |
|   9 | NVMe over Fabrics requires a Linux kernel version 5.x, the nvme-tcp module, and nvme-cli tools for connectivity.                                             |
|  10 | Connecting an NVMe device requires the target IP address, Subsystem NQN, and Host NQN identifiers.                                                           |
|  11 | NVMe over Fabrics supports standard TCP mode and RDMA mode, with RDMA offering higher performance via UDP packets and PFC-enabled switches.                  |
|  12 | OVHcloud currently uses TCP mode but plans to switch to RDMA in the future after infrastructure preparation.                                                 |
|  13 | Native multipathing in the Linux kernel provides high availability by exposing multiple data paths as a single block device.                                 |
|  14 | Integration with OpenStack required modifying Cinder with a custom volume driver to translate requests to the storage RESTful API.                           |
|  15 | A custom Nova connector was developed to support native multipathing, as upstream support was not yet available in their production version.                 |
|  16 | The custom connector was designed to be compatible with upstream code to facilitate future upgrades.                                                         |
|  17 | NVMe devices are attached at the hypervisor kernel level, unlike Ceph which uses user-space libraries like libRBD.                                           |
|  18 | Kernel device naming is dynamic and can lead to attachment errors if device paths are reused after disconnection.                                            |
|  19 | Udev rules were implemented to rename NVMe devices based on their unique NQN, ensuring predictable and non-reusable device paths.                            |
|  20 | Udev rules also move NVMe devices to a specific location to prevent operator errors and disable automatic assembly of customer data structures like MD RAID. |
|  21 | If the QEMU process dies, the NVMe device remains in the kernel, requiring manual cleanup to avoid stale attachments.                                        |
|  22 | Upgrading storage nodes can result in missing data paths if the initial connection fails, requiring manual recovery.                                         |
|  23 | Replacing storage servers with different IPs is not transparent and requires manual intervention to update connections.                                      |
|  24 | Race conditions can leave stale attachments in the database or prevent VM shutdown if volumes are deleted while attached.                                    |
|  25 | Gradual migration to the new storage was managed using Cinder filter and goodness functions to control volume placement.                                     |
|  26 | Complex boolean logic in Cinder filter and goodness functions can cause evaluation errors, requiring careful configuration.                                  |

# Video

[![Video thumbnail](https://img.youtube.com/vi/mo848fh2Nhg/hqdefault.jpg)](https://www.youtube.com/watch?v=mo848fh2Nhg)

[Watch on YouTube](https://www.youtube.com/watch?v=mo848fh2Nhg)
