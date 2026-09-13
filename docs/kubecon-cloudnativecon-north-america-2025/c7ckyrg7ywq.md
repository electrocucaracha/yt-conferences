---
layout: default
title:
  "Keynote: Predictive Scaling and Capacity Planning With Machine Learni... Artur
  Souza & Chunpeng Wang"
nav_order: 126
parent: Kubecon Cloudnativecon North America 2025
type: Video Note
description:
  Amazon uses a combination of reactive and proactive scaling strategies
  to handle peak traffic during events like Black Friday. Reactive scaling relies
  on monitoring systems to detect high CPU utilization and trigger scaling actions,
  but it...
resource: https://www.youtube.com/watch?v=C7cKYRg7YwQ
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

Amazon uses a combination of reactive and proactive scaling strategies to handle peak traffic during events like Black Friday.
Reactive scaling relies on monitoring systems to detect high CPU utilization and trigger scaling actions, but it often falls short due to the steep initial spike in traffic.
Proactive scaling involves modeling expected peak loads, continuously assessing AWS capacity needs, and using metrics such as MTT (mean time to scale) to determine instance counts and service owners can use other independent variables to compose a richer scaling formula.
Amazon also uses forecast logic to set expectations for future events, including probabilistic forecasts and stress testing to ensure readiness and mitigate risk.

# Main Points

|   # | Main point |
| --: | ---------- |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=C7cKYRg7YwQ)
