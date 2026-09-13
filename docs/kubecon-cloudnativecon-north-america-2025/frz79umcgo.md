---
layout: default
title:
  "Efficient Kubernetes Autoscaling: News, Challenges, and Best Practi... Zbynek
  Roubalik & Jan Wozniak"
nav_order: 67
parent: Kubecon Cloudnativecon North America 2025
type: Video Note
description:
  In this session, Jan and Binak, both maintainers of KEDA (pronounced
  "kay-da"), introduce the project and discuss its features, best practices, and challenges
  in Kubernetes autoscaling. KEDA extends Kubernetes' native Horizontal Pod Autosca...
resource: https://www.youtube.com/watch?v=-frz79uMCgo
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

In this session, Jan and Binak, both maintainers of KEDA (pronounced "kay-da"), introduce the project and discuss its features, best practices, and challenges in Kubernetes autoscaling.
KEDA extends Kubernetes' native Horizontal Pod Autoscaler (HPA) by enabling autoscaling based on a wide range of event sources and custom metrics, not just CPU or memory, and supports over 65 integrated event sources.
The presenters explain KEDA's architecture, including its use of custom resources like ScaledObject for horizontal scaling and ScaleJob for event-driven job scheduling, and highlight new features such as enhanced fallback strategies and scaling modifiers that allow for more flexible scaling logic.
They emphasize best practices like carefully configuring scaling behavior, understanding polling intervals, and being cautious with Prometheus or DataDog scalers to avoid overloading metric servers.
The session also covers advanced autoscaling scenarios, such as coordinated scaling across dependent services and scaling groups, and addresses audience questions about integrating KEDA with custom resources, combining HPA and VPA, and handling Java workloads.
The presenters conclude by inviting attendees to provide feedback and visit their booth for further discussion and activities.

# Main Points

|   # | Main point                                                                                                         |
| --: | ------------------------------------------------------------------------------------------------------------------ |
|   1 | Jan and Binak introduced themselves as KDA maintainers; Binak is also CTO at Kify.                                 |
|   2 | Audience includes current, potential, and unfamiliar KDA users.                                                    |
|   3 | KDA simplifies Kubernetes autoscaling, allowing scaling based on events and custom metrics, not just CPU/memory.   |
|   4 | KDA supports 65-80 integrated event sources (e.g., Prometheus, Kafka).                                             |
|   5 | Only one KDA installation per cluster due to Kubernetes external metrics limitation.                               |
|   6 | KDA uses custom resources: main components are the K operator/controller and metric server.                        |
|   7 | Two main use cases: horizontal scaling (scaled objects) and scheduling Kubernetes jobs (scaled jobs).              |
|   8 | Scaled objects define targets, scaling configuration, and triggers (scalers); only one scaled object per workload. |
|   9 | Scale jobs allow on-demand job creation based on events or custom metrics.                                         |
|  10 | New features: more scalers, improved fallback strategies for metric server outages.                                |
|  11 | Fallback now supports richer strategies beyond static replica counts.                                              |
|  12 | Best practices:                                                                                                    |
|  13 | Always specify scaling behavior (how fast to scale, stabilization windows).                                        |
|  14 | For cron scaler, set minReplicas to zero in scaled object, not in cron schedule.                                   |
|  15 | Polling interval is only for 0→1 scaling; avoid unnecessary polling if minReplicas > 0.                            |
|  16 | Use scaling modifiers to customize scaling logic (e.g., average, min, formulas).                                   |
|  17 | Prometheus scaler is easy but can overload Prometheus at scale; consider direct metrics or OpenTelemetry scaler.   |
|  18 | Coordinated scaling: use Kubernetes workload trigger to chain scaling between related services, reducing HPA lag.  |
|  19 | Scaling groups: scaling modifiers help manage shared resource limits across independent services.                  |
|  20 | VPA and HPA should not be combined on same metrics; combining with custom metrics is under consideration.          |
|  21 | To scale custom resources without scale subresource, patching is possible but scale subresource is preferred.      |
|  22 | JVM workloads: expose JVM-specific metrics for better scaling decisions.                                           |
|  23 | Kify booth offers further discussion                                                                               |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=-frz79uMCgo)
