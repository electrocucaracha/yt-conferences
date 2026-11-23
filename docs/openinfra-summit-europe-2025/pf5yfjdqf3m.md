---
layout: default
title: "A Universe from Nothing: A hands on introduction to OpenStack"
nav_order: 9
parent: OpenInfra Summit Europe 2025
type: Video Note
description: "Max and Matt from StackHPC present a workshop on deploying a Linux-based OpenStack cloud from bare metal using the Kob project, which stands for Kolla on Bifrost."
resource: "https://www.youtube.com/watch?v=Pf5yfJDQf3M"
youtube_stats:
  view_count: 569
  like_count: 10
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

Max and Matt from StackHPC present a workshop on deploying a Linux-based OpenStack cloud from bare metal using the Kob project, which stands for Kolla on Bifrost.
The session explains how Kob integrates Kolla-Ansible for containerized service deployment with Bifrost, a standalone version of Ironic, to solve the chicken-and-egg problem of enrolling hardware into a cloud that does not yet exist.
Participants follow a hands-on lab where they configure local networking, discover and inspect virtual bare-metal nodes, and provision operating systems using Kob’s idempotent Ansible playbooks.
The demonstration covers the deployment of core OpenStack services, the addition of monitoring tools like Prometheus and Grafana, and the creation of a virtual machine with a floating IP to verify cloud functionality.
The presenters emphasize the importance of managing configurations through the Kob-config repository, utilizing environments for multi-cluster management, and leveraging hooks for site-specific automation to ensure a repeatable and maintainable infrastructure.

# Main Points

|   # | Main point                                                                                                                                                          |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | The session covers deploying a Linux-based OpenStack cloud from bare metal using StackHPC's Kob project.                                                            |
|   2 | Kob is an acronym for Kolla on Bifrost, combining Kolla-Ansible for containerized services and Bifrost for bare metal enrollment.                                   |
|   3 | Bifrost is a standalone version of Ironic deployed on a seed host to bridge the gap between bare metal and the OpenStack control plane.                             |
|   4 | Kolla-Ansible provides Ansible playbooks to deploy OpenStack services as containers on Docker or Podman.                                                            |
|   5 | Kob Config is the central directory for all infrastructure-as-code changes, supporting multiple environments for staging and production.                            |
|   6 | All configuration changes must be made in the Kob Config etc/kob directory, as the etc/kolla directory is generated and ephemeral.                                  |
|   7 | The deployment process involves configuring local networking, discovering inventory, inspecting hardware, provisioning, host configuration, and service deployment. |
|   8 | Inventory discovery uses Bifrost to detect nodes and map them to Ansible groups like controllers and computes.                                                      |
|   9 | Hardware inspection gathers detailed node information via PXE boot and the Ironic Python Agent to enable proper provisioning.                                       |
|  10 | Provisioning installs the operating system on nodes, transitioning them from an available to a manageable state in Bifrost.                                         |
|  11 | Host configuration prepares nodes for containerization by installing packages, setting up networking, and creating the stack user.                                  |
|  12 | Service deployment pulls container images and runs OpenStack services using Kolla-Ansible playbooks driven by Kob.                                                  |
|  13 | The process is idempotent, allowing safe re-runs to apply changes or recover from failures without disrupting existing services.                                    |
|  14 | Hooks allow custom Ansible playbooks to run before or after specific Kob commands for site-specific requirements.                                                   |
|  15 | Additional services like Grafana and Prometheus can be deployed by enabling them in the Kob Config and running service deployment.                                  |
|  16 | Users can interact with the cloud via the Horizon web interface using credentials found in the templated Kob Config files.                                          |
|  17 | Virtual machines can be created using OpenStack CLI commands after sourcing the appropriate admin or public OpenRC files.                                           |
|  18 | Floating IPs can be created and attached to instances to provide external network access for SSH connectivity.                                                      |
|  19 | The lab environment uses virtual machines to simulate bare metal nodes, with a seed VM hosting Bifrost and a Docker registry.                                       |
|  20 | Kob supports managing physical networking for various switch vendors and allows fine-grained control over deployment configurations.                                |
|  21 | The team recommends keeping the seed VM running for future expansions, OS upgrades, and image registry access.                                                      |
|  22 | Custom playbooks can be stored in the Kob Config Ansible directory and executed via the Kob playbook run command.                                                   |
|  23 | The deployment workflow is designed to be repeatable and scalable, supporting both small test environments and large production clouds.                             |

# Video

[![Video thumbnail](https://img.youtube.com/vi/Pf5yfJDQf3M/hqdefault.jpg)](https://www.youtube.com/watch?v=Pf5yfJDQf3M)

[Watch on YouTube](https://www.youtube.com/watch?v=Pf5yfJDQf3M)
