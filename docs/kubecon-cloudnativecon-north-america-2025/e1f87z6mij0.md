---
layout: default
title: I’ve Got 99 Problems and They’re All Controllers - Tim Goodwin, UC Santa Cruz
nav_order: 113
parent: Kubecon Cloudnativecon North America 2025
type: Video Note
description:
  Tim Goodwin, a PhD student at UC Santa Cruz, discusses the challenges
  of composing Kubernetes controllers to build higher-level platform abstractions
  and introduces "camera," a simulation testing tool he developed to address these
  issues. H...
resource: https://www.youtube.com/watch?v=E1f87Z6mij0
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

Tim Goodwin, a PhD student at UC Santa Cruz, discusses the challenges of composing Kubernetes controllers to build higher-level platform abstractions and introduces "camera," a simulation testing tool he developed to address these issues.
He explains how Kubernetes evolved from container orchestration to a universal control plane by leveraging its declarative model and extensible API, allowing custom resources and controllers to manage diverse infrastructure.
However, composing multiple controllers introduces complexity and subtle bugs, especially in their asynchronous interactions, making debugging difficult.
Camera simulates the Kubernetes control plane, enabling exhaustive testing of controller interactions and verifying properties like deterministic convergence using model checking, all without requiring a live cluster.
The tool is open source but research-grade, and Tim encourages practitioners to try it out and provide feedback to help refine its capabilities.

# Main Points

|   # | Main point                                                                                                                                                                                                 |
| --: | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Tim Goodwin, PhD student at UC Santa Cruz, presents on composing Kubernetes controllers for higher-level platform abstractions and introduces a new simulation testing tool.                               |
|   2 | Kubernetes evolved from container orchestration to managing diverse cloud infrastructure, enabled by its declarative model and extensible API.                                                             |
|   3 | Custom resources (CRDs) and controllers allow adding new functionality; composing these resources enables higher-level abstractions (e.g., bundling service, deployment, and database into an "appstack"). |
|   4 | Composing controllers increases complexity and debugging difficulty due to indirect, asynchronous interactions via resource state updates.                                                                 |
|   5 | Writing correct reconcile loops is challenging; issues like infinite update loops and cross-controller conflicts can arise.                                                                                |
|   6 | Debugging controller interactions is hard due to loose coupling, asynchronous updates, and reproducibility challenges.                                                                                     |
|   7 | Simulation testing can help catch interaction issues before deployment by modeling and testing controller behavior and interactions.                                                                       |
|   8 | The simulation tool, "camera," interposes at the API client interface, simulates the cluster, and runs controller code without a real cluster.                                                             |
|   9 | Camera models cluster state as resource contents plus pending reconciles, simulates reconciliation steps, and checks for convergence (empty pending reconcile set).                                        |
|  10 | Detects undesirable outcomes: non-convergence (infinite loops) and non-deterministic convergence (race conditions).                                                                                        |
|  11 | Uses model checking to exhaustively explore execution paths and verify properties like deterministic convergence.                                                                                          |
|  12 | Demo: camera simulates Knative serverless service reconciliation, showing stepwise controller actions and state changes.                                                                                   |
|  13 | Camera is open source but research-grade, not production-ready; feedback from practitioners is sought.                                                                                                     |
|  14 | Q&A highlights:                                                                                                                                                                                            |
|  15 | Camera can simulate concurrency issues between controllers and cache update events.                                                                                                                        |
|  16 | Faithful API server simulation is a challenge; ongoing improvements t                                                                                                                                      |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=E1f87Z6mij0)
