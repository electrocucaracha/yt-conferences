---
layout: default
title:
  "Lightning Talk: How We Used Data Structures When Contributing To the Kubernetes
  Proje... Arsh Sharma"
nav_order: 150
parent: Kubecon Cloudnativecon North America 2025
type: Video Note
description:
  Arsh from Metalbear shares his journey into the Kubernetes ecosystem,
  focusing on his initial dislike for data structures and algorithms (DSA) learned
  in university, which he found unhelpful for practical application development. His
  perspe...
resource: https://www.youtube.com/watch?v=e6z3ijBfPUU
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

Arsh from Metalbear shares his journey into the Kubernetes ecosystem, focusing on his initial dislike for data structures and algorithms (DSA) learned in university, which he found unhelpful for practical application development.
His perspective changed when he joined the Linux Foundation's mentorship program and worked on a project evaluating dependency updates for Kubernetes, where he realized the practical necessity of DSA concepts like graphs.
By building a tool that visualizes and tracks direct and transitive dependencies in Kubernetes projects, Arsh found real-world value in the knowledge he once dismissed, especially when maintainers could see the impact of pull requests on dependencies.
This experience transformed his relationship with DSA from frustration to respect, culminating in the satisfaction of seeing his tool used by others and visualizing the complex dependency graph of Kubernetes.
He concludes by inviting the audience to connect with him and try out the tool.

# Main Points

|   # | Main point                                                                                                            |
| --: | --------------------------------------------------------------------------------------------------------------------- |
|   1 | Arsh works at Metalbear, building a Kubernetes developer tool.                                                        |
|   2 | The talk focuses on Arsh's journey into the Kubernetes ecosystem, not the tool itself.                                |
|   3 | Arsh includes memes in the presentation, referencing data structures and algorithms (DSA).                            |
|   4 | Most attendees have learned DSA in university or during job hunting; few enjoyed the process.                         |
|   5 | Arsh dislikes the traditional DSA grind, finding it unhelpful for building real applications.                         |
|   6 | A friend's frustration with job interviews and DSA resonated with Arsh.                                               |
|   7 | Arsh avoided learning DSA in college, seeing it as useless for practical development.                                 |
|   8 | Discovery of open-source and the Linux Foundation's mentorship program changed Arsh's perspective.                    |
|   9 | Arsh joined a project to develop tools for evaluating dependency updates in Kubernetes.                               |
|  10 | Initially, Arsh had no knowledge of Kubernetes, dependencies, or related concepts.                                    |
|  11 | Learned about the "go mod graph" command, which displays project dependencies.                                        |
|  12 | Realized the need for data structures (specifically graphs) to manage dependencies.                                   |
|  13 | Began learning DSA with a practical purpose, making the process enjoyable and meaningful.                             |
|  14 | Used a directed acyclic graph (DAG) to represent project dependencies.                                                |
|  15 | Direct dependencies are those a project relies on directly; transitive dependencies are dependencies of dependencies. |
|  16 | The tool was integrated as a CI job in the Kubernetes project to track dependency changes in pull requests.           |
|  17 | Maintainers use this information to monitor the impact of pull requests on dependencies.                              |
|  18 | Arsh's software was used by others, leading to a "full circle" moment and a newfound respect for DSA.                 |
|  19 | The tool includes a command to visualize all project dependencies, producing a complex graph for Kubernetes.          |
|  20 | Arsh invites attendees to connect via his website or visit booth 1560 for more information.                           |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=e6z3ijBfPUU)
