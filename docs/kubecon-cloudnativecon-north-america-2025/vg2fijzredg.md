---
layout: default
title:
  "Managing a Million Infra Resources at Spotify: Designing the Platfo... Oliver
  Soell & Fredrik Sommar"
nav_order: 163
parent: Kubecon Cloudnativecon North America 2025
type: Video Note
description:
  In this KubeCon talk, Spotify engineers Frederick and Oliver discuss
  the evolution of Spotify’s internal resource management platform, which supports
  nearly a million resources across more than 150 types. Initially, after migrating
  to Googl...
resource: https://www.youtube.com/watch?v=Vg2FiJZReDg
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

In this KubeCon talk, Spotify engineers Frederick and Oliver discuss the evolution of Spotify’s internal resource management platform, which supports nearly a million resources across more than 150 types.
Initially, after migrating to Google Cloud Platform in 2016, Spotify faced challenges with manual infrastructure management, prompting the development of a Kubernetes-based declarative infrastructure platform in 2020.
This platform leverages Kubernetes Resource Model (KRM) and GitOps principles, enabling platform teams to manage resources at scale and feature teams to request resources like Bigtable more easily.
However, operational scaling issues and poor user experiences led Spotify to introduce new tools—Crow, a no-code solution for abstractions and compositions, and K-pop, an internal tool for managed operators using familiar technologies like gRPC and protobuf—to simplify platform extension development and improve ergonomics.
The team also enhanced developer experiences by integrating resource management into IDEs and Backstage, providing real-time validation and feedback.
Through these improvements, Spotify aims to make resource management more scalable, user-friendly, and ubiquitous across developer workflows.

# Main Points

|   # | Main point                                                                                                                                     |
| --: | ---------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Spotify uses Google Cloud Bigtable for playlist storage, managed by a dedicated platform team.                                                 |
|   2 | Resource management platform bridges feature teams (e.g., playlist) and platform teams (e.g., storage).                                        |
|   3 | Spotify migrated from data centers to Google Cloud Platform (GCP) in 2016, initially managing resources manually via GCP console.              |
|   4 | In 2020, Spotify built a Kubernetes-based declarative infrastructure platform for resource management.                                         |
|   5 | Platform manages nearly 1 million resources of 150+ kinds, with 15+ platform teams involved.                                                   |
|   6 | Initial challenges included manual configuration, scaling issues, and poor user experience for both feature and platform developers.           |
|   7 | Feature developers found resource configuration too low-level and slow feedback cycles.                                                        |
|   8 | Platform developers struggled with writing Kubernetes operators, which differed from their usual Java microservices work.                      |
|   9 | Strategy for improvement focuses on:                                                                                                           |
|  10 | Making platform extensions easier for platform teams.                                                                                          |
|  11 | Making resource management ubiquitous in developer tools (Backstage, GitHub, IDE, etc.).                                                       |
|  12 | Three patterns for platform extension: abstractions (intent-focused), compositions (multi-resource), and external API calls.                   |
|  13 | Introduced Crow (open-source, no-code tool for abstractions/compositions) and K-pop (internal tool using protobuf/gRPC for managed operators). |
|  14 | Crow reduces YAML complexity and development time for abstractions.                                                                            |
|  15 | K-pop allows platform developers to work in familiar stacks (Java, protobuf) and offloads operational complexity.                              |
|  16 | Backstage integration provides feature developers with live resource state and commit impact views.                                            |
|  17 | IDE integration enables field validation and semantic validation via gRPC API, reducing CI/CD feedback delays.                                 |
|  18 | Platform clusters are sharded by namespace for scalability; close collaboration with Google for cluster performance.                           |
|  19 | Resource cleanup is automated via GitOps; rollbacks are managed for supported configurations.                                                  |
|  20 | Platform team supports other platfor                                                                                                           |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=Vg2FiJZReDg)
