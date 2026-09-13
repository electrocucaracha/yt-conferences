---
layout: default
title:
  "Into the Shopfloor: Moving Manufacturing Execution Syste... Manuel Peuster
  & Andrei Traian Cucuruzac"
nav_order: 132
parent: Kubecon Cloudnativecon Europe 2025
type: Video Note
description:
  Bosch Connected Industry, a software provider within Bosch, has successfully
  migrated its Manufacturing Execution System (MES) to Kubernetes, enabling faster
  and more efficient deployment of its industrial control systems. The company initi...
resource: https://www.youtube.com/watch?v=GgxRHpQIEfg
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

Bosch Connected Industry, a software provider within Bosch, has successfully migrated its Manufacturing Execution System (MES) to Kubernetes, enabling faster and more efficient deployment of its industrial control systems.
The company initially took a "lift and shift" approach, containerizing existing applications before moving to Kubernetes, but later adopted a library helm chart approach to improve scalability and maintainability.
This transition allowed Bosch to reduce deployment times from hours or days to minutes, making it possible to deploy complex manufacturing systems quickly and reliably.
The company also leveraged custom operators to manage legacy components and ensure reliable connections between on-prem and cloud environments.
By adopting Kubernetes, Bosch has improved its ability to scale and maintain its industrial control systems in a rapidly changing environment.

# Main Points

|   # | Main point                                                                                                                                        |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | The MES is a software that monitors, manages, and optimizes production on the shop floor in real-time.                                            |
|   2 | It serves as a bridge between enterprise systems and shop floor operations.                                                                       |
|   3 | The company decided to move its legacy MES to Kubernetes for scalability and flexibility.                                                         |
|   4 | They used a lift-and-shift approach, containerizing individual modules before deploying them on Kubernetes.                                       |
|   5 | This resulted in slow deployments and updates, but they improved by using Helm charts and simultaneous pipeline deployment.                       |
|   6 | They also built custom operators for managing databases and implementing identity and access management.                                          |
|   7 | The company had challenges with legacy systems, including those running OPC DA and HMI.                                                           |
|   8 | They considered using the Cube Word project to connect to these systems, but kept them on-prem for now.                                           |
|   9 | Bosch Connected Industry operates its MES entirely on-prem clouds, with some non-latency sensitive modules available in the public cloud (Azure). |
|  10 | The company plans to use Kubernetes for all MES functionality in the future.                                                                      |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=GgxRHpQIEfg)
