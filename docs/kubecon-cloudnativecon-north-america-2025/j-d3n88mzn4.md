---
layout: default
title:
  "Project Lightning Talk: The Same Great OPA, Only Faster! - Philip Conrad,
  Maintainer"
nav_order: 239
parent: Kubecon Cloudnativecon North America 2025
type: Video Note
description:
  Philip Conrad, a maintainer of the Open Policy Agent (OPA) project, presented
  updates on OPA’s performance improvements at CubeCon, using slides prepared by his
  colleague Sebastian. OPA is a CNCF graduated, general-purpose policy engine that...
resource: https://www.youtube.com/watch?v=j-d3n88MZn4
tags:
  - kubecon-cloudnativecon-north-america-2025
  - video
  - learning
status: stable
generated:
  by: process:yt-conferences-okf
  at: 2026-09-12 00:00:00+00:00
---

# Summary

Philip Conrad, a maintainer of the Open Policy Agent (OPA) project, presented updates on OPA’s performance improvements at CubeCon, using slides prepared by his colleague Sebastian.
OPA is a CNCF graduated, general-purpose policy engine that allows software authorization logic to be decoupled from applications, enabling flexible policy enforcement such as verifying trusted container registries in Kubernetes.
Over the past year, OPA reached its 1.0 release, incorporating significant performance enhancements like reduced unnecessary work, fewer memory allocations, improved interpreter efficiency, and better use of sync.pool in Go.
Additional improvements include more efficient text handling, faster decision log generation, and advancements in the rule indexer and storage layer.
Conrad encouraged users to upgrade to version 1.0, utilize tools like OPA format and the Regal linter, and participate in the active community, highlighting upcoming features and inviting engagement through Slack, the conference booth, and a forthcoming community survey.

# Main Points

|   # | Main point                                                                                                                                      |
| --: | ----------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Philip Conrad is presenting on behalf of Sebastian for the Open Policy Agent (OPA) project at KubeCon.                                          |
|   2 | OPA is a CNCF graduated project, about 10 years old, and has been graduated for at least four years.                                            |
|   3 | OPA is described as a general-purpose policy engine for software, processing inputs through rules to produce outputs.                           |
|   4 | Policies in OPA allow decoupling authorization logic from applications and can check conditions such as container registry trust in Kubernetes. |
|   5 | OPA 1.0 was released in the past year, finalizing language changes and introducing significant performance improvements.                        |
|   6 | Performance improvements include fewer unnecessary operations, reduced allocations, and a more efficient interpreter.                           |
|   7 | Version 1.0 introduced heavier use of sync.Pool in Go to reuse allocations and reduce garbage collector load.                                   |
|   8 | Version 1.4 improved efficiency of several text handling built-ins by reducing allocations.                                                     |
|   9 | Version 1.3 included enhancements for faster decision log generation, aiding audit logging.                                                     |
|  10 | Further improvements were made to the compiler, storage layer, and rule indexer.                                                                |
|  11 | The rule indexer now allows OPA to bail out early on policies that will not succeed, with support for more rule types.                          |
|  12 | Upgrading to OPA 1.0 is relatively easy, with tools like OPA format to automate many changes.                                                   |
|  13 | The Regal Linter is recommended for writing better Rego code and is part of the open-source community.                                          |
|  14 | Upcoming roadmap items include new keywords, string interpolation, rule indexer improvements, and enhanced type checking.                       |
|  15 | The OPA Slack community is active and helpful for users and adopters.                                                                           |
|  16 | OPA has a booth at kiosk 12A, a maintainer talk on Thursday, and an upcoming community survey.                                                  |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=j-d3n88MZn4)
