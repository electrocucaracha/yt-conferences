---
layout: default
title: Adventures of Using OVN in Production
nav_order: 12
parent: OpenInfra Summit Europe 2025
type: Video Note
description: 'Christie, a systems engineer at SWITCH, presented the organization’s transition from the legacy OpenStack-based "engines" system to the new "switch cloud," which runs OpenStack on Kubernetes using ...'
resource: "https://www.youtube.com/watch?v=hS2Ytpo9mpM"
youtube_stats:
  view_count: 457
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

Christie, a systems engineer at SWITCH, presented the organization’s transition from the legacy OpenStack-based "engines" system to the new "switch cloud," which runs OpenStack on Kubernetes using OVN for networking.
The team selected OVN for its superior performance, achieving over 9 Gbps throughput in tests, but encountered significant operational challenges with the Octavia load balancer provider.
Key issues included incompatibility between Octavia and VxLAN networks, data synchronization failures when rebuilding databases, and a critical bug where deleting a pool with shared backend members wiped IP port mappings, rendering load balancers unreachable.
Additionally, the team faced complex routing problems when extending external IP pools, where east-west traffic failed due to ARP request issues, requiring a disruptive maintenance window to reconfigure subnets.
Other hurdles included security group restrictions blocking return traffic from load balancers, the necessity of virtual routers for isolated subnets to reach load balancers, and high control plane load during upgrades from Antelope to Caracal.
Christie concluded by emphasizing the need for better documentation of these corner cases, improved debugging tools like OVN trace, and stronger community collaboration to share workarounds and resolve these persistent integration issues.

# Main Points

|   # | Main point                                                                                                                                              |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | SWITCH operates the Swiss National Research and Educational Network and manages the .ch and .li domain registries.                                      |
|   2 | The team provides cloud services to schools, universities, and research institutes using OpenStack.                                                     |
|   3 | The new SWITCH Cloud runs OpenStack on Kubernetes, deployed via OpenStack Helm with Flux for configuration management.                                  |
|   4 | The networking stack uses Neutron with the OVN mechanism driver, replacing the legacy OVS plugin.                                                       |
|   5 | OVN was chosen for superior performance, achieving over 9 Gbps throughput in tests with 10 VMs across different hypervisors.                            |
|   6 | Octavia load balancers do not function correctly in VxLAN networks due to known upstream issues with distributed floating IPs.                          |
|   7 | A missing script to sync the Northbound database caused load balancer failures after manual database cleanup.                                           |
|   8 | A bug was identified where deleting a pool with shared backend members wiped IP port mappings, rendering load balancers unreachable.                    |
|   9 | Extending external network IP pools by increasing subnet size failed, requiring the creation of a new subnet as a workaround.                           |
|  10 | East-west traffic between VMs in different subnets failed to reach load balancers due to ARP request issues in virtual routers.                         |
|  11 | Restricted security groups on backend VMs caused connection failures because the source IP was the load balancer's public IP rather than the tenant IP. |
|  12 | Load balancers require a virtual router attached to the subnet to function, even for isolated networks without external connectivity.                   |
|  13 | The Horizon dashboard does not support Octavia load balancers because it only supports the source port algorithm.                                       |
|  14 | An upgrade from Antelope to Caracal caused Neutron instability due to high load from the schedule_new_gateway command.                                  |
|  15 | Changing the chassis selection strategy from least_load to chance restored service stability after the upgrade.                                         |
|  16 | The team recommends documenting corner cases, improving debug tools like OVN trace, and fostering community collaboration for issue resolution.         |

# Video

[![Video thumbnail](https://img.youtube.com/vi/hS2Ytpo9mpM/hqdefault.jpg)](https://www.youtube.com/watch?v=hS2Ytpo9mpM)

[Watch on YouTube](https://www.youtube.com/watch?v=hS2Ytpo9mpM)
