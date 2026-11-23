---
layout: default
title: External Networks with native BGP in OVN
nav_order: 13
parent: OpenInfra Summit Europe 2025
type: Video Note
description: "This presentation details the integration of external networks using native Open vSwitch (OVS) features, specifically focusing on the OVN (Open Virtual Network) architecture to replace traditional ..."
resource: "https://www.youtube.com/watch?v=TC70lfP91Ns"
youtube_stats:
  view_count: 435
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

This presentation details the integration of external networks using native Open vSwitch (OVS) features, specifically focusing on the OVN (Open Virtual Network) architecture to replace traditional provider networks.
The speaker explains a setup where a "magic router" acts as an intermediary between project networks and the physical external network, utilizing logical router ports bound to specific gateway chassis interfaces to enable precise route learning and failover management.
This approach eliminates the need for large stretched Layer 2 domains and proprietary bonding technologies, allowing for dynamic routing via Linux VRFs where the OVN controller adjusts route priorities based on local port bindings to optimize traffic flow.
The talk outlines the necessary configuration steps, including creating the magic router, setting up logical switch and router ports for each physical link, and managing static routes to advertise networks or individual host routes to the upstream fabric.
Finally, the speaker addresses current inefficiencies, such as ECMP processing overhead when traffic traverses non-local chassis, and mentions ongoing upstream work to improve local route prioritization and potential future integrations with Neutron and deployment tooling.

# Main Points

|   # | Main point                                                                                                                                                                                                                      |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | The presentation focuses on integrating external networks using native OVN features, specifically addressing limitations of traditional provider network setups.                                                                |
|   2 | Traditional setups often rely on large stretched Layer 2 networks and gateway chassis, which can cause issues with broadcast domains, flapping, and MAC address handling.                                                       |
|   3 | Current dynamic routing implementations often use external agents like the OVN BGP agent, which operate outside the core OVN database and lack full context for optimal route derivation.                                       |
|   4 | A proposed architecture introduces a "magic router" that acts as a default gateway for project routers, connecting to a virtual public network rather than a direct provider network.                                           |
|   5 | This design uses logical router ports bound to specific gateway chassis interfaces, allowing OVN to learn distinct routes for each physical link and manage failover independently.                                             |
|   6 | By modeling network interfaces as separate logical router ports, the need for proprietary bonding technologies is eliminated, enabling separate route learning and failure management per link.                                 |
|   7 | Failover in this model involves moving the ideal route from one gateway chassis to another, allowing OVN to reroute traffic based on the best learned path without requiring the network fabric to know about internal changes. |
|   8 | OVN release 25.3 supports learning and advertising routes from Linux VRFs, allowing the magic router to advertise either entire subnets or individual host routes.                                                              |
|   9 | The OVN controller adjusts route priorities based on whether the backing port is bound locally, enabling path preference for local chassis to improve efficiency.                                                               |
|  10 | Support is included for redirecting BGP and EVPN packets to logical switch ports, allowing BGP sessions to be established via logical router port IPs while processing occurs in a Linux VRF.                                   |
|  11 | Implementation requires creating a non-provider external network, a magic router with specific options for dynamic routing, and logical router port and logical switch port combinations for each physical link.                |
|  12 | Project routers must be configured to remove the OVN chassis value and set a gateway port to prevent Neutron from pinning the entire router to a single chassis.                                                                |
|  13 | A known inefficiency exists where east-west traffic may traverse the project router and magic router, potentially causing suboptimal ECMP selections if local links are not prioritized.                                        |
|  14 | Future work includes integrating this setup with Neutron and deployment tooling, as well as upstream improvements to prioritize local ECMP routes for better performance.                                                       |
|  15 | The architecture supports announcing static routes or optimized host routes to the network fabric, depending on the configuration of the magic router and connected logical ports.                                              |

# Video

[![Video thumbnail](https://img.youtube.com/vi/TC70lfP91Ns/hqdefault.jpg)](https://www.youtube.com/watch?v=TC70lfP91Ns)

[Watch on YouTube](https://www.youtube.com/watch?v=TC70lfP91Ns)
