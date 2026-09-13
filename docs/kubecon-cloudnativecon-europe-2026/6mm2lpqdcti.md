---
layout: default
title:
  "Project Lightning Talk: What’s New In Kairos, 2026 Edition - Mauro Morales,
  Maintainer"
nav_order: 298
parent: Kubecon Cloudnativecon Europe 2026
type: Video Note
description:
  Mar Morales, a maintainer of the Kyros project, provides an update on
  the sandbox project's progress, currently at version 43. Kyros transforms Linux
  systems into immutable, image-based, declarative, and container-based systems, supporting...
resource: https://www.youtube.com/watch?v=6MM2LpqDCTI
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

Mar Morales, a maintainer of the Kyros project, provides an update on the sandbox project's progress, currently at version 43.
Kyros transforms Linux systems into immutable, image-based, declarative, and container-based systems, supporting various Linux and Kubernetes distributions to simplify day-two operations like upgrades and rollbacks.
Community use cases include Deep Network, which leverages Kyros's trusted boot feature for secure devices, and Arya Imaging, which uses Kyros on Nvidia boards for consistent, rollback-capable deployments in agricultural technology.
Recent developments include the Chyros init tool for easy image conversion, the Chyros factory for generating bootable artifacts, and the Chyros operator for managing system operations via Kubernetes.
The team has also introduced their own minimal Linux distribution optimized for Kubernetes and welcomed William Rizzo as a new maintainer.

# Main Points

|   # | Main point                                                                                                                                 |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------ |
|   1 | Mar Morales is a maintainer of the Kyros project, a sandbox project currently at version 43.                                               |
|   2 | Kyros transforms Linux systems into immutable, image-based systems.                                                                        |
|   3 | Supports making Ubuntu and openSUSE immutable.                                                                                             |
|   4 | Kyros is declarative, container-based, and uses familiar Kubernetes tools.                                                                 |
|   5 | Focused on Linux and Kubernetes workloads.                                                                                                 |
|   6 | Default Kubernetes options are K3s and KES; community providers support other distributions.                                               |
|   7 | Kyros aims to simplify day-2 operations such as upgrades, rollbacks, and node resets across edge and cloud environments.                   |
|   8 | Community use case: Deep Network uses Kyros with trusted boot and TPM to ensure only signed systems run, preventing tampering.             |
|   9 | Community use case: Arya Imaging uses Kyros on Nvidia boards in tractors for consistent, rollback-capable images in agricultural analysis. |
|  10 | New features:                                                                                                                              |
|  11 | Chyros init: One-liner tool to convert Dockerfiles into Kyros-ready images.                                                                |
|  12 | Chyros factory: Generates bootable artifacts (ISOs, raw images, cloud images) from Kyros images.                                           |
|  13 | Chyros operator: Enables system operations (like node upgrades) directly from Kubernetes clusters.                                         |
|  14 | Kyros is developing its own minimal, upstream-focused Linux distribution for Kubernetes, image-based, and immutable deployments.           |
|  15 | William Rizzo (WR code on GitHub, Field CTO at Mirantis) has joined as a maintainer, working on the Kyros copy feature.                    |
|  16 | Kyros will be at project pavilion booth 18A tomorrow morning and Thursday afternoon.                                                       |
|  17 | Session: "Cloud Native at the Farm Edge" on Thursday at 13:45 in the auditorium, discussing Kyros use with Arya Imaging in farming.        |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=6MM2LpqDCTI)
