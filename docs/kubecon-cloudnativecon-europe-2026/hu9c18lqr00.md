---
type: Video Note
title: "DNS Tracing & Metrics Via eBPF in OpenTelemetry - Endre Sara & Nikola Grcevski"
description: "Nikola Grachevski and Andras Szabo present on DNS observability using the OpenTelemetry BPF (OB) Instrumentation project, which leverages eBPF technology for low-overhead, kernel-level monitoring of DNS activity in Linux environments. They..."
resource: https://www.youtube.com/watch?v=hu9c18lqR00
tags: ["kubecon-cloudnativecon-europe-2026", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

Nikola Grachevski and Andras Szabo present on DNS observability using the OpenTelemetry BPF (OB) Instrumentation project, which leverages eBPF technology for low-overhead, kernel-level monitoring of DNS activity in Linux environments.
They highlight the common challenge of diagnosing DNS-related performance issues, noting that slow or excessive DNS queries often go unnoticed and are difficult to attribute to specific clients or services.
OB captures DNS metrics and traces without requiring code changes or service restarts, enriching telemetry with Kubernetes and cloud metadata, and integrates seamlessly with existing OpenTelemetry setups.
The tool enables users to identify inefficient DNS usage, such as unnecessary lookups or misconfigured search domains, and provides accurate end-to-end timing by monitoring events at the kernel level.
The presenters emphasize OB’s security benefits, ease of deployment, and its ability to operate alongside or independently of existing instrumentation, making DNS observability accessible and actionable for large-scale production environments.
# Main Points

|   # | Main point                                                                                                                                                                |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Nikola Grachevski (OpenTelemetry BPF Instrumentation maintainer, Grafana Labs) and Andras Szabo (Cosly co-founder) presented on DNS observability.                        |
|   2 | DNS issues are common but often hard to diagnose due to lack of client-side visibility.                                                                                   |
|   3 | eBPF-based auto instrumentation provides low-overhead DNS observability without code changes or service restarts.                                                         |
|   4 | OpenTelemetry BPF Instrumentation (OB) captures DNS queries at the kernel level, correlates requests and responses, and enriches data with Kubernetes and cloud metadata. |
|   5 | OB exports DNS metrics (e.g., lookup duration, queried name, service info) and optional trace spans.                                                                      |
|   6 | DNS trace spans can be correlated with HTTP or gRPC traces, showing DNS as a child of outgoing client calls.                                                              |
|   7 | OB works with or without existing OpenTelemetry instrumentation and avoids duplicating telemetry for already-instrumented services.                                       |
|   8 | DNS metrics are captured for all services by default but can be limited to specific namespaces or resources.                                                              |
|   9 | OB provides accurate end-to-end timing from kernel event to completion, including time not visible to application-level instrumentation.                                  |
|  10 | Installation is simple via Kubernetes DaemonSet or Helm chart.                                                                                                            |
|  11 | Real-world issues observed include excessive DNS requests due to partial names, search domains, and lack of caching.                                                      |
|  12 | OB helps identify which clients are causing DNS overload, enabling targeted fixes.                                                                                        |
|  13 | OB is the only open-source eBPF-based DNS observability tool; Grafana Beyla is a shell on top of OB.                                                                      |
|  14 | OB requires certain system-level privileges but can be securely isolated from application processes.                                                                      |
|  15 | Current limitations include Linux-only support and hardcoded DNS ports (53, 5353), but configuration options are planned.                                                 |
|  16 | OB is in active development with a release candidate planned; already used in production by some users.                                                                   |
|  17 | Q&A covered permissions, multi-level DNS tracing, port configuration, project status, and trace correlation challenges.                                                   |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=hu9c18lqR00)