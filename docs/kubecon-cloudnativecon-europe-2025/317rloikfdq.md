---
layout: default
title:
  "KEDA: Unlocking Advanced Event-Driven Scaling for Kubernetes - Zbynek Roubalik
  & Jorge Turrado"
nav_order: 137
parent: Kubecon Cloudnativecon Europe 2025
type: Video Note
description: Here is a summary of the video transcript in 3-5 sentences.
resource: https://www.youtube.com/watch?v=317rLOIKfDQ
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

Here is a summary of the video transcript in 3-5 sentences: Jorge Dorado, principal SR at CRM and Microsoft MVP, introduced himself and discussed KDA (Kubernetes Dynamic Autoscaling), a project that extends Kubernetes' autoscaling capabilities to support more metrics and use cases.
He demonstrated how KDA can be used to scale workloads based on external metrics from sources like RabbitMQ or Prometheus, and showed examples of its features, including predictive scaling and HTTP autoscaling.
The presentation also covered best practices for using KDA, such as using HPA scaling behavior and defining custom triggers, as well as common challenges and limitations, including delays in scraping metrics from external sources.

# Main Points

|   # | Main point                                                                                                                                               |
| --: | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | KDA (Kubernetes Dynamic Autoscaling) is a project that builds on top of Kubernetes, reusing its internals to scale workloads based on different metrics. |
|   2 | KDA supports 70+ event sources, including Prometheus, RabbitMQ, and Kafka.                                                                               |
|   3 | KDA extends HPA (Horizontal Pod Autoscaler) capabilities by adding support for external metrics and custom scaling logic.                                |
|   4 | KDA introduces a new concept called "scale job" which allows for more fine-grained control over scaling, especially for workloads with state.            |
|   5 | KDA has improved observability features, including aligning with community standards for metrics and flows.                                              |
|   6 | KDA includes authentication improvements, such as better support for AWS and other cloud providers.                                                      |
|   7 | Best practices for using KDA include:                                                                                                                    |
|   8 | Using HPA scaling behavior                                                                                                                               |
|   9 | Defining a schedule for autoscaling (e.g., chron scaler)                                                                                                 |
|  10 | Using scaly modifiers to customize scaling logic                                                                                                         |
|  11 | Properly configuring database resources to avoid overloading                                                                                             |
|  12 | Cluster autoscalers can be challenging, but KDA has features like provisioning requests and matrix caching to mitigate issues.                           |
|  13 | KDA is community-driven and supports integrating with various AWS services, including SQS.                                                               |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=317rLOIKfDQ)
