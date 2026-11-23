---
layout: default
title: "Digging Through the Toolbox:  Ten Years of Ironic Features"
nav_order: 116
parent: OpenInfra Summit Europe 2025
type: Video Note
description: "Jay Faulner, an OSS developer at G Research, presents a condensed overview of the Ironic bare metal provisioning project, emphasizing that its extensive feature set is best understood through its o..."
resource: "https://www.youtube.com/watch?v=cuCOLz-YrTI"
youtube_stats:
  view_count: 52
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

Jay Faulner, an OSS developer at G Research, presents a condensed overview of the Ironic bare metal provisioning project, emphasizing that its extensive feature set is best understood through its official documentation.
The talk details Ironic’s architecture, which relies on conductors to manage hardware via in-band agents or out-of-band BMC interfaces, and introduces the concept of hardware types as pluggable collections of interfaces for specific server capabilities.
Faulner explains the node lifecycle, covering onboarding, automated cleaning, deployment, and retirement, while highlighting new features such as runbooks for standardized maintenance workflows, node servicing for active instances, and the integration of the inspector service directly into Ironic to reduce operational complexity.
The presentation also explores various deployment drivers, including direct, Anaconda, and Ansible, alongside operational tools like conductor groups, sharding for scaling, and node history for auditing.
Finally, Faulner discusses recent advancements in user access, such as project-based ownership and lease management, and mentions new capabilities like BootC and OCI image support, encouraging community engagement through the PTG and IRC channels.

# Main Points

|   # | Main point                                                                                                                                                          |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | The full 60-minute version of this talk is available on the G Research Open Source Software YouTube channel.                                                        |
|   2 | Ironic features are documented in the official docs, and many require direct Ironic API access rather than just Nova integration.                                   |
|   3 | Ironic architecture consists of an API service for database communication and a conductor service that performs the actual hardware work.                           |
|   4 | Hardware interaction occurs via in-band methods using the IPA RAM disk or out-of band methods using BMC interfaces like Redfish or IPMI.                            |
|   5 | Hardware types define a collection of pluggable interfaces for specific hardware capabilities, such as BIOS, boot, console, deploy, and power.                      |
|   6 | Node lifecycle management includes states for enrollment, cleaning, available, active, and manageable, with cleaning ensuring a consistent state before deployment. |
|   7 | Node retirement allows servers to exit the deployment loop, leaving them in a manageable state for decommissioning without automatic redeployment.                  |
|   8 | Steps are the fundamental units of work in Ironic, consisting of a name, interface, priority, and arguments, and can be in-band, out-of band, or control flow.      |
|   9 | Control flow steps, added in 2023, allow for explicit power actions, waiting, and holding workflows to integrate with external systems.                             |
|  10 | Automated cleaning uses hardware managers to detect hardware and run necessary steps, such as erasing disks or modifying RAID, by default.                          |
|  11 | Runbooks are pre-assembled collections of steps that can be used for automated cleaning or manual servicing to provide consistent maintenance workflows.            |
|  12 | Manual cleaning and node servicing allow operators to execute specific steps on nodes, with recent updates enabling servicing of active nodes.                      |
|  13 | Deployment methods include direct deploy, RAM disk deploy, Anaconda for Kickstart-based systems, and custom drivers like Ansible or custom agent.                   |
|  14 | Standalone Ironic deployment requires multiple API calls, but tools like the Allocations API and Bifrost simplify the process for reserving and deploying nodes.    |
|  15 | Conductor groups and node sharding are used to manage large environments by assigning specific conductors to node sets or parallelizing API calls.                  |
|  16 | Graceful shutdown features allow conductors to finish current tasks before stopping, minimizing impact on ongoing operations.                                       |
|  17 | Node history, added in 2022, provides a database log of events and steps for troubleshooting and auditing node activities.                                          |
|  18 | Notifications support sending events to message buses like Kafka or RabbitMQ to trigger external workflows or integrations.                                         |
|  19 | Adoption allows adding servers with existing operating systems to Ironic without immediately wiping the OS, useful for migrations.                                  |
|  20 | End user access is supported via owner and lessee assignments, allowing projects to manage their own nodes and run maintenance runbooks.                            |
|  21 | The Ironic community encourages engagement through the PTG, IRC, and mailing list to discuss features and hardware issues.                                          |
|  22 | New features include BootC support for deploying container contents to bare metal and OCI image support for standalone Ironic deployments.                          |

# Video

[![Video thumbnail](https://img.youtube.com/vi/cuCOLz-YrTI/hqdefault.jpg)](https://www.youtube.com/watch?v=cuCOLz-YrTI)

[Watch on YouTube](https://www.youtube.com/watch?v=cuCOLz-YrTI)
