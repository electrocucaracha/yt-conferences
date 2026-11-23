---
layout: default
title: My journey from contributor to operator
nav_order: 108
parent: OpenInfra Summit Europe 2025
type: Video Note
description: "Kuba, a member of the CERN CL team, shares his journey from becoming an upstream contributor to an OpenStack operator."
resource: "https://www.youtube.com/watch?v=PTXqzRzL3FY"
youtube_stats:
  view_count: 58
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

Kuba, a member of the CERN CL team, shares his journey from becoming an upstream contributor to an OpenStack operator.
As a summer intern at CERN, he developed a feature for OpenStack Ironic to prevent data deletion on specific disks during node reinstalls, but faced significant challenges testing this on real hardware due to time constraints and limited access.
After completing his studies, he returned to CERN as a bare metal engineer, where his primary focus shifted to maintaining data center stability and handling user tickets, leaving only about 30% of his time for planned tasks.
When tasked with deploying his previous feature in production, he discovered critical bugs that required extensive fixes, including a major 1,500-line code change that was eventually merged upstream.
This experience highlighted the distinct responsibilities of operators, who must balance downstream priorities with upstream contributions, and demonstrated how access to real hardware at CERN allowed for more robust testing and successful collaboration with the OpenStack community.

# Main Points

|   # | Main point                                                                                                                          |
| --: | ----------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Kuba transitioned from an individual contributor to an operator at CERN, sharing his journey with OpenStack Ironic.                 |
|   2 | As a summer student at CERN, he developed a feature to prevent data deletion on specific disks during node reinstallation.          |
|   3 | The feature allows specifying disks to skip via WWN or size hints, initially supporting physical disks and later RAID arrays.       |
|   4 | Implementing RAID support required introducing unique volume names to distinguish between identical RAID configurations.            |
|   5 | Testing was limited to DevStack environments and unit tests due to lack of access to physical hardware during the internship.       |
|   6 | Building a DevStack environment capable of compiling Ironic Python Agent from source took approximately three weeks.                |
|   7 | Unit tests required extensive mocking of hardware outputs, which introduced potential for errors compared to real hardware testing. |
|   8 | Upon joining CERN as an operator, Kuba prioritized maintaining data center stability over upstream contributions.                   |
|   9 | Operators at CERN spend approximately 70% of their time on firefighting and user support, leaving only 30% for planned work.        |
|  10 | Kuba upgraded Ironic from Yoga to Zed, enabling the deployment of his previously developed feature in production.                   |
|  11 | Real hardware testing at CERN revealed bugs that were not apparent in virtualized DevStack environments.                            |
|  12 | A user reported a critical bug by identifying the exact code line, allowing for a quick fix of one line of code.                    |
|  13 | Fixing remaining RAID-related issues took months, with a major patch of 1,500 lines of code eventually merged upstream.             |
|  14 | The large size of the patch made backporting to stable releases difficult due to merge conflicts and behavioral changes.            |
|  15 | CERN uses Rally to deploy and provision Ironic instances hourly across all regions to ensure production readiness.                  |
|  16 | Continuous monitoring tracks task completion times and trends to detect performance degradation over time.                          |
|  17 | Operator status provides access to diverse physical hardware, increasing confidence in upstream contributions.                      |
|  18 | Collaboration between operators and upstream communities is encouraged to validate features on real hardware.                       |
|  19 | CERN aims to stay close to upstream releases while managing the balance between user support and development.                       |

# Video

[![Video thumbnail](https://img.youtube.com/vi/PTXqzRzL3FY/hqdefault.jpg)](https://www.youtube.com/watch?v=PTXqzRzL3FY)

[Watch on YouTube](https://www.youtube.com/watch?v=PTXqzRzL3FY)
