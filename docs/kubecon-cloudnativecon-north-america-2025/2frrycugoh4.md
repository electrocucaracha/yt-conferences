---
type: Video Note
title: "Don't Panic! A Beginner's Guide To K8s Debugging - Ivan Porta & Phil Henderson, Buoyant"
description: "Phil Henderson and Ivan Pora present a beginner-friendly guide to troubleshooting Kubernetes, focusing on the complexities of managing microservices across single and multi-cluster environments. They explain how service meshes like Linkerd..."
resource: https://www.youtube.com/watch?v=2fRRYcugOh4
tags: ["kubecon-cloudnativecon-north-america-2025", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

Phil Henderson and Ivan Pora present a beginner-friendly guide to troubleshooting Kubernetes, focusing on the complexities of managing microservices across single and multi-cluster environments.
They explain how service meshes like Linkerd simplify service-to-service communication by deploying proxies that handle load balancing, retries, circuit breaking, and observability, allowing developers to focus on business logic.
The talk covers Linkerd’s architecture, including its control and data planes, and demonstrates how metrics, logs, and traces can be collected and visualized using tools like Grafana, Prometheus, and Loki.
The presenters discuss common troubleshooting scenarios, such as DNS issues, control plane overload, and configuration errors, emphasizing the importance of good monitoring dashboards and collaboration between platform and application teams.
Despite some live demo challenges, they encourage audience interaction and highlight the need for effective processes and visibility to quickly identify and resolve issues in Kubernetes environments.
# Main Points

|   # | Main point                                                                                                                                                                       |
| --: | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | The talk is aimed at beginners and focuses on troubleshooting Kubernetes.                                                                                                        |
|   2 | Microservices can be written in different languages and managed by different teams, leading to repeated implementations of features like metrics, tracing, and circuit breaking. |
|   3 | Failures in one microservice can cause cascading failures across others, making troubleshooting complex.                                                                         |
|   4 | Troubleshooting becomes more difficult with multi-cluster Kubernetes environments.                                                                                               |
|   5 | Downtime has both direct and indirect financial impacts, including damaged relationships and regulatory fines.                                                                   |
|   6 | Service mesh (specifically Linkerd) helps manage service-to-service communication by deploying proxies alongside applications.                                                   |
|   7 | Service mesh proxies handle load balancing, retries, circuit breaking, and traffic encryption, reducing developer overhead.                                                      |
|   8 | Linkerd has a two-layer architecture: control plane (service discovery, certificate management, config) and data plane (policy enforcement, encryption).                         |
|   9 | Proxies expose metrics at both layer 4 (TCP) and layer 7 (HTTP/gRPC), including latency, request rates, and success rates.                                                       |
|  10 | Metrics are exposed in Prometheus format and can be visualized with tools like Grafana, DataDog, and OpenSearch.                                                                 |
|  11 | Tracing is supported out-of-the-box via OpenTelemetry; spans can be visualized in tools like Jaeger or Splunk.                                                                   |
|  12 | Linkerd CLI provides commands to check mesh health, certificate validity, and perform diagnostics.                                                                               |
|  13 | Linkerd can be installed via Helm charts, CLI, or operator.                                                                                                                      |
|  14 | AI/ML features are being developed for Linkerd (MCP support in beta).                                                                                                            |
|  15 | Demo uses Grafana stack (Loki for logs, Tempo for traces, Pyroscope for profiling) and a test app (Emoji Voto).                                                                  |
|  16 | Emphasis on monitoring core Kubernetes components like CoreDNS and etcd.                                                                                                         |
|  17 | Importance of having dashboards for observability; application developers should have access to relevant metrics and logs.                                                       |
|  18 | Platform and application teams often have a knowledge gap; good processes and communication are essential.                                                                       |
|  19 | Service mesh can                                                                                                                                                                 |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=2fRRYcugOh4)