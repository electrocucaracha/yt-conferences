---
layout: default
title: "VMware to OpenStack with Ansible OS-Migrate"
nav_order: 50
parent: OpenInfra Summit Europe 2025
type: Video Note
description: "Matthew, a principal engineer at Red Hat, presented on OS Migrate, a tool designed for large-scale VMware to OpenStack migrations."
resource: "https://www.youtube.com/watch?v=-i7XiH5aVRE"
youtube_stats:
  view_count: 151
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

Matthew, a principal engineer at Red Hat, presented on OS Migrate, a tool designed for large-scale VMware to OpenStack migrations.
He explained that while VMware to KVM migration is a well-established topic often handled by tools like libvirt and v2v, OS Migrate offers a distinct advantage by leveraging existing OpenStack-to-OpenStack migration expertise and utilizing a pure Ansible architecture that requires no complex API or database deployments.
The solution addresses the specific challenges of VMware ecosystems, such as the need for disk conversion and resource mapping, by employing a workflow that includes discovery, mapping, transfer, and conversion phases.
To achieve high scalability and performance, the core migration modules are written in Go rather than Python, allowing for parallel processing on conversion hosts and significantly faster data synchronization using VMware’s Change Block Tracking feature.
This approach enables the migration of massive workloads, such as multi-terabyte disks, with minimal downtime by performing background synchronizations and only requiring a final delta sync during the maintenance window.

# Main Points

|   # | Main point                                                                                                                                          |
| --: | --------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Matthew, a principal engineer at Red Hat, presented on OS Migrate, focusing on VMware to OpenStack migration at scale.                              |
|   2 | The VMware to KVM migration topic has been addressed for years by open-source projects like libvirt and the V2V tool.                               |
|   3 | OS Migrate leverages existing workload migration experience and is built as a pure Ansible collection consisting of modules, roles, and playbooks.  |
|   4 | The tool requires no complex architecture, APIs, or databases, making it easy to deploy, customize, and integrate with automation platforms or CLI. |
|   5 | Scalability is a key feature, allowing the tool to handle very large workloads efficiently.                                                         |
|   6 | The architecture relies on OpenStack APIs for source and destination, requiring only an Ansible host and a conversion host instance.                |
|   7 | Pre-workload migration involves exporting resources like flavors and networks to serial data for modification before import.                        |
|   8 | Workload migration moves the virtual machine itself, requiring disk conversion because VMware disks cannot run directly under KVM.                  |
|   9 | The migration workflow includes discovery, resource mapping from vCenter to OpenStack, transfer, conversion, and instance spawning.                 |
|  10 | Migrations run from live virtual machine snapshots, using Change Block Tracking (CBT) to synchronize only changed data blocks.                      |
|  11 | Data is moved to Cinder volumes via the conversion host, allowing for minimal downtime during the final delta sync.                                 |
|  12 | Ansible Automation Platform (AAP) can orchestrate migrations, enabling scheduling and isolation of workloads for different teams.                   |
|  13 | Parallelization allows the conversion host to handle multiple migrations simultaneously, requiring 2 GB of RAM and 1 vCPU per process.              |
|  14 | Multiple conversion hosts can be used to scale further, with AAP allowing specific hosts to be assigned to different teams.                         |
|  15 | Core migration modules are written in Go instead of Python to achieve higher performance, utilizing the gophercloud and govmomi SDKs.               |
|  16 | Using compiled languages in Ansible collections presents challenges, such as architecture-specific building and collection size limits.             |
|  17 | Lab results showed that 100 small VMs could be migrated in under 30 minutes with linear scaling performance.                                        |
|  18 | Large disk migrations, such as 4 to 6 terabytes, benefit significantly from CBT to reduce downtime.                                                 |
|  19 | A specific feature supports migrating workloads via NFS datastores, adopting volumes into Cinder without full data synchronization.                 |
|  20 | The final step involves converting the adopted Cinder volumes to a KVM-compatible format to spawn the OpenStack instance.                           |

# Video

[![Video thumbnail](https://img.youtube.com/vi/-i7XiH5aVRE/hqdefault.jpg)](https://www.youtube.com/watch?v=-i7XiH5aVRE)

[Watch on YouTube](https://www.youtube.com/watch?v=-i7XiH5aVRE)
