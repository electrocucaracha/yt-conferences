---
layout: default
title: "VM Migration Lightning Demo: Automated Disaster Recovery in OpenStack with Masakari and Consul"
nav_order: 58
parent: OpenInfra Summit Europe 2025
type: Video Note
description: "This lightning demo by Canonical presents an automated disaster recovery solution for OpenStack environments, specifically addressing the migration from VMware."
resource: "https://www.youtube.com/watch?v=CeDD-qZIfFk"
youtube_stats:
  view_count: 130
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

This lightning demo by Canonical presents an automated disaster recovery solution for OpenStack environments, specifically addressing the migration from VMware.
The presentation highlights the importance of maintaining high availability and resilience during the transition, introducing the Mazakari service as a built-in OpenStack component for workload high availability.
The core of the demonstration involves a simulated network outage on a compute node running two virtual machines, where a monitoring service called Console detects the failure via periodic TCP checks.
Upon detecting the unreachability, Console triggers Mazakari to communicate with the Nova API, which automatically shuts down the faulty compute service and evacuates the running workloads to a healthy node.
The demo concludes by showing the successful migration of the virtual machines to a different compute node, illustrating how this configuration-aware process ensures business continuity without requiring manual intervention or full node replacement.

# Main Points

|   # | Main point                                                                                                                                           |
| --: | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | The session focuses on automated disaster recovery and migration from VMware to OpenStack at Canonical.                                              |
|   2 | Building a highly available, resilient, and secure OpenStack environment is essential before addressing the final migration steps.                   |
|   3 | Key infrastructure components include availability zones, image catalogs, provisioning, storage, load balancers, and firewall rules.                 |
|   4 | OpenStack provides networking security features through Neutron security groups, comparable to VMware NSX capabilities.                              |
|   5 | High availability for workloads in OpenStack is managed by the Maasakari service, which handles VM evacuation during outages.                        |
|   6 | The demo architecture uses Sunbeam, a cloud-native OpenStack installation model, with three compute nodes.                                           |
|   7 | The Console service monitors network health using TCP checks every 10 seconds to detect unreachability on compute nodes.                             |
|   8 | Upon detecting a network outage, Console notifies the Maasakari administrator to trigger the evacuation process.                                     |
|   9 | Maasakari coordinates with the Nova API to shut down the Nova compute service on the faulty node and evacuate workloads.                             |
|  10 | The demo simulated a network outage on a compute node running two VMs, resulting in their automatic migration to a healthy node.                     |
|  11 | Logs confirmed that Maasakari detected the outage and initiated the evacuation of virtual machines to a live compute node.                           |
|  12 | Migration destinations are configurable to accommodate hardware dependencies such as GPUs or specific CPU requirements.                              |
|  13 | Maasakari supports both hyperconverged and disaggregated architectures without requiring a full compute node restart.                                |
|  14 | This solution serves as a foundational disaster recovery strategy for single-site clusters, with potential expansion to multi-cluster architectures. |
|  15 | Attendees are encouraged to visit the Canonical booth for deeper technical discussions on Maasakari and Console implementation.                      |

# Video

[![Video thumbnail](https://img.youtube.com/vi/CeDD-qZIfFk/hqdefault.jpg)](https://www.youtube.com/watch?v=CeDD-qZIfFk)

[Watch on YouTube](https://www.youtube.com/watch?v=CeDD-qZIfFk)
