---
layout: default
title:
  "Project Lightning Talk: youki: What’s New and What’s Next? - Yusuke Sakurai,
  Reviewer"
nav_order: 301
parent: Kubecon Cloudnativecon Europe 2026
type: Video Note
description:
  Yusuke Sakai, a maintainer of Yoki, provides an update on the project's
  recent developments and future plans. Yoki is an OCI-compliant, low-level container
  runtime that has grown beyond its experimental phase, now serving as a practical
  com...
resource: https://www.youtube.com/watch?v=L4AgLkGk_T8
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

Yusuke Sakai, a maintainer of Yoki, provides an update on the project's recent developments and future plans.
Yoki is an OCI-compliant, low-level container runtime that has grown beyond its experimental phase, now serving as a practical component in cloud-native environments and Kubernetes execution flows.
Recent updates include support for net devices and Linux memory policy, improved compatibility with other runtimes and the OCI specification, expanded testing, and various bug fixes and security improvements.
Looking ahead to version 1.0.0, the roadmap focuses on enhancing real-world compatibility with other runtimes, integrating microVM-based container execution for stronger isolation, and simplifying Kubernetes adoption through easier deployment methods.
These efforts aim to make Yoki more practical, reliable, and accessible for broader use.

# Main Points

|   # | Main point                                                                                                                        |
| --: | --------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Yusuke Sakai is a maintainer of Yoki and provides an update on the project.                                                       |
|   2 | Yoki is an OCI runtime written in Rust, similar to runtimes like runc or crun.                                                    |
|   3 | The project has about 7,300 GitHub stars and became a CNCF sandbox project in October 2024.                                       |
|   4 | Yoki is now part of the broader cloud native runtime ecosystem and is no longer just experimental.                                |
|   5 | Yoki operates at the low-level runtime layer in the Kubernetes execution flow.                                                    |
|   6 | Recent updates:                                                                                                                   |
|   7 | Added support for net devices and Linux memory policy, aligning with newer OCI runtime specifications.                            |
|   8 | Net device support is important for Kubernetes networking models, especially for AI, ML, and high-performance workloads.          |
|   9 | Memory policy support is relevant for NUMA workloads.                                                                             |
|  10 | Improved compatibility with runc behavior and the OCI specification.                                                              |
|  11 | Expanded OCI conformance and compatibility testing.                                                                               |
|  12 | Bug fixes and security improvements, including general stability and shell-related fixes.                                         |
|  13 | The project is becoming more practical and reliable.                                                                              |
|  14 | Roadmap toward Yoki 1.0.0 focuses on practicality for production use:                                                             |
|  15 | Improve compatibility with runc, including features outside the specification like exec update and checkpoint.                    |
|  16 | Continue aligning Yoki’s behavior with runc and expand compatibility test coverage.                                               |
|  17 | Add support for microVM-based containers using libkrun, enabling lightweight VM-based container execution for stronger isolation. |
|  18 | Explore integration of this execution model with Yoki.                                                                            |
|  19 | Make Kubernetes adoption easier by simplifying installation and configuration steps.                                              |
|  20 | Plan to introduce deployment tooling similar to kata-deploy for easier and repeatable setup on Kubernetes.                        |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=L4AgLkGk_T8)
