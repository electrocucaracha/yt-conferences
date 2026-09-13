---
layout: default
title:
  "Project Lightning Talk: Argo Workflows 4, What's New And What's Next - Alan
  Clucas, Lead"
nav_order: 251
parent: Kubecon Cloudnativecon Europe 2026
type: Video Note
description:
  The speaker introduces Argo Workflows, a Kubernetes-native batch processing
  engine that orchestrates steps or DAGs as pods and facilitates data transfer between
  them. Recent updates in version 4.0 include new artifact drivers for custom dat...
resource: https://www.youtube.com/watch?v=YbW24qbJ78I
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

The speaker introduces Argo Workflows, a Kubernetes-native batch processing engine that orchestrates steps or DAGs as pods and facilitates data transfer between them.
Recent updates in version 4.0 include new artifact drivers for custom data transport plugins, enhanced CRD validation to catch errors before runtime, removal of plural primitive versions with a new tool for migration, and improved pod restart strategies.
Workflow tracing has been added for better performance insights, and future plans involve reworking the DAG engine for unified implementation and potential DAG plugins, as well as enabling pod reuse to reduce spin-up times.
Additionally, there are efforts to simplify and modernize the expressions system for better usability and compatibility with Helm templating.
The speaker invites attendees to visit their booth for further discussion.

# Main Points

|   # | Main point                                                                                                                                   |
| --: | -------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Argo Workflows is a batch processing engine for Kubernetes, running steps in pods.                                                           |
|   2 | Users can define steps as a series or a DAG, with orchestration and data passing between pods.                                               |
|   3 | Version 4.0 was released earlier this year with several new features.                                                                        |
|   4 | Artifact drivers allow custom plugins for data transport in and out of pods.                                                                 |
|   5 | Full schema validation is now available in CRDs, improving error detection for invalid workflows.                                            |
|   6 | Plural versions of certain primitives introduced in 3.6 have been removed in 4.0; a new tool, argo convert, helps with migration.            |
|   7 | The controller now restarts pods that never started, with a restart strategy for safe cases.                                                 |
|   8 | Workflow tracing is merged for 4.1, enabling full workflow tracing and integration with CI/CD and open telemetry.                            |
|   9 | Tracing helps visualize workflow timing and allows tracing inside workloads.                                                                 |
|  10 | Future plans include reworking the DAG engine to separate it from pod creation, unifying steps and DAGs, and enabling DAG plugins.           |
|  11 | Plans to allow pod reuse for workflows to reduce pod spin-up time, with an annotation for reusable pods (at the cost of pod isolation).      |
|  12 | Work is ongoing to improve expressions in Argo Workflows, aiming for easier use, better readability, and compatibility with Helm templating. |
|  13 | Speaker is available for questions at the Pipkit booth (494) in the project pavilion on the Argo stand.                                      |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=YbW24qbJ78I)
