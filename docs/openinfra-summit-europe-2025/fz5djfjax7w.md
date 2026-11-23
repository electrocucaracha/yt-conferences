---
layout: default
title: "VM Migration Lightning Demo Showcase: Red Hat OpenStack VMware Migration toolkit"
nav_order: 107
parent: OpenInfra Summit Europe 2025
type: Video Note
description: "Pedro and Matthew from Red Hat presented a live demo of the Red Hat OpenShift VMware Migration Toolkit, which leverages the Ansible Automation Platform (AAP) to orchestrate large-scale migrations f..."
resource: "https://www.youtube.com/watch?v=fz5dJFJaX7w"
youtube_stats:
  view_count: 58
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

Pedro and Matthew from Red Hat presented a live demo of the Red Hat OpenShift VMware Migration Toolkit, which leverages the Ansible Automation Platform (AAP) to orchestrate large-scale migrations from VMware to Red Hat OpenStack.
The solution utilizes a modular Ansible collection to automate complex multi-stage processes, including pre-migration tasks, live data synchronization, and post-migration validations, thereby reducing risk and ensuring consistency.
Key features demonstrated include discovery mode for gathering VM metadata, flavor mapping for resource conversion, and warm migration using MBD kit and CBT to synchronize only data deltas during the transfer.
The presentation highlighted how AAP integrates with enterprise tools like ServiceNow and Kafka, supporting a comprehensive lifecycle from initial assessment to day-two operations.
The team confirmed that the toolkit supports VNFs, allows for parallelization to handle scale, and is currently available via upstream documentation with a downstream version planned for release in November.

# Main Points

|   # | Main point                                                                                                                                                                |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Red Hat announced the OpenShift VMware migration toolkit, which is built on an Ansible collection and integrates with the Ansible Automation Platform (AAP).              |
|   2 | AAP enables large-scale migrations from VMware to Red Hat OpenStack by using job workflows to orchestrate complex multi-stage processes with full visibility and control. |
|   3 | The workflow structure allows for modular, reusable steps including pre-migration tasks, the core migration, floating IP attachment, and post-migration validations.      |
|   4 | Orchestration logic within AAP supports defining dependencies, error handling, and parallel execution to ensure graceful recovery without manual intervention.            |
|   5 | The toolkit supports discovery mode to gather information such as MAC addresses, NICs, and multi-NIC configurations from the source environment.                          |
|   6 | Key features include exporting and importing MAC addresses, flavor mapping and creation to convert CPU and RAM resources, and live migration using MBD kit and CBT.       |
|   7 | The migration process involves deploying a conversion host, snapshotting the VM on vCenter, creating a Cinder volume, and attaching it to the conversion host.            |
|   8 | Live data synchronization uses CBT to track changes during the long migration phase, allowing the tool to synchronize only the delta in the takeover phase.               |
|   9 | After synchronization, the tool detaches the volume, creates a new machine in OpenStack, attaches the Cinder volume, and powers on the VM.                                |
|  10 | The solution supports various operating systems compatible with v2v and allows for optional automatic power-off of the source VM upon completion.                         |
|  11 | The migration journey is divided into three phases: virtual machine assessment, center phase migration, and steady state day-two operations.                              |
|  12 | AAP integrates with enterprise tools such as ServiceNow, Kafka, Prometheus, and Datadog for ticketing and event management.                                               |
|  13 | Day-two operations leverage OpenStack APIs and Ansible collections for patching and workload automation using tools like Watcher.                                         |
|  14 | The toolkit supports network mapping to associate vCenter networks with specific pre-created OpenStack networks.                                                          |
|  15 | Performance and scale testing demonstrates the ability to parallelize migrations for large-scale deployments.                                                             |
|  16 | The toolkit is currently available via upstream documentation and GitHub, with a downstream version planned for release around November.                                  |
|  17 | A hands-on lab is available for attendees to practice the migration process at their own pace.                                                                            |

# Video

[![Video thumbnail](https://img.youtube.com/vi/fz5dJFJaX7w/hqdefault.jpg)](https://www.youtube.com/watch?v=fz5dJFJaX7w)

[Watch on YouTube](https://www.youtube.com/watch?v=fz5dJFJaX7w)
