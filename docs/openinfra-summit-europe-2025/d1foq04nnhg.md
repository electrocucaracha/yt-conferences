---
layout: default
title: Migrating Neutron from Linux Bridge to OVN
nav_order: 34
parent: OpenInfra Summit Europe 2025
type: Video Note
description: "CERN’s OpenStack team, led by Lu, Kuba, and Daniel, presented their migration strategy from the deprecated Linux bridge to OVN (Open Virtual Network) to modernize their cloud networking capabilities."
resource: "https://www.youtube.com/watch?v=D1FOQ04NNhg"
youtube_stats:
  view_count: 199
  like_count: 4
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

CERN’s OpenStack team, led by Lu, Kuba, and Daniel, presented their migration strategy from the deprecated Linux bridge to OVN (Open Virtual Network) to modernize their cloud networking capabilities.
Operating one of the world’s largest particle physics facilities, CERN runs two data centers on OpenStack, having previously relied on basic Linux bridge networking since 2013.
The team adopted a phased approach to mitigate risk, first deploying OVN in a new data center and then migrating the legacy infrastructure by enabling OVN and Linux bridge to coexist within the Neutron control plane.
This allowed for a gradual transition using cross-cell cold migrations for hardware refurbishments and live migrations for remaining capacity, avoiding a single high-risk downtime event.
Key challenges included significant memory consumption increases, database synchronization conflicts during the initial sync of 15,000 ports, and complex issues with cross-cell migrations such as RPC timeouts and lost TPM or key pair data.
Despite these hurdles, the team successfully verified that running both drivers side-by-side is a stable and preferred method, achieving approximately one-third completion of the migration while maintaining service stability and preparing for future advanced networking features.

# Main Points

|   # | Main point                                                                                                                             |
| --: | -------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | CERN migrated its OpenStack networking from Linux bridge to OVN to modernize capabilities and support advanced features.               |
|   2 | The migration was driven by the deprecation of Linux bridge and the need to offer better networking options to users.                  |
|   3 | A new data center deployed in 2024 used OVN from the start, while the older facility required a complex migration strategy.            |
|   4 | Scalability tests involved spawning 2,000 hypervisors and 14,000 virtual machines to validate OVN performance before full migration.   |
|   5 | The team adopted a phased approach to allow Linux bridge and OVN to coexist, avoiding a single high-risk downtime event.               |
|   6 | Initial synchronization of 15,000 ports took 24 hours, causing conflicts with continuous port creation and deletion operations.        |
|   7 | Enabling OVN as a mechanism driver resulted in an 8 to 10 times increase in memory consumption for Neutron services.                   |
|   8 | Neutron startup processes incorrectly reported Linux bridge ports as down, requiring a patch to ignore non-ovn ports.                  |
|   9 | Cross-cell resizes were used to migrate workloads to new AMD hardware, as live migration between Intel and AMD CPUs was impossible.    |
|  10 | Cross-cell migrations revealed issues with lost port binding information and accidental deletion of vTPM secrets.                      |
|  11 | Live migrations from Linux bridge to OVN required two steps due to bridge name mismatches in the Nova cache.                           |
|  12 | A code patch was applied to force the correct OVN bridge name during the first live migration step.                                    |
|  13 | OVN DHCP replaced the central DHCP service, providing immediate lease updates but lacking IPv6 privacy extension support.              |
|  14 | The team disabled OVN's automatic DNS resolution to rely on the site's existing DNS infrastructure.                                    |
|  15 | Network performance is generally stable, though some high-intensity workloads show packet drops that require further investigation.    |
|  16 | The migration is approximately one-third complete, with remaining work planned for the next year alongside data center refurbishments. |
|  17 | Operators maintain a community of practice to share experiences and solutions regarding OVN migrations.                                |
|  18 | Detailed technical documentation and blog posts are available for those wishing to replicate the migration process.                    |

# Video

[![Video thumbnail](https://img.youtube.com/vi/D1FOQ04NNhg/hqdefault.jpg)](https://www.youtube.com/watch?v=D1FOQ04NNhg)

[Watch on YouTube](https://www.youtube.com/watch?v=D1FOQ04NNhg)
