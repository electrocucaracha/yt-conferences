---
layout: default
title:
  "Declarative Edge Kubernetes: Immutable Clusters with Talos + Zarf - Brandt
  Keller & Merijn Keppel"
nav_order: 89
parent: Kubecon Cloudnativecon Europe 2026
type: Video Note
description:
  In this session, Brent Keller and Marell discuss deploying and managing
  Kubernetes clusters in air-gapped and edge environments using Talos Linux and Zarf.
  They demonstrate a live setup with pre-provisioned Talos Linux nodes, highlighting
  T...
resource: https://www.youtube.com/watch?v=6Ss9wMZhMJc
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

In this session, Brent Keller and Marell discuss deploying and managing Kubernetes clusters in air-gapped and edge environments using Talos Linux and Zarf.
They demonstrate a live setup with pre-provisioned Talos Linux nodes, highlighting Talos’s declarative, immutable, and deterministic configuration, which is especially valuable for isolated or low-connectivity scenarios.
The presenters show how Zarf enables portable, declarative application packaging and deployment by initializing an internal registry and mutating image references, making it easier to manage applications and updates in disconnected environments.
They further illustrate updating the Talos operating system itself from within Kubernetes using a custom controller and Zarf package, emphasizing the importance of sustainable, reliable, and reproducible workflows.
The session concludes by reinforcing the benefits of declarative and immutable infrastructure for both application and system updates, and invites attendees to explore further or ask questions.

# Main Points

|   # | Main point                                                                                                                        |
| --: | --------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Presenters: Brent Keller (Defense Unicorns, CNCF ambassador, OpenSSF maintainer) and Marell (True Fullstack principal consultant) |
|   2 | Live demo using home lab hardware pre-provisioned with Talos Linux in maintenance mode                                            |
|   3 | Focus on declarative, deterministic, and immutable edge Kubernetes deployments                                                    |
|   4 | Slides are high-level; emphasis on live demonstration                                                                             |
|   5 | Stages covered: preparation, takeoff (Talos Linux), ascent (workload deployment with Zarf), operation (sustainable management)    |
|   6 | Edge and airgapped Kubernetes deployments face challenges like poor/no connectivity                                               |
|   7 | Goal: create highly available, reliable systems regardless of environment (cloud, edge, airgap)                                   |
|   8 | Importance of managing dependencies and deploying in declarative, deterministic ways                                              |
|   9 | Immutability enables predictable, scoped, and safe changes (replacement over modification)                                        |
|  10 | Talos Linux: declarative, immutable OS configured via YAML; no manual intervention needed                                         |
|  11 | Cluster bootstrapped with Talos; nodes configured with static IPs; cluster formed via Talos commands                              |
|  12 | Zarf used for declarative package management and airgap application deployment                                                    |
|  13 | Zarf bootstraps an internal registry for image management in airgapped environments                                               |
|  14 | Zarf agent mutates image references to point to internal registry; supports GitOps tools (Argo, Flux)                             |
|  15 | Application deployment demonstrated with a declarative Zarf package (Doom game)                                                   |
|  16 | Zarf packages are portable, signed, and include SBOMs for supply chain security                                                   |
|  17 | Talos Linux can be updated from within Kubernetes using a custom controller and CRD via Talos API                                 |
|  18 | OS upgrades managed declaratively as Zarf packages, including all necessary images and manifests                                  |
|  19 | Emphasis on sustainability, reliability, and secure feedback loops in airgapped/edge environments                                 |
|  20 | Zarf package creation fails fast if dependencies are missing, ensuring completeness before deployment                             |
|  21 | Immutable clusters and declarative workflows preferred over imperative, manual changes                                            |
|  22 | Demo showed successful ap                                                                                                         |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=6Ss9wMZhMJc)
