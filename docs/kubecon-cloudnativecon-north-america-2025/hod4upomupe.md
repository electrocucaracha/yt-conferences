---
layout: default
title:
  Unleash the Power of Inplace Pod Resource Resizing for Startup and Cost...
  Zhang Zhen & Yuxing Yuan
nav_order: 332
parent: Kubecon Cloudnativecon North America 2025
type: Video Note
description:
  J from Alibaba Cloud, maintainer of the OpenKruise project, introduces
  in-place pod resizing, a feature enabling non-disruptive vertical autoscaling in
  Kubernetes, now in beta and available in recent releases. He discusses several use
  cases...
resource: https://www.youtube.com/watch?v=Hod4UPoMUPE
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

J from Alibaba Cloud, maintainer of the OpenKruise project, introduces in-place pod resizing, a feature enabling non-disruptive vertical autoscaling in Kubernetes, now in beta and available in recent releases.
He discusses several use cases, including emergency scaling during high-traffic events like China’s "grid promotion," improving Java application startup by temporarily boosting CPU, and enhancing stateful application scaling, such as databases during leader switches.
The talk also covers advanced vertical pod autoscaling (AVPA), which tracks short-term resource changes and applies scaling at the individual pod level, addressing issues with unbalanced workloads and hotspots.
J explains integration with workload controllers in OpenKruise, JVM tuning guidelines for effective resizing, and challenges like invisible resizing and hot migration.
He concludes with future plans for integrating AVPA with event-driven autoscaling and HPA, and answers audience questions on technical implementation, JVM checkpointing, metric support, and practical migration strategies.

# Main Points

|   # | Main point                                                                                                                                                                                                  |
| --: | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Introduction by J from Alibaba Cloud, maintainer of OpenKruise project                                                                                                                                      |
|   2 | Topic: Use cases of in-place pod resizing, debuting at KubeCon North America                                                                                                                                |
|   3 | In-place pod resizing enables non-disruptive vertical autoscaling, now beta in Kubernetes                                                                                                                   |
|   4 | OpenKruise implemented in-place image update and in-house API for resource resizing before native Kubernetes support                                                                                        |
|   5 | Emergency scaling use case: grid promotion (high-traffic events like Black Friday in China) requires fast scaling; in-place resizing allows immediate resource increase before horizontal scaling completes |
|   6 | Three main parts of the talk: use cases/tools for in-place resizing, Java/Spark application guidelines, future work                                                                                         |
|   7 | Application startup is a common use case, especially for Java apps; JVM startup is resource-intensive                                                                                                       |
|   8 | In-place resizing allows temporary CPU boost during startup, then scales down after readiness; users specify boost factor and duration                                                                      |
|   9 | Combined with CRaC (Coordinated Restore at Checkpoint) for near-instant Java restarts                                                                                                                       |
|  10 | Stateful application scaling: in-place resizing helps avoid disruption and speeds up leader switch in databases by scaling up secondaries                                                                   |
|  11 | Automatic application sizing: developers often overestimate resources; in-place resizing allows safe, non-disruptive scaling down                                                                           |
|  12 | Advanced Vertical Pod Autoscaler (AVPA) tracks short-term resource changes, applies changes per pod, and uses in-place resizing for unbalanced workloads/hotspots                                           |
|  13 | AVPA exposes HPA-like API, supports targetRef and generic pod selectors, and applies changes via resize subresources                                                                                        |
|  14 | OpenKruise advanced workload controllers (e.g., CloneSet, Advanced StatefulSet) integrate in-place resizing, supporting rolling updates and lifecycle hooks                                                 |
|  15 | PodUnavailableBudget protects availability during disruptive operations like memory resizing                                                                                                                |
|  16 | Hot migration used when node resources are insufficient for resizing; migration has limitations (e.g., freeze time)                                                                                         |
|  17 | JVM tuning guidelines provided for effective in-place re                                                                                                                                                    |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=Hod4UPoMUPE)
