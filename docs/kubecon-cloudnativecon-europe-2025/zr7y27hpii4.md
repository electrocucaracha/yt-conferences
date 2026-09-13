---
layout: default
title: "Set Your Developers Free: Fleet Management at Spotify - Stefan Särne, Spotify"
nav_order: 301
parent: Kubecon Cloudnativecon Europe 2025
type: Video Note
description:
  Stefan, a Spotify engineer, shares the story of how they handled a security
  incident involving Log4j 1.4.12, which allowed attackers to execute arbitrary code
  in their backend services. The team realized that their current approach to manag...
resource: https://www.youtube.com/watch?v=Zr7y27HpII4
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

Stefan, a Spotify engineer, shares the story of how they handled a security incident involving Log4j 1.4.12, which allowed attackers to execute arbitrary code in their backend services.
The team realized that their current approach to managing software updates was not scalable and decided to implement fleet management, a process that automates the deployment of updates across all services and pipelines.
This involved creating a "fleet shift" service that pushes changes to GitHub, runs continuous integration tests, and deploys updates automatically.
As a result, the team was able to complete 70% of their migrations in under two weeks, freeing up time for engineers to focus on feature development.
The implementation has also led to increased efficiency and reduced the workload of engineers by an estimated 355 full-time equivalent years.

# Main Points

|   # | Main point |
| --: | ---------- |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=Zr7y27HpII4)
