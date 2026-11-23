---
layout: default
title: "VM Migration Lightning Demo Showcase: A Long Distance VMware to OpenStack Migration Story"
nav_order: 123
parent: OpenInfra Summit Europe 2025
type: Video Note
description: "Ken Randle from Rackspace presents a live demonstration of migrating a virtual machine from a vSphere 7 environment in Chicago to an OpenStack Flex cloud in Dallas, a distance of approximately 1,40..."
resource: "https://www.youtube.com/watch?v=JwBpCgJVwsg"
youtube_stats:
  view_count: 46
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

Ken Randle from Rackspace presents a live demonstration of migrating a virtual machine from a vSphere 7 environment in Chicago to an OpenStack Flex cloud in Dallas, a distance of approximately 1,400 kilometers over the public internet.
The migration utilizes the Corololis tool, which is selected for its user-friendly interface that clearly visualizes the transfer and deployment steps, contrasting with the complex CLI outputs of other open-source tools.
The process involves taking a snapshot of the source VM, transferring the data, and deploying it as a new instance in the target cloud, where necessary OS adjustments and floating IP assignments are performed.
Randle emphasizes that while the technical execution is manageable, successful large-scale migrations require careful planning, such as using cold migrations for large databases to avoid data synchronization issues and leveraging load balancers to seamlessly switch traffic between the old and new endpoints.
The demo concludes with the successful activation of the new Dallas-based VM and the redirection of user traffic, proving the viability of moving workloads across distant data centers without private network connections.

# Main Points

|   # | Main point                                                                                                                                                                             |
| --: | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | The presenter demonstrates a live VMware to OpenStack migration from a Chicago data center to a Dallas data center over the public internet.                                           |
|   2 | The source environment is a vSphere 7 lab with three ESXi hosts, vCenter, NFS shared storage, and a distributed vSwitch.                                                               |
|   3 | VSphere 7 was chosen for the demo because approximately 80% of customers seeking migration services currently use vSphere 7 perpetual licenses.                                        |
|   4 | The target environment is Rackspace OpenStack Flex in the Dallas region, utilizing pre-created networks with IP ranges matching the source private network to simplify configuration.  |
|   5 | A load balancer is used to manage traffic between the source (Chicago) and destination (Dallas) endpoints, allowing for a seamless cutover.                                            |
|   6 | The migration is executed using Corololis, a partner tool selected for its user-friendly interface compared to CLI-driven alternatives like V2V or Ansible.                            |
|   7 | Corololis utilizes a "minion pool" of helper VMs in the target cloud to perform the migration work, with a larger flavor selected to improve speed.                                    |
|   8 | The migration process involves taking a snapshot of the source VM, transferring the data over the internet, and deploying a new OpenStack VM from that snapshot.                       |
|   9 | For large VMs with significant RAM or disk usage, cold migrations during maintenance windows are recommended to avoid data synchronization issues inherent in live migrations.         |
|  10 | Database migrations often require specialized approaches, such as snapshotting and replaying transaction logs, rather than simple live replication.                                    |
|  11 | Successful migrations require a detailed plan that accounts for physical constraints like disk read/write speeds and network bandwidth, especially when moving data over the internet. |
|  12 | Customers often use the migration opportunity to rearchitect their IT infrastructure from decentralized departmental VMware deployments to a centralized OpenStack model.              |
|  13 | The deployment phase includes OS transformation tasks, such as changing IP and MAC addresses and replacing VMware tools with QEMU guest tools.                                         |
|  14 | The demo concludes by assigning a floating IP to the new VM, switching the load balancer to the Dallas endpoint, and shutting down the Chicago source VM to verify the cutover.        |

# Video

[![Video thumbnail](https://img.youtube.com/vi/JwBpCgJVwsg/hqdefault.jpg)](https://www.youtube.com/watch?v=JwBpCgJVwsg)

[Watch on YouTube](https://www.youtube.com/watch?v=JwBpCgJVwsg)
