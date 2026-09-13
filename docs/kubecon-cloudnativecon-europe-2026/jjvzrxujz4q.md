---
layout: default
title: "Project Lightning Talk: Harbor Update - Prasanth Baskar, Maintainer"
nav_order: 268
parent: Kubecon Cloudnativecon Europe 2026
type: Video Note
description:
  Prashant, a core contributor to Harbor, provided updates on the project,
  highlighting the recent release of version 2.15, which introduces features such
  as disabling tags for S3 and other storages to enhance garbage collection performance...
resource: https://www.youtube.com/watch?v=jJVZrXuJZ4Q
tags:
  - kubecon-cloudnativecon-europe-2026
  - video
  - learning
status: stable
generated:
  by: process:yt-conferences-okf
  at: 2026-09-12 00:00:00+00:00
---

# Summary

Prashant, a core contributor to Harbor, provided updates on the project, highlighting the recent release of version 2.15, which introduces features such as disabling tags for S3 and other storages to enhance garbage collection performance, upstream proxy cache registry connection limits to better manage rate limits, and support for Cosign v3 signatures.
The next release will focus on replacing Redis with Valky for improved performance and expanding support for uTrivy results, including config secrets from scans.
Harbor’s subprojects include Harbor Satellite, a lightweight, stateless registry for edge devices, and Harbor CLI, a tool for automating Harbor management, which recently surpassed 100,000 downloads.
Prashant also acknowledged key contributors, especially those who advanced from mentees to maintainers, and invited the community to connect via Slack, Twitter, LinkedIn, or at their booth and bi-weekly meetings to share feedback and use cases.

# Main Points

|   # | Main point                                                                                                               |
| --: | ------------------------------------------------------------------------------------------------------------------------ |
|   1 | Prashant is a core contributor to Harbor and other registry-based CNC projects.                                          |
|   2 | Harbor version 2.15 has been released.                                                                                   |
|   3 | New features in 2.15:                                                                                                    |
|   4 | Option to disable tags landing onto S3 and different storages to improve garbage collection performance.                 |
|   5 | Upstream proxy cache registry connection limits to avoid wasting rate limits in Docker Hub or other upstream registries. |
|   6 | Support for Cosign v3 signatures.                                                                                        |
|   7 | Next release plans:                                                                                                      |
|   8 | Replace Redis with Valky to improve performance.                                                                         |
|   9 | Support for UTrivy results, including config secrets and additional scan data beyond vulnerabilities.                    |
|  10 | Harbor has two subprojects: Harbor Satellite and Harbor CLI.                                                             |
|  11 | Harbor Satellite:                                                                                                        |
|  12 | Stateless, secretless, zero-trust registry with minimal footprint.                                                       |
|  13 | Designed for edge and gap devices.                                                                                       |
|  14 | Prashant will present on Harbor Satellite at Kubernetes on Edge Day at 12:25 p.m.                                        |
|  15 | Harbor CLI:                                                                                                              |
|  16 | Celebrating 100k+ downloads.                                                                                             |
|  17 | Provides a UI for automating Harbor management and configuration.                                                        |
|  18 | Easier integration into workflows.                                                                                       |
|  19 | Thanks to contributors, especially Lakshit and Patrick, who started as LFX mentees and became maintainers.               |
|  20 | Harbor CLI supports zero CVE workflow for patching images with a single command.                                         |
|  21 | Harbor has a booth at Project Pavilion 20B, available Tuesday to Thursday afternoons.                                    |
|  22 | Community contacts:                                                                                                      |
|  23 | Slack: #Harboradev                                                                                                       |
|  24 | Twitter                                                                                                                  |
|  25 | Mailing list                                                                                                             |
|  26 | LinkedIn page for updates                                                                                                |
|  27 | Bi-weekly community meetings on Wednesdays                                                                               |
|  28 | Encouragement to join meetings, communicate use cases, and visit the booth.                                              |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=jJVZrXuJZ4Q)
