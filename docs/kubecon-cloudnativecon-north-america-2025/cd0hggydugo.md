---
layout: default
title:
  "Lightning Talk: Know Before You Go! Speedrun Intro To Gateway API - Christine
  Kim"
nav_order: 151
parent: Kubecon Cloudnativecon North America 2025
type: Video Note
description:
  Christine from Isovalent introduces the Gateway API as the successor
  to Kubernetes Ingress, highlighting its role-oriented, portable design that allows
  users to avoid vendor lock-in and switch implementations easily. She explains that
  Gatew...
resource: https://www.youtube.com/watch?v=Cd0hGGydUGo
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

Christine from Isovalent introduces the Gateway API as the successor to Kubernetes Ingress, highlighting its role-oriented, portable design that allows users to avoid vendor lock-in and switch implementations easily.
She explains that Gateway API supports advanced routing features such as URL and header-based routing, traffic splitting, and both north-south and east-west traffic management, with extensibility through reference grants and policy attachments.
To get started, users need to select a gateway controller, install the Gateway CRDs, deploy a gateway, and apply an HTTP route, with the latest standard release being version 1.4.
Christine also recommends resources like the official guides, the ingress-to-gateway translation tool, and gateway-cuddle for visualizing resources, and encourages community involvement and feedback through GitHub discussions and SIG network participation.

# Main Points

|   # | Main point                                                                                                    |
| --: | ------------------------------------------------------------------------------------------------------------- |
|   1 | Christine from Isovalent, committer to Gateway API, Cilium, and upstream projects                             |
|   2 | Presentation is a beginner speedrun to Gateway API                                                            |
|   3 | Gateway API is the successor to Ingress, which is now frozen (no new features)                                |
|   4 | Gateway API introduces new objects and a role-oriented, portable API design                                   |
|   5 | Portability allows use of different vendors and implementations without being tied to one                     |
|   6 | Supports URL-based and header-based routing (e.g., routing /login.example.com to food.service)                |
|   7 | Enables traffic splitting (e.g., 90% to version one, 10% to version two)                                      |
|   8 | Gateway API has comprehensive documentation and user guides                                                   |
|   9 | Supports both north-south and east-west traffic definitions using CRDs                                        |
|  10 | Features include reference grants and policy attachments for extended usability                               |
|  11 | End user steps: select gateway controller, install Gateway CRDs, deploy gateway, apply HTTPRoute              |
|  12 | Latest release is version 1.4, now the standard channel                                                       |
|  13 | Implementations must pass conformance tests for each release                                                  |
|  14 | Example gateway can specify class name (e.g., Cilium) and is portable across implementations                  |
|  15 | HTTPRoute example listens for the deployed gateway                                                            |
|  16 | Resources for getting started: guides on the Gateway API site                                                 |
|  17 | Tools: ingress-to-gateway (translates Ingress to Gateway API), gateway-cuddle (visualizes resources)          |
|  18 | Encouragement to provide feedback and get involved with the community (SIG Network group, GitHub discussions) |
|  19 | Contact Christine for questions                                                                               |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=Cd0hGGydUGo)
