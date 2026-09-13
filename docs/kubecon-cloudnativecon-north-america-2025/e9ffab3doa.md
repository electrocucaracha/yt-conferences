---
layout: default
title: Adopting a Fleet-first Mindset - Andy Beane, Spotify
nav_order: 11
parent: Kubecon Cloudnativecon North America 2025
type: Video Note
description:
  The speaker, an engineer at Spotify, discusses the challenges of managing
  software at scale and the evolution toward a "fleet first" mindset, which treats
  all software components as a unified fleet. Historically, migrations and updates
  acro...
resource: https://www.youtube.com/watch?v=-E9ffAB3DoA
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

The speaker, an engineer at Spotify, discusses the challenges of managing software at scale and the evolution toward a "fleet first" mindset, which treats all software components as a unified fleet.
Historically, migrations and updates across Spotify’s vast and complex ecosystem were slow and labor-intensive, often taking months and requiring significant coordination among teams.
By standardizing on "golden technologies," adopting declarative infrastructure, and building the Fleet Shift platform, Spotify now automates fleetwide changes—such as dependency updates, security patches, and infrastructure optimizations—through automated pull requests and continuous monitoring, drastically reducing manual effort and engineering toil.
This approach has saved hundreds of thousands of engineering hours, enabled rapid responses to incidents (e.g., patching 80% of services for Log4j in 11 hours), and improved the consistency and reliability of software maintenance.
Looking ahead, Spotify aims to further enhance fleet management with AI-driven automation and broader adoption, continuing to reduce complexity and empower engineers to focus on higher-value work.

# Main Points

|   # | Main point                                                                                                                                         |
| --: | -------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Spotify's engineering team manages a large and complex software ecosystem with thousands of components.                                            |
|   2 | The number of software components has grown faster than the number of engineers, increasing maintenance and migration challenges.                  |
|   3 | Spotify handles over 3,800 production deployments per day, 1.7 trillion events per day, and 10 million peak requests per second.                   |
|   4 | Migrations, such as updating the Apollo framework, historically took around 200 days to complete.                                                  |
|   5 | Traditional migration approaches required significant manual effort from many teams, leading to slow and inconsistent adoption.                    |
|   6 | The "fleet first" mindset automates fleetwide changes, reducing manual intervention and increasing speed and consistency.                          |
|   7 | Fleet Shift is Spotify's platform for automating fleetwide changes, creating jobs that clone repos, apply transformations, and open pull requests. |
|   8 | Automerging is used where possible, based on eligibility criteria like passing tests and team availability.                                        |
|   9 | Golden technologies (standardized libraries, frameworks, tools) enable easier fleetwide changes and maintenance.                                   |
|  10 | Infrastructure is defined in code (YAML), making deployments standardized, versioned, and auditable.                                               |
|  11 | Fleetwide changes can be recurring (e.g., dependency updates, security patches) or one-time (e.g., major migrations).                              |
|  12 | Targeting components for changes can be done via code search, data queries, or explicit lists.                                                     |
|  13 | Communication and context are included in automated PRs to aid understanding and transparency.                                                     |
|  14 | Fleet Shift has saved over 450,000 engineering hours in the first half of 2025 and created over 2.4 million PRs.                                   |
|  15 | Real-life examples include rapid patching of log4j vulnerabilities and ongoing dependency updates.                                                 |
|  16 | Migration to monorepos is underway, enabling faster and safer fleetwide changes.                                                                   |
|  17 | AI is being explored to automate more complex code refactorings.                                                                                   |
|  18 | Key assumptions for this approach include test automation and standardized technology.                                                             |
|  19 | Adoption of fleet management                                                                                                                       |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=-E9ffAB3DoA)
