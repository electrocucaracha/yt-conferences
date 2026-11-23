---
layout: default
title: Improve connectivity issues at live migrations
nav_order: 94
parent: OpenInfra Summit Europe 2025
type: Video Note
description: Max Lamri and Hoffmann from the Schwarz Group and Cloud Technologies presented a solution to connectivity issues experienced during live migrations of small virtual machines in OpenStack environmen...
resource: "https://www.youtube.com/watch?v=POjSOxKyrE0"
youtube_stats:
  view_count: 68
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

Max Lamri and Hoffmann from the Schwarz Group and Cloud Technologies presented a solution to connectivity issues experienced during live migrations of small virtual machines in OpenStack environments using OVN.
They identified that the root cause was a significant delay in the OVN Northd service propagating port binding changes from the northbound to the southbound database, which resulted in packet loss and downtime of up to 30 seconds.
To address this, they implemented a temporary production fix where Nova waits for the OVN controller to apply flows before proceeding, while also contributing upstream improvements like incremental engines to reduce reconciliation times from 30 seconds to 3 seconds.
For a long-term, upstream-acceptable solution, they proposed modifying Neutron to send migration completion events only after the "additional chassis" field is set in the southbound database, ensuring the network is fully ready before the migration switch-over.
This approach requires coordinating changes between Nova, Neutron, and Libvirt to trigger port creation earlier and validate the correct state, a proposal currently under discussion with the OpenStack community.

# Main Points

|   # | Main point                                                                                                                                                                                         |
| --: | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | The presentation addresses connectivity issues and packet loss lasting up to 30 seconds during live migrations of small virtual machines in an OpenStack environment using OVN.                    |
|   2 | The issue was reported by internal teams and customers, primarily affecting load balancer VMs, and was reproducible only with small VMs, not those with over 100 GB of memory.                     |
|   3 | Live migration in OpenStack involves pre-checks, pre-migration setup including port binding via Neutron, actual memory and storage synchronization, and post-migration cleanup.                    |
|   4 | OVN architecture separates logical network data in the Northbound database from physical flow information in the Southbound database, with OVN controllers on compute nodes watching for changes.  |
|   5 | During migration, Neutron updates the Northbound database with multi-chassis bindings and activation strategies, which OVN Northd must then propagate to the Southbound database.                  |
|   6 | Debugging revealed a significant delay of up to 11 seconds between the Northbound update and the Southbound database reflecting the port binding changes, causing connectivity loss.               |
|   7 | The root cause was identified as OVN Northd being too slow to reconcile changes, exacerbated by large database sizes with over 100,000 ports and 5,000 routers.                                    |
|   8 | OVN Northd leader election failures could cause reconnection delays of up to 90 seconds, during which no network changes are propagated, leading to prolonged outages.                             |
|   9 | A temporary production fix involved modifying Nova to create the tap interface early and busy-waiting for the OVN installed flag in the local OVSDB to ensure flows were applied before migration. |
|  10 | This workaround was rejected upstream because Nova should not be responsible for waiting on Neutron or OVN internal states, violating architectural separation of concerns.                        |
|  11 | Upstream improvements included upgrading to OVN 24.3 and contributing incremental engines for BFD and IP addresses, reducing reconciliation time from 30 seconds to 3 seconds.                     |
|  12 | A proposed proper solution involves changing Neutron to send the migration-ready event to Nova only after the additional chassis field is set in the Southbound database.                          |
|  13 | This approach requires Nova to trigger port creation earlier, potentially via Swift, and adjust Libvirt to accept pre-existing tap interfaces for OVN-managed ports.                               |
|  14 | The team is seeking upstream feedback on this proposal, which includes adding a port property to distinguish OVN ports requiring early creation from standard ports.                               |
|  15 | Investigation took approximately two to three months, utilizing OVSDB client tools to trace transaction timelines and identify the specific delay in database propagation.                         |
|  16 | OVSDB server single-threadedness remains a performance bottleneck, especially during mass client reconnections, though OVSDB relays help mitigate network and CPU load.                            |
|  17 | The current production environment runs the temporary fix, while the team continues to refine and submit the proposed architectural changes to the OpenStack community.                            |

# Video

[![Video thumbnail](https://img.youtube.com/vi/POjSOxKyrE0/hqdefault.jpg)](https://www.youtube.com/watch?v=POjSOxKyrE0)

[Watch on YouTube](https://www.youtube.com/watch?v=POjSOxKyrE0)
