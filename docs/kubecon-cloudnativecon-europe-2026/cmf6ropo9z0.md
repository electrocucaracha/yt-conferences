---
layout: default
title:
  "In-place Updates with Cluster API: The Sweet Spot Between Immu... Fabrizio
  Pandini & Stefan Büringer"
nav_order: 152
parent: Kubecon Cloudnativecon Europe 2026
type: Video Note
description:
  The talk, led by Fabritz Pandini and Stefan Ginger, focuses on the introduction
  of in-place updates in Cluster API, a significant and technically complex change
  aimed at reducing disruption during cluster upgrades. Traditionally, Cluster AP...
resource: https://www.youtube.com/watch?v=CMf6rOPo9Z0
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

The talk, led by Fabritz Pandini and Stefan Ginger, focuses on the introduction of in-place updates in Cluster API, a significant and technically complex change aimed at reducing disruption during cluster upgrades.
Traditionally, Cluster API has followed Kubernetes’ immutable infrastructure model, where updates involve creating new machines and deleting old ones, which ensures simplicity, predictability, and avoids configuration drift.
However, this approach can be slow or disruptive, especially when infrastructure resources are limited or applications are sensitive to node changes.
The new in-place update feature allows certain machine changes without full replacement, guided by user-defined constraints like max surge and max unavailable, and relies on an update extension component to determine if changes can be safely applied in place.
The system prioritizes safety and predictability, falling back to immutable rollouts if in-place updates are not feasible, and is designed to be extensible and minimally disruptive.
The speakers emphasize that while in-place updates are useful for non-disruptive changes (e.g., updating SSH keys), foundational issues like proper pod draining and infrastructure readiness should still be addressed, as immutable updates remain the safest method for major changes.

# Main Points

|   # | Main point                                                                                                                                                                                                     |
| --: | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | The talk focuses on Cluster API and in-place updates, not AI.                                                                                                                                                  |
|   2 | Speakers: Fabrizio Pandini and Stefan Schimanski, both principal engineers at Broadcom and Cluster API maintainers.                                                                                            |
|   3 | In-place update is the most complex change merged into Cluster API in recent years.                                                                                                                            |
|   4 | Kubernetes is based on immutability: pods are replaced, not updated in place.                                                                                                                                  |
|   5 | Cluster API treats machines like immutable pods: create, delete, and replace for changes.                                                                                                                      |
|   6 | Immutability brings simplicity, robustness, predictability, and avoids configuration drift.                                                                                                                    |
|   7 | Real-world constraints (infrastructure, application limitations) make pure immutability challenging.                                                                                                           |
|   8 | Cluster API has improved rollouts: avoids unnecessary rollouts, allows label/annotation/taint updates without replacement, reduces pod draining, and skips some worker upgrades during multi-version upgrades. |
|   9 | In-place updates aim to reduce disruption and work better across infrastructures.                                                                                                                              |
|  10 | Design principles:                                                                                                                                                                                             |
|  11 | User defines desired state; system implements it.                                                                                                                                                              |
|  12 | New "update extension" component handles in-place updates.                                                                                                                                                     |
|  13 | No user workflow changes; in-place is opt-in/opt-out.                                                                                                                                                          |
|  14 | Decision to use in-place is based on spec fields: replicas, max surge, max unavailable.                                                                                                                        |
|  15 | In-place updates only used if disruption budget allows; otherwise, fallback to immutable rollout.                                                                                                              |
|  16 | Update extension must support all requested changes; otherwise, fallback to rollout.                                                                                                                           |
|  17 | No human intervention during in-place update to avoid drift.                                                                                                                                                   |
|  18 | Cluster API is extensible; update methods are implementation-specific.                                                                                                                                         |
|  19 | Control plane in-place updates:                                                                                                                                                                                |
|  20 | Only performed if more than one replica and control plane is healthy.                                                                                                                                          |
|  21 | Follows max surge and max unavailable rules to maintain availability.                                                                                                                                          |
|  22 | Worker machine in-place updates:                                                                                                                                                                               |
|  23 | Uses machine deployments and machine sets.                                                                                                                                                                     |
|  24 | Max surge and max unavailable can both be >0.                                                                                                                                                                  |
|  25 | In-place updates combined with "move" to align machines with new machine sets.                                                                                                                                 |
|  26 | System prefers in-place when allowed by user spec.                                                                                                                                                             |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=CMf6rOPo9Z0)
