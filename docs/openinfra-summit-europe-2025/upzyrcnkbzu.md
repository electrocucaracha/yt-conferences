---
layout: default
title: "VFIO improvements, Resource Reservation and smarter allocations  What’s New in Nova making life bett"
nav_order: 112
parent: OpenInfra Summit Europe 2025
type: Video Note
description: "This presentation by a Red Hat software engineer outlines key updates in the Nova project, focusing on improved support for NVIDIA GPUs via VFIO variant drivers."
resource: "https://www.youtube.com/watch?v=UPZyRcNkbZU"
youtube_stats:
  view_count: 54
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

This presentation by a Red Hat software engineer outlines key updates in the Nova project, focusing on improved support for NVIDIA GPUs via VFIO variant drivers.
The speaker explains that new kernels expose GPUs as standard PCI devices, requiring the use of PCI placement and custom resource classes to manage device assignment and live migration effectively.
Additionally, the session introduces "one-time use" devices, a feature that allows operators to reserve hardware like NVMe disks for manual cleanup or firmware updates before they can be reallocated to instances.
A significant algorithmic improvement to the placement service is also detailed, which now permits migrations and resizes even when a compute node is at capacity, provided the action does not worsen the resource situation.
Finally, the presenter requests community assistance in testing the transition to native tracing and encourages participation in the upcoming Virtual Technical Planning Group to discuss future feature development.

# Main Points

|   # | Main point                                                                                                                                                                                        |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | The presentation covers new Nova features including VFIO variant driver support, one-time use devices, and improved placement logic for capacity limits.                                          |
|   2 | VFIO variant driver support was introduced to handle new GPU exposure methods in Ubuntu Noble and RHEL 9, where GPUs appear as standard PCI devices rather than mediated devices.                 |
|   3 | This feature leverages existing PCI pass-through and VFIO integrations to enable device assignment and live migration for Nvidia GPUs and other compatible devices.                               |
|   4 | Configuring GPU types involves using special files in the sysfs directory to set current and creatable vGPU types, which determines the number of available virtual devices based on memory size. |
|   5 | Enabling PCI placement is required to distinguish between different vGPU types during device selection, as legacy matching relies only on vendor and product IDs.                                 |
|   6 | PCI placement configuration is irreversible and should be tested in non-production environments before deployment to avoid operational issues.                                                    |
|   7 | New configuration parameters include 'manage_control' to determine if Nova or the driver handles device state changes, and 'live_migratable' to specify if a device supports live migration.      |
|   8 | Flavor configuration requires defining PCI pass-through properties with specific alias names and quantities, subject to limitations on mapping multiple devices per VM.                           |
|   9 | Live migration of vGPUs involves transferring memory from source to destination hosts, allowing workloads to resume without interruption if compatible devices are available.                     |
|  10 | One-time use devices allow operators to mark devices for manual cleanup or firmware updates before reuse, preventing automatic reallocation after instance destruction.                           |
|  11 | When a one-time use device is released, it remains reserved in placement until the operator manually resets its state using OpenStack provider inventory commands.                                |
|  12 | A new repository provides example scripts for managing one-time use devices, serving as a starting point for custom cleanup workflows.                                                            |
|  13 | Placement logic has been improved to allow allocations that reduce or maintain capacity, even when a compute node is over capacity, enabling migrations and resizes without manual intervention.  |
|  14 | This change removes the need for operators to manually adjust allocation ratios or unreserve resources during capacity recovery scenarios.                                                        |
|  15 | The project is transitioning from the asn1 library to native tracing for performance improvements, requiring testing from operators via environment variables.                                    |
|  16 | Users are encouraged to report bugs related to native tracing and participate in the upcoming PTG to discuss new feature requests and viability.                                                  |
|  17 | PCI placement is not enabled by default due to performance concerns with candidate selection algorithms and the need for further testing before making it standard behavior.                      |
|  18 | Migration scheduling matches devices by vGPU type rather than specific PCI addresses, ensuring the correct device is selected on the destination host.                                            |
|  19 | The transition to native tracing is planned for all OpenStack services, with Nova completing the migration for its compute component in the current cycle.                                        |

# Video

[![Video thumbnail](https://img.youtube.com/vi/UPZyRcNkbZU/hqdefault.jpg)](https://www.youtube.com/watch?v=UPZyRcNkbZU)

[Watch on YouTube](https://www.youtube.com/watch?v=UPZyRcNkbZU)
