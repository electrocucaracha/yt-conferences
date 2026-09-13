---
type: Video Note
title: "OTel+K8s= ❤️: An Introduction To OpenTelemetry for Kubernetes... Christos Markou & Jacob Aronoff"
description: "The presentation introduces OpenTelemetry (OTEL) and its integration with Kubernetes, covering both foundational concepts and advanced topics. The speakers explain that OTEL is a vendor-neutral, open-source standard for collecting metrics..."
resource: https://www.youtube.com/watch?v=cCGNs7nyutU
tags: ["kubecon-cloudnativecon-north-america-2025", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

The presentation introduces OpenTelemetry (OTEL) and its integration with Kubernetes, covering both foundational concepts and advanced topics.
The speakers explain that OTEL is a vendor-neutral, open-source standard for collecting metrics, logs, and traces, and is widely adopted in the CNCF ecosystem.
They detail how OTEL’s collector can be deployed in various modes (sidecar, DaemonSet, deployment, gateway) to gather telemetry from Kubernetes clusters, nodes, and workloads, using specialized receivers and processors for metrics, logs, and events.
The session also highlights the use of the OTEL operator and Helm charts to simplify deployment, configuration, and auto-instrumentation, as well as advanced features like auto-discovery, leader election, log resilience, and semantic conventions for standardizing telemetry.
Operational considerations such as resource planning, configuration management, and handling back pressure are discussed, and the Q&A addresses backend storage options, log handling strategies, deployment patterns, and future plans for more flexible configuration and presets.
# Main Points

|   # | Main point                                                                                                                                         |
| --: | -------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Introduction to OpenTelemetry (OTEL) and Kubernetes monitoring, covering basics and advanced topics.                                               |
|   2 | Presenters: Jacob Areronoff (Tero, OTEL operator/Helm maintainer) and Christo Marco (Elastic, OTEL collector/semantic conventions approver).       |
|   3 | Goals: Explain OTEL basics for Kubernetes, reference architectures, and trade-offs.                                                                |
|   4 | OTEL is an open-source, vendor-neutral standard for telemetry (metrics, logs, traces); second largest CNCF project.                                |
|   5 | Observability in Kubernetes focuses on metrics (system state, usually via Prometheus), traces (request flow), and logs (diagnostics).              |
|   6 | Prometheus is pull-based (may lose data from ephemeral pods); OTEL supports both pull and push, with push better for short-lived jobs.             |
|   7 | Annotate telemetry with cluster, namespace, deployment for multi-cluster environments; OTEL provides semantic conventions.                         |
|   8 | OTEL Collector: Vendor-neutral agent for building telemetry pipelines; can run as agent (edge) or centralized gateway.                             |
|   9 | Key collector receivers:                                                                                                                           |
|  10 | Cluster-level: k8s_cluster receiver (singleton per cluster), Kubernetes events receiver (singleton), Kubernetes object receiver (watch/pull mode). |
|  11 | Prometheus receiver: Scrapes Prometheus endpoints, supports distributed scraping.                                                                  |
|  12 | Node-level: kubeletstats receiver (per node, daemonset), filelog receiver (container logs), hostmetrics receiver (host system metrics).            |
|  13 | Processors: Kubernetes attributes processor (enriches telemetry), transform processor (OTTL for declarative transformations).                      |
|  14 | Deployment strategies:                                                                                                                             |
|  15 | Sidecar (granular, expensive, hard to update)                                                                                                      |
|  16 | Daemonset (per node, efficient, risk of data loss on node failure)                                                                                 |
|  17 | Deployment (centralized, easy to scale, bottleneck risk)                                                                                           |
|  18 | Gateway pattern (local collection + central processing)                                                                                            |
|  19 | OTEL Operator: CRDs for collector config, auto-instrumentation, distributed Prometheus scraping (target allocator).                                |
|  20 | Helm charts: Four available (collector, operator, demo, kubestack); support for presets (e.g., log collection, K                                   |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=cCGNs7nyutU)