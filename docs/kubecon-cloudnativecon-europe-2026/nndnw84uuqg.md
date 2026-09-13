---
type: Video Note
title: "Cloud Native Theater | Cloud Native University: A Simple and Practical Guide to Obser... Diana Todea"
description: "The speaker, an OpenTelemetry contributor and cloud native community organizer, discusses the challenges and best practices of observability in Kubernetes environments. They highlight the complexity caused by the abundance of tools, metrics..."
resource: https://www.youtube.com/watch?v=nNDNw84Uuqg
tags: ["kubecon-cloudnativecon-europe-2026", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

The speaker, an OpenTelemetry contributor and cloud native community organizer, discusses the challenges and best practices of observability in Kubernetes environments.
They highlight the complexity caused by the abundance of tools, metrics, and dashboards, emphasizing the need to simplify onboarding for both contributors and end users.
Key issues include inconsistent metric naming, high cardinality, and non-standardized logs, with sources ranging from control plane components to application logs and audit logs.
The speaker demonstrates how audit logs can be parsed and visualized using open-source tools like Grafana, offering valuable insights for troubleshooting and monitoring.
They advocate for structured logging, early instrumentation, and thoughtful alerting, and encourage community involvement in SIG Instrumentation to improve metric documentation, dashboard usability, and onboarding resources, ultimately aiming to enhance the developer and user experience in Kubernetes observability.
# Main Points

|   # | Main point                                                                                                               |
| --: | ------------------------------------------------------------------------------------------------------------------------ |
|   1 | Speaker is an OpenTelemetry contributor and Cloud Native Romania organizer, discussing observability for Kubernetes.     |
|   2 | Observability in Kubernetes is complex due to many tools, platforms, metrics, and dashboards.                            |
|   3 | Key sources of Kubernetes metrics: API server, applications, kubelets, cAdvisor, control manager, scheduler.             |
|   4 | Kubernetes metrics stability:                                                                                            |
|   5 | Alpha level: no stability guarantees; metrics can change or be deleted anytime.                                          |
|   6 | Stable metrics: guaranteed not to change except for deprecation in future versions.                                      |
|   7 | Important metrics include:                                                                                               |
|   8 | Control plane: API server request rates, latency, errors.                                                                |
|   9 | Nodes/workloads: CPU usage, memory usage, resource requests vs. limits, pod restarts.                                    |
|  10 | Scheduling: scheduling latency, pending pods.                                                                            |
|  11 | Common metric problems: inconsistent naming/labels, high cardinality, duplicated metrics, purposeless dashboards.        |
|  12 | Log sources: application logs, Kubernetes events, control plane logs, container runtime logs.                            |
|  13 | Common log problems: lack of standardization, varying formats (structured JSON, arbitrary formats, strict schemas).      |
|  14 | Kubernetes events and audit logs are valuable; audit logs show who did what and may contain sensitive info.              |
|  15 | Example: Kubernetes event exporter and audit log stats app (GitHub repo) parse audit logs and visualize data in Grafana. |
|  16 | Audit log visualizations can show operations per username, resource, verb, namespace, latency, etc.                      |
|  17 | Recommendations for developers:                                                                                          |
|  18 | Use structured logs.                                                                                                     |
|  19 | Instrument from day zero.                                                                                                |
|  20 | Focus on defining and automating alerts.                                                                                 |
|  21 | Consider tracing for vendor-neutral, standardized observability.                                                         |
|  22 | SIG Instrumentation is working on:                                                                                       |
|  23 | Better metric documentation.                                                                                             |
|  24 | Grouping metrics by severity.                                                                                            |
|  25 | Improving dashboards, alerts, structured logging, and observability guides.                                              |
|  26 | Community efforts aim to improve onboarding, documentation, and developer experience for Kubernetes observability.       |
|  27 | Ideas include classifying metrics by user level (beginner, intermedi                                                     |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=nNDNw84Uuqg)