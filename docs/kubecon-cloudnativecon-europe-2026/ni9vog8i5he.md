---
layout: default
title:
  "Evolving KServe: The Unified Model Inference Platform for Both Predic... Filippe
  Spolti & JooHoo Lee"
nav_order: 107
parent: Kubecon Cloudnativecon Europe 2026
type: Video Note
description:
  Phillip and Julie, senior engineers at Red Hat, introduce KServe, an
  open-source project for serving AI and machine learning models on Kubernetes. They
  explain that KServe abstracts the complexity of deploying and managing models, supporting.
resource: https://www.youtube.com/watch?v=nI9VOG8I5HE
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

Phillip and Julie, senior engineers at Red Hat, introduce KServe, an open-source project for serving AI and machine learning models on Kubernetes.
They explain that KServe abstracts the complexity of deploying and managing models, supporting both predictive and generative AI workloads, and integrates with tools like Envoy, KNative, and KEDA for autoscaling and networking.
The team highlights recent developments, such as support for large language models (LLMs) through LLMD, efficient caching mechanisms, and advanced routing using the Kubernetes Gateway API and gateway inference extension.
They demonstrate how KServe simplifies complex deployments, including multi-GPU setups and optimized inference workflows, and emphasize its growing adoption, active community, and openness to new contributors.
The session concludes with an invitation to join the project and a group selfie with the audience.

# Main Points

|   # | Main point                                                                                                             |
| --: | ---------------------------------------------------------------------------------------------------------------------- |
|   1 | Phillip and Julie are senior engineers at Red Hat, working on the KServe inference team.                               |
|   2 | KServe is a model serving orchestrator on top of Kubernetes, supporting GPUs, CPUs, and TPUs.                          |
|   3 | KServe abstracts Kubernetes complexity for data scientists, handling networking, security, ingress, and scaling.       |
|   4 | KServe started as a Kubeflow project (originally KFServing), developed by Google, IBM, Bloomberg, Nvidia, and others.  |
|   5 | KServe was rebranded, joined the Linux Foundation, and is now an incubating CNCF project.                              |
|   6 | Autoscaling initially used Knative, now moving to KEDA for more flexibility.                                           |
|   7 | Networking uses Envoy and Envoy AI Gateway; moving from Ingress to Gateway API.                                        |
|   8 | KServe supports both predictive and generative AI workloads.                                                           |
|   9 | LLM inference is accelerated using LLMD, enabling fast, efficient serving of large language models.                    |
|  10 | KServe provides a unified API (CRD: InferenceService) for deploying and managing models.                               |
|  11 | Generative AI support includes a new CRD, integrated with LLMD, supporting complex dependencies and efficient scaling. |
|  12 | KV cache is used to maximize GPU utilization and enable concurrent inference requests.                                 |
|  13 | LLMD architecture includes components for routing, prefill, and decode, optimizing inference performance.              |
|  14 | KServe supports both single-node and multi-node deployments, using StatefulSets for large-scale LLMs.                  |
|  15 | Model storage options include OCI images, S3 buckets, and persistent volumes.                                          |
|  16 | The router component efficiently directs inference requests to the appropriate pods.                                   |
|  17 | KServe operator automates deployment and configuration, reducing manual setup.                                         |
|  18 | Performance monitoring is integrated with Prometheus and Grafana dashboards.                                           |
|  19 | KServe is open source, with increasing community contributions and resources available on GitHub.                      |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=nI9VOG8I5HE)
