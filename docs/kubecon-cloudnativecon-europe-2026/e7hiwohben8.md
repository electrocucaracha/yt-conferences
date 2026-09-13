---
layout: default
title:
  "No Pain No Drain: Lessons From Node Drains at Scale - Ryan Hallisey & Natalie
  Bandel, NVIDIA"
nav_order: 223
parent: Kubecon Cloudnativecon Europe 2026
type: Video Note
description:
  In this talk, Ryan Haly and Natalie Vanell from Nvidia describe their
  journey transitioning from manual to fully automated node drain and maintenance
  processes in their GPU cloud infrastructure, which supports latency-sensitive game
  streami...
resource: https://www.youtube.com/watch?v=E7HIwOHbeN8
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

In this talk, Ryan Haly and Natalie Vanell from Nvidia describe their journey transitioning from manual to fully automated node drain and maintenance processes in their GPU cloud infrastructure, which supports latency-sensitive game streaming workloads.
Initially relying on manual "kubectl drain" commands, they encountered challenges such as operational costs, workload awareness, silent failures, and the need for coordinated, topology-aware maintenance.
To address these, they developed a system with two microservices: a drain coordinator that intelligently schedules and ranks nodes for maintenance, and a life cycle orchestrator that manages state transitions, enforces SLAs, and handles notifications, all coordinated via a custom resource definition (CRD).
Their solution includes features like adaptive drain throttling, node-type awareness, self-healing recovery, and comprehensive metrics, aiming to minimize disruption and maximize GPU availability.
They emphasize the importance of treating maintenance as a first-class lifecycle concern, advocate for community collaboration on Kubernetes-native solutions, and invite others to contribute use cases and ideas to the Kubernetes node lifecycle working group.

# Main Points

|   # | Main point                                                                                                                    |
| --: | ----------------------------------------------------------------------------------------------------------------------------- |
|   1 | Nvidia team manages thousands of GPUs for latency-sensitive, ephemeral game streaming workloads.                              |
|   2 | Previously, node drains were manual and rare; now, about 1,000 node drains occur daily.                                       |
|   3 | Manual drain processes caused capacity loss and operational challenges.                                                       |
|   4 | Transitioned from manual to fully automated, seamless life cycle management.                                                  |
|   5 | Initial approach used `kubectl drain`, which only handles basic cordon and eviction.                                          |
|   6 | Realized drain involves multiple states and complexities beyond basic tools.                                                  |
|   7 | Key challenges identified:                                                                                                    |
|   8 | Velocity control to avoid impacting user capacity.                                                                            |
|   9 | Workload awareness for smarter drain decisions.                                                                               |
|  10 | Drains can get stuck silently without visibility.                                                                             |
|  11 | Need for automation and coordination across maintenance types.                                                                |
|  12 | Topology awareness for complex hardware dependencies.                                                                         |
|  13 | Developed two microservices/controllers:                                                                                      |
|  14 | Drain coordinator (cluster-level): decides what and when to drain, schedules and ranks nodes, monitors drain progress.        |
|  15 | Life cycle orchestrator (node-level): manages state transitions, enforces SLAs, sends notifications.                          |
|  16 | Communication between controllers via a maintenance CRD that mirrors node state.                                              |
|  17 | Extended maintenance life cycle with clear states: scheduled, cordoned, drained, maintenance, complete, incomplete.           |
|  18 | Node selection uses a composable ranking system, considering urgency, workload, and diversity injection to avoid bottlenecks. |
|  19 | Node type awareness ensures correct drain detection per node type.                                                            |
|  20 | Self-tuning drain throttle adapts maintenance concurrency based on success/failure rates.                                     |
|  21 | Implemented timeouts and auto-remediation for stuck drains.                                                                   |
|  22 | Added safeguards: cordon ownership, admission webhooks, metrics, and prevention of accidental mass maintenance.               |
|  23 | Key takeaways:                                                                                                                |
|  24 | Separate drain decision from maintenance actions.                                                                             |
|  25 | Use self-tuning throttles and expressive configuration.                                                                       |
|  26 | Implement stuck drain recovery.                                                                                               |
|  27 | Treat maintenance as a first-class life cycle.                                                                                |
|  28 | Encourages community                                                                                                          |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=E7HIwOHbeN8)
