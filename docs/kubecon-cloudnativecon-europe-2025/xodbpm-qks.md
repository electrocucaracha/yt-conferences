---
layout: default
title:
  etcd V3.6.0 and etc... Benjamin Wang, Ivan Valdes Castillo, Siyuan Zhang, Arka
  Saha & Ciprian Hacman
nav_order: 378
parent: Kubecon Cloudnativecon Europe 2025
type: Video Note
description:
  The latest release of LCD 3.6.0 and LCD operator 0.1.0 introduce several
  key features, including migration to W3 store, grid L3.6.0 Zero, and feature gates.
  The new release aims to improve performance, security, and usability. Grid L3.6.0
  Z...
resource: https://www.youtube.com/watch?v=_xoDbpm-Qks
tags:
  - kubecon-cloudnativecon-europe-2025
  - video
  - learning
status: stable
generated:
  by: process:yt-conferences-okf
  at: 2026-09-12 00:00:00+00:00
---

# Summary

The latest release of LCD 3.6.0 and LCD operator 0.1.0 introduce several key features, including migration to W3 store, grid L3.6.0 Zero, and feature gates.
The new release aims to improve performance, security, and usability.
Grid L3.6.0 Zero allows for downgrades from 3.6 to 3.5, while feature gates enable users to enable or disable features through a Kubernetes-style process.
Additionally, the release introduces two new health check endpoints (live Z and ready Z) and improved performance metrics, including reduced memory usage.
The LCD operator is also being developed with a focus on standardization and community adoption.

# Main Points

|   # | Main point                                                                                                                                    |
| --: | --------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Release process improvements:                                                                                                                 |
|   2 | Automation of releases                                                                                                                        |
|   3 | Improved security with periodic vulnerability scans                                                                                           |
|   4 | CD operator work group:                                                                                                                       |
|   5 | New repository and road map                                                                                                                   |
|   6 | Future plans include TLS communication, upgrades, and disaster recovery                                                                       |
|   7 | Performance improvements:                                                                                                                     |
|   8 | Reduced memory usage in 3.6 release candidate 3                                                                                               |
|   9 | Plans to improve performance further in future releases                                                                                       |
|  10 | HCD database size limit: + Current default is 2 GB, but can be configured up to 8 GB + Limitation due to network bandwidth and internal cache |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=_xoDbpm-Qks)
