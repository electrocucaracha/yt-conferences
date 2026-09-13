---
layout: default
title:
  "What Survived Production: Operating Game Backends at Million-Player Scale
  - Berkay Uckac"
nav_order: 396
parent: Kubecon Cloudnativecon Europe 2026
type: Video Note
description:
  At CubeCon 2026 in Amsterdam, Barai shared insights from three years
  of backend development for March Gardens, a mobile game launched in 2020. After
  initial success and a plateau in metrics, the team revamped the game in 2023, leading
  to a...
resource: https://www.youtube.com/watch?v=Aa04SuPhxtA
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

At CubeCon 2026 in Amsterdam, Barai shared insights from three years of backend development for March Gardens, a mobile game launched in 2020.
After initial success and a plateau in metrics, the team revamped the game in 2023, leading to a significant increase in downloads and player engagement.
To support ongoing live operations, they built an internal platform called James, focusing on features like A/B testing, campaign management, analytics, and multiplayer tournaments, all managed by a small server team.
Their backend architecture emphasizes simplicity, high availability, and scalability, utilizing Kubernetes, Go, MongoDB Atlas, and managed services to minimize operational overhead.
Barai highlighted the importance of a decision journal for tracking architectural choices, shared lessons from incidents and scaling challenges, and stressed the value of keeping systems straightforward to ensure reliability and ease of management for a small team.

# Main Points

|   # | Main point                                                                                                               |
| --: | ------------------------------------------------------------------------------------------------------------------------ |
|   1 | Speaker: Barai, presenting backend experiences from the last three years at CubeCon 2026 Amsterdam                       |
|   2 | Focus on small teams and operational complexities in backend development                                                 |
|   3 | Main product: March Gardens, a mobile game launched in 2020                                                              |
|   4 | Game metrics plateaued; major revamp in 2023 led to 1000% more downloads                                                 |
|   5 | Liveops is a key concept: post-launch content, AB testing, campaigns, segmentation, analytics, multiplayer tournaments   |
|   6 | Built an internal liveops platform called James                                                                          |
|   7 | High availability prioritized for global, always-online player base                                                      |
|   8 | Backend managed by a small team (grew from 1 to 3 people)                                                                |
|   9 | Chose vendor neutrality and developer-friendly programming language (Go)                                                 |
|  10 | Infrastructure: GCP, single VPC, three GKE clusters, MongoDB Atlas, Confluent Kafka, Prometheus, Grafana                 |
|  11 | Production runs on three 4-core nodes; lightweight platform                                                              |
|  12 | Used a decision journal for major architectural choices, with ease-of-change estimates                                   |
|  13 | Adopted a "micro model" approach: microservices only where scalability required, mostly stateless, Go containers         |
|  14 | Kubernetes chosen for high availability, self-healing, ecosystem, and operational familiarity                            |
|  15 | Trade-offs: initial setup time, operational cost, GKE platform limitations                                               |
|  16 | Communication: HTTP for most services, Kafka and websockets added for async and real-time needs (e.g., in-app purchases) |
|  17 | Go praised for efficient websocket handling (tens of thousands of open connections)                                      |
|  18 | Document database (MongoDB) chosen for evolving player-centric schemas; ClickHouse used for hot analytics storage        |
|  19 | Observability: Prometheus, Grafana, GCP managed services, PagerDuty for alerts                                           |
|  20 | Minimal developer tooling; simple multi-tenant system via namespaces and Bash scripts                                    |
|  21 | Caching: avoided Redis, used in-memory or simple Go key-value store for small, dynamic data                              |
|  22 | Major incidents: GCP network failure, client-side request spike, HPA misconfiguration causing resource chaos             |
|  23 | Scaling: built proactive autoscaling tool for predictable player                                                         |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=Aa04SuPhxtA)
