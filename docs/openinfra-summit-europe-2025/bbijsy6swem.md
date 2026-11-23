---
layout: default
title: "Building Resilient Systems: Lessons from High Availability Architecture in StarlingX"
nav_order: 60
parent: OpenInfra Summit Europe 2025
type: Video Note
description: "Elliot, a software engineer at Wind River, presents an overview of the Starling X project, focusing on building resilient systems and high availability (HA) architectures for critical infrastructur..."
resource: "https://www.youtube.com/watch?v=BBijsY6sweM"
youtube_stats:
  view_count: 121
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

Elliot, a software engineer at Wind River, presents an overview of the Starling X project, focusing on building resilient systems and high availability (HA) architectures for critical infrastructure services.
The presentation outlines various deployment configurations, ranging from single-node setups to distributed cloud environments with system controllers and subclouds, emphasizing that HA is achieved through a combination of architectural choices and dedicated system services.
Key challenges discussed include avoiding single points of failure, managing infrastructure overload, handling network latency, and balancing cost against redundancy during upgrades.
To address these issues, Starling X employs a data-driven approach using standardized Linux scripts for service monitoring, multiple communication paths for redundancy, and a service state dependency tree to manage active-standby or active-active models.
The speaker also highlights the importance of distinguishing between connectivity issues and performance lags by utilizing internal heartbeats between the heartbeat agent and Service Manager, as well as cluster heartbeats to determine controller health and automate failover processes.

# Main Points

|   # | Main point                                                                                                                                                                                    |
| --: | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | The presentation covers the Starling X project, focusing on building resilient systems and high availability (HA) architecture for critical infrastructure services.                          |
|   2 | The primary goal of HA is to create a computing environment with negligible downtime and rapid recovery from errors.                                                                          |
|   3 | The scope of the discussion is limited to HA on controller nodes for services such as Docker, SE, Gravit, Postgres, Hawking, and DNS mass.                                                    |
|   4 | Starling X supports various deployment configurations, including all-in-one, two-node HA, and dedicated controller, storage, and compute nodes.                                               |
|   5 | Distributed cloud configurations allow a system controller to manage multiple subclouds across different regions, with the system controller handling management rather than heavy workloads. |
|   6 | The Starling X architecture includes OpenStack and Kubernetes components, with core services providing configuration, fault, host, service, and software management.                          |
|   7 | Host management services monitor processes, interfaces, resources, and sensors while interfacing with server BMCs and other Starling X services.                                              |
|   8 | Service management utilizes an active-standby or redundancy model, typically configured as one active and one standby node, though the software supports n plus m configurations.             |
|   9 | Service monitoring is achieved using simple Linux scripts, such as LSB or OCF standardized scripts, to maintain a low footprint.                                                              |
|  10 | Communication between nodes occurs over multiple network interfaces to ensure connectivity persists if one interface fails.                                                                   |
|  11 | Common architectural challenges include avoiding single points of failure, managing infrastructure overload that impacts HA capabilities, and handling network latency.                       |
|  12 | Operational challenges involve balancing the cost of redundancy against budget constraints and maintaining HA during software upgrades or versioning.                                         |
|  13 | The HA approach is data-driven and configurable, utilizing multiple communication interfaces with security features like HMAC 512 and IP sets.                                                |
|  14 | A service state dependency tree ensures that services are only activated when their dependencies are enabled, organizing services into groups and domains based on node function.             |
|  15 | Specific services like OAM network use an active-standby model, while services like Seth and Horizon use an active-active model.                                                              |
|  16 | A finite state machine governs service states, transitioning between initial, active, standby, and disabled states based on monitoring script responses.                                      |
|  17 | An internal heartbeat between the heartbeat agent and Service Manager helps distinguish between network lag and local performance issues.                                                     |
|  18 | Heartbeat messages between service managers on multiple networks and cluster heartbeats from storage or compute nodes help determine controller health and trigger automatic failover.        |

# Video

[![Video thumbnail](https://img.youtube.com/vi/BBijsY6sweM/hqdefault.jpg)](https://www.youtube.com/watch?v=BBijsY6sweM)

[Watch on YouTube](https://www.youtube.com/watch?v=BBijsY6sweM)
