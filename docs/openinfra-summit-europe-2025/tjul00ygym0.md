---
layout: default
title: "Beyond Neutron's core: Building your own L3 plugin"
nav_order: 96
parent: OpenInfra Summit Europe 2025
type: Video Note
description: "This workshop, led by Alejandro Garcia and Felipe, guides participants through building a basic Layer 3 plugin for OpenStack Neutron to extend its networking capabilities."
resource: "https://www.youtube.com/watch?v=Tjul00YGyM0"
youtube_stats:
  view_count: 68
  like_count: 1
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

This workshop, led by Alejandro Garcia and Felipe, guides participants through building a basic Layer 3 plugin for OpenStack Neutron to extend its networking capabilities.
The session focuses on intercepting Neutron’s router creation and deletion methods using Python callbacks to mock a standard router with a BIOS virtual machine, a technique used to support open networking devices in production environments.
Participants access remote OpenStack environments via SSH tunnels and modify the Neutron server code within a Docker container to implement logic that creates, configures, and deletes these virtual router instances.
The practical exercises involve configuring service providers, creating network flavors, and attaching interfaces to the virtual router to enable traffic routing between two private networks.
The workshop concludes with a successful connectivity test, where participants ping one virtual machine from another across different networks, demonstrating that the custom plugin effectively routes traffic through the BIOS VM.

# Main Points

|   # | Main point                                                                                                                                                                     |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   1 | The workshop focuses on building a Neutron Layer 3 plugin to extend OpenStack networking functionality using artificial intelligence concepts.                                 |
|   2 | The goal is to intercept OpenStack router primitives and implement custom logic, such as mocking a router with a virtual machine.                                              |
|   3 | Participants access pre-deployed OpenStack environments via a remote desktop using an SSH tunnel and specific credentials from a provided spreadsheet.                         |
|   4 | The lab environment uses containers for OpenStack services, allowing direct modification of the Neutron server code and container restarts to apply changes.                   |
|   5 | The first activity involves inspecting the Neutron configuration file to verify the service provider settings for the custom L3 router plugin.                                 |
|   6 | Participants inspect the existing Python class for the plugin, which includes helper methods for Nova and Neutron API interactions.                                            |
|   7 | The second activity implements the logic for the `process_router_create` and `process_router_delete` callbacks to create and delete a BIOS virtual machine acting as a router. |
|   8 | The third activity modifies the `process_add_router_interface` method to create mirror ports and attach them to the virtual machine for network connectivity.                  |
|   9 | The final activity tests connectivity by configuring default routes on test VMs and pinging between two private networks through the BIOS router VM.                           |
|  10 | In production, this approach is used to configure physical data center fabric devices via an SDN controller rather than virtual machines.                                      |
|  11 | The plugin architecture allows for multiple flavor profiles, each linked to different Python classes to implement varied routing logic.                                        |
|  12 | Participants are encouraged to use the provided slides to copy and paste code snippets to ensure correct indentation and syntax.                                               |
|  13 | The workshop demonstrates that Neutron plugins can intercept various OpenStack commands, including router creation, port attachment, and floating IP assignments.              |
|  14 | The BIOS virtual machine used in the lab routes traffic by default without additional configuration once interfaces are attached and IPs are assigned.                         |
|  15 | Attendees are advised to use Chrome for the remote desktop connection due to compatibility issues with other browsers.                                                         |
|  16 | The plugin code is registered in the Neutron server container and invoked whenever specific router operations are performed via the OpenStack API.                             |
|  17 | The workshop concludes with a demonstration of successful inter-network communication, validating the custom L3 plugin implementation.                                         |

# Video

[![Video thumbnail](https://img.youtube.com/vi/Tjul00YGyM0/hqdefault.jpg)](https://www.youtube.com/watch?v=Tjul00YGyM0)

[Watch on YouTube](https://www.youtube.com/watch?v=Tjul00YGyM0)
