---
layout: default
title:
  "Sync or Swim: Building Platforms You Can See - Heather Lee & Mike Cutsail,
  Apple"
nav_order: 298
parent: Kubecon Cloudnativecon North America 2025
type: Video Note
description:
  In this talk, Mike and Heather from Apple discuss the challenges and
  solutions for building observable developer platforms using Kubernetes, Crossplane,
  Argo CD, and OpenTelemetry. They demonstrate how platform engineers and end users
  can b...
resource: https://www.youtube.com/watch?v=g70y40Qk7bs
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

In this talk, Mike and Heather from Apple discuss the challenges and solutions for building observable developer platforms using Kubernetes, Crossplane, Argo CD, and OpenTelemetry.
They demonstrate how platform engineers and end users can benefit from enhanced visibility into platform health by instrumenting both infrastructure and custom code, enabling rapid detection and root cause analysis of issues.
Through live demos, they show how claims made via the Kubernetes API are tracked, how Argo CD and Grafana dashboards provide real-time insights into resource states, and how observability tools can immediately surface the impact of platform changes, such as configuration bugs.
The speakers emphasize best practices like consistent labeling, treating observability as code, and correlating metrics and traces to create unified, actionable dashboards.
They conclude that robust observability is essential for platform trust and effective troubleshooting, sharing practical techniques for integrating these tools and patterns into any platform engineering workflow.

# Main Points

|   # | Main point                                                                                            |
| --: | ----------------------------------------------------------------------------------------------------- |
|   1 | Audience includes both platform engineers and end users; content is for both groups                   |
|   2 | Goal: improve platform end user experience and observability for platform teams                       |
|   3 | Key takeaways:                                                                                        |
|   4 | Shared understanding of observability challenges for platform teams                                   |
|   5 | Unique problems in building developer platforms                                                       |
|   6 | Making platforms visible to platform engineers and end users                                          |
|   7 | Demonstrate observability signals from a real platform stack                                          |
|   8 | Share best practices for composing instrumentation patterns                                           |
|   9 | Agenda:                                                                                               |
|  10 | Walkthrough of tech stack used for demo                                                               |
|  11 | Discuss issues arising from using such platforms                                                      |
|  12 | Demos addressing issues from both user and operator perspectives                                      |
|  13 | How observability was built into the platform                                                         |
|  14 | Tech stack:                                                                                           |
|  15 | Crossplane extends Kubernetes to manage infrastructure via APIs                                       |
|  16 | Composition templates automate resource creation                                                      |
|  17 | Argo CD as GitOps engine for syncing infrastructure claims                                            |
|  18 | OpenTelemetry (Otel) for collecting metrics, traces, and logs                                         |
|  19 | Demo uses a local kind cluster, Crossplane, custom composition function, and full observability stack |
|  20 | Platform use cases:                                                                                   |
|  21 | Cluster, database, and security policy claims via Kubernetes API                                      |
|  22 | Crossplane provisions resources per team, ensuring isolation and standards                            |
|  23 | Observability challenges:                                                                             |
|  24 | Users need visibility into claim status and resource health                                           |
|  25 | Argo CD and Grafana dashboards provide real-time health and state tracking                            |
|  26 | Dashboards allow filtering by claim, team, or platform-wide resources                                 |
|  27 | Demo scenarios:                                                                                       |
|  28 | End user tracks claim health and root causes via dashboards                                           |
|  29 | Platform engineer pushes a buggy function; observability tools detect, trace, and audit the impact    |
|  30 | Observability implementation:                                                                         |
|  31 | Cube state metrics extracts resource states as Prometheus metrics                                     |
|  32 | OpenTelemetry instruments custom code, emits traces, and generates metrics                            |
|  33 | Linking metrics and traces via exemplars in Grafana                                                   |
|  34 | Consistent labeling (claim name, namespace, cluster) enable                                           |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=g70y40Qk7bs)
