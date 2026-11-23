---
layout: default
title: "ZIASTACK = OpenStack + ZConverter: A new OpenStack distribution"
nav_order: 22
parent: OpenInfra Summit Europe 2025
type: Video Note
description: "Zikcom presents a hypervisor-agnostic migration solution that simplifies the complex process of moving virtual machines from VMware to OpenStack by leveraging existing backup and disaster recovery ..."
resource: "https://www.youtube.com/watch?v=TBjklqYB-ts"
youtube_stats:
  view_count: 276
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

Zikcom presents a hypervisor-agnostic migration solution that simplifies the complex process of moving virtual machines from VMware to OpenStack by leveraging existing backup and disaster recovery workflows.
The company addresses the heterogeneity challenges between different platforms by converting diverse source environments into a standardized Zikcom backup format, which is then restored to the target OpenStack infrastructure, effectively reducing thousands of potential migration scenarios to a single, tested process.
This approach allows IT teams to utilize their existing backup and recovery expertise, treating migration as a routine backup operation that ensures data protection and enables accurate time estimation through disaster recovery drills.
The presentation highlights that this method supports flexible "move in and move out" capabilities across various hypervisors and clouds, meeting market demands for automated, affordable, and single-tool migration solutions.
A live demonstration confirmed the feasibility of this strategy by successfully executing both full and incremental virtual machine migrations from VMware to OpenStack using the described backup and recovery steps.

# Main Points

|   # | Main point                                                                                                                                                             |
| --: | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Zikcom is a 20-year-old company with three entities that offers a new OpenStack distribution integrating backup, migration, and disaster recovery.                     |
|   2 | An IT manager expressed concern about the complexity of migrating over 10,000 virtual machines from VMware to OpenStack.                                               |
|   3 | The speaker proposed treating the migration process as a standard backup and recovery routine to simplify the task.                                                    |
|   4 | Migration complexity arises from heterogeneity between VMware and OpenStack, including differences in platforms, hypervisors, and disk formats.                        |
|   5 | The number of potential migration scenarios can exceed 2,000 when multiple platforms are involved, with over 30 components contributing to heterogeneity per platform. |
|   6 | Zikcom utilizes hypervisor-agnostic migration, backup, and disaster recovery technology to eliminate heterogeneity issues.                                             |
|   7 | The migration process consists of two steps: capturing VMs in Zikcom's hypervisor-agnostic backup format and then restoring them to OpenStack.                         |
|   8 | This approach reduces complex migration scenarios to a single case, with a guaranteed migration recovery success rate of 99.9% based on thousands of tests.            |
|   9 | Market requirements include flexible move-in and move-out capabilities, data protection during migration, and migration drill capabilities.                            |
|  10 | Organizations seek automated migration processes to eliminate human errors and affordable or complimentary migration licenses.                                         |
|  11 | A single migration tool is preferred over multiple tools to address all needs for a project.                                                                           |
|  12 | Zikcom identified three technology gaps in OpenStack: backup, disaster recovery, and migration capabilities, which it has integrated.                                  |
|  13 | Data protection is achieved by capturing VMs in Zikcom's backup format, which serves as both a migration and backup solution.                                          |
|  14 | Disaster recovery drills can be leveraged as migration drills, where the Recovery Time Objective (RTO) of the drill estimates the migration completion time.           |
|  15 | The solution supports cross-migration capabilities using a single backup solution, allowing migration from VMware, Nutanix, or Red Hat to OpenStack.                   |
|  16 | Replicating the backup repository to a remote storage location provides disaster recovery capabilities alongside migration.                                            |
|  17 | A live demo showcased the migration of a video streaming service from VMware to OpenStack using full and incremental backup processes.                                 |
|  18 | The migration process does not rely on VMware APIs but uses Zikcom's independent, hypervisor-agnostic technology.                                                      |
|  19 | Network connectivity is handled by pre-provisioning virtual machines in OpenStack and linking operating system applications from the source.                           |
|  20 | IP address assignment can be automated via DHCP or static IP programs, simplifying post-migration configuration.                                                       |
|  21 | Zikcom's migration product was released in 2007, making it one of the oldest migration software solutions in the market.                                               |
|  22 | The solution supports CPU changes between Intel and AMD architectures, with Windows drivers handled automatically.                                                     |
|  23 | The core value proposition is that IT teams can perform complex migrations using their existing backup and recovery skills and processes.                              |

# Video

[![Video thumbnail](https://img.youtube.com/vi/TBjklqYB-ts/hqdefault.jpg)](https://www.youtube.com/watch?v=TBjklqYB-ts)

[Watch on YouTube](https://www.youtube.com/watch?v=TBjklqYB-ts)
