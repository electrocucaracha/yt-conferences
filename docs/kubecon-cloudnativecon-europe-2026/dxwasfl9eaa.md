---
type: Video Note
title: "Route, Serve, Adapt, Repeat: Adaptive Routing for AI Inference Workl... Nir Rozenbaum & Kellen Swain"
description: "In this talk, Kellen, a software engineer at Google, introduces adaptive routing for AI inference within the inference gateway, focusing on improving how requests are routed to model servers. The current system leverages L7 proxies like Env..."
resource: https://www.youtube.com/watch?v=DxWAsFl9EAA
tags: ["kubecon-cloudnativecon-europe-2026", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

In this talk, Kellen, a software engineer at Google, introduces adaptive routing for AI inference within the inference gateway, focusing on improving how requests are routed to model servers.
The current system leverages L7 proxies like Envoy to inspect request bodies and uses a pluggable framework for routing decisions based on various scores, such as prefix matching and server load.
However, manual tuning of these scores can lead to issues like the thundering herd problem, where certain servers become overloaded.
To address this, the team developed adaptive routing, which dynamically adjusts the weighting between affinity-based and distribution-based scores using asynchronous detectors and an adaptive configurator, ensuring better load balancing without user intervention.
Initial benchmarks show that adaptive routing mitigates hot node issues and maintains baseline performance, and the team is exploring further enhancements, including predictive latency and flow control, while inviting community contributions.
# Main Points

|   # | Main point                                                                                                                                                 |
| --: | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Talk focuses on adaptive routing for AI inference in inference gateway (gateway inference extension).                                                      |
|   2 | Inference routing requires inspecting request body for prompt content or model name.                                                                       |
|   3 | Envoy L7 proxy is used for its XROC capabilities and global model server state view.                                                                       |
|   4 | Inference gateway adds an extension protocol to provide routing hints based on request content.                                                            |
|   5 | Endpoint picker service analyzes request and suggests routing based on filters and scoring plugins.                                                        |
|   6 | Filters can prioritize requests (e.g., high-priority customers, specific hardware).                                                                        |
|   7 | Scoring plugins evaluate model servers on metrics like QEP, KV cache utilization, and prompt prefix match.                                                 |
|   8 | Routing algorithms include max score, weighted random, and power-of-two/epsilon greedy.                                                                    |
|   9 | Prefix-aware routing enables performance gains by leveraging shared prompt prefixes, reducing prefill time and resource usage.                             |
|  10 | Benchmarks show significant improvements in output tokens per second and time to first token (TTFT) for prefill-heavy workloads.                           |
|  11 | Current issues: manual score weighting can cause thundering herd problem and overload single model servers; end users shouldn't need to tune weights.      |
|  12 | Adaptive routing categorizes scores into affinity (e.g., prefix match) and distributive (e.g., load, utilization).                                         |
|  13 | Adaptive routing dynamically adjusts score weights based on pool imbalance, favoring distribution when imbalance is high.                                  |
|  14 | Two core components: async detector (calculates pool state, e.g., imbalance) and adaptive configurator (adjusts scorer weights based on detector signals). |
|  15 | Async detector is asynchronous, rate-limited, and produces smoothed signals between 0 and 1.                                                               |
|  16 | Imbalance detector uses endpoint metrics to emit imbalance signals.                                                                                        |
|  17 | Adaptive configurator reallocates scorer weights based on signals, using monotonic translation (e.g., sigmoid function).                                   |
|  18 | Benchmarks show adaptive routing mitigates thundering herd problem and maintains baseline performance.                                                     |
|  19 | Adaptive routing is fully async,                                                                                                                           |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=DxWAsFl9EAA)