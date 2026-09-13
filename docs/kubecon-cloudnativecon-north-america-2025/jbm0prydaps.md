---
layout: default
title:
  Tools and Strategies for Making the Most of Kubernetes Access Con... Lucas
  Käldström & Micah Hausler
nav_order: 320
parent: Kubecon Cloudnativecon North America 2025
type: Video Note
description: Here is a summary of the video transcript in 3-5 sentences.
resource: https://www.youtube.com/watch?v=JBM0PRyDaPs
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

Here is a summary of the video transcript in 3-5 sentences: Lucas and Mike Hler discuss Kubernetes access control, focusing on role-based access control (RBAC) using Cube Arbback, which is widely deployed but has limitations such as privilege escalation prevention.
They introduce a new enhancement proposal that aims to add more fine-grained alternatives to existing methods, including capabilities-based access control.
The proposal utilizes the Cedar authorization language, which provides expressivity, safety, and analyzability, allowing for better policy management and enforcement.
The authors demonstrate the use of Cedar in a demo, showcasing its ability to constrain reads and ensure authorized access.
They conclude by encouraging viewers to join the SIG-O special interest group for authentication and authorization discussions.

# Main Points

|   # | Main point                                                                                                                                                                           |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   1 | Kubernetes access control is a delicate balance between expressiveness, speed, safety, and analyzability.                                                                            |
|   2 | Arbback (Role-Based Access Control) is a widely deployed method that provides fast, safe, and analyzable access control but has limitations such as privilege escalation prevention. |
|   3 | Validating Admission Policy allows for more expressivity but is not as fast or safe as arbback.                                                                                      |
|   4 | Web hooks provide even more expressivity but are prone to failures and cannot be analyzed.                                                                                           |
|   5 | A new Kubernetes Enhancement Proposal (KEP) aims to integrate authorization and admission layers further, enabling partial evaluation of policies.                                   |
|   6 | Cedar is an open-source authorization language that supports expressive policies, analyzability, and decidable mathematical logic.                                                   |
|   7 | Cedar can be used to create a unified interface for access control, allowing for more fine-grained controls and better analyzability.                                                |
|   8 | Analyzability is a key feature of Cedar, enabling the comparison of policies, detection of logical inconsistencies, and proof of policy correctness.                                 |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=JBM0PRyDaPs)
