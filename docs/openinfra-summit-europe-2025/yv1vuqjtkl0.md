---
layout: default
title: OpenStack at Scale  Operating a bare metal cloud for quant research
nav_order: 11
parent: OpenInfra Summit Europe 2025
type: Video Note
description: "This presentation details the operational experiences of a quantitative research firm in London that utilizes OpenStack and Ironic to manage a massive bare-metal cloud infrastructure comprising 13,..."
resource: "https://www.youtube.com/watch?v=yV1vUqjtKl0"
youtube_stats:
  view_count: 519
  like_count: 8
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

This presentation details the operational experiences of a quantitative research firm in London that utilizes OpenStack and Ironic to manage a massive bare-metal cloud infrastructure comprising 13,000 GPUs, half a million cores, and up to 50 million batch jobs per day.
The speakers emphasize a "high integrity" security mindset, which enforces strict two-person rule approvals, automated pipelines for all changes, and comprehensive encryption to protect valuable intellectual property.
To handle the scale and diversity of hardware, the team relies heavily on Terraform for provisioning, Vault for secrets management, and Jenkins for operational automation, while maintaining a minimal appetite for outages by upgrading existing environments in place rather than building new clouds.
Key technical challenges addressed include tuning Ironic for thousands of nodes, managing concurrent builds to prevent network switch lockups, and implementing self-healing playbooks to automatically detect and remediate hardware failures.
Future plans focus on standardizing hardware management through Redfish drivers and virtual media to eliminate PXE boot complexities, improving build reliability, and enabling user self-service capabilities for firmware updates and node management.

# Main Points

|   # | Main point                                                                                                                                                                  |
| --: | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | G Research is a quantitative research firm in London that uses massive data to predict market patterns and has operated for about 20 years.                                 |
|   2 | The company operates a large-scale infrastructure with 13,000 GPUs, half a million cores, and up to 50 million batch jobs per day.                                          |
|   3 | The hardware estate is diverse, mixing AMD and Intel processors across various generations, which presents significant management challenges.                               |
|   4 | The platform processes 90 billion events per day, equating to one million messages per second, requiring robust infrastructure for authentication and metrics.              |
|   5 | The core provisioning system is OpenStack Yoga, operating across six production regions and 26 computer networks with hundreds of hypervisors.                              |
|   6 | Kubernetes is deployed on bare metal across over 100 clusters, some containing up to 1,000 machines, managed by a custom scheduler called Armada.                           |
|   7 | Terraform is used extensively for provisioning and configuration, while Vault handles service accounts and PKI, and Jenkins manages operational pipelines.                  |
|   8 | The organization follows a high-integrity mindset where no single person can modify production, requiring two pairs of eyes for all changes from source code to deployment. |
|   9 | Security measures include heavy encryption for hardware, controllers, and APIs, along with strict access controls and minimal permissions for administrators.               |
|  10 | The team implements rolling rebuilds, aiming to rebuild all systems from scratch every 30 to 90 days to maintain stability and security.                                    |
|  11 | The environment is air-gapped, requiring special processes to introduce code and manage dependencies, which adds complexity to daily operations.                            |
|  12 | The team has upgraded OpenStack from Queens to Yoga in-place without downtime, maintaining a minimal appetite for outages and tracking platform SLIs.                       |
|  13 | Ironic and OpenStack are deployed using Ansible and Ansible-core, with a focus on minimizing custom code and pushing changes upstream.                                      |
|  14 | Tuning for scale involves adjusting Ironic conductor power state sync intervals and limiting concurrent builds to around 50 per conductor for stability.                    |
|  15 | Metrics from OpenStack exporters and Oslo messaging notifications are fed into ELK to analyze performance and identify hidden failures like port binding errors.            |
|  16 | RabbitMQ has been migrated to quorum queues for improved stability, though Nova Compute Ironic lacks a stable high-availability story, requiring careful runbooks.          |
|  17 | Newer hardware often has firmware issues and BMC inconsistencies, such as OEM quirks that can stop BMC communication with the BIOS.                                         |
|  18 | The team builds custom hardware validation checks for GPU, CPU, memory, and cabling, including detecting reversed cables using LLDP data.                                   |
|  19 | Ironic RAM disks can become bloated with packages, causing PXE boot failures on some nodes, which is mitigated by using standard compression for images.                    |
|  20 | An Ironic self-healing collection of playbooks driven by Jenkins detects common failure modes and automatically repairs nodes or raises tickets for hardware replacement.   |
|  21 | The platform achieves a 99% success rate for 33,000 monthly rebuilds, with Ironic abstracting and masking many underlying hardware failures.                                |
|  22 | Future plans include standardizing on the Redfish driver and virtual media to remove the PXE boot flow and improve build reliability.                                       |
|  23 | Upcoming features include Ironic runbooks for self-service node management, remote console access, and trade-based portuling for dynamic bonding.                           |
|  24 | The team is exploring container-based steps in the IPA to run firmware updates and other tasks within the provisioning process.                                             |

# Video

[![Video thumbnail](https://img.youtube.com/vi/yV1vUqjtKl0/hqdefault.jpg)](https://www.youtube.com/watch?v=yV1vUqjtKl0)

[Watch on YouTube](https://www.youtube.com/watch?v=yV1vUqjtKl0)
