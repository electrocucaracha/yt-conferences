---
layout: default
title: "OVN traffic flow & Troubleshooting"
nav_order: 5
parent: OpenInfra Summit Europe 2025
type: Video Note
description: "This presentation provides a beginner-level overview of OVN (Open Virtual Network) traffic flow and troubleshooting within OpenStack, delivered by a cloud architect with extensive experience in pri..."
resource: "https://www.youtube.com/watch?v=qtcYjFeCDOU"
youtube_stats:
  view_count: 923
  like_count: 14
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

This presentation provides a beginner-level overview of OVN (Open Virtual Network) traffic flow and troubleshooting within OpenStack, delivered by a cloud architect with extensive experience in private cloud implementations.
The speaker explains the core architecture, distinguishing between the north bridge, which handles the control plane and translates Neutron objects, and the south bridge, which manages the data path and configures compute nodes.
Key topics include the mapping of Neutron resources to OVN objects, such as logical switches, ports, and routers, with specific attention to how DHCP, DNS, and metadata services are handled internally by OVN rather than traditional agents.
The session details the native high-availability system for virtual routers, explaining how traffic is distributed across multiple chassis using priority tables, and clarifies the differences between distributed and non-distributed floating IPs.
Finally, the speaker shares practical troubleshooting examples, including resolving duplicate metadata agents after power cuts, addressing packet fragmentation issues between private networks, and utilizing the `ovn-nbctl` trace tool and migration scripts to debug and maintain synchronization between Neutron and OVN databases.

# Main Points

|   # | Main point                                                                                                                                                      |
| --: | --------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | The session covers OVN traffic flow, architecture, resource mapping, and troubleshooting for OpenStack.                                                         |
|   2 | OVN uses the ML2 plugin with VSTP protocol and events instead of legacy OVS, featuring a unique HA system based on EV.                                          |
|   3 | The architecture consists of a North Bridge for control plane and a South Bridge for data path configuration on compute nodes.                                  |
|   4 | OVN controllers can operate in different gateway modes to handle north-south or east-west traffic across the cluster.                                           |
|   5 | Debugging requires understanding the underlying OVSDB server and mapping Neutron objects to OVN logical objects.                                                |
|   6 | Users should check external IDs in OVN resources to verify if data was correctly copied from the Neutron database.                                              |
|   7 | DNS records for private networks are created in the OVN database, enabling internal name resolution without external cluster traffic.                           |
|   8 | Logical ports in OVN have various types, including compute ports, router ports, localnet ports for provider networks, and local ports for metadata.             |
|   9 | DHCP options are mapped to a special table in OVN, and responses are handled by local OVN controllers on compute nodes rather than the virtual router.          |
|  10 | Virtual routers use a native HA system with multiple chassis copies, where the active interface is determined by priority settings in the gateway chassis list. |
|  11 | OVN agents include a controller agent for configuration and a gateway agent that handles HA routers and traffic absorption.                                     |
|  12 | A common issue after unprepared host shutdowns is duplicated metadata in the controller agent, which may require manual chassis removal to fix.                 |
|  13 | Packet fragmentation issues between private networks with different MTUs were fixed in the 2024.2 OpenStack release.                                            |
|  14 | Switching between DVR and non-DVR floating IPs involves modifying specific external marks in the OVN database.                                                  |
|  15 | Inconsistent OVN bridge mappings across nodes are a frequent cause of VM launch failures on specific hosts.                                                     |
|  16 | The OVN trace tool is recommended for debugging unicast traffic paths from private to public networks.                                                          |
|  17 | The migration script from Neutron ML2 to OVN includes check and repair keys to detect and fix database desynchronization.                                       |

# Video

[![Video thumbnail](https://img.youtube.com/vi/qtcYjFeCDOU/hqdefault.jpg)](https://www.youtube.com/watch?v=qtcYjFeCDOU)

[Watch on YouTube](https://www.youtube.com/watch?v=qtcYjFeCDOU)
