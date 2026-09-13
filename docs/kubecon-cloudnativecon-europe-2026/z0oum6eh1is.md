---
type: Video Note
title: "We Deleted Our Observability Stack and Rebuilt It With OTEL: 12 Engine... Yash Sharma & Kunju Perath"
description: "In this session, Yash and Kunju from DigitalOcean discuss the evolution of observability for their managed Kubernetes service, DOKS, which operates over 20,000 clusters across 13 regions. Initially, their observability relied on large, file..."
resource: https://www.youtube.com/watch?v=Z0oum6Eh1is
tags: ["kubecon-cloudnativecon-europe-2026", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

In this session, Yash and Kunju from DigitalOcean discuss the evolution of observability for their managed Kubernetes service, DOKS, which operates over 20,000 clusters across 13 regions.
Initially, their observability relied on large, file-based databases and a single Prometheus instance for control plane metrics, but this setup lacked searchable audit logs, comprehensive telemetry from worker nodes, and effective event logging, making it difficult to proactively detect and resolve issues.
To address these gaps, they transitioned to an architecture based on OpenTelemetry (otel), deploying lightweight agent and gateway collectors across both control and data planes, and leveraging open source plugins for flexible, scalable telemetry collection and processing.
This new approach enabled them to achieve searchable logs (using OpenSearch), improved metadata enrichment, and more efficient resource usage, while also reducing mean time to detect issues from hours to minutes.
The team emphasized the importance of understanding new telemetry formats, monitoring the observability stack itself, and carefully managing dependencies, ultimately resulting in a more robust, scalable, and customer-responsive observability platform.
# Main Points

|   # | Main point                                                                                                  |
| --: | ----------------------------------------------------------------------------------------------------------- |
|   1 | Session covers observability at DigitalOcean for managed Kubernetes service (DOKS)                          |
|   2 | Presenters: Yash (Developer Advocate, CNCF maintainer) and Kunju (Engineer, DOKS team)                      |
|   3 | DOKS team: 18 people managing 20,000+ clusters across 13 cloud regions                                      |
|   4 | Achieved 99.97% uptime (above promised 99.95%)                                                              |
|   5 | DigitalOcean uses and supports open source, including Hacktoberfest                                         |
|   6 | Observability is crucial to detect issues before customers notice                                           |
|   7 | Previous strengths: good control plane metrics and long-term storage, searchable logs for backend services  |
|   8 | Previous weaknesses:                                                                                        |
|   9 | Poor Kubernetes audit logs (file-based, lost on cluster restarts)                                           |
|  10 | Lack of searchable container logs for control plane components                                              |
|  11 | Insufficient telemetry for managed customer data plane and worker nodes                                     |
|  12 | Architecture:                                                                                               |
|  13 | Customer clusters’ control planes are hosted in separate Kubernetes clusters (cluster API, "kubeception")   |
|  14 | Telemetry previously collected via single large Prometheus instance per control plane cluster               |
|  15 | Gaps: no worker node telemetry, no kube-system telemetry, non-searchable audit logs, no event logging       |
|  16 | Solution: Adopted OpenTelemetry ("otel") for metrics and logs across stack                                  |
|  17 | Used open telemetry contrib image with community plugins                                                    |
|  18 | Pipeline: receiver → processor (add/filter fields, batch, memory limit) → exporter (OTLP format, S3/Spaces) |
|  19 | Gateway-agent pattern: lightweight agents collect telemetry, send to gateway, then to observability backend |
|  20 | Telemetry now covers control plane, kube-system, and worker nodes                                           |
|  21 | Lessons learned:                                                                                            |
|  22 | Avoided overcomplicating with OpenTelemetry operator CRDs; bare deployments preferred                       |
|  23 | Importance of understanding resource vs. telemetry attributes                                               |
|  24 | Early observability for observability components is critical                                                |
|  25 | Transition reduced compute needs, improved scalability, and mean time to detect issues (hours → minutes)    |
|  26 | Searchable logs now indexed in OpenSearch by log type                                                       |
|  27 | Presentation handled via Grafana dashboards; O                                                              |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=Z0oum6Eh1is)