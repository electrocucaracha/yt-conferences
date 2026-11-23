---
layout: default
title: "Challenge and opportunity for AI in telco cloud  How we should face sustainability requirement?"
nav_order: 118
parent: OpenInfra Summit Europe 2025
type: Video Note
description: "The speaker presents a strategy for enhancing energy efficiency in technical cloud environments, driven by global sustainability goals and the increasing energy demands of 6G networks."
resource: "https://www.youtube.com/watch?v=-kCCV7h4xho"
youtube_stats:
  view_count: 51
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

The speaker presents a strategy for enhancing energy efficiency in technical cloud environments, driven by global sustainability goals and the increasing energy demands of 6G networks.
By analyzing the gap between actual power consumption and theoretical requirements, the presentation proposes a "Cloud Green Brain" solution that dynamically manages hardware states, such as CPU frequency scaling and sleep modes, to reduce idle power usage.
Specific optimizations include leveraging C6 states to save 2.5 to 4 watts per core, resolving resource fragmentation to power off idle servers, and offloading packet processing to DPUs to lower CPU load.
The speaker also addresses the integration of AI for more accurate workload prediction and power management, while acknowledging current limitations in API support for GPUs and NPUs.
During the Q&A, the discussion expands to include the environmental impact of energy sources, the use of ARM architecture for efficiency, and the importance of considering the full lifecycle and manufacturing impact of hardware in sustainability efforts.

# Main Points

|   # | Main point                                                                                                                                                                     |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   1 | The presentation addresses sustainability challenges in the technical cloud, aiming for carbon neutrality by 2050 in alignment with global agreements.                         |
|   2 | Industry organizations like ITU and GSMA have set targets to reduce carbon emissions by 50% in fixed networks, mobile networks, and data centers.                              |
|   3 | Energy efficiency in mobile networks is determined by the ratio of data volume to energy consumption, highlighting a gap between actual and optimal power usage.               |
|   4 | The core strategy for energy saving is to consume power on demand by reducing workload, improving management, and eliminating ineffective loads.                               |
|   5 | A proposed solution called "Cloud Green Brain" features a three-layer architecture including a control brain, dynamic power management, and hardware-level automatic features. |
|   6 | The controller manages energy-saving policies by sensing application-layer traffic and utilizing metrics reported by hardware to identify idle or busy states.                 |
|   7 | Hardware optimization focuses primarily on the CPU, which accounts for approximately 6% of total server power usage, by adjusting frequency and power states.                  |
|   8 | Testing indicates that keeping CPUs at the lowest frequency under light loads can save 30% to 35% of CPU power consumption.                                                    |
|   9 | Implementing C6 sleep states for unused CPU cores can save 2.5 to 4 watts per core, leveraging the fact that 20% of CPU capacity is often unallocated in cloud deployments.    |
|  10 | Dynamic frequency adjustment for CPU cores based on load can save an additional 20% of power for a single CPU.                                                                 |
|  11 | The system categorizes hardware and collects historical data for prediction and real-time data for immediate state adjustments.                                                |
|  12 | Idle IO servers can be powered off with periodic keep-alive checks to ensure business continuity without affecting service.                                                    |
|  13 | Resource fragmentation is resolved by migrating workloads to consolidate servers, allowing idle servers to be powered down for energy savings.                                 |
|  14 | DPDK usage consumes 100% of CPU regardless of actual traffic; the system detects low load to reduce usage, saving 1.2 watts per core at 10-30% load.                           |
|  15 | Predictive scaling is applied to handle daily traffic patterns, reducing server copies during low-activity periods such as nighttime.                                          |
|  16 | Current AI integration is in the development phase, focusing on intelligent consumption and accurate prediction to enhance energy savings.                                     |
|  17 | There is a lack of standard APIs for controlling power on GPUs and NPUs, unlike CPUs, which limits current optimization capabilities for these accelerators.                   |
|  18 | The approach reuses existing maintenance agents for AI predictions to avoid introducing additional energy consumption from the prediction process itself.                      |
|  19 | System-wide optimization is required, involving model layer specification, platform scheduling, and accelerator design to ensure applications run on efficient hardware.       |
|  20 | Offloading packet processing to DPUs can improve performance by over 10 times compared to CPUs, potentially saving power for specific workloads.                               |
|  21 | The technical cloud operates as a private closed network where power consumption is primarily driven by calling traffic rather than public solar energy availability.          |
|  22 | The team uses ARM-based machines as a major service component, noting their energy efficiency compared to other architectures.                                                 |
|  23 | C-state support varies by manufacturer, with Intel and custom ARM designs being used, while AMD is noted to have less support for lower C-states.                              |

# Video

[![Video thumbnail](https://img.youtube.com/vi/-kCCV7h4xho/hqdefault.jpg)](https://www.youtube.com/watch?v=-kCCV7h4xho)

[Watch on YouTube](https://www.youtube.com/watch?v=-kCCV7h4xho)
