---
layout: default
title:
  "Stateful Connections in Kubernetes: The Scaling Secrets Nobody... André Mocke
  & Rodrigo Fior Kuntzer"
nav_order: 317
parent: Kubecon Cloudnativecon Europe 2025
type: Video Note
description:
  The speaker, Andre, introduces himself and Rodrigo, a visionary behind
  Miro's evolution into cloud-native technologies. They discuss the challenges of
  stateful connections in websockets, particularly with ephemeral ports and connection
  trac...
resource: https://www.youtube.com/watch?v=h1AyaAIf3HA
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

The speaker, Andre, introduces himself and Rodrigo, a visionary behind Miro's evolution into cloud-native technologies.
They discuss the challenges of stateful connections in websockets, particularly with ephemeral ports and connection tracking.
To address these issues, they implemented a new websocket manager using Kubernetes, which enabled them to scale more efficiently and reduce operational costs.
The team used AWS load balancer controller, Kada, and Prometheus to manage traffic and scaling, but encountered issues with the HPA algorithm's tolerance and metrics flapping.
They eventually defined scale-up policies and mitigated these problems, resulting in improved performance and cost savings.

# Main Points

|   # | Main point |
| --: | ---------- |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=h1AyaAIf3HA)
