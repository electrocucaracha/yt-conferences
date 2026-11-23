---
layout: default
title: "L3 All the Way: Reinventing Our Cloud Architecture with BGP and OpenStack/OVN"
nav_order: 3
parent: OpenInfra Summit Europe 2025
type: Video Note
description: A European private technology company specializing in dedicated cloud computing for the space sector has reinvented its OpenStack cloud architecture by transitioning from a Layer 2 to a Layer 3 net...
resource: "https://www.youtube.com/watch?v=5Kk8ZUIBbZ4"
youtube_stats:
  view_count: 1488
  like_count: 31
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

A European private technology company specializing in dedicated cloud computing for the space sector has reinvented its OpenStack cloud architecture by transitioning from a Layer 2 to a Layer 3 networking model using the BGP protocol.
This shift was driven by significant scalability and debugging challenges associated with proprietary Layer 2 solutions and the complex interplay between OVN and network devices.
The new architecture utilizes a spine-leaf design where hosts connect via BGP sessions, allowing for dynamic IP management through a modified OVN BGP agent that synchronizes with the northbound database.
While this approach leverages the proven scalability of BGP and simplifies traffic balancing, it introduces complexities in configuration management, requiring extensive VRF setups and careful handling of Linux routing rules to ensure proper packet flow between virtual and physical networks.
The team has successfully deployed this architecture in two infrastructures, addressing performance bottlenecks in the synchronization process by optimizing IP rule configurations to reduce setup time from minutes to seconds for large port counts.

# Main Points

|   # | Main point                                                                                                                                                            |
| --: | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | The company is a European private technology provider specializing in dedicated cloud computing for the space sector, handling satellite data storage and processing. |
|   2 | The team faced scalability and debugging challenges with Layer 2 networking in OpenStack, specifically with proprietary vendor solutions and OVN integration issues.  |
|   3 | They decided to reinvent their cloud architecture by implementing BGP for Layer 3 networking to replace complex Layer 2 domains.                                      |
|   4 | The new approach uses a spine-leaf network architecture where hosts connect via PCI devices to leaf switches for BGP sessions.                                        |
|   5 | Control plane nodes use static configurations for internal network connectivity, while compute nodes handle dynamic IP assignments.                                   |
|   6 | Internal VRFs are used to isolate networks, with placeholder dummy interfaces for static IPs and dynamic interfaces for agent-controlled IPs.                         |
|   7 | The implementation leverages the OVN BGP agent to synchronize dynamic IP configurations from the OpenStack database to host network interfaces.                       |
|   8 | A custom modification was made to the OVN BGP agent to support multiple physical networks and VRFs beyond the default block network.                                  |
|   9 | The team uses IPv6 link-local addresses for BGP sessions to avoid the complexity of assigning unique IPs to every interface.                                          |
|  10 | Challenges include configuration conflicts between Zebra and other services, requiring workarounds for IP rule management.                                            |
|  11 | Linux routing table priorities had to be adjusted to allow traffic between VRFs and bridge interfaces, as default rules prioritize local lookups.                     |
|  12 | The OVN BGP agent's single-threaded synchronization process caused delays, taking up to two minutes for 1,000 ports to configure.                                     |
|  13 | Optimization efforts focused on reducing IP rule entries by using subnet-based rules instead of individual IP rules, improving speed by tenfold.                      |
|  14 | The solution allows every host IP to be accessible like any internet IP, simplifying boundary definition between network and cloud components.                        |
|  15 | Legacy Layer 2 regions must still be maintained alongside the new Layer 3 infrastructure, requiring careful migration to avoid disconnections.                        |
|  16 | The team gained new skills in BGP routing and Linux network configuration, moving from cloud-only expertise to full-stack network management.                         |
|  17 | Two infrastructures are currently running on this new architecture, with ongoing testing to validate it as the optimal solution.                                      |
|  18 | Vendor device limitations and bugs in BGP implementations remain a source of instability, requiring careful configuration and monitoring.                             |
|  19 | The approach encapsulates Layer 2 networks within VRFs, allowing the delivery of Layer 2 services without exposing the underlying complexity.                         |

# Video

[![Video thumbnail](https://img.youtube.com/vi/5Kk8ZUIBbZ4/hqdefault.jpg)](https://www.youtube.com/watch?v=5Kk8ZUIBbZ4)

[Watch on YouTube](https://www.youtube.com/watch?v=5Kk8ZUIBbZ4)
