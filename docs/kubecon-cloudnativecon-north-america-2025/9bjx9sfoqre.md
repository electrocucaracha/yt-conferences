---
layout: default
title:
  "Anatomy of a Kubernetes Scheduler: Narrate Workloads Priority in Sequence
  - Hoon Jo, Megazone"
nav_order: 18
parent: Kubecon Cloudnativecon North America 2025
type: Video Note
description:
  The speaker introduces a beginner-level session focused on Kubernetes,
  emphasizing the importance of understanding essential concepts beyond just using
  AI tools. They explain the structure of a Kubernetes cluster, highlighting the roles
  of...
resource: https://www.youtube.com/watch?v=9BjX9SFOqRE
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

The speaker introduces a beginner-level session focused on Kubernetes, emphasizing the importance of understanding essential concepts beyond just using AI tools.
They explain the structure of a Kubernetes cluster, highlighting the roles of nodes, scheduling, filtering, and scoring, and discuss how node names and taints affect workload assignment.
Through diagrams and demos, the presenter illustrates how different scheduling stages work, such as assigning workloads directly to nodes, using filters to optimize resource use, and applying scoring for more complex scenarios.
The session is designed to help juniors and team members grasp these foundational scheduling mechanisms, which are crucial for effective Kubernetes management.
The speaker concludes by stressing that while AI can enhance productivity, a solid grasp of core Kubernetes concepts remains vital for engineers and teams.

# Main Points

|   # | Main point                                                                                                                   |
| --: | ---------------------------------------------------------------------------------------------------------------------------- |
|   1 | Session is aimed at beginners, focusing on Kubernetes.                                                                       |
|   2 | Emphasizes importance of understanding essential Kubernetes concepts for AI and productivity tools.                          |
|   3 | Presentation includes an infographic and demo.                                                                               |
|   4 | Focus is on Kubernetes cluster architecture: communities, cluster, control plane, and nodes.                                 |
|   5 | Three key stages discussed in the diagram:                                                                                   |
|   6 | Stage 1: Node name assignment bypasses scheduler; node name can be assigned directly.                                        |
|   7 | Stage 2: Filtering and scoring process; filter is more efficient and saves resources compared to scoring.                    |
|   8 | Stage 3: Scoring assigns nodes based on weights and specs.                                                                   |
|   9 | Node name assignment is described as "invincible" because it bypasses the scheduler and assigns directly if the node exists. |
|  10 | Taints and tolerations are used to control node assignment and scheduling.                                                   |
|  11 | Filter (pter) is prioritized over scoring when both are present.                                                             |
|  12 | Demo shows node selection, tainting, and assignment process.                                                                 |
|  13 | Emphasizes that understanding these mechanisms is important for team members and juniors.                                    |
|  14 | AI is popular, but foundational Kubernetes knowledge is essential for effective use.                                         |
|  15 | Best practices include deploying NGINX with high availability and understanding node failures.                               |
|  16 | AI can generate code quickly, but understanding the underlying technology leads to better outcomes.                          |
|  17 | Encourages learning essential Kubernetes skills for engineers and developers.                                                |
|  18 | Demo cluster consists of one control plane and six worker nodes.                                                             |
|  19 | Presentation materials and scenarios can be reused for team training or workshops.                                           |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=9BjX9SFOqRE)
