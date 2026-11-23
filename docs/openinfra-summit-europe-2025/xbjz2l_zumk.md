---
layout: default
title: Challenges and Innovative Approaches to VM and Baremetal Integration in OpenStack
nav_order: 120
parent: OpenInfra Summit Europe 2025
type: Video Note
description: 'LY Corporation presented a bare metal as a service solution within their "Flower" private cloud, which is built on a single large-scale OpenStack cluster.'
resource: "https://www.youtube.com/watch?v=XBjZ2L_Zumk"
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

LY Corporation presented a bare metal as a service solution within their "Flower" private cloud, which is built on a single large-scale OpenStack cluster.
The system aims to provide a unified user experience where physical machines are managed with the same ease as virtual machines, utilizing a single API endpoint and reusing internal provisioning tools instead of adopting Ironic.
Key features include integrated networking that enforces isolation between virtual and physical instances using Neutron tags, and a flexible hardware profile system that allows users to specify RAID configurations directly during instance creation.
The architecture employs a notification handler to automate asset registration and OS installation workflows by consuming events from the OpenStack message queue, ensuring seamless integration with internal services without heavily modifying the core platform.
Additionally, the solution implements a stock management lifecycle that allows projects to request, approve, and return physical server inventory through a user-friendly dashboard.
During large-scale testing, the team identified performance bottlenecks when creating over 100 instances simultaneously, leading to the optimization of timeout settings and the recommendation to limit concurrent creation requests to maintain system stability.

# Main Points

|   # | Main point                                                                                                                                                                                           |
| --: | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | LY Corporation developed a private cloud called Flower based on a single large-scale OpenStack cluster to provide both virtual and bare metal instances.                                             |
|   2 | The primary demand for bare metal services includes AI and machine learning workloads requiring direct GPU access, legacy system migration, and software with CPU core-based licensing.              |
|   3 | The system design prioritizes a unified API for both VMs and physical machines, fully automated provisioning in minutes, and integrated networking features.                                         |
|   4 | Instead of using Ironic, the team adopted a pluggable architecture with a custom driver to reuse existing in-house provisioning tools for power control, network, and asset management.              |
|   5 | A notification handler consumes RabbitMQ events from OpenStack components to trigger interactions with internal services such as database registration and OS installation.                          |
|   6 | Network isolation between VMs and bare metal servers is enforced using Neutron tags, specifically marking subnets for bare metal to prevent IP range mixing.                                         |
|   7 | Hardware profiles, such as RAID 1 or RAID 5 configurations, are specified via flavor extra-spec metadata to allow users to select disk layouts during instance creation.                             |
|   8 | The instance creation workflow involves Nova emitting notifications that trigger a handler to register assets in internal databases before proceeding with OS installation and PXE boot.             |
|   9 | Physical machine stock management is implemented using Nova and Placement APIs, allowing projects to request, approve, use, and return server inventory through a dashboard.                         |
|  10 | Large-scale testing revealed that creating 50 instances simultaneously failed due to a 60-second load balancer timeout, which was resolved by extending the timeout to 1800 seconds.                 |
|  11 | Creating 100 instances at once achieved a success rate of 96% to 99%, while attempting 500 instances resulted in a 41% failure rate due to saturation of Keystone and other core services.           |
|  12 | The solution emphasizes user experience by simplifying operations for different resource types and aligning with OpenStack mechanisms through modular event handlers rather than core modifications. |

# Video

[![Video thumbnail](https://img.youtube.com/vi/XBjZ2L_Zumk/hqdefault.jpg)](https://www.youtube.com/watch?v=XBjZ2L_Zumk)

[Watch on YouTube](https://www.youtube.com/watch?v=XBjZ2L_Zumk)
