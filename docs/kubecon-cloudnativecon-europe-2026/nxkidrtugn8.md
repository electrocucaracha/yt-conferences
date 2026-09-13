---
layout: default
title: How To (Not) Fork Headlamp - Joaquim Rocha, Amutable
nav_order: 145
parent: Kubecon Cloudnativecon Europe 2026
type: Video Note
description:
  Raim, a maintainer of Headlamp at Immutable, presents an overview of
  Headlamp—a graphical user interface for Kubernetes focused on operators—and discusses
  its extensibility through a plugin system. He explains that while plugins allow
  for s...
resource: https://www.youtube.com/watch?v=nxkidRtUGn8
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

Raim, a maintainer of Headlamp at Immutable, presents an overview of Headlamp—a graphical user interface for Kubernetes focused on operators—and discusses its extensibility through a plugin system.
He explains that while plugins allow for significant customization, not all core functionalities are exposed to plugins due to maintenance and security considerations, so sometimes forking Headlamp is necessary for deeper changes.
Raim outlines several approaches to forking, including direct cloning, using git subtrees, and git submodules, each with their own pros and cons regarding repository structure, history management, and maintenance burden.
He emphasizes best practices for maintaining forks, such as keeping changes atomic, rebasing frequently, and contributing useful changes back to the upstream project to minimize maintenance overhead.
Ultimately, Raim encourages users to choose the forking strategy that best fits their needs and to leverage both plugins and forks for maximum flexibility when customizing Headlamp.

# Main Points

|   # | Main point                                                                                                                       |
| --: | -------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Headlamp is a graphical user interface (GUI) for Kubernetes, focused on operators.                                               |
|   2 | It allows users to view workloads, open port forwards, and is extensible via plugins.                                            |
|   3 | Headlamp is officially part of the Kubernetes project under SIG UI.                                                              |
|   4 | Can be run as a desktop app, in-cluster, or as a deployed service.                                                               |
|   5 | Extensions exist for Docker, Podman Desktop, and Backstage.                                                                      |
|   6 | Vendor independent; does not require installation in Kubernetes.                                                                 |
|   7 | No authentication layer; relies on Kubernetes or OIDC for auth and adapts UI based on permissions.                               |
|   8 | Extensible via plugins (JavaScript bundles) using an SDK; plugins are dynamically loaded.                                        |
|   9 | Plugin catalog is decentralized and published via Artifact Hub.                                                                  |
|  10 | Plugins can extend the GUI, add routes, actions, branding, and interact with Kubernetes APIs.                                    |
|  11 | Not all functionality is exposed to plugins by default; exposure is based on need and maintenance considerations.                |
|  12 | Plugins allow focused functionality without modifying core Headlamp code.                                                        |
|  13 | Forking may be necessary if plugins are insufficient, for speed, security fixes, or organizational needs.                        |
|  14 | Forking means cloning the project and maintaining a small delta; changes beneficial to the community should be contributed back. |
|  15 | Several ways to fork Headlamp:                                                                                                   |
|  16 | Direct clone: simple, but repo structure and CI are tied to Headlamp.                                                            |
|  17 | Git subtrees: import Headlamp into a subdirectory; history is mixed, but structure is clean.                                     |
|  18 | Git submodules: separate histories for plugin and Headlamp; more complex, not self-contained, but clear separation.              |
|  19 | Submodule pointing to same repo but different branches: used in AKS Desktop; maintains separate histories within one repo.       |
|  20 | Best approach depends on user preference and maintenance needs.                                                                  |
|  21 | Fork maintenance best practices:                                                                                                 |
|  22 | Use atomic commits (one change per commit).                                                                                      |
|  23 | Minimize number of commits in the fork.                                                                                          |
|  24 | Label commits intended for upstream contribution.                                                                                |
|  25 | Rebase early and often.                                                                                                          |
|  26 | Contribute changes upstream frequently.                                                                                          |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=nxkidRtUGn8)
