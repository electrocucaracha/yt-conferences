---
layout: default
title: Beyond Overcommit  Monitoring Aware OpenStack Nova Scheduling
nav_order: 69
parent: OpenInfra Summit Europe 2025
type: Video Note
description: "David Warsmart, an architect at OVHcloud, presents a proposal to enhance OpenStack Nova’s scheduling by integrating dynamic monitoring data to optimize virtual machine placement."
resource: "https://www.youtube.com/watch?v=1Nn0JQ6Xum4"
youtube_stats:
  view_count: 104
  like_count: 2
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

David Warsmart, an architect at OVHcloud, presents a proposal to enhance OpenStack Nova’s scheduling by integrating dynamic monitoring data to optimize virtual machine placement.
He explains that while Nova currently uses static overcommitment ratios and basic filters, this approach often leads to inefficient resource utilization because it does not account for actual historical CPU usage or future load predictions.
To address this, the team developed a prototype plugin interface that allows Nova to query external time-series databases, such as Prometheus, during the scheduling process to make more informed decisions based on real-time and predictive metrics.
This method aims to improve server efficiency and reduce environmental costs by packing more VMs onto hosts without compromising quality of service, while remaining optional and compatible with existing static overcommitment bounds.
Warsmart emphasizes that this solution is generic, allowing operators to use various metrics beyond CPU, and seeks community feedback to upstream the plugin, noting that it complements rather than replaces existing mechanisms like the Watcher project for load rebalancing.

# Main Points

|   # | Main point                                                                                                                                                                    |
| --: | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | OpenStack Nova scheduling relies on filtering and weighing to select hosts based on static attributes like CPU features, NUMA, and GPU affinity.                              |
|   2 | Static overcommitment ratios are often suboptimal because they do not account for actual workload usage, leading to wasted resources or missed optimization opportunities.    |
|   3 | The goal is to enhance VM placement by incorporating dynamic, real-time monitoring data to predict future load and optimize resource utilization.                             |
|   4 | Existing solutions like the matrix weighter in Nova rely on current metrics, which may not reflect historical trends or future predictions needed for efficient scheduling.   |
|   5 | A proposed generic plugin interface allows Nova to query external time-series monitoring systems like Prometheus without modifying core Nova conductor logic.                 |
|   6 | This approach enables custom filters and weighters that can analyze historical CPU usage, standard deviation, and percentiles to estimate available resources.                |
|   7 | The plugin design is intended to be optional and non-disruptive, ensuring that if monitoring data is unavailable, standard static overcommitment rules still apply.           |
|   8 | Performance optimizations include limiting API requests to monitoring stacks by using single queries and skipping checks for hosts with low VM density.                       |
|   9 | The solution aims to improve quality of service by preventing over-packing of VMs during high-load periods while maximizing efficiency during low-load times.                 |
|  10 | While the current focus is on CPU usage, the generic interface supports other metrics such as network traffic, water cooling temperatures, and hardware intervention history. |
|  11 | The project is currently a prototype seeking community feedback, with plans to upstream the plugin interface to the OpenStack community.                                      |
|  12 | Integration with the Watcher project is considered for post-scheduling load rebalancing, complementing the initial placement optimization provided by the new plugin.         |
|  13 | Memory and storage overcommitment are generally avoided due to safety risks, with the dynamic optimization primarily targeting CPU resources.                                 |
|  14 | The system maintains existing Nova filters and weighters, using the external data only to refine the final host selection for better precision.                               |
|  15 | Hardware failure evacuation processes remain compatible with the new scheduling logic, relying on the same filtering mechanisms to find suitable alternative hosts.           |

# Video

[![Video thumbnail](https://img.youtube.com/vi/1Nn0JQ6Xum4/hqdefault.jpg)](https://www.youtube.com/watch?v=1Nn0JQ6Xum4)

[Watch on YouTube](https://www.youtube.com/watch?v=1Nn0JQ6Xum4)
