---
layout: default
title: From VMware Horizon to OpenStack  Building a Next Gen Virtual Desktop Infrastructure
nav_order: 41
parent: OpenInfra Summit Europe 2025
type: Video Note
description: 'Sang from FPT Smart Cloud presented a solution for migrating VMware Horizon to OpenStack, introducing their "Cloud Desktop" product designed to address the rising costs of VMware licensing and the ...'
resource: "https://www.youtube.com/watch?v=qVzLLN8zmew"
youtube_stats:
  view_count: 175
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

Sang from FPT Smart Cloud presented a solution for migrating VMware Horizon to OpenStack, introducing their "Cloud Desktop" product designed to address the rising costs of VMware licensing and the security challenges associated with hybrid work environments.
The architecture leverages OpenStack components, such as Glance for golden images and Nova for GPU support, alongside the open-source OpenUDS connection broker to enable rapid provisioning of virtual desktops in under one minute.
Key benefits highlighted include centralized management, enhanced data protection through cloud backups, and the ability to scale resources dynamically, which significantly reduces the IT department's workload compared to traditional PC management.
The presentation also addressed technical challenges, such as the current limitation of OpenUDS to the RDP protocol and the lack of native thin client support, though the company has recently partnered with Dell and HP to integrate their product with existing thin client hardware.
With five customers across industries like banking and outsourcing currently running 5,000 cloud desktops, FPT Smart Cloud demonstrated a streamlined onboarding process that allows new employee environments to be created and accessed in less than five minutes.

# Main Points

|   # | Main point                                                                                                             |
| --: | ---------------------------------------------------------------------------------------------------------------------- |
|   1 | FPT Smart Cloud is a Vietnamese OpenStack-based cloud provider and subsidiary of FPT Corporation.                      |
|   2 | The company invested 200 million dollars in new AI infrastructure products in Vietnam and Japan.                       |
|   3 | Cloud Desktop was developed to address hybrid work security risks and rising VMware Horizon licensing costs.           |
|   4 | Open source VDI solutions enable instant resource provisioning, governance via golden images, and zero-trust security. |
|   5 | Cloud Desktop centralizes management, reducing IT workload by approximately 80% compared to traditional PCs.           |
|   6 | The architecture uses OpenUDS as a connection broker on top of OpenStack infrastructure.                               |
|   7 | OpenStack Glance is used for golden images and caching to achieve VM creation times under one minute.                  |
|   8 | Cinder manages user data volumes, snapshots, and backups for the cloud desktop environment.                            |
|   9 | Nova supports GPU passthrough and vGPU flavors for visualization and AI training workloads.                            |
|  10 | Neutron handles DNS, routing tables, and custom metadata for virtual machines.                                         |
|  11 | End users access the desktop via HTML5, thin clients, or mobile devices through a secure RDP connection.               |
|  12 | Network latency under 100 ms is ideal for maintaining 60 frames per second in video playback.                          |
|  13 | Benchmarking shows the OpenStack-based solution offers better latency than VMware for standard office tasks.           |
|  14 | A key challenge is that OpenUDS currently only supports the Microsoft RDP protocol.                                    |
|  15 | RDP performance degrades in unstable networks with high latency or packet loss, causing frame drops.                   |
|  16 | The team plans to integrate BCOIB protocol in the next phase to improve video transmission efficiency.                 |
|  17 | Thin client support was initially missing but has been resolved through partnerships with Dell and HP.                 |
|  18 | Official plugins for Dell and HP thin clients are now available for connecting to the Cloud Desktop.                   |
|  19 | The company is developing its own OEM mini PC thin client device for the next phase.                                   |
|  20 | FPT Smart Cloud has replaced 1,000 VMware Horizon VDIs and serves 5,000 cloud desktops.                                |
|  21 | Current customers include entities in banking, product development, and outsourcing industries.                        |
|  22 | New employee onboarding takes less than five minutes using the automated cloud desktop creation flow.                  |
|  23 | Performance optimizations include changing disk queue depth from one to eight for better Windows latency.              |
|  24 | Network interface multi-queue settings were adjusted to enhance network performance for Windows workloads.             |

# Video

[![Video thumbnail](https://img.youtube.com/vi/qVzLLN8zmew/hqdefault.jpg)](https://www.youtube.com/watch?v=qVzLLN8zmew)

[Watch on YouTube](https://www.youtube.com/watch?v=qVzLLN8zmew)
