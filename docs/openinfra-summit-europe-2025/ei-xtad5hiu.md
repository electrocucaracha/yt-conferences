---
layout: default
title: "Deep Dive into OpenStack Private Cloud: Issues & Fixes at NTT Docomo Business, Inc."
nav_order: 76
parent: OpenInfra Summit Europe 2025
type: Video Note
description: "This presentation details three critical challenges encountered during the upgrade of an enterprise OpenStack cloud platform to the Queens release, focusing on virtual machine high availability, ne..."
resource: "https://www.youtube.com/watch?v=eI-XtAD5HIU"
youtube_stats:
  view_count: 92
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

This presentation details three critical challenges encountered during the upgrade of an enterprise OpenStack cloud platform to the Queens release, focusing on virtual machine high availability, network interface compatibility, and memory performance.
The first issue involved evacuation timeouts where instances failed to migrate within the required 10-minute window due to network controller behavior changes; this was resolved by adjusting VIF timeouts, increasing parallel evacuation limits, and tuning Nova parameters.
The second problem affected Windows VMs, where a change in the virtual chipset version caused network interface renaming and loss of static configurations upon reboot; the team fixed this by locking the chipset version using system metadata and developed an automated tool to validate virtual hardware consistency.
The third issue was a gradual memory leak in the kernel slab cache caused by containerized monitoring tools, which increased interrupt handling latency; this was mitigated by disabling the offending jobs and applying a kernel parameter to disable khugepaged, requiring a coordinated live migration strategy to update thousands of hosts without downtime.
Key lessons learned include the importance of shift-left testing to detect compatibility issues early, the need for detailed monitoring of system-wide impacts from application-level changes, and the necessity of automated live migration capabilities to maintain service availability during infrastructure upgrades.

# Main Points

|   # | Main point                                                                                                                                                                                             |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   1 | The presentation covers three major challenges faced during an OpenStack upgrade from Mitaka to Queen for an enterprise cloud platform.                                                                |
|   2 | The first issue involved Virtual Machine High Availability (VM HA) where evacuating 230 instances failed to meet the 10-minute service level objective.                                                |
|   3 | The root cause of the HA failure was a behavior change in OpenStack Queen where Nova Compute waited for a VIF Plugged event that the network controller did not send during evacuation.                |
|   4 | The solution involved reducing the VIF timeout from 300 to 90 seconds, increasing the Nova Conductor evacuation timeout to 150 seconds, and raising parallel execution limits to speed up the process. |
|   5 | The second issue was a network interface problem in Windows VMs where static IP configurations were lost after migration and reboot to new compute nodes.                                              |
|   6 | This occurred because the virtual chipset version changed, causing Windows to recognize the device as new and discard previous network settings.                                                       |
|   7 | The fix utilized OpenStack system metadata to lock the virtual chipset type to the old platform's value, preserving device identity and network configurations.                                        |
|   8 | The third issue was increased I/O latency and memory ballooning on compute nodes due to Slab memory growth caused by containerized monitoring tools.                                                   |
|   9 | The root cause was identified as kernel instability related to containerization, where growing Slab caches led to longer interrupts and higher latency.                                                |
|  10 | The remediation involved disabling specific kernel features via command-line parameters and performing a rolling reboot of over 1,000 hosts using automated live migration.                            |
|  11 | A key lesson from the HA issue is that upgrades can have unexpected performance side effects, making thorough testing and configuration tuning essential.                                              |
|  12 | The Windows VM issue highlighted the need for a shift-left testing approach to detect compatibility problems earlier in the development lifecycle.                                                     |
|  13 | The memory issue demonstrated that small application-layer changes can have system-wide impacts, requiring monitoring of real workloads and key metrics.                                               |
|  14 | Automated live migration is critical for maintaining high availability and applying fixes without downtime in large-scale enterprise environments.                                                     |
|  15 | The team emphasized the importance of checking configuration files first, as tuning settings often resolves issues without requiring code changes.                                                     |
|  16 | Validating virtual hardware consistency between old and new platforms is necessary to ensure customer environments remain stable after upgrades.                                                       |

# Video

[![Video thumbnail](https://img.youtube.com/vi/eI-XtAD5HIU/hqdefault.jpg)](https://www.youtube.com/watch?v=eI-XtAD5HIU)

[Watch on YouTube](https://www.youtube.com/watch?v=eI-XtAD5HIU)
