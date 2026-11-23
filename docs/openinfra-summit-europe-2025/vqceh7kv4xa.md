---
layout: default
title: Ironic Project Updates
nav_order: 79
parent: OpenInfra Summit Europe 2025
type: Video Note
description: "The Ironic project team presented significant architectural updates, most notably the removal of the eventlet library in favor of native operating system threads to improve CPU core usage and reduc..."
resource: "https://www.youtube.com/watch?v=vQcEH7KV4xA"
youtube_stats:
  view_count: 85
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

The Ironic project team presented significant architectural updates, most notably the removal of the eventlet library in favor of native operating system threads to improve CPU core usage and reduce bugs, a change that requires careful performance testing before production deployment.
The team also highlighted the deprecation and removal of several legacy components, including the in-band Ironic Inspector (whose features have been integrated into Ironic), Metalmith, and the SNMP driver, while emphasizing the removal of Python 3.9 support and the transition to newer Python versions.
Substantial improvements were made to the servicing and firmware update workflows, introducing features such as runbooks for custom cleaning, the ability to abort servicing operations, and more efficient Redfish-based inspection that reduces the need for reboots.
Additionally, the presentation covered security enhancements, including the resolution of a file path vulnerability, and outlined future work areas such as advanced networking, storage improvements, and graphical console support, while also detailing community efforts like the Outreachy internship program and upcoming virtual project team gatherings.

# Main Points

|   # | Main point                                                                                                                                                                                |
| --: | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Ironic is an open-source project under the OpenStack umbrella for bare-metal provisioning and management, including discovery, cataloging, and lifecycle servicing.                       |
|   2 | The eventlet library has been removed in favor of native operating system threads to improve CPU core usage and reduce bugs, requiring performance testing before production migration.   |
|   3 | Redfish inspection is being enhanced to achieve feature parity with the deprecated in-band inspector, allowing API-driven inspection rules and external API calls within workflows.       |
|   4 | A bugfix ensures conductor records are cleaned up properly to prevent accumulation in large deployments.                                                                                  |
|   5 | Servicing improvements include logging steps in node history, BMC clock management to resolve certificate validation issues, and the ability to abort servicing if firmware updates fail. |
|   6 | Runbooks have been introduced to allow custom cleaning workflows without modifying hardware managers, providing a more user-friendly implementation.                                      |
|   7 | Firmware updates now use the Redfish simple update API to avoid unnecessary reboots into IPA, saving time during the update process.                                                      |
|   8 | Security vulnerabilities, including arbitrary file access via file paths, have been resolved by restricting file serving to explicitly configured paths.                                  |
|   9 | Python 3.9 support has been removed, and the project now supports only Python 3.10 or higher, requiring updates to CI pipelines and IPA builds.                                           |
|  10 | Root support has been removed due to security concerns, and the SNMP driver is deprecated and scheduled for removal due to reliance on outdated libraries.                                |
|  11 | Ironic-inspector and metalmith have been removed; users are advised to use Bifrost or MetalCube for standalone Ironic testing and deployment.                                             |
|  12 | Bifrost has dropped support for CentOS 9 and VM 11 due to Python incompatibilities and maintenance costs, while adding support for OCI artifact registries.                               |
|  13 | MetalCube, a CNCF incubating project, uses Ironic as its core engine and provides a new Ironic operator for managing Ironic lifecycles within Kubernetes clusters.                        |
|  14 | The Outreachy internship program supports underrepresented groups in open source, with recent projects focusing on setting server BMC clocks using Redfish.                               |
|  15 | Future work includes improvements to networking, storage, graphical console support, bulk action workflows, and expanded Redfish hardware support.                                        |
|  16 | A virtual Project Team Gathering (PTG) is scheduled for the week after next to discuss these future enhancements and gather community input.                                              |
|  17 | CentOS 10 images for IPA are being built but not yet officially published due to hardware driver limitations and CI testing requirements.                                                 |
|  18 | The default time skew window for the agent remains at one hour, with discussions ongoing regarding compatibility with local time zones for certain operating systems.                     |

# Video

[![Video thumbnail](https://img.youtube.com/vi/vQcEH7KV4xA/hqdefault.jpg)](https://www.youtube.com/watch?v=vQcEH7KV4xA)

[Watch on YouTube](https://www.youtube.com/watch?v=vQcEH7KV4xA)
