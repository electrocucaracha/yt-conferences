---
layout: default
title: "Live Demo: How the OpenInfra Ecosystem is Tackling VMware Migration with OpenStack"
nav_order: 6
parent: OpenInfra Summit Europe 2025
type: Video Note
description: "The video features a live demonstration by five organizations—Rackspace, Zconverter, Canonical, Vortex, and Red Hat—showcasing various methods for migrating workloads from VMware to OpenStack."
resource: "https://www.youtube.com/watch?v=slOxTkVEiSE"
youtube_stats:
  view_count: 855
  like_count: 15
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

The video features a live demonstration by five organizations—Rackspace, Zconverter, Canonical, Vortex, and Red Hat—showcasing various methods for migrating workloads from VMware to OpenStack.
Citing market research that predicts VMware will lose significant market share to open-source alternatives, the presenters highlight the ease and flexibility of these migrations using different tools and environments.
Rackspace and Canonical utilized the Coriolis tool to migrate virtual machines across different cloud infrastructures, while Red Hat employed Ansible automation to orchestrate the migration to its OpenShift-based OpenStack service.
Vortex demonstrated the use of the community-driven OS Migrate tool, and Zconverter presented a container-based migration approach that emphasizes eliminating vendor lock-in and automating large-scale migrations.
The session concluded with all teams successfully completing their respective migrations, underscoring the viability of OpenStack as a robust, zero-downtime alternative for enterprises seeking to move away from VMware.

# Main Points

|   # | Main point                                                                                                                                                            |
| --: | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Gartner predicts VMware will lose up to 30% of its market share by 2029, creating a significant opportunity for OpenStack and open source.                            |
|   2 | Forrester indicates that open source is the top choice for VMware users seeking alternatives.                                                                         |
|   3 | Five organizations demonstrated live migrations from VMware to OpenStack using various tools and methods.                                                             |
|   4 | Rackspace used Coriolis from Cloudbase to migrate workloads from a private cloud in Chicago to a public OpenStack Flex cloud in Dallas.                               |
|   5 | The Rackspace migration spanned approximately 1,400 kilometers over the public internet while maintaining zero downtime behind a load balancer.                       |
|   6 | Zconverter utilized its G-Converter technology combined with native import and export to perform container-based migrations.                                          |
|   7 | Zconverter’s solution enables flexible movement across any hypervisor or cloud platform, eliminating vendor lock-in.                                                  |
|   8 | The Zconverter approach includes built-in backup features during migration and supports automated migration drills to reduce human error.                             |
|   9 | Canonical partnered with Cloudbase to use Coriolis for an automated lift-and-shift migration to their OpenStack environment.                                          |
|  10 | Canonical emphasizes building a cloud-native, resilient, and secure environment using their Sunbeam project, which integrates Kubernetes with OpenStack.              |
|  11 | Vortex, a French-based company, used the OS Migrate community tool, specifically the VMware migration kit, for their demonstration.                                   |
|  12 | The Vortex process involves creating a conversion host on the OpenStack side to synchronize data and launch instances after conversion.                               |
|  13 | Red Hat leveraged its Ansible Automation Platform to orchestrate the entire migration process from discovery to workload movement.                                    |
|  14 | Red Hat migrated a virtual machine to RHOSE (Red Hat OpenStack Services on OpenShift) using a warm migration technique.                                               |
|  15 | Warm migration utilizes change block tracking to minimize downtime by transferring only changed data since the last synchronization.                                  |
|  16 | Complex VMware installations require assessment of underlying applications and dependencies, which can be addressed with community open source tools.                 |
|  17 | Canonical notes that the actual VM migration represents only about 20% of the total work, with the remaining 80% focused on designing a highly available environment. |
|  18 | Rackspace highlighted that healthcare and financial sectors are increasingly adopting cloud capabilities for data storage and infrastructure re-evaluation.           |
|  19 | The successful demonstrations show that migrations can be performed without administrative rights in the target OpenStack cloud.                                      |
|  20 | A follow-up event called VM Migration Day was announced for further discussions on VMware to OpenStack migration strategies.                                          |

# Video

[![Video thumbnail](https://img.youtube.com/vi/slOxTkVEiSE/hqdefault.jpg)](https://www.youtube.com/watch?v=slOxTkVEiSE)

[Watch on YouTube](https://www.youtube.com/watch?v=slOxTkVEiSE)
