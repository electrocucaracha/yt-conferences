---
layout: default
title:
  "Navigating the Gateway API Maze: 40+ Implementations, 55+ Features... Beka
  Modebadze & Christine Kim"
nav_order: 222
parent: Kubecon Cloudnativecon Europe 2026
type: Video Note
description:
  The presentation, "Navigating the Gateway API Maze," discusses the evolution
  from Kubernetes' Ingress API to the Gateway API, highlighting the limitations of
  Ingress—such as lack of portability, complexity from annotations, and shared objec...
resource: https://www.youtube.com/watch?v=aBoqH0wf4Yk
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

The presentation, "Navigating the Gateway API Maze," discusses the evolution from Kubernetes' Ingress API to the Gateway API, highlighting the limitations of Ingress—such as lack of portability, complexity from annotations, and shared object confusion—that led to the development of Gateway API as a next-generation, collaborative, and extensible load balancing solution.
The speakers, Becca from Google Cloud and Christine from Cisco, explain the Gateway APIs improved design, including clear role-based personas, support for both L4 and L7 traffic, and a rich ecosystem of controllers and tools to aid migration and management.
They introduce resources like the controller matching wizard, conformance reports, and tools such as "ingress to gateway" and "gateway cuddle" to simplify adoption and visualization.
The talk also covers the project's agile release process, experimental feature channels, and ongoing community-driven development, including extensions for AI inference and agent networking.
In the Q&A, they clarify that Gateway API and Ingress can run in parallel, CRDs are not bundled with Kubernetes by default, and while stable releases aim to avoid breaking changes, minor updates may introduce some, urging operators to stay engaged with the community for support and feedback.

# Main Points

|   # | Main point                                                                                                                                                            |
| --: | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Presentation: "Navigating the Gateway API Maze"                                                                                                                       |
|   2 | Speakers: Becca (Google Cloud, Gateway API release manager) and Christine (Cisco, software engineer)                                                                  |
|   3 | Ingress API in Kubernetes was simple but lacked portability, became complex with annotations, and had issues with multiple users editing the same object              |
|   4 | Gateway API developed as next-generation load balancing API (L4/L7), now stable with a rich ecosystem and collaborative design                                        |
|   5 | Ingress-nginx was recently archived, making migration to Gateway API more relevant                                                                                    |
|   6 | Gateway API introduces clear personas: infrastructure providers, cluster operators, application developers                                                            |
|   7 | Gateway API is a collection of specs and conformance tests, not a standalone binary; requires a controller/operator                                                   |
|   8 | Over 40 conformant controllers available; users can implement their own or choose an existing one                                                                     |
|   9 | Three project types: greenfield (new), ingress migration, and "other" (mixed/advanced)                                                                                |
|  10 | Tools for getting started: use LLMs (e.g., ChatGPT, Gemini) for config generation and translation; official documentation and guides available                        |
|  11 | Controller Matching Wizard helps select controllers based on required features; backed by conformance reports                                                         |
|  12 | Features matrix/comparison table available for in-depth controller comparison                                                                                         |
|  13 | Supported features now listed in gateway class status for easier automation and portability                                                                           |
|  14 | Tools highlighted: "ingress to gateway" (migrates ingress resources to Gateway API CRDs) and "gatewayctl" (visualizes resource relationships)                         |
|  15 | Gateway API release process now uses release trains and experimental channels for agility; features move from experimental to standard after community feedback       |
|  16 | Two adjacent projects: Gateway Inference Extension (smart load balancing for LLM/inference workloads) and KubeAgentic Networking (agent-to-agent/model/tool policies) |
|  17 | Gateway API and Ingress API can run in parallel; Ingress API is frozen, no new features                                                                               |
|  18 | No current plans to bundle Gateway API CRDs with Kubernetes core;                                                                                                     |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=aBoqH0wf4Yk)
