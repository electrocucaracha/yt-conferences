---
layout: default
title: 10 years of OpenStack in Finnish Research
nav_order: 137
parent: OpenInfra Summit Europe 2025
type: Video Note
description: "Kalahan from CSC, a Finnish research and education IT provider, presented a decade-long overview of their OpenStack infrastructure, highlighting its evolution from a 2010 bioinformatics pilot to a ..."
resource: "https://www.youtube.com/watch?v=tr94SP1r1Kc"
youtube_stats:
  view_count: 28
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

Kalahan from CSC, a Finnish research and education IT provider, presented a decade-long overview of their OpenStack infrastructure, highlighting its evolution from a 2010 bioinformatics pilot to a robust platform supporting both sensitive data and community clouds.
CSC leverages its strong high-performance computing tradition to maintain a stable, multi-tenant environment that has grown to approximately 700 hypervisors and over 3,000 virtual machines, serving diverse users from researchers to university students.
The presentation emphasized the critical importance of long-term stability and continuous hardware renewal, noting that while the team faced significant operational challenges during rapid growth, recent staffing increases have allowed them to resume regular upgrades and modernize their stack.
Key lessons learned included prioritizing maintainability over extreme performance optimizations, carefully planning hardware exit strategies, and recognizing that operational workload scales with infrastructure size, which can otherwise hinder development efforts.
Currently, CSC is shifting focus toward providing higher-level services like virtual desktops and OpenShift on top of OpenStack, aiming to reduce user complexity while ensuring the underlying platform remains a reliable foundation for their expanding ecosystem of research and educational tools.

# Main Points

|   # | Main point                                                                                                                                                                                  |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | CSC is a Finnish research and education IT provider with two data centers, one in the capital region and one in Kajaani, housing the Lumi supercomputer.                                    |
|   2 | The organization began providing cloud services around 2010 using OpenNebula to meet bioinformatics demands before transitioning to OpenStack.                                              |
|   3 | OpenStack was selected primarily for its built-in multi-tenancy and API-first approach, which facilitated scaling and serving multiple research tenants.                                    |
|   4 | The first production OpenStack release occurred in 2014, with customer loads running prior to that, and the sensitive data cloud migrated to OpenStack around 2015.                         |
|   5 | Platform stability is a core priority, evidenced by a virtual machine that has remained running since April 2013 despite hardware and infrastructure changes.                               |
|   6 | Hardware integration is continuous, averaging 2.5 new integrations per year, driven by customer demand, growth, and the need to replace aging equipment.                                    |
|   7 | Key milestones include achieving ISO 27001 certification in 2015, adding GPUs in 2017, launching Ceph-based object storage in 2018, and OpenShift in 2019.                                  |
|   8 | The team grew from five to seven members post-pandemic, allowing for increased development focus and the execution of four simultaneous OpenStack upgrades.                                 |
|   9 | Current infrastructure includes approximately 700 hypervisors supporting two similar-sized clouds: a sensitive data cloud with about 70 projects and a community cloud with 1,700 projects. |
|  10 | User base has evolved to include higher-level services like virtual desktops and OpenShift to reduce the technical burden on researchers and improve resource efficiency.                   |
|  11 | Automation relies on RDO and Puppet, with the team emphasizing that process maturity is more critical than the specific tooling used.                                                       |
|  12 | Strategic decisions prioritize long-term maintainability over short-term performance gains, avoiding complex optimizations that increase operational overhead.                              |
|  13 | Operational work scales with infrastructure size, which previously constrained development time and delayed upgrades to newer OpenStack versions.                                           |
|  14 | The sensitive data cloud is more restricted with whitelisted APIs and direct network connections, functioning as a virtual private cloud compared to the broader community cloud.           |
|  15 | Future plans include moving away from Linux bridge, providing IPv6 in the community cloud, and continuing to upgrade to supported OpenStack versions.                                       |

# Video

[![Video thumbnail](https://img.youtube.com/vi/tr94SP1r1Kc/hqdefault.jpg)](https://www.youtube.com/watch?v=tr94SP1r1Kc)

[Watch on YouTube](https://www.youtube.com/watch?v=tr94SP1r1Kc)
