---
layout: default
title: "Swift Deployment, Monitoring, and Real-time Performance Analysis of Regular vs. BlueStore Backends"
nav_order: 117
parent: OpenInfra Summit Europe 2025
type: Video Note
description: "Adrian and David present a project focused on deploying and monitoring OpenStack Swift using a tool called Swift Occular, which utilizes Ansible for automated multi-node setup and Grafana for perfo..."
resource: "https://www.youtube.com/watch?v=5cN0oriyXY0"
youtube_stats:
  view_count: 52
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

Adrian and David present a project focused on deploying and monitoring OpenStack Swift using a tool called Swift Occular, which utilizes Ansible for automated multi-node setup and Grafana for performance visualization.
The core objective of their research is to evaluate the performance benefits of replacing Swift’s default XFS disk backend with Ceph’s BlueStore, a high-performance, memory-efficient storage engine that writes objects directly to block devices and stores metadata in RocksDB.
Through rigorous benchmarking, they demonstrated that BlueStore significantly outperforms XFS, achieving write speeds three to four times faster for various block sizes and offering superior metadata handling with linear scalability compared to the exponential growth and memory overhead associated with XFS extended attributes.
The presenters also detailed a development environment that facilitates code modification and cluster-level observation, while acknowledging that their current implementation is a proof-of-concept using simulated disks that requires further validation on bare-metal hardware.
They concluded by inviting the community to replicate their benchmarks and contribute to future work, including addressing replication mechanisms and exploring additional storage configurations to solidify the case for adopting BlueStore as a backend for Swift.

# Main Points

|   # | Main point                                                                                                                                                                                |
| --: | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Swift is an OpenStack project for distributed object storage featuring middleware architecture, partial object retrieval, and a browser-based control panel.                              |
|   2 | The project uses Ansible for agentless deployment, requiring Vagrant, Libvirt, and an internet connection to automate provisioning and network setup.                                     |
|   3 | Deployment includes proxy nodes, storage nodes, Keystone for authentication, and Grafana for monitoring, with dashboards created using the Grafonnet library.                             |
|   4 | Monitoring dashboards track host overview metrics, object distribution, and XFS file system performance, specifically highlighting inode memory usage issues with small files.            |
|   5 | The current Swift architecture uses XFS file systems on 5GB loop devices, where objects are stored as files and metadata is written as extended attributes.                               |
|   6 | The proposed alternative uses BlueStore, which writes objects directly to block devices and stores metadata in RocksDB, sharing the device with BlueFS.                                   |
|   7 | Benchmarks show BlueStore is significantly faster than XFS for writing objects, with times approximately one-third of XFS for 4KB blocks and performance gaps widening for larger blocks. |
|   8 | Metadata performance tests indicate RocksDB is an order of magnitude faster than XFS extended attributes for values under 16KB, while XFS performance becomes non-linear and glitchy.     |
|   9 | A simple implementation approach involves replacing extended attribute calls in diskfile.py with Python bindings to RocksDB and using a BlueStore utility for file storage.               |
|  10 | A more robust approach suggests rewriting the object server as a C++ service using the BlueStore API to eliminate Python overhead and improve integration.                                |
|  11 | The development environment uses Vagrant boxes with pre-compiled Ceph to facilitate multi-node Swift cluster testing, allowing code changes on any node to be observed cluster-wide.      |
|  12 | Previous attempts to replace Swift's disk backend were abandoned, but this project validates the benefits of BlueStore based on Ceph's proven architecture and community support.         |
|  13 | Future work includes addressing replication support, testing on bare metal hardware to verify performance, and exploring additional configurations for cold and hot data storage.         |
|  14 | The project is not yet production-grade as it relies on simulated disks, but the findings strongly support BlueStore as a high-performance, memory-efficient backend for Swift.           |

# Video

[![Video thumbnail](https://img.youtube.com/vi/5cN0oriyXY0/hqdefault.jpg)](https://www.youtube.com/watch?v=5cN0oriyXY0)

[Watch on YouTube](https://www.youtube.com/watch?v=5cN0oriyXY0)
