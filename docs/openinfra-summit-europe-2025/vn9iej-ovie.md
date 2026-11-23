---
layout: default
title: "OpenStack Ansible Project Update & Onboarding"
nav_order: 71
parent: OpenInfra Summit Europe 2025
type: Video Note
description: "Mitri, the project team leader for OpenStack-Ansible, presented an update on the deployment tool, highlighting its flexibility, reproducibility, and low operational overhead by leveraging plain Ans..."
resource: "https://www.youtube.com/watch?v=VN9iej-oViE"
youtube_stats:
  view_count: 100
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

Mitri, the project team leader for OpenStack-Ansible, presented an update on the deployment tool, highlighting its flexibility, reproducibility, and low operational overhead by leveraging plain Ansible and system containers.
The project supports a mix of Ubuntu, Debian, Rocky, and Alma Linux, prioritizing security through TLS support and version pinning, while also accommodating environments with limited or no internet connectivity.
Recent updates since the Caracal release include the removal of SSH into containers, an upgrade to RabbitMQ 4.0, the introduction of an OpenStack resources role, and the addition of playbook hooks for custom automation.
Adoption statistics indicate that approximately 18% of OpenStack deployments currently use the tool, with another 4% in testing, reflecting a healthy and sustainable project state.
Looking ahead, the team plans to revive support for VMware, improve Magnum Cluster API integration, refactor the HAProxy role, and seek community assistance for reviewing patches and maintaining enterprise Linux distributions.

# Main Points

|   # | Main point                                                                                                                                                 |
| --: | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | OpenStack Ansible is a deployment tool using plain Ansible with minimal custom modules to deploy and manage OpenStack.                                     |
|   2 | The project provides roles, playbooks, and collections for deployment, day-two operations, upgrades, and configuration changes.                            |
|   3 | Deployment supports LXC system containers and bare metal, with services installed in separate virtual lands and pinned by commit SHA for reproducibility.  |
|   4 | Supported operating systems include Ubuntu, Debian, Rocky Linux, and Alma Linux, with multi-architecture support and mixed OS environments.                |
|   5 | The tool offers high flexibility for custom architectures, backend separation, and integration with existing Ansible infrastructure.                       |
|   6 | Security features include TLS support for frontend and backend communication, SSH certificates for Nova, and limited or no connectivity environments.      |
|   7 | The project is GitOps-ready, allowing pipeline triggers based on variable changes to apply specific updates without full redeployment.                     |
|   8 | Operational overhead is low as it relies on standard Linux and Ansible knowledge without requiring external projects.                                      |
|   9 | Project health is indicated by a median patch merge time of six days and sustainable contribution levels from multiple organizations.                      |
|  10 | Adoption statistics show approximately 18% of deployments use OpenStack Ansible, with another 4% in testing phases.                                        |
|  11 | Recent updates include removing SSH to containers in favor of LXC attach, upgrading RabbitMQ to version 4.0, and introducing resilient upgrade safeguards. |
|  12 | New roles have been added for OpenStack resources management, FRR for OVN BGP agent, and a common Apache role to avoid module conflicts.                   |
|  13 | Playbook hooks allow users to define pre and post-execution tasks, such as custom user provisioning or driver deployment.                                  |
|  14 | All playbooks have been moved to a collection with tab autocomplete support for improved user experience.                                                  |
|  15 | Systemd overrides have been added to support network configuration via netplan and systemd-networkd without conflicts.                                     |
|  16 | Future plans include reviving Water, improving Magnum Cluster API support, and refactoring the HAProxy role for better certificate flexibility.            |
|  17 | The community seeks assistance with Enterprise Linux distribution support, code reviews, and documentation improvements.                                   |
|  18 | Contributors are encouraged to join mailing lists, answer questions on Launchpad Answers, and participate in batch reviews to maintain project health.     |

# Video

[![Video thumbnail](https://img.youtube.com/vi/VN9iej-oViE/hqdefault.jpg)](https://www.youtube.com/watch?v=VN9iej-oViE)

[Watch on YouTube](https://www.youtube.com/watch?v=VN9iej-oViE)
