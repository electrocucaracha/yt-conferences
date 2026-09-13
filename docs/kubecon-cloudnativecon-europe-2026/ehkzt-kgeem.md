---
type: Video Note
title: "Retroactive Sampling with OpenTelemetry: Cut 90% Distributed Traci... Roman Khavronenko & Zhu Jiekun"
description: "In this session, Shu-Jie Khun and Roman Khvoroenkov from VictoriaMetrics introduced the concept of retroactive sampling in OpenTelemetry as a way to reduce the costs associated with distributed tracing. They explained the challenges of trad..."
resource: https://www.youtube.com/watch?v=ehKzt_kGEeM
tags: ["kubecon-cloudnativecon-europe-2026", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

In this session, Shu-Jie Khun and Roman Khvoroenkov from VictoriaMetrics introduced the concept of retroactive sampling in OpenTelemetry as a way to reduce the costs associated with distributed tracing.
They explained the challenges of traditional head and tail sampling methods, particularly the high memory, CPU, and network overhead of tail sampling, which requires collecting and buffering all spans before making sampling decisions.
Retroactive sampling addresses these issues by extracting only key information needed for sampling decisions, sending minimal data to a centralized sampling server, and buffering full spans locally until a decision is made, thus significantly reducing network traffic and resource usage.
Benchmark results showed that retroactive sampling can cut network traffic by 70% and lower CPU and memory consumption compared to tail sampling, with only a modest increase in disk usage.
The speakers also discussed trade-offs, such as limitations when sampling based on many attributes, and answered questions about implementation details, emphasizing their intent to open source their solution and inviting community feedback.
# Main Points

|   # | Main point                                                                                                                                           |
| --: | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Presentation on retroactive sampling in OpenTelemetry to reduce distributed tracing costs                                                            |
|   2 | Speakers: Shu-Jie Khun (Software Engineer) and Roman Khvoroenkov (Engineering Manager) from VictoriaMetrics                                          |
|   3 | VictoriaMetrics provides open-source metrics, logs, and traces solutions                                                                             |
|   4 | Agenda: overview of distributed tracing, cost issues, head vs. tail sampling, retroactive sampling concept, benchmarks, trade-offs, and alternatives |
|   5 | Distributed tracing tracks requests across microservices using spans and traces                                                                      |
|   6 | Spans are expensive (~1KB each), making tracing resource-intensive (network, compute, storage)                                                       |
|   7 | Head sampling: first service decides to sample or not; efficient but lacks future context                                                            |
|   8 | Tail sampling: all spans sent to collector, which samples after receiving all data; accurate but high memory, network, and scaling costs             |
|   9 | Tail sampling requires time windows, load balancing by trace ID, and can cause high cross-region network traffic                                     |
|  10 | Most traces are uninteresting; only a small fraction are needed                                                                                      |
|  11 | Retroactive sampling aims to reduce unnecessary network traffic by sending only key span info to the sampling server                                 |
|  12 | Local agents buffer spans, extract key info, send to sampling server, receive sampling decisions, and forward only sampled traces to backend         |
|  13 | Sampling server buffers minimal data, makes decisions, and communicates results to agents                                                            |
|  14 | Benchmarks: retroactive sampling reduces network traffic by 70% compared to tail/no sampling; sampling results are consistent                        |
|  15 | Retroactive sampling uses 60-70% less CPU/memory than tail sampling; disk usage is minimal and trades off for memory                                 |
|  16 | Trade-offs: limited if sampling requires many attributes; local agents can make decisions for complex cases                                          |
|  17 | FIFO queues used instead of databases to avoid lookups and random IO                                                                                 |
|  18 | Custom protocol used between agents and sampling server; OTLP used for exporting sampled traces                                                      |
|  19 | Approach currently groups by trace ID; may not support span links across traces                                                                      |
|  20 | Plan to open sour                                                                                                                                    |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=ehKzt_kGEeM)