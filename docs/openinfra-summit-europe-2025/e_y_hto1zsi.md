---
layout: default
title: "Ironic at your Service!"
nav_order: 88
parent: OpenInfra Summit Europe 2025
type: Video Note
description: 'This presentation details advancements in Ironic, an OpenStack-based bare-metal provisioning service, specifically focusing on the new "servicing" feature that allows for firmware upgrades and BIOS...'
resource: "https://www.youtube.com/watch?v=e_y_hTO1ZsI"
youtube_stats:
  view_count: 77
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

This presentation details advancements in Ironic, an OpenStack-based bare-metal provisioning service, specifically focusing on the new "servicing" feature that allows for firmware upgrades and BIOS configuration changes on already provisioned nodes.
The speakers explain that while traditional "cleaning" operations occur during initial deployment, servicing enables day-two maintenance tasks, such as applying critical firmware updates or downgrades, without requiring the node to be deprovisioned and redeployed.
The technical implementation relies on Redfish APIs to communicate with the Baseboard Management Controller (BMC), allowing for out-of-band updates that are triggered via Ironic’s provision API or through the Metal³ project, a CNCF incubating project that uses Ironic as its backend for Kubernetes integration.
Live demonstrations showcased the end-to-end process of upgrading and downgrading firmware on Dell servers, highlighting how the system manages state transitions, reboots, and validation to ensure the hardware successfully applies the new versions.
Future development plans include improving resilience against unresponsive BMCs, adding the ability to abort failed operations, reducing overall update time by minimizing unnecessary reboots, and exploring the application of multiple firmware changes simultaneously to enhance operational efficiency.

# Main Points

|   # | Main point                                                                                                                                              |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Ironic is an OpenStack environmental provisioning service used for bare metal node operations like discovery, inspection, and provisioning.             |
|   2 | The presentation focuses on advancing the servicing process for already provisioned nodes, specifically for firmware upgrades and BIOS settings.        |
|   3 | Metal Cube is an incubating CNCF project that uses Ironic as its backend to provide bare metal provisioning for Kubernetes.                             |
|   4 | The mission is to ensure bare metal clouds are easy to manage and maintain a good operational state by enforcing firmware versions and configurations.  |
|   5 | Keeping firmware up to date is essential for stability, regulatory compliance, and feature availability, while downgrades may be required for bugfixes. |
|   6 | Initial implementations were vendor-specific and limited to manual cleaning operations before deployment, which caused significant downtime.            |
|   7 | The Flamingo cycle introduces a merged feature combining cleaning and servicing to allow operations on both day one and day two nodes.                  |
|   8 | Firmware upgrades are currently supported for BIOS, system firmware, BMC, and Android components.                                                       |
|   9 | Jacob improved operation times, added resilience, and enabled servicing for firmware upgrades and settings on provisioned nodes.                        |
|  10 | The underlying implementation relies on Redfish APIs using GET, POST, and PATCH requests to query and update firmware and settings.                     |
|  11 | Ironic implements servicing through the provision API by setting the node to a servicing state and specifying the upgrade stack and image.              |
|  12 | The bare metal CLI allows users to monitor firmware versions and issue commands for firmware updates or BIOS settings changes.                          |
|  13 | Metal Cube exposes these features through custom resources and a post-update policy that defines whether operations apply as day one or day two.        |
|  14 | A demo demonstrated an Ironic firmware upgrade from version 219 to 224 using the simple update mechanism and BMC image download.                        |
|  15 | The upgrade process involves the BMC downloading the image, rebooting to apply the BIOS package, and using a RAM disk to validate successful reboots.   |
|  16 | A second demo showed a Metal Cube firmware downgrade from version 263 to 235 triggered by a reboot annotation in the host update policy.                |
|  17 | Future work includes handling unresponsive BMCs after updates by actively checking responsiveness across multiple resources.                            |
|  18 | A service abort feature is being developed to allow backing out of interrupted firmware upgrade steps rather than retrying indefinitely.                |
|  19 | Efforts are underway to reduce operation time by exploring Redfish facilities to track reboots without using the RAM disk.                              |
|  20 | The team is investigating the possibility of applying multiple firmware updates and settings changes simultaneously to improve efficiency.              |
|  21 | Firmware images must be hosted on an HTTP source accessible by the BMC, as Ironic does not provide a built-in web server for images.                    |
|  22 | Ironic tracks installed firmware versions but does not validate images, leaving that responsibility to the vendor and BMC.                              |
|  23 | Testing has been performed on Dell and Supermicro hardware, with support intended for any reasonable Redfish implementation.                            |
|  24 | Servicing is recommended for nodes with deployed images, while cleaning is used for unprovisioned nodes or those requiring deprovisioning.              |
|  25 | Special service steps like hold, power off, and power on allow for manual intervention during the servicing process.                                    |
|  26 | Maintenance mode is distinct from servicing and is used for severe issues like unreachable BMCs, whereas servicing handles operational updates.         |

# Video

[![Video thumbnail](https://img.youtube.com/vi/e_y_hTO1ZsI/hqdefault.jpg)](https://www.youtube.com/watch?v=e_y_hTO1ZsI)

[Watch on YouTube](https://www.youtube.com/watch?v=e_y_hTO1ZsI)
