---
type: Video Note
title: "Cloud Native Theater | Data on Kubernetes Day: From Billion... Victoriya Kalmanovich & Shahar Azulay"
description: "In this presentation, Shahara Zilai and Vicki Kalmanovich discuss the challenges of monitoring Kubernetes environments at scale, emphasizing the complexity introduced by microservices and the explosion of telemetry data such as logs, metric..."
resource: https://www.youtube.com/watch?v=G9Bt-7OHVBk
tags: ["kubecon-cloudnativecon-europe-2026", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

In this presentation, Shahara Zilai and Vicki Kalmanovich discuss the challenges of monitoring Kubernetes environments at scale, emphasizing the complexity introduced by microservices and the explosion of telemetry data such as logs, metrics, and traces.
They share personal experiences illustrating how inadequate observability can hinder troubleshooting and lead to operational setbacks, highlighting the necessity of robust observability as a prerequisite for managing modern cloud-native systems.
The speakers outline the limitations of both self-hosted and managed SaaS observability solutions—self-hosted stacks demand significant maintenance and can become unstable, while SaaS offerings often lead to high costs, data sovereignty concerns, and forced data reduction.
As an alternative, they introduce the "bring your own cloud" (BYOC) approach, where observability backends are deployed within the customer’s own cloud environment, combining the control and cost benefits of self-hosting with the ease of managed services.
This model leverages open-source databases like Clickhouse and VictoriaMetrics for scalable, efficient data storage, supports advanced use cases including AI-driven analysis, and aims to eliminate trade-offs between data access, cost, and operational simplicity in Kubernetes observability.
# Main Points

|   # | Main point                                                                                                                                                |
| --: | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Presentation covers Kubernetes monitoring at scale, technologies, and suggestions.                                                                        |
|   2 | Speakers: Shahara Zilai (CEO/co-founder, Ground Cover) and Vicki Kalmanovich (engineering leader).                                                        |
|   3 | Personal story: Startup acquired by Walmart, required to split monolith into microservices for scale.                                                     |
|   4 | Move to microservices and Kubernetes increased complexity and reduced system visibility.                                                                  |
|   5 | Troubleshooting and debugging became difficult due to inadequate observability tools.                                                                     |
|   6 | Visibility issues led to reverting back to monolith, highlighting observability as essential for microservices.                                           |
|   7 | Kubernetes enables powerful scaling for teams and infrastructure, but increases telemetry data volume and complexity.                                     |
|   8 | Telemetry data (logs, metrics, traces) is doubling every 15 months, with further acceleration expected from AI workloads.                                 |
|   9 | Cloud native environments are complex due to ephemeral infrastructure, autoscaling, and interdependent configurations.                                    |
|  10 | Hundreds of microservices, varying replica sets, and unpredictable user use cases add to complexity.                                                      |
|  11 | Each stack layer affects others, requiring more data and understanding for troubleshooting.                                                               |
|  12 | Observability requires infrastructure monitoring, log management, APM tracing, and real user monitoring, all correlated.                                  |
|  13 | Shift from passive monitoring to observability, now moving toward autonomy with AI workloads generating massive telemetry.                                |
|  14 | Telemetry is now used for more than troubleshooting, including development and AI agents.                                                                 |
|  15 | Need for tools to sample and find relevant data amid noise.                                                                                               |
|  16 | Example: Misdiagnosed production bug due to overwhelming telemetry; observability enabled finding the right signal.                                       |
|  17 | Two main telemetry storage options: self-hosted open source (control, but high maintenance) or managed SaaS (simplicity, but high cost and less control). |
|  18 | Both options have scaling issues: self-hosted is resource-intensive, SaaS leads to data throttling and vendor lock-in.                                    |
|  19 | Bring Your Own Cloud (BYOC) for observability offers man                                                                                                  |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=G9Bt-7OHVBk)