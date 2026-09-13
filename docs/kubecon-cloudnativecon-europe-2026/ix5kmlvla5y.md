---
layout: default
title:
  "Project Lightning Talk: Still Burning GPUs On Debugging? Scale AI In One Line
  - Anna Kramar"
nav_order: 291
parent: Kubecon Cloudnativecon Europe 2026
type: Video Note
description:
  Ana Kmer, a certified engineer at Red Hat and maintainer of the KFL SDK,
  discusses the challenges data scientists face when scaling AI workloads from local
  environments to Kubernetes, such as dealing with infrastructure complexities and
  cos...
resource: https://www.youtube.com/watch?v=Ix5kmLvlA5Y
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

Ana Kmer, a certified engineer at Red Hat and maintainer of the KFL SDK, discusses the challenges data scientists face when scaling AI workloads from local environments to Kubernetes, such as dealing with infrastructure complexities and costly debugging.
To address these issues, she introduces the KFL SDK, a set of unified Python APIs that simplify running AI workloads at any scale, allowing users to switch between local and distributed execution with minimal code changes.
The SDK supports various backends, including local subprocesses, containerized environments, and Kubernetes, and offers features like trainer and optimizer clients for training and hyperparameter optimization, a model registry for versioning, and a Spark client for distributed data processing.
Upcoming features include workflow orchestration, feature store integration, observability, experiment tracking, and an MCP server for AI agent operations.
Ana also highlights the SDK's recent milestone of 140,000 downloads and invites the community to engage through their website, blog, Slack channel, and regular meetings.

# Main Points

|   # | Main point                                                                                                                                                                                  |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Ana Kmer, a certified engineer at Red Hat and KFL SDK maintainer, presents on running AI workloads at any scale.                                                                            |
|   2 | Data scientists face challenges scaling training functions from local to Kubernetes, dealing with infrastructure issues like pods, CRDs, and YAML files.                                    |
|   3 | Debugging infrastructure consumes time and GPU resources, increasing costs.                                                                                                                 |
|   4 | Qflow SDK is being developed to simplify running AI workloads at any scale.                                                                                                                 |
|   5 | Qflow SDK provides unified Pythonic APIs and can be installed via pip.                                                                                                                      |
|   6 | Training functions can be run locally using trainer client and local process backend config.                                                                                                |
|   7 | Scaling to distributed training on Kubernetes requires minimal code changes, mainly backend configuration.                                                                                  |
|   8 | Distributed training allows specifying number of nodes and resources per node; example given of distributing across 800 GPUs.                                                               |
|   9 | Environment backend can be switched (local subprocess, Docker/Podman, Kubernetes) with a single line change, without modifying the training function.                                       |
|  10 | Trainer client supports both fine-tuning and distributed training.                                                                                                                          |
|  11 | Hyperparameter optimization is available via optimizer client.                                                                                                                              |
|  12 | Model versioning and artifact storage are supported through model registry client.                                                                                                          |
|  13 | Spark client recently added for distributed data processing on Spark.                                                                                                                       |
|  14 | Upcoming features include pipelines client for workflow orchestration, fist client for feature store, integration with OpenTelemetry for observability, and MLflow for experiment tracking. |
|  15 | MCP server is planned to enable AI agents to operate Qflow.                                                                                                                                 |
|  16 | KFL SDK recently reached 140,000 downloads in recent months.                                                                                                                                |
|  17 | Community engagement includes a website, blog post, Slack channel under CNCF, bi-weekly meetings, and maintainer sessions.                                                                  |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=Ix5kmLvlA5Y)
