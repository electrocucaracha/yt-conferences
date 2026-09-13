---
layout: default
title:
  "Project Lightning Talk: Evolving KServe: The Unified Model Inference Platform
  For Both... Yuan Tang"
nav_order: 259
parent: Kubecon Cloudnativecon Europe 2026
type: Video Note
description:
  Yantan, a senior principal software engineer at Red Hat and project lead
  for Kserve, introduces Kserve as a standardized, distributed, and scalable model
  inference platform on Kubernetes, supporting both predictive and generative AI workloa...
resource: https://www.youtube.com/watch?v=kE6lNBA56vM
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

Yantan, a senior principal software engineer at Red Hat and project lead for Kserve, introduces Kserve as a standardized, distributed, and scalable model inference platform on Kubernetes, supporting both predictive and generative AI workloads.
Kserve integrates with various serving runtimes and cloud-native technologies, offering features like autoscaling, request batching, security, distributed tracing, logging, and traffic management.
The project, now an incubating CNCF project with over 300 contributors, has expanded from its predictive AI roots to include advanced generative AI capabilities, such as metrics-based autoscaling and support for additional runtimes and caching to improve efficiency and throughput.
Yantan encourages community participation through bi-weekly meetings, dedicated Slack channels, and invites attendees to visit the project booth and maintainer sessions during the week.

# Main Points

|   # | Main point                                                                                                                                                                                                          |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Speaker: Yantan, Senior Principal Software Engineer at Red Hat and project lead for Kserve                                                                                                                          |
|   2 | Topic: Introduction and overview of Kserve                                                                                                                                                                          |
|   3 | Kserve is a standardized, distributed, and scalable model inference platform on Kubernetes for predictive and generative AI                                                                                         |
|   4 | Supports serving runtimes such as VRM for generative AI, XGBoost, and scikit-learn for predictive AI                                                                                                                |
|   5 | Integrates with genAI solutions like LMD, Envoy AI Gateway, and RM Cache                                                                                                                                            |
|   6 | Integrated with cloud-native technologies such as Knative and KEDA for autoscaling                                                                                                                                  |
|   7 | Supports Kubernetes Gateway API for compatibility with Istio and Envoy                                                                                                                                              |
|   8 | Runs anywhere Kubernetes can be deployed                                                                                                                                                                            |
|   9 | Joined CNCF as an incubating project in September last year                                                                                                                                                         |
|  10 | 19 maintainers and over 300 contributors to date                                                                                                                                                                    |
|  11 | Originated as a model serving project focused on predictive AI; still supports predictive workloads                                                                                                                 |
|  12 | Features include scaling to/from zero, request batching, security (ON and OZ), distributed tracing, autoscaling based on GPU/CPU usage, request/response logging, traffic management, and out-of-box metric support |
|  13 | Actively developing generative AI features, especially for large language models                                                                                                                                    |
|  14 | Metrics-based autoscaling available (e.g., KEDA autoscaling based on serving runtime metrics)                                                                                                                       |
|  15 | Supports additional generative AI runtimes: VRM, TRT, RM, and RMD                                                                                                                                                   |
|  16 | Pump caching supported to reduce cost and improve throughput via intelligent routing and traffic management                                                                                                         |
|  17 | Leverages RMD project for model inference optimizations for large language models; RMD recently accepted as a CNCF sandbox project                                                                                  |
|  18 | Community includes contributors from various organizations                                                                                                                                                          |
|  19 | Bi-weekly community meetings on Thursdays                                                                                                                                                                           |
|  20 | Dedicated Slack channels for end users and contributors                                                                                                                                                             |
|  21 | Maintainer session on Thursday and project booth available Tuesday, Wednesday, and Thursday (mainly mornings, sometimes early afternoon)                                                                            |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=kE6lNBA56vM)
