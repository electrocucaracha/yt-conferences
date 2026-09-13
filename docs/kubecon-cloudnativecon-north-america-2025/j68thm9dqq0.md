---
layout: default
title: "Just Do It: OpAMP - Panos Tsilopoulos & Bob Johnson, Nike, Inc."
nav_order: 114
parent: Kubecon Cloudnativecon North America 2025
type: Video Note
description:
  In this presentation, Panos and Bob from Nike discuss their experience
  implementing the Open Agent Management Protocol (OpAMP) for managing large fleets
  of OpenTelemetry collectors, particularly during high-scale events like Singles
  Day in...
resource: https://www.youtube.com/watch?v=J68ThM9DqQ0
tags:
  - kubecon-cloudnativecon-north-america-2025
  - video
  - learning
status: stable
generated:
  by: process:yt-conferences-okf
  at: 2026-09-12 00:00:00+00:00
---

# Summary

In this presentation, Panos and Bob from Nike discuss their experience implementing the Open Agent Management Protocol (OpAMP) for managing large fleets of OpenTelemetry collectors, particularly during high-scale events like Singles Day in China.
They explain the challenges of managing tens of thousands of collectors without a centralized control plane and the limitations of existing vendor and open-source solutions.
OpAMP, a CNCF-backed, vendor-agnostic protocol, enables remote management of agents, allowing for configuration updates, status reporting, and secure communication between servers and agents.
The team describes their phased rollout strategy, the importance of KPIs for justifying the project, and demonstrates a Java-based reference implementation that showcases agent-server interactions, resilience, and scalability.
They address questions about deployment strategies, security, configuration management, and future plans to open source their Java implementation, emphasizing the protocol’s flexibility and the operational benefits of centralized agent management.

# Main Points

|   # | Main point                                                                                                                                     |
| --: | ---------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Presentation covers Open Agent Management Protocol (OpAMP) and its enterprise adoption at Nike.                                                |
|   2 | Nike manages about 90,000 OpenTelemetry collectors, especially during peak events like Singles Day.                                            |
|   3 | Current challenge: No centralized way to manage collector configurations across teams.                                                         |
|   4 | Previous vendor solutions (e.g., Splunk heavy forwarders) had control planes; open-source OpenTelemetry lacks equivalent management tools.     |
|   5 | OpAMP is a CNCF-backed, vendor-agnostic protocol for remote management of agent fleets, not just collectors.                                   |
|   6 | OpAMP defines communication between server and agent: status reporting, updates, commands, versioning, package deployment, remote config.      |
|   7 | Protocol supports varied agent versions and configurations across large fleets.                                                                |
|   8 | Security: Multiple authentication layers, including certificate signing and header-based auth; must consider fleet size and certificate costs. |
|   9 | OpAMP uses WebSocket (preferred for full-duplex, persistent connections) or HTTP; plan for failover and scaling.                               |
|  10 | Reference implementation is in Go; Nike built a Java-based version with persistent storage and UI for fleet visualization.                     |
|  11 | Rollout strategy: phased approach—foundation, initial scale, then full rollout.                                                                |
|  12 | Supervisor process deployed alongside collectors enables remote management without user intervention.                                          |
|  13 | Migration requires teams to adopt new collector versions/distributions, with opt-in build steps to avoid breaking changes.                     |
|  14 | KPIs: Focus on reducing engineering toil and measuring deployment/config change efficiency.                                                    |
|  15 | Demo showcased Java-based OpAMP server, agent simulation, status updates, and fleet management.                                                |
|  16 | Nike currently uses a single OpAMP cluster per AWS region; scaling and concurrency may require multiple clusters at larger scale.              |
|  17 | WebSocket chosen for persistent, efficient two-way communication; initial connection involves multiple quick message exchanges.                |
|  18 | Agent upgrades via OpAMP are tested offline before fleet-wide deployment due to p                                                              |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=J68ThM9DqQ0)
