---
layout: default
title:
  "Kubernetes-Native ≠ Cloud Native: Avoiding Architecture Theater - Prerit Munjal,
  Groupon"
nav_order: 197
parent: Kubecon Cloudnativecon Europe 2026
type: Video Note
description:
  The speaker, a senior technical product manager at Groupon, discusses
  the distinction between "Kubernetes native" and "cloud native," emphasizing that
  these terms mean different things to different people and organizations. He argues
  that w...
resource: https://www.youtube.com/watch?v=T1inWaulUyQ
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

The speaker, a senior technical product manager at Groupon, discusses the distinction between "Kubernetes native" and "cloud native," emphasizing that these terms mean different things to different people and organizations.
He argues that while Kubernetes and cloud-native approaches are often conflated, Kubernetes is not suitable for every company, especially at large scale, due to its operational complexity, increased codebase, and maintenance overhead.
Through personal experience and benchmarks, he demonstrates that Kubernetes-native applications require significantly more code and configuration than non-cloud-native approaches, often without delivering proportional benefits in scalability, resiliency, or developer experience.
The speaker suggests that many problems addressed by the cloud-native ecosystem are not relevant for most companies, and that adding layers of abstraction and tooling can create more issues than they solve.
Ultimately, he advocates for a pragmatic approach: focus on actual business needs, avoid unnecessary complexity, and empower developers to manage infrastructure directly when possible, rather than blindly adopting the latest trends or tools.

# Main Points

|   # | Main point                                                                                                                                                         |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   1 | Approximately 950 RSVPs, about 300 attendees present                                                                                                               |
|   2 | Talk title: "Kubernetes native is not equal to cloud native and avoiding architectural theatrics"                                                                  |
|   3 | Speaker is Senior Technical Product Manager at Groupon, manages CI/CD, observability, cloud, Kubernetes, databases, infrastructure, and platform engineering teams |
|   4 | Believes real things happen offline, values in-person events like CubeCon                                                                                          |
|   5 | Speaker creates content on YouTube and LinkedIn, has 100K followers, 20 million yearly impressions                                                                 |
|   6 | Talk originated from a conversation with Kelsey Hightower questioning the need for Kubernetes                                                                      |
|   7 | Cloud native has different definitions for different people and organizations                                                                                      |
|   8 | Audience polled on what cloud native means; responses varied (portability, scalability, resiliency, disaster recovery, etc.)                                       |
|   9 | No solid CNCF definition for cloud native; generally should be agnostic                                                                                            |
|  10 | Portability is difficult and often not relevant for most companies; migrations are hard                                                                            |
|  11 | At Groupon: 423 microservices, use AWS and GCP, large Kubernetes footprint (400 nodes, 10,000–50,000 pods)                                                         |
|  12 | Kubernetes native means the app "speaks Kubernetes," but most people lack deep Kubernetes knowledge                                                                |
|  13 | Kubernetes is not for everyone; may be overkill for high-scale companies, better suited for mid-scale                                                              |
|  14 | Building Kubernetes native apps is complex and requires significant engineering effort                                                                             |
|  15 | More Kubernetes layers and tools (Helm, YAML, etc.) do not necessarily improve developer experience (DX)                                                           |
|  16 | Cloud native ecosystem creates new problems and solutions, leading to tool proliferation and increased costs                                                       |
|  17 | Platform engineering is not always necessary; ideally, developers should own infrastructure                                                                        |
|  18 | More code and configuration increases liability and maintenance burden                                                                                             |
|  19 | Kubernetes codebase is 3x larger than non-cloud native; more files, dependencies, and slower benchmarks                                                            |
|  20 | For most use cases, cloud native (not Kubernetes native) is sufficient; avoid unnecessary complexity                                                               |
|  21 | 80% of incidents caused by operation                                                                                                                               |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=T1inWaulUyQ)
