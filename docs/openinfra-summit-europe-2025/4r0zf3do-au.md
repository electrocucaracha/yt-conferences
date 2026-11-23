---
layout: default
title: Operator nightmares  in the trenches of CERN’s OpenStack cloud
nav_order: 19
parent: OpenInfra Summit Europe 2025
type: Video Note
description: "Jose Castellon and Luis, representing CERN’s cloud infrastructure team, presented their extensive experience operating an OpenStack-based Infrastructure as a Service since 2013."
resource: "https://www.youtube.com/watch?v=4r0ZF3dO-aU"
youtube_stats:
  view_count: 325
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

Jose Castellon and Luis, representing CERN’s cloud infrastructure team, presented their extensive experience operating an OpenStack-based Infrastructure as a Service since 2013.
They detailed the scale of their environment, which includes approximately 10,000 physical servers, 15,000 virtual machines, and 1.65 petabytes of memory, while highlighting their strategy of in-place upgrades and active contribution to the upstream community.
The talk focused on several critical operational challenges, including a hardware firmware bug that caused CPU throttling, a kernel memory issue that led to hypervisor crashes, and complex networking issues arising from their migration to OVN.
A particularly significant incident involved a KVM kernel bug causing virtual CPU hangs, which the team mitigated by developing a custom eBPF module to proactively monitor at-risk VMs and perform live migrations before failure.
Additionally, they described a networking anomaly where unclean reboots caused traffic misrouting, which they resolved by implementing a systemd unit to clean up OVN state and Open vSwitch interfaces before services started.
The session concluded with an invitation for other operators to share their experiences and participate in upcoming OpenStack community discussions regarding operational best practices.

# Main Points

|   # | Main point                                                                                                                                                                       |
| --: | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | CERN operates the world's largest particle physics lab, founded in 1954 with 25 member states, focusing on fundamental research by colliding particles and analyzing data.       |
|   2 | The IT department manages data transmission, storage on tape, and hosts analysis facilities under an OpenStack cloud infrastructure as a service established in July 2013.       |
|   3 | The cloud infrastructure runs on Red Hat Enterprise Linux 9 and Alma Linux 9, utilizing two data centers, one started in 2013 and another brought online in 2024.                |
|   4 | Services include computational resources like physical servers, VMs, and container clusters, along with storage options such as images, volumes, file shares, and object stores. |
|   5 | Network services provide access to load balancers and private networks, supporting x86_64, ARM, GPUs, and other accelerators.                                                    |
|   6 | Current statistics show approximately 10,000 physical servers, 15,000 virtual machines, 1.65 petabytes of memory, and 300,000 cores.                                             |
|   7 | The setup has been upgraded in place since 2013, transitioning from CentOS and Grizzly to current versions, with nearly 25 OpenStack releases applied.                           |
|   8 | Migration from Nova network to Neutron was finalized in 2023, and the transition from Linux bridge to OVN is currently at 35% completion.                                        |
|   9 | A major effort in 2024 aligned scattered services to the Zed release, with the objective of aligning all components to Epoxy and later Caracal.                                  |
|  10 | A hardware issue caused CPU throttling to 400 MHz due to a bug in the CPLD firmware of quad servers, which was resolved by rebooting and monitoring energy metrics.              |
|  11 | A hypervisor crash loop was resolved by disabling defective memory modules and limiting CPUs to one to facilitate VM migration.                                                  |
|  12 | Random blue screens on Windows VMs were linked to the Windows Subsystem for Linux or IPV virtualization flag, requiring migration to remove these defaults.                      |
|  13 | Windows 11 support initially failed due to Microsoft reducing supported CPU families, necessitating the removal of specific hardware traits from placement.                      |
|  14 | Further Windows 11 issues in 2025 involved a sub-flag of the BMX CPU flag, requiring updates to libvirt and Nova to enable necessary flags.                                      |
|  15 | Linux kernel upgrades occasionally caused issues with CPU flags affecting live migrations, such as the AMD flash by SID flag invading the host model.                            |
|  16 | Library incompatibilities during OS minor releases caused block storage attachment problems, managed through controlled rollouts and machine migration.                          |
|  17 | A critical bug during the migration from 6.7 to 8.0 caused VMs to hang due to a sign extension error in the KVM memory management unit.                                          |
|  18 | The bug was identified via a Proxmox forum entry, and disabling KSM reduced incidents, though a permanent fix was pending in later kernel releases.                              |
|  19 | An eBPF module was developed to monitor the problematic counter value, allowing proactive live migration or user notification before VM failure.                                 |
|  20 | The eBPF solution successfully prevented further failures until the kernel fix was released, demonstrating precise estimation of VM failure times.                               |
|  21 | The migration to OVN has introduced new challenges, including traffic broadcasting issues and MAC duplicates after unclean hypervisor reboots.                                   |
|  22 | A workaround for OVN issues involves a systemd unit that cleans OVN database entries and Open vSwitch interfaces before starting the OVN controller.                             |
|  23 | Operators are encouraged to share experiences through IRC, Matrix, and the Open Infra Foundation, with a proposal to discuss ops-facing activities at the next PTG.              |

# Video

[![Video thumbnail](https://img.youtube.com/vi/4r0ZF3dO-aU/hqdefault.jpg)](https://www.youtube.com/watch?v=4r0ZF3dO-aU)

[Watch on YouTube](https://www.youtube.com/watch?v=4r0ZF3dO-aU)
