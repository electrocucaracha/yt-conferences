---
layout: default
title:
  "From Creepers to Clusters: Evolving Minecraft Into a Cloud Native... Jaden
  Walderich & Alex Mizerak"
nav_order: 117
parent: Kubecon Cloudnativecon Europe 2026
type: Video Note
description:
  Alex and Jaden, platform engineers at ZAX, shared the evolution of CubeCraft,
  one of the largest Minecraft servers, from its humble beginnings in 2012 as a small
  server for friends to supporting tens of thousands of concurrent players. Init...
resource: https://www.youtube.com/watch?v=XAJySxpKdzo
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

Alex and Jaden, platform engineers at ZAX, shared the evolution of CubeCraft, one of the largest Minecraft servers, from its humble beginnings in 2012 as a small server for friends to supporting tens of thousands of concurrent players.
Initially, as teenagers with limited resources and experience, they relied on overclocked servers, IRC for backend communication, and a monolithic architecture, which eventually became unsustainable as the server grew.
After Microsoft approached them to bring CubeCraft to more platforms, they attempted to break up their monolith into microservices, a process that took four years and resulted in a more scalable but still fragmented and hard-to-maintain system.
Realizing the need for a robust, maintainable solution, they developed Rocket, a universal platform built on OKD (an open-source Kubernetes distribution) and Quarkus, designed to manage both game and data workloads efficiently, with features like custom load balancing, autoscaling, and optimized networking for low latency.
By iterating on their design and focusing on CubeCraft as a flagship client, they created a platform now used by multiple partners, handling thousands of queries per second and massive amounts of player data, while contributing improvements to the open-source community and continuing to refine their architecture for scalability and maintainability.

# Main Points

|   # | Main point                                                                                                                                                 |
| --: | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | CubeCraft started in 2012 as a small Minecraft server for friends, quickly grew to 30,000 concurrent players by 2014.                                      |
|   2 | Original team were teenagers with no formal computer science experience or budget; overclocked servers and used IRC for backend communication.             |
|   3 | Early infrastructure: single Minecraft server instances, backend server with custom plugins, no frameworks, orchestration, or containers.                  |
|   4 | Explosive growth led to scaling challenges and single points of failure (MySQL, IRC).                                                                      |
|   5 | Microsoft approached CubeCraft to bring the server to console and mobile editions.                                                                         |
|   6 | Decided to move from monolithic backend ("masterhub") to microservices; migration took four years.                                                         |
|   7 | Built custom solutions instead of using Kubernetes; resulted in disorganized but more scalable infrastructure.                                             |
|   8 | Realized need for a maintainable, developer-friendly platform rather than just backend services.                                                           |
|   9 | Identified key requirements: low latency, resistance to network attacks, high bandwidth, memory-intensive workloads, large player data, and many features. |
|  10 | Decided to build a universal platform (Rocket) for game studios to focus on games, not infrastructure.                                                     |
|  11 | Chose OKD (open-source OpenShift) as Kubernetes distribution; used Quarkus framework for microservices.                                                    |
|  12 | Platform split into game platform (for running Minecraft servers) and data platform (for data storage, matchmaking, social features).                      |
|  13 | Data platform uses GraphQL as interface, gRPC for microservice communication.                                                                              |
|  14 | Game platform uses Kubernetes with custom load balancing and secondary network interfaces for low latency.                                                 |
|  15 | Used compressed swap memory (zram) to increase server density; experimenting with Kubernetes swap support.                                                 |
|  16 | CubeCraft became Rocket's flagship client, helping iterate and refine the platform for broader use.                                                        |
|  17 | Platform now supports multiple partners and R&D projects (e.g., Hytale).                                                                                   |
|  18 | Current architecture: regional clusters, data clusters, 5,000 GraphQL queries/sec, 16TB player data daily, 1,600 online instance                           |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=XAJySxpKdzo)
