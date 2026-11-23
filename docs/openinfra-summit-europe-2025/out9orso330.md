---
layout: default
title: "Ten years of OpenStack at the MPCDF: Bootstrapping & scaling a private cloud for Max Planck Society"
nav_order: 138
parent: OpenInfra Summit Europe 2025
type: Video Note
description: "The Max Planck Computing and Data Facility (MPCDF) has spent the last decade evolving its private cloud infrastructure to support the diverse research needs of the Max Planck Society, a major Germa..."
resource: "https://www.youtube.com/watch?v=oUT9orSO330"
youtube_stats:
  view_count: 25
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

The Max Planck Computing and Data Facility (MPCDF) has spent the last decade evolving its private cloud infrastructure to support the diverse research needs of the Max Planck Society, a major German research organization.
Initially relying on HPC systems and disparate virtualization solutions, the facility transitioned to an OpenStack-based platform around 2015 to address flexibility and licensing concerns, eventually hosting significant scientific projects such as the MoveBank animal tracking database and the digitization of the Biblioteca Hertziana’s photographic archive.
When the SUSE OpenStack distribution was discontinued, the team rebuilt the platform using OpenStack Train on CentOS 8, subsequently performing in-place upgrades through the Wallaby release while migrating storage from SUSE Enterprise Storage to upstream Ceph.
To address the deprecation of TripleO, the team is currently migrating to Colansible, a process that involves backporting features like Podman support and aims to simplify operations while enabling new capabilities such as FIPS support for external dashboard access.
This transition, managed by a small team of two to three engineers, reflects a strategic shift toward a more maintainable and customizable infrastructure that continues to serve as a critical resource for high-throughput computing and data analysis across various scientific disciplines.

# Main Points

|   # | Main point                                                                                                                                                                                                    |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | The Max Planck Society is a major German research organization with 84 institutes, 26,000 staff, and 31 Nobel laureates, focusing on researcher-driven projects rather than specific grants.                  |
|   2 | The Max Planck Computing and Data Facility (MPCDF) supports research with approximately 500,000 CPU cores, 500 petabytes of data, and 3,500 GPUs, primarily through High-Performance Computing (HPC) systems. |
|   3 | Prior to 2015, MPCDF offered fragmented services including VMware, KVM, and bare-metal hosting, which were resource-intensive to maintain and lacked flexibility for rapid project scaling.                   |
|   4 | The initial OpenStack cloud was established around 2015 using IBM blade centers and Packstack, later scaling with nodes inherited from older HPC systems.                                                     |
|   5 | Early adoption of the cloud was limited due to a chicken-and-egg problem where projects were either satisfied with existing setups or too large for the initial cloud capacity.                               |
|   6 | The Move Apps project, from the Institute for Animal Behavior, was an early cloud user, utilizing GPS data from tagged animals to analyze migration patterns and behavior through web-based interfaces.       |
|   7 | In late 2019, the team rebuilt the platform from scratch after SUSE discontinued its OpenStack product, migrating to OpenStack Train on CentOS 8.                                                             |
|   8 | The team performed in-place upgrades annually from Train to Ussuri, Victoria, and finally Wallaby, the last release supported by OpenStack-Ansible.                                                           |
|   9 | Storage infrastructure transitioned from SUSE Enterprise Storage to upstream Ceph, with older clusters handling block and file storage and newer clusters dedicated to object storage.                        |
|  10 | The Bibliotheca Hertziana project digitized over 100 years of art and architecture photography, storing approximately 150 terabytes of scans on Ceph and processing them on HPC systems.                      |
|  11 | The cloud architecture consists of a single availability zone with a mix of 25 Gb and 100 Gb networking, connected to the core network and HPC infrastructure.                                                |
|  12 | Hardware includes standard Intel and AMD processors, with GPUs and local NVMe drives provided via PCI pass-through without a disaggregated layer.                                                             |
|  13 | Software services include Keystone with LDAP backend, OVN networking, Ceph-based storage, Octavia load balancers, Manila file shares, and Heat templating.                                                    |
|  14 | The Institute for the Science of Light uses object storage for microfluidics data, processing blood cell samples to diagnose conditions like long COVID.                                                      |
|  15 | Heat templates are used to deploy Slurm clusters and Kubernetes environments, with a custom recipe named "Magnum on a Magnum" supporting high-availability and test setups.                                   |
|  16 | The team is migrating from OpenStack-Ansible to Kolla-Ansible due to the deprecation of the former, planning to go live with the production migration in November.                                            |
|  17 | The migration involves mapping settings, patching containers or roles, and using Alma Linux 8 for new compute nodes to prepare for the transition.                                                            |
|  18 | Kolla-Ansible enables the deployment of additional services like Mistral, Trove, Cyborg, and Magnum, and introduces FIPS support requested by the security team.                                              |
|  19 | The team of two to two-and-a-half people manages the upgrades and maintenance, documenting divergences from upstream code to ensure system stability.                                                         |
|  20 | The production and test environments are separate systems with similar configurations, allowing for thorough testing of migration scenarios before production deployment.                                     |

# Video

[![Video thumbnail](https://img.youtube.com/vi/oUT9orSO330/hqdefault.jpg)](https://www.youtube.com/watch?v=oUT9orSO330)

[Watch on YouTube](https://www.youtube.com/watch?v=oUT9orSO330)
