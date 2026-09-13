---
layout: default
title:
  Fusing FinOps, Forecasting, and Kubernetes at Scale - Ankur Singh & Satyam
  Bhardwaj
nav_order: 129
parent: Kubecon Cloudnativecon Europe 2026
type: Video Note
description:
  In this presentation, Ankur Singh from Red Hat and Satyam from Mirantis
  introduce a Kubernetes-native, open-source solution called Auger to address pain
  points in PHOPS (presumably "FinOps" or cost optimization) within Kubernetes environmen...
resource: https://www.youtube.com/watch?v=65TRuI5hvn4
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

In this presentation, Ankur Singh from Red Hat and Satyam from Mirantis introduce a Kubernetes-native, open-source solution called Auger to address pain points in PHOPS (presumably "FinOps" or cost optimization) within Kubernetes environments.
They explain that current PHOPS cycles are slow, taking 6–8 weeks, and existing autoscalers only react to current data without forecasting future needs.
Auger integrates existing open-source tools for metrics collection (like Prometheus and OpenCost), time series forecasting models (such as Toto and ARMA), and optimization engines, providing a modular and extensible platform.
The system standardizes data formats, supports multiple forecasting models, includes mechanisms for accuracy and drift detection, and incorporates a human-in-the-loop approval process for recommendations.
A live demo showcases Auger’s architecture, custom resources, and its ability to generate actionable, cost-saving recommendations for Kubernetes clusters, with future plans for enhanced drift detection and multi-cluster support.

# Main Points

|   # | Main point                                                                                                                                                |
| --: | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Presentation addresses pain points in Kubernetes PHOPS (Platform Operations) and proposes an open-source, Kubernetes-native solution.                     |
|   2 | Presenters: Ankur Singh (Red Hat, Azure Red Hat OpenShift SRE) and Satyam (Mirantis, open-source multi-cloud management).                                 |
|   3 | Current PHOPS cycles take 6-8 weeks to identify, fix, and validate cost/resource issues, which is too slow for modern deployment cycles.                  |
|   4 | Existing autoscalers only use current data; no solution leverages forecasted data for proactive optimization.                                             |
|   5 | Many open-source tools exist for metrics (Prometheus, Thanos), forecasting (Oneshot, ARMA, TimesFM), and actions (Carpenter, KEDA), but lack integration. |
|   6 | Proposed solution integrates observability, forecasting, and optimization into a single extensible, open-source platform.                                 |
|   7 | System uses agents and automated loops to collect metrics (via OpenTelemetry, OpenCost), feed time-series models, and generate recommendations.           |
|   8 | Human-in-the-loop approval is required for recommendations due to potential AI model drift or inaccuracies.                                               |
|   9 | Project "Auger" implements this pattern using three custom Kubernetes resources: forecast pipeline, forecast model, and recommendation.                   |
|  10 | Standard data formats ensure extensibility and integration with various data sources.                                                                     |
|  11 | Supports multi-model inference, allowing users to compare and select the best model for their workloads.                                                  |
|  12 | Includes drift detection by comparing forecasted and actual values, raising Kubernetes events if accuracy drops.                                          |
|  13 | Human approval mechanism ensures recommendations are audited before action.                                                                               |
|  14 | Extensible architecture: contributors can add new data sources, models, or policies by implementing minimal Python classes/functions.                     |
|  15 | Hybrid Golang (Kubernetes plumbing) and Python (AI/ML inference) design.                                                                                  |
|  16 | Supports multi-cluster deployments and plug-in approaches.                                                                                                |
|  17 | Demo showcased Auger running on a local kind cluster, using ARMA and Oneshot models, with recommendations visualized in Grafana.                          |
|  18 | Project is open source                                                                                                                                    |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=65TRuI5hvn4)
