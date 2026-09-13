---
layout: default
title:
  One Controller to Rule Them All - Taming Multiple Orchestrator... Srikar Paruchuru
  & Egor Grishechko
nav_order: 227
parent: Kubecon Cloudnativecon Europe 2026
type: Video Note
description:
  Sri and Eager from Uber’s compute team in Amsterdam discussed their experience
  managing stateless compute at scale, focusing on reconciling multiple orchestrators
  for workload scaling. They described Uber’s compute platform, where the “up”...
resource: https://www.youtube.com/watch?v=lVt510hb8kY
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

Sri and Eager from Uber’s compute team in Amsterdam discussed their experience managing stateless compute at scale, focusing on reconciling multiple orchestrators for workload scaling.
They described Uber’s compute platform, where the “up” federation layer manages service deployments across numerous Kubernetes clusters and regions, and explained the challenges introduced by adding a failover orchestrator to optimize resource usage and reduce idle capacity.
To address conflicts between orchestrators, they developed a new custom resource definition (CRD) called “service scale,” which tracks scaling intentions from different controllers and enables reliable failover and failback without external dependencies.
They also highlighted the complexities of ensuring consistency and avoiding stale reads in Kubernetes’ eventually consistent model, implementing a “read your own write” guardrail and observability tools to detect and heal inconsistencies.
The team emphasized the importance of extensive integration testing to ensure a smooth rollout and shared lessons learned about the unexpected difficulties and debugging challenges encountered when building seemingly simple solutions at Uber’s scale.

# Main Points

|   # | Main point                                                                                                                                 |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------ |
|   1 | Sri and Eager from Uber's stateless compute team in Amsterdam presented on managing multiple scale orchestrators.                          |
|   2 | Uber runs millions of workloads across many Kubernetes clusters in multiple regions and zones.                                             |
|   3 | The "UP" platform is the main interface for service owners to deploy and scale services, acting as a federation layer.                     |
|   4 | UP interacts with Kubernetes clusters, which are managed by the compute team, and aggregates resource data for smarter workload placement. |
|   5 | Uber uses a custom CRD called "Uber deployment" to encapsulate service requirements, managed by a dedicated controller.                    |
|   6 | UP also functions as Uber's continuous deployment platform, relying on status objects from deployments.                                    |
|   7 | Failover orchestration was introduced to handle emergencies, requiring regional failover and workload reallocation.                        |
|   8 | Historically, Uber kept double hardware capacity for failover, leading to idle resources.                                                  |
|   9 | To optimize, Uber evicts lower-tier workloads during failover and reallocates high-tier workloads.                                         |
|  10 | The introduction of a second orchestrator (failover) created challenges with multiple controllers managing scaling.                        |
|  11 | A new "service scale" CRD was developed to coordinate scaling intentions from different controllers, enabling clear failover and failback. |
|  12 | The service scale CRD maintains a map of desired instances per controller, aiding debugging and state tracking.                            |
|  13 | Status computation is complicated by Kubernetes' eventual consistency and stale informer reads.                                            |
|  14 | Uber implemented a "read your own write" guardrail to ensure controllers see their own latest changes before computing status.             |
|  15 | Multiple controllers writing to the same deployment caused annotation/spec drift and stuck workloads.                                      |
|  16 | Observability and healing automation were built to detect and fix these inconsistencies in production.                                     |
|  17 | Integration and unit tests were critical to safely rolling out the new solution without outages.                                           |
|  18 | Developing even simple controller solutions at Uber's scale required signifi                                                               |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=lVt510hb8kY)
