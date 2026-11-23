---
layout: default
title: "All aboard the Release Train: Lessons from our last 100 OpenStack upgrades"
nav_order: 64
parent: OpenInfra Summit Europe 2025
type: Video Note
description: "Alex from StackHPC and colleague Sunhun presented lessons learned from managing over 100 OpenStack upgrades, highlighting the challenges of maintaining stability across diverse cloud environments."
resource: "https://www.youtube.com/watch?v=EatsGH8cgG4"
youtube_stats:
  view_count: 117
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

Alex from StackHPC and colleague Sunhun presented lessons learned from managing over 100 OpenStack upgrades, highlighting the challenges of maintaining stability across diverse cloud environments.
They detailed how the discontinuation of CentOS 8 forced a strategic shift, leading to the development of ARC, a custom repository system based on Pulp that snapshots package repositories to create stable, reproducible minor releases for both CentOS Stream and Rocky Linux.
To ensure reliability, the team implemented a rigorous CI/CD pipeline using self-hosted GitHub Action runners on Kubernetes, which allows for flexible, resource-efficient testing of single-node and multi-node scenarios, including complex upgrade paths.
The presentation concluded with six golden rules for successful upgrades: engage with the upstream community, ensure system health before upgrading, time the upgrade between four and eight months post-release, minimize the scope of changes, start preparation early, and maintain a comprehensive written plan that begins and ends with thorough testing.

# Main Points

|   # | Main point                                                                                                                             |
| --: | -------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | StackHPC is a UK-based consultancy managing approximately 60 OpenStack systems with a team of around 40 members.                       |
|   2 | The company specializes in HPC and scientific computing, deploying clouds using Kolla with containerized services.                     |
|   3 | Early deployment strategies involved building container images on-site and updating host OS packages without centralized testing.      |
|   4 | The discontinuation of CentOS 8 and its replacement by CentOS Stream introduced instability due to the lack of minor version releases. |
|   5 | Unpinned dependencies in CentOS Stream led to issues such as unprivileged users being unable to ping and memory leaks in Vert.         |
|   6 | Host OS updates can still cause problems like PCI pass-through failures affecting GPUs, even when using containers.                    |
|   7 | StackHPC developed ARC, a repository based on Pulp, to snapshot package repositories and build stable container images.                |
|   8 | ARC allows for the creation of custom minor stable versions, enabling consistent builds and validation before deployment.              |
|   9 | The scope of ARC expanded to include Rocky Linux and Ubuntu releases, as well as specific drivers like Nvidia.                         |
|  10 | Upstream packages are synchronized into ARC nightly, a process that takes between 12 and 18 hours depending on changes.                |
|  11 | Container images are built from pinned dependencies in ARC, tested, and then moved to a production release namespace.                  |
|  12 | Customers pull packages and images from a local mirror of ARC, allowing them to build consistent container images on-site.             |
|  13 | Testing is critical to ensure that consistency does not result in consistently bad outcomes, requiring automated CI/CD pipelines.      |
|  14 | CI tests are triggered by new features, bugfixes, dependency updates, and new OpenStack releases to prevent upgrade hazards.           |
|  15 | Test scenarios vary by host OS, network backend (OVN or OVS), node count, and whether upgrades are included.                           |
|  16 | Multi-node tests take approximately 10 hours, while single-node tests can be completed in up to two hours.                             |
|  17 | Tempest tests and StackHPC cloud tests are used to verify OpenStack functionality and system health via monitoring services.           |
|  18 | Self-hosted GitHub Action runners are deployed on Kubernetes clusters managed by Magnum or Azimuth within OpenStack.                   |
|  19 | The ARC Action Runner Controller manages scaling and scheduling of runners on worker nodes for CI jobs.                                |
|  20 | Runners provision VMs using Terraform and Ansible, allowing for flexible resource allocation and cost efficiency.                      |
|  21 | Self-hosted runners offer better security for sensitive data and full control but require more maintenance than hosted runners.        |
|  22 | Future plans include integrating Zuul, adding bare metal tests with Ironic, and implementing long-lived reliability tests.             |
|  23 | Golden rule one: Pay attention to the upstream community to identify and avoid known issues early.                                     |
|  24 | Golden rule two: Ensure the cloud is healthy before starting an upgrade to avoid compounding existing problems.                        |
|  25 | Golden rule three: Time upgrades between four and eight months after release to balance stability and dependency freshness.            |
|  26 | Golden rule four: Keep upgrades as small as possible by focusing solely on the version change to isolate potential failures.           |
|  27 | Golden rule five: Start preparation early, as major OS upgrades can take months or years on larger systems.                            |
|  28 | Golden rule six: Write down a detailed plan and tick off steps to maintain track of progress and ensure comprehensive testing.         |

# Video

[![Video thumbnail](https://img.youtube.com/vi/EatsGH8cgG4/hqdefault.jpg)](https://www.youtube.com/watch?v=EatsGH8cgG4)

[Watch on YouTube](https://www.youtube.com/watch?v=EatsGH8cgG4)
