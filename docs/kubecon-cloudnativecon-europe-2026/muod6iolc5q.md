---
layout: default
title:
  "Keynote: How Ubisoft Orchestrates Global Multiplayer Games wit... Jean-François
  Hubert & Mark Mandel"
nav_order: 175
parent: Kubecon Cloudnativecon Europe 2026
type: Video Note
description:
  Jean-François, Software Development Director at Ubisoft, and Mark Mandel,
  founder of Agones, discuss how they have built a global multiplayer infrastructure
  by leveraging cloud-native and open-source technologies, specifically Kubernetes
  an...
resource: https://www.youtube.com/watch?v=MUOd6IoLC5Q
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

Jean-François, Software Development Director at Ubisoft, and Mark Mandel, founder of Agones, discuss how they have built a global multiplayer infrastructure by leveraging cloud-native and open-source technologies, specifically Kubernetes and the CNCF ecosystem.
Instead of creating custom integrations for each cloud provider, they adopted a "build-once, deploy-everywhere" approach, allowing their workloads to run seamlessly across any cloud or on-premises environment.
Agones, an open-source project now part of the CNCF sandbox, enables Kubernetes to host, scale, and orchestrate authoritative multiplayer game servers, which is crucial for real-time gameplay where low latency and global server placement are essential.
This architecture was successfully used in the global launch of Rainbow Six Mobile, allowing Ubisoft to dynamically adapt to regional demand and ensure a stable, scalable experience for millions of players.
Agones has become widely adopted in the industry, with many contributors, and both speakers encourage others to learn more and get involved.

# Main Points

|   # | Main point                                                                                                                              |
| --: | --------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Jean-François is the software development director at Ubisoft.                                                                          |
|   2 | Mark Mandel is the founder of Agones, presenting independently from Discord.                                                            |
|   3 | The presentation focuses on building global multiplayer infrastructure using cloud-native and open-source technologies.                 |
|   4 | Creating tailored integrations for each cloud provider is unsustainable due to increasing differences and custom code requirements.     |
|   5 | Ubisoft adopted Kubernetes and the CNCF ecosystem to define their operational model.                                                    |
|   6 | This approach enables a build-once, deploy-everywhere strategy across any cloud provider or on-premises.                                |
|   7 | CNCF projects evolve faster than in-house solutions due to contributions from thousands of developers.                                  |
|   8 | Ubisoft leverages CNCF projects for operational maturity to support massive multiplayer games worldwide.                                |
|   9 | Authoritative multiplayer game server workloads are unique; all players connect to a single server that maintains game state in memory. |
|  10 | Game servers cannot be shut down during play without crashing the game.                                                                 |
|  11 | Agones is an open-source project that enables Kubernetes to host, scale, and orchestrate game servers.                                  |
|  12 | Agones recently became a CNCF sandbox project.                                                                                          |
|  13 | Low latency is crucial for real-time gameplay, requiring global server deployment close to players.                                     |
|  14 | Agones allows dynamic placement of server capacity based on player location.                                                            |
|  15 | Rainbow Six Mobile used this architecture for a stable, scalable global launch, serving millions of sessions across regions.            |
|  16 | The infrastructure adapts to different regional peaks and availability, routing traffic and capacity to the best cloud provider.        |
|  17 | Agones has become widely adopted in the industry over the past 8 years, with many contributors.                                         |
|  18 | Ubisoft invites others to learn more about Agones and join their community.                                                             |
|  19 | Ubisoft encourages trying Rainbow Six Mobile and visiting their website for more information.                                           |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=MUOd6IoLC5Q)
