---
layout: default
title:
  "Project Lightning Talk: Bare Metal Provisioning With Tinkerbell - Jacob Weinstock,
  Maintainer"
nav_order: 252
parent: Kubecon Cloudnativecon Europe 2026
type: Video Note
description:
  Jacob Weintock, the core maintainer of the Tinkerbell project, introduces
  Tinkerbell as a Kubernetes-native bare metal provisioning engine designed to simplify
  and modernize the process of provisioning physical hardware. Unlike older techno...
resource: https://www.youtube.com/watch?v=DvsMNlrOxcM
tags:
  - kubecon-cloudnativecon-europe-2026
  - video
  - learning
status: stable
generated:
  by: process:yt-conferences-okf
  at: 2026-09-12 00:00:00+00:00
---

# Summary

Jacob Weintock, the core maintainer of the Tinkerbell project, introduces Tinkerbell as a Kubernetes-native bare metal provisioning engine designed to simplify and modernize the process of provisioning physical hardware.
Unlike older technologies like Kickstart or PXE booting, Tinkerbell uses Kubernetes Custom Resource Definitions (CRDs) to define hardware and installation templates, which are combined into workflows for tasks such as disk imaging, partitioning, and power operations.
Recent features include a read-only web UI, the new Captain OS (successor to Hook OS), serial over SSH for secure console access, and discovery modes for automatic hardware detection and workflow assignment.
Tinkerbell offers a single-binary deployment with zero external dependencies, supports various DHCP and static provisioning modes, and allows integration of custom CRDs through hardware references.
Upcoming enhancements include expanded data source support, new specifications, and greater flexibility for Kubernetes installations via the cap t provider, with opportunities for community involvement through meetings, sessions, and demos.

# Main Points

|   # | Main point                                                                                                          |
| --: | ------------------------------------------------------------------------------------------------------------------- |
|   1 | Jacob Weintock is the core maintainer of the Tinkerbell project.                                                    |
|   2 | Tinkerbell is a Kubernetes native bare metal provisioning engine.                                                   |
|   3 | Tinkerbell uses CRDs (Custom Resource Definitions) for hardware and templates.                                      |
|   4 | Hardware CRD defines disk, network, and hardware details.                                                           |
|   5 | Template defines operating system installation steps, similar to CI system manifests.                               |
|   6 | Combining hardware and template objects creates a workflow.                                                         |
|   7 | Workflows enable power operations, PXE boot, ISO mounting, static layer 3 provisioning, installations, and reboots. |
|   8 | Tinkerbell is fully Kubernetes native.                                                                              |
|   9 | Recent features include a readonly web UI and Captain OS (successor to Hook OS).                                    |
|  10 | Serial over SSH allows SSH access to BMC consoles using public keys.                                                |
|  11 | Discovery mode enables auto-discovery of machines and automatic CRD creation and workflow execution.                |
|  12 | Tinkerbell can be deployed as a single binary with zero external dependencies for initial setup.                    |
|  13 | Supports multiple DHCP modes and fully static layer 3 provisioning.                                                 |
|  14 | Hardware references allow integration of custom CRDs into Tinkerbell.                                               |
|  15 | Upcoming features: support for no cloud data source, new spec, extended template and workflow references.           |
|  16 | Tinkerbell supports full Kubernetes installations via the cap t provider.                                           |
|  17 | Will support running Tinkerbell externally to an existing Cappy structure for more flexibility.                     |
|  18 | Community meetings are held every Tuesday on CNCF Slack.                                                            |
|  19 | Project information is available on the site and GitHub.                                                            |
|  20 | Upcoming sessions include a contributor meeting and a project booth for demos.                                      |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=DvsMNlrOxcM)
