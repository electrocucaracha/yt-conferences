---
layout: default
title: "SIG API Machinery: Project Updates and Release Planning - Joe Betz, Google"
nav_order: 285
parent: Kubecon Cloudnativecon Europe 2025
type: Video Note
description:
  The SIG API Machinery is a broad cross-cutting Special Interest Group
  (SIG) within Kubernetes, responsible for the rest mechanics of the Kubernetes API,
  including versioning, serialization protocols, resources, sub-resources, and support
  of...
resource: https://www.youtube.com/watch?v=VCmp--NcxeE
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

The SIG API Machinery is a broad cross-cutting Special Interest Group (SIG) within Kubernetes, responsible for the rest mechanics of the Kubernetes API, including versioning, serialization protocols, resources, sub-resources, and support for building resource definitions such as Custom Resource Definitions (CRDs).
The group focuses on making upgrades safer, improving declarative APIs, and enhancing performance.
Recent features include snapshotable API server cache, emulation version, mixed version proxy, seabboard serializer, declarative validation, coordinated leader election, streaming encoded list responses, and CRD validation ratcheting.
The SIG is actively seeking contributors to improve the toolset for making upgrades safer and more efficient.

# Main Points

|   # | Main point                                                                                                                     |
| --: | ------------------------------------------------------------------------------------------------------------------------------ |
|   1 | The SIG provides support for building resource definitions, including custom resources (CRDs) and control plane extensibility. |
|   2 | Key features of API Machinery include:                                                                                         |
|   3 | Admission control with web hooks and inline logic                                                                              |
|   4 | Controller infrastructure, including the controller manager and informer infrastructure                                        |
|   5 | Support for Go clients, typed and dynamic forms                                                                                |
|   6 | Discovery for clients                                                                                                          |
|   7 | Reliability, scale, and performance of most control plane components                                                           |
|   8 | The SIG is not responsible for API review, all APIs are owned by respective SIGs.                                              |
|   9 | Current beta features include:                                                                                                 |
|  10 | Declarative validation                                                                                                         |
|  11 | Coordinated leader election                                                                                                    |
|  12 | Streaming encoded list responses                                                                                               |
|  13 | CRD validation ratcheting                                                                                                      |
|  14 | Future plans focus on making upgrades safer and more declarative, including:                                                   |
|  15 | Improving defaulting and validation                                                                                            |
|  16 | Bringing CRDs in line with native types                                                                                        |
|  17 | Adding new formats for API fields                                                                                              |
|  18 | Enhancing streaming support and watch mechanism                                                                                |
|  19 | The SIG is actively looking for contributors and can be reached through Slack.                                                 |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=VCmp--NcxeE)
