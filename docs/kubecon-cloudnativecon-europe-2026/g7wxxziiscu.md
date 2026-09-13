---
layout: default
title:
  "From Jenkins to Tekton: Our Journey Toward a Kubernetes-Native CI... Mustafa
  Barış Ege & Özge Aygül"
nav_order: 120
parent: Kubecon Cloudnativecon Europe 2026
type: Video Note
description:
  In this presentation, Ozge and Baris share their DevOps team's migration
  journey from Jenkins to a Kubernetes-native CI/CD pipeline using Tekton and Argo
  CD. They describe the challenges faced with Jenkins, such as scalability issues,
  plugi...
resource: https://www.youtube.com/watch?v=g7WXxziISCU
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

In this presentation, Ozge and Baris share their DevOps team's migration journey from Jenkins to a Kubernetes-native CI/CD pipeline using Tekton and Argo CD.
They describe the challenges faced with Jenkins, such as scalability issues, plugin management, and lack of standardization, which prompted the shift to a more declarative, scalable, and standardized approach.
By adopting Tekton, they implemented a unified, event-driven pipeline architecture with ephemeral execution and Kubernetes-native features, enabling universal adoption and improved efficiency, though at the cost of some developer flexibility.
The team also integrated Argo CD for continuous deployment, leveraging Git as the single source of truth and automating deployments with human approval steps for production.
They discuss technical and cultural lessons learned, including pipeline scheduling, caching strategies, and the importance of communication over excessive configuration, and conclude with a live demo showcasing their streamlined CI/CD process and automated notifications.

# Main Points

|   # | Main point                                                                                                                                                          |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Presentation covers migration from Jenkins to Tekton for Kubernetes-native CI/CD with Argo CD.                                                                      |
|   2 | Focus shifted from managing servers to managing pipelines.                                                                                                          |
|   3 | Initial Jenkins setup worked for small teams but faced issues as repositories and teams grew.                                                                       |
|   4 | Main Jenkins problems: scalability (static agents), plugin management ("plugin hell"), and consistency across Jenkinsfiles.                                         |
|   5 | Needed declarative, pipeline-as-code infrastructure with ephemeral execution and Kubernetes-native controls.                                                        |
|   6 | Chose Tekton for its unified pipeline architecture, decoupled logic, event-driven model, and Kubernetes-native features.                                            |
|   7 | Tekton uses custom resource definitions: steps (run scripts/commands), grouped into tasks (run as pods), composed into pipelines.                                   |
|   8 | Triggers (with templates and bindings) and event listeners handle webhook events and parameter extraction.                                                          |
|   9 | Adopted a "one pipeline to rule them all" approach for standardization and easier management.                                                                       |
|  10 | Container tasks (e.g., Kaniko) used for builds; standardized tasks enabled universal adoption, even for non-Kubernetes projects.                                    |
|  11 | Trade-off: lost some flexibility for teams but gained massive standardization.                                                                                      |
|  12 | CI/CD flow: Developer commits to Git, webhook triggers Tekton pipeline, common tasks (clone, build, scan, notify), image pushed to registry.                        |
|  13 | CD flow: Argo CD monitors Git for manifest changes, syncs and redeploys Kubernetes resources; image updater watches registry for new images and triggers redeploys. |
|  14 | Git is the single source of truth; human approval required for production/staging deployments.                                                                      |
|  15 | Main challenges were cultural, not technical; developers initially resisted loss of control.                                                                        |
|  16 | Solution: shift CI pipeline responsibility to DevOps team, build trust through reliability.                                                                         |
|  17 | Lessons learned:                                                                                                                                                    |
|  18 | Disabled Tekton affinity assistant to avoid pipeline scheduling stalls.                                                                                             |
|  19 | Used persistent volume claims for dependency caching to reduce build times.                                                                                         |
|  20 | Communication solved common package issues better than more YA                                                                                                      |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=g7WXxziISCU)
