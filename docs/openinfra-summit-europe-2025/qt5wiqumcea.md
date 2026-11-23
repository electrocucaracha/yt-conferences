---
layout: default
title: Getting the most out of your OpenStack infrastructure the benefits of using OpenStack Watcher
nav_order: 51
parent: OpenInfra Summit Europe 2025
type: Video Note
description: "G Rosenberg, a product manager responsible for OpenStack’s open architecture and OpenShift integrations, presents the resurrection of the Watcher service to address day-two workload optimization ch..."
resource: "https://www.youtube.com/watch?v=Qt5wIqumcEA"
youtube_stats:
  view_count: 147
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

G Rosenberg, a product manager responsible for OpenStack’s open architecture and OpenShift integrations, presents the resurrection of the Watcher service to address day-two workload optimization challenges in high-churn enterprise environments.
Unlike static telco use cases, industries such as banking and insurance require dynamic resource management to maintain SLAs, which traditional OpenStack placement mechanisms do not fully support.
Watcher introduces a decision engine and applier framework that utilizes metrics like CPU, memory, and network latency to execute strategies for workload stabilization, node evacuation for maintenance, and infrastructure consolidation to reduce costs.
The service is currently undergoing a productization journey with technical previews released in March and June 2025, aiming for full support by November 2025, and is accessible via UI, CLI, and API endpoints.
A live demonstration illustrates how the system detects high CPU utilization on a host and automatically generates an action plan to migrate workloads to balance resources, while future enhancements include layered strategy execution and improved handling of periodic load patterns.

# Main Points

|   # | Main point                                                                                                                                                      |
| --: | --------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | G Rosenberg, a product manager, oversees OpenStack's open architecture, OpenShift integrations, and new service evolutions.                                     |
|   2 | The Watcher project was resurrected to address day-two workload optimization needs for enterprises with high churn, such as banks and insurance companies.      |
|   3 | Traditional OpenStack placement handles day-one static workloads well but lacks the dynamic optimization required for high-churn environments.                  |
|   4 | Watcher aims to optimize workloads by avoiding congestion and bottlenecks in large, high-density virtualization clouds.                                         |
|   5 | The first tech preview of Watcher was released in March 2025, with a second phase adding stability and new strategies in June.                                  |
|   6 | Full support for Watcher is targeted for the end of November 2025.                                                                                              |
|   7 | Key strategies include workload stabilization, which shuffles workloads based on CPU and memory metrics to ensure stability.                                    |
|   8 | An evacuation strategy allows for smart node draining during maintenance, such as hardware updates or faulty memory replacement.                                |
|   9 | A consolidation strategy identifies underutilized infrastructure to evacuate and shut down nodes, saving on power and amortization costs.                       |
|  10 | Future plans include layering multiple strategies simultaneously to create interactions between them without causing hotspots or timeouts.                      |
|  11 | The system architecture consists of a decision engine that processes metrics and appliers that execute workload migrations.                                     |
|  12 | The long-term goal is to create a fully fledged steering system in OpenStack that mimics advanced cloud automation capabilities.                                |
|  13 | Watcher is accessible via UI, CLI, and API endpoints, allowing users to create audit templates with specific optimization goals.                                |
|  14 | The decision engine can prioritize metrics like network latency over CPU consumption for distributed systems to optimize performance.                           |
|  15 | A demo demonstrated the workload balance migration strategy moving an instance from a high-CPU host to a new host after a threshold was exceeded.               |
|  16 | Audit intervals are tunable, allowing the system to gather sufficient metrics to identify patterns and make informed migration decisions.                       |
|  17 | The system can distinguish between moving a noisy neighbor versus evacuating lighter workloads to balance the infrastructure effectively.                       |
|  18 | Action plans are currently manually invoked but can be scheduled for specific times, such as weekends for consolidation tasks.                                  |
|  19 | The core Watcher functionality is upstream, while the Go operators wrapping it are in a different OpenStack community repository.                               |
|  20 | Watcher does not currently replace instance auto-recovery features like VMware HA, though integration is a potential future consideration.                      |
|  21 | Current metrics focus on CPU and memory utilization, with plans to incorporate IO latency and other storage-related metrics.                                    |
|  22 | Memory measurement algorithms are complex due to differences between guest OS and hypervisor perspectives, including issues with huge pages.                    |
|  23 | Storage-specific metrics like IOPS and volume migration dependencies are not yet fully integrated but are recognized as important areas for future development. |

# Video

[![Video thumbnail](https://img.youtube.com/vi/Qt5wIqumcEA/hqdefault.jpg)](https://www.youtube.com/watch?v=Qt5wIqumcEA)

[Watch on YouTube](https://www.youtube.com/watch?v=Qt5wIqumcEA)
