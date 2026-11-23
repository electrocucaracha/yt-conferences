---
layout: default
title: "OpenStack-ception: Unleash the Power of OpenStack!"
nav_order: 100
parent: OpenInfra Summit Europe 2025
type: Video Note
description: "Arnold, an engineer at OVH Cloud, presents a solution for testing OpenStack changes in an environment that closely mirrors production, addressing the limitations of DevStack which is often misalign..."
resource: "https://www.youtube.com/watch?v=7BHYmrpfeKI"
youtube_stats:
  view_count: 62
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

Arnold, an engineer at OVH Cloud, presents a solution for testing OpenStack changes in an environment that closely mirrors production, addressing the limitations of DevStack which is often misaligned with real-world multi-node setups.
He introduces "Bootstrap OpenStack," a tool designed to deploy a functional, multi-node OpenStack instance on top of an existing public cloud within five minutes, utilizing stable branches and precompiled packages to ensure reliability and ease of use.
The architecture consists of a controller node running OpenStack components in Kubernetes containers, alongside two compute nodes and two network nodes configured via Ansible, allowing for comprehensive testing of features like live migration and router debugging.
During the live demonstration, Arnold showcases how to patch the Nova API locally, rebuild the Docker image, and inject it into the Kubernetes cluster to verify code changes, such as modifying server description defaults, without needing to manage complex infrastructure manually.
This approach provides a rapid, reproducible, and production-like testing environment that can be adapted to other cloud platforms, enabling developers to efficiently validate upstream patches or downstream modifications before deployment.

# Main Points

|   # | Main point                                                                                                                                                                              |
| --: | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | The speaker, Arnold from OVH Cloud, presents a tool called "bootstrap open stack" for testing OpenStack changes in an environment closer to production than DevStack.                   |
|   2 | OVH Cloud has operated OpenStack since 2012, starting with Swift and later adding Nova and Neutron, currently running over 40 production regions with approximately 30,000 hypervisors. |
|   3 | The largest OVH region contains nearly 3,000 compute nodes, a scale that presents significant management challenges despite OpenStack not being designed for such size.                 |
|   4 | DevStack is considered unsuitable for production-like testing because it is single-node, relies on the master branch, and takes 20 to 30 minutes to deploy.                             |
|   5 | The bootstrap open stack tool deploys a multi-node OpenStack instance on top of an existing public cloud in under five minutes.                                                         |
|   6 | The deployment consists of five instances: one controller, two compute nodes, and two network nodes, allowing for live migration and router debugging tests.                            |
|   7 | The controller node runs OpenStack components as Docker containers within Kubernetes, using K3s and flat YAML files templated with the Frap tool.                                       |
|   8 | Compute and network nodes are configured using Ansible playbooks and precompiled Debian packages rather than vendor-specific repositories.                                              |
|   9 | The tool uses the OVS driver for Neutron to align with OVH production standards, though it can also be used to test OVN.                                                                |
|  10 | Cloud-init is used for initial setup, and the system is preconfigured with images and flavors to ensure it is ready for immediate use.                                                  |
|  11 | The solution supports real public IPs, a feature available in OVH Cloud that may not be present in other providers.                                                                     |
|  12 | A live demo showed cloning the project, applying Terraform to create instances, and accessing the controller via SSH.                                                                   |
|  13 | The demo involved patching the Nova API source code locally to change the default server description behavior.                                                                          |
|  14 | The patched Nova code was used to rebuild a Docker image, which was then pushed to the local Kubernetes registry.                                                                       |
|  15 | The Kubernetes deployment was updated to use the new image, and a rollout restarted the Nova API service.                                                                               |
|  16 | Creating a new server after the patch successfully displayed the modified description, confirming the test workflow.                                                                    |
|  17 | The tool allows testing unmerged patches from Gerrit by cloning specific branches, facilitating development and bug verification.                                                       |
|  18 | Compute and network services are not containerized; they use standard Debian packages installed directly on the instances for easier patching.                                          |
|  19 | The project is open source on GitHub and does not rely on OVH-specific infrastructure, making it portable to other OpenStack-based clouds.                                              |

# Video

[![Video thumbnail](https://img.youtube.com/vi/7BHYmrpfeKI/hqdefault.jpg)](https://www.youtube.com/watch?v=7BHYmrpfeKI)

[Watch on YouTube](https://www.youtube.com/watch?v=7BHYmrpfeKI)
