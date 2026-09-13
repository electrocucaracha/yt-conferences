---
layout: default
title:
  OpenFeature Update From the Ma... Lukas Reining, André Silva, Thomas Poignant
  & Alexandra Oberaigner
nav_order: 231
parent: Kubecon Cloudnativecon Europe 2026
type: Video Note
description:
  The OpenFeature maintainers provided an update on the project's progress,
  beginning with introductions and an overview for newcomers. OpenFeature is an incubating
  CNCF project that offers a vendor-agnostic, open specification for feature fl...
resource: https://www.youtube.com/watch?v=9ebYq4cbjIY
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

The OpenFeature maintainers provided an update on the project's progress, beginning with introductions and an overview for newcomers.
OpenFeature is an incubating CNCF project that offers a vendor-agnostic, open specification for feature flagging, allowing developers to toggle features at runtime without modifying source code.
The team highlighted recent advancements, including the move of most SDKs to version 1.0, growing community adoption, and contributions from major companies.
Key technical updates included the OpenFeature Remote Evaluation Protocol (OFREP) to further reduce vendor lock-in, the MCP tool for enhanced agent communication and automation, and new GitHub Actions and command-line tools to streamline flag management and consistency.
The maintainers also discussed community-driven design decisions, such as supporting isolated API instances for advanced use cases, and ongoing efforts to separate API from implementation packages.
They encouraged participation, highlighted educational resources, and addressed audience questions on performance optimization and future MCP capabilities, emphasizing the project's growth and openness to new contributors.

# Main Points

|   # | Main point                                                                                                                                                                                             |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   1 | Maintainers introduced themselves: Andre (Lexus Nexus, governance committee), Lucas (Codecentric, technical committee), Alex (Dynatrace, contributor), Thomas (John Conference, governance committee). |
|   2 | Agenda: Introduction to OpenFeature, updates on MCP and Offrep, GitHub actions/CLI, community insights, Q&A.                                                                                           |
|   3 | OpenFeature is an incubating CNCF project providing an open, vendor-agnostic specification for feature flagging.                                                                                       |
|   4 | Feature flags allow enabling/disabling features at runtime without code changes.                                                                                                                       |
|   5 | OpenFeature SDK standardizes flag evaluation; providers are plug-and-play for different flag management systems.                                                                                       |
|   6 | Supported SDKs: React, Angular (recently 1.0), Kotlin, Swift (in progress), C++ (early stage), Java, Python, JS, etc.                                                                                  |
|   7 | Community adoption and usage are growing; more companies (e.g., Datadog, Google, Spotify) are contributing.                                                                                            |
|   8 | OpenFeature is now featured on the ThoughtWorks Radar.                                                                                                                                                 |
|   9 | Offrep (OpenFeature Remote Evaluation Protocol) aims to further reduce vendor lock-in and standardize provider integration via two simple APIs (single and bulk flag evaluation).                      |
|  10 | Offrep is adopted by vendors like flagd, DevCycle, GoFlag, Flipt; 1.0 release is imminent.                                                                                                             |
|  11 | MCP (Management Control Plane) is in active development, providing enhanced agent intelligence and best practices, leveraging Offrep for flag queries.                                                 |
|  12 | OpenFeature GitHub Action and CLI enable flag-driven development, flag change tracking, and consistency across environments/providers.                                                                 |
|  13 | CLI commands: pull (fetch remote config), compare (diff manifests), generate (create typed variables).                                                                                                 |
|  14 | Singleton API pattern is used for simplicity, but advanced use cases (micro frontends, dependency injection, parallel testing) prompted work on isolated API instances.                                |
|  15 | Proposal to separate API from implementation packages for stability and easier library integration is under discussion.                                                                                |
|  16 | Free feature flagging course available on LFX Education platform; 500+ enrollments.                                                                                                                    |
|  17 | Community is growing, with over 120 cont                                                                                                                                                               |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=9ebYq4cbjIY)
