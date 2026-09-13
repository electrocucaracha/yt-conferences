---
layout: default
title:
  "A Fork to Reckon With: Minimizing Friction When Adopting... Alexander Perlman
  & Narayanamurthi Mari"
nav_order: 5
parent: Kubecon Cloudnativecon Europe 2025
type: Video Note
description:
  The speaker discusses the importance of avoiding "NIH" (Not Invented
  Here), a phenomenon where companies reinvent the wheel instead of leveraging mature
  industry-standard open-source solutions. They present four approaches to address
  capabi...
resource: https://www.youtube.com/watch?v=yeg-uoBYCO0
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

The speaker discusses the importance of avoiding "NIH" (Not Invented Here), a phenomenon where companies reinvent the wheel instead of leveraging mature industry-standard open-source solutions.
They present four approaches to address capability gaps in open-source dependencies: contribution, forking, wrapping, and mutation.
Contribution is ideal but often not feasible due to proprietary functionality or urgent needs.
Forking can be done when necessary, but it requires high maintenance burden.
Wrapping can abstract underlying dependencies, but it also introduces complexity and brittleness.
Mutation is a powerful solution that allows direct modification of manifests at runtime, making it easy to address specific use cases without requiring extensive coding knowledge.
The speaker emphasizes the importance of closing gaps in upstream dependencies instead of rebuilding them in-house and provides a decision tree to help users evaluate which approach to use for their specific use case.

# Main Points

|   # | Main point                                                                                                                                   |
| --: | -------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | NIH (Not Invented Here) refers to companies rolling their own solutions instead of leveraging mature industry-standard open-source software. |
|   2 | Capability gaps can occur due to regulatory requirements, security concerns, or proprietary functionality.                                   |
|   3 | Four approaches to address capability gaps:                                                                                                  |
|   4 | Contribution: distributing maintenance burden across a worldwide network of engineers.                                                       |
|   5 | Forking: creating a copy of existing code and providing changes on top.                                                                      |
|   6 | Wrapping: abstracting underlying dependencies with a wrapper.                                                                                |
|   7 | Mutation: modifying manifests at runtime without touching source code.                                                                       |
|   8 | Contribution is ideal, but may not be feasible for proprietary or urgent projects.                                                           |
|   9 | Mutation is awesome, but comes with computational overhead.                                                                                  |
|  10 | Forking should only be done when necessary and keeping the fork small.                                                                       |
|  11 | Wrapping should only be done if the cost is justified. Note: The response is within the 2000 character limit.                                |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=yeg-uoBYCO0)
