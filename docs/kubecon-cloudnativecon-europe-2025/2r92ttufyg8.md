---
layout: default
title:
  "Fresh Secrets From the Docks: Lessons Learnt From Analyzing 180,000 Public
  Dock... Guillaume Valadon"
nav_order: 99
parent: Kubecon Cloudnativecon Europe 2025
type: Video Note
description:
  The speaker, a French security researcher, discusses the importance of
  scanning for secrets in Docker images. He reveals that 5% of repositories on Docker
  Hub contain secrets, with 60% of these secrets being leaked before 2024. The most
  com...
resource: https://www.youtube.com/watch?v=2r92tTuFYg8
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

The speaker, a French security researcher, discusses the importance of scanning for secrets in Docker images.
He reveals that 5% of repositories on Docker Hub contain secrets, with 60% of these secrets being leaked before 2024.
The most common types of secrets are related to data storage and cloud providers, with 100,000 secrets found across 230 detector types.
The researcher highlights several "docker pitfalls" that can lead to secret leaks, including hardcoded secrets in Docker files, using build arguments to pass secrets, and not properly securing secrets during the build process.
He emphasizes the importance of auditing images for art secrets and using tools like Gardian to scan for secrets, as it is more effective than dealing with a leak after it happens.

# Main Points

|   # | Main point |
| --: | ---------- |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=2r92tTuFYg8)
