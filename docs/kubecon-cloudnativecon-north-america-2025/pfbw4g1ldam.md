---
type: Video Note
title: "Observing Dark Matter With OpenTelemetry - Sam Alipio & Mario Macías, Grafana Labs"
description: "In this talk, Mario Matias and Sam discuss approaches to instrumenting applications for observability, focusing on OpenTelemetry and the use of eBPF (extended Berkeley Packet Filter) auto-instrumentation. They explain that while agent-based..."
resource: https://www.youtube.com/watch?v=pfBw4g1LdAM
tags: ["kubecon-cloudnativecon-north-america-2025", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

In this talk, Mario Matias and Sam discuss approaches to instrumenting applications for observability, focusing on OpenTelemetry and the use of eBPF (extended Berkeley Packet Filter) auto-instrumentation.
They explain that while agent-based and manual SDK instrumentation are common, eBPF offers a seamless, low-latency alternative that operates at the Linux kernel level, enabling instant telemetry without code changes or redeployment.
eBPF provides more accurate system-level data, such as improved response time measurements and visibility into hidden network traffic and DNS activity, which traditional SDKs may miss.
However, eBPF has limitations, including lack of business-level context, limited distributed tracing support, and a requirement for Linux environments.
The speakers introduce Grafana's OBI (OpenTelemetry eBPF Instrumentation) project, highlighting its capabilities and integration with existing SDKs, and emphasize that eBPF is a complementary tool rather than a replacement for SDKs.
They conclude by noting ongoing development to improve integration and protocol support, and address questions about performance impact, compatibility, and deployment options.
# Main Points

|   # | Main point                                                                                                                                              |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Speakers: Mario Matias (Grafana Labs, OpenTelemetry eBPF maintainer) and Sam (Paster Labs, Tessact Core product manager)                                |
|   2 | Topic: Observing dark matter with OpenTelemetry, focusing on eBPF auto-instrumentation                                                                  |
|   3 | Traditional options for telemetry:                                                                                                                      |
|   4 | Agent-based instrumentation for Java/.NET (inject agent, no code changes)                                                                               |
|   5 | Manual instrumentation for compiled languages (Go, C++), requires code changes and redeployment                                                         |
|   6 | eBPF auto-instrumentation:                                                                                                                              |
|   7 | Runs in the Linux kernel, attaches to runtimes/libraries                                                                                                |
|   8 | Generates metrics and traces without code changes or redeployment                                                                                       |
|   9 | Low latency, fast due to JIT compilation                                                                                                                |
|  10 | Provides improved system-level data, deeper visibility than SDKs                                                                                        |
|  11 | Limitations: generic instrumentation, lacks business-level context, limited distributed tracing, Linux-only, may not work with all languages/frameworks |
|  12 | Grafana BA and OpenTelemetry eBPF Instrumentation (OBI):                                                                                                |
|  13 | Both open source, vendor-neutral, work with any OpenTelemetry or Prometheus collector                                                                   |
|  14 | OBI: application-level RED metrics, partial trace support, network flow metrics                                                                         |
|  15 | BA: all OBI features plus process-level metrics and Grafana Cloud integrations                                                                          |
|  16 | Use cases for improved system-level data:                                                                                                               |
|  17 | More accurate response time measurement compared to SDKs (captures kernel/network queuing)                                                              |
|  18 | Detection of hidden network traffic, including unsupported protocols                                                                                    |
|  19 | Visualization of network flows with source/destination metadata, useful for cost analysis (e.g., inter-AZ traffic)                                      |
|  20 | DNS tracing for troubleshooting DNS issues                                                                                                              |
|  21 | OBI can be used alongside SDKs; not a replacement but a complementary solution                                                                          |
|  22 | Ongoing/future work: better integration with SDKs and profiler, more protocol support, improved trace propagation                                       |
|  23 | OBI can detect and avoid duplicate instrumentation if SDKs are present                                                                                  |
|  24 | Performance impact: typically <1% CPU, up to 2-3% under high load                                                                                       |
|  25 | Works on Alpine Linux                                                                                                                                   |
|  26 | Deployment: runs as a daemonset on the node (instruments all pods/services) or as a s                                                                   |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=pfBw4g1LdAM)