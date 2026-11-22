---
layout: default
title: "Lightning Talk: Introducing LLM Instance Gateways for Efficient I... Abdel Sghiouar & Daneyon Hansen"
nav_order: 4
parent: "Cloud Native & Kubernetes AI Day 2025 - Europe"
type: Video Note
description: "The Gateway API Inference Extension is a new initiative designed to address the unique challenges of LLM traffic, which differs from standard web traffic due to larger request sizes, longer process..."
resource: "https://www.youtube.com/watch?v=UbJdAlyefow"
youtube_stats:
  view_count: 501
  like_count: 6
  channel_subscriber_count: 141000
tags:
  - cloud-native-kubernetes-ai-day-2025-europe
  - video
  - learning
status: stable
generated:
  by: process:yt-summarizer-okf
  at: 2026-11-15T17:34:27+00:00
---

# Summary

The Gateway API Inference Extension is a new initiative designed to address the unique challenges of LLM traffic, which differs from standard web traffic due to larger request sizes, longer processing times, and the need for specific caching techniques.
Presented by engineers from Google and Solo.io, the extension introduces new resources such as the InferencePool and InferenceModel to manage inference workloads, abstracting hardware resources like GPUs and enabling model-aware routing based on the model name found in the request body.
A key component is the endpoint selection extension, or endpoint picker, which acts as a separate service that receives live metrics from model server pods to make intelligent routing decisions, supporting use cases like serving priority and canary rollouts.
The system utilizes a persona-based permission model, distinguishing between platform admins who manage the inference pool and workload owners who define the target models.
Finally, the presenters highlighted that while the current endpoint picker relies on metrics like KV cache utilization rather than prompt content, the architecture is designed to be pluggable and extensible to accommodate future requirements for deeper context-aware scheduling.

# Main Points

|   # | Main point                                                                                                                                                                                 |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   1 | The Gateway API is the next-generation ingress API introduced in 2019 to address limitations of the previous Ingress API, such as the lack of a permission model and separation of duties. |
|   2 | Gateway API separates the load balancer definition (Gateway) from routing rules (HTTP, TCP, and UDP routes), allowing resources to be defined in different namespaces.                     |
|   3 | LLM inference traffic differs from standard web traffic due to larger request and response sizes, longer processing times, and the prevalence of streaming responses.                      |
|   4 | Inference caching is critical for LLMs because repeated or similar prompts often yield the same responses, unlike typical web application traffic.                                         |
|   5 | The Inference Extension is a Gateway API extension designed to support inference traffic by providing specific APIs for routing decisions and reference implementations.                   |
|   6 | Inference is analogous to a web server for LLMs, requiring a server to process prompts and return standardized responses via REST or gRPC.                                                 |
|   7 | Key use cases for the Inference Extension include model-aware routing based on the model name in the request body, serving priority for different models, and managing model rollouts.     |
|   8 | The project introduces new personas: the Inference Platform Owner manages the InferencePool, while the Inference Workload Owner manages the InferenceModel.                                |
|   9 | The InferencePool resource abstracts hardware resources like GPUs and groups model server pods using label selectors and target ports.                                                     |
|  10 | The InferenceModel resource allows workload owners to define target models and configure traffic splitting or canary rollouts based on weights.                                            |
|  11 | The endpoint selection extension, or endpoint picker, runs as a separate pod and service to make intelligent routing decisions for inference requests.                                     |
|  12 | The gateway forwards inference requests to the endpoint picker, which determines the optimal backend endpoint based on live metrics from model server pods.                                |
|  13 | The endpoint picker utilizes metrics such as KV cache utilization and loaded fine-tuned adapters to formulate scheduling decisions.                                                        |
|  14 | A consistent set of metrics is defined for various model server frameworks like Triton and vLLM to ensure uniform scheduling logic.                                                        |
|  15 | The endpoint picker currently uses metrics pulled from endpoints for scheduling and does not analyze the content of the prompt for routing decisions.                                      |
|  16 | Future developments may include making the scheduler pluggable to integrate external systems for KV cache awareness or extending the endpoint picker to consider input context.            |
|  17 | Benchmark testing results for the Inference Extension are detailed in a Kubernetes blog post and available on the project site.                                                            |
|  18 | Users are encouraged to engage with the project by scanning a provided QR code, opening issues, or contributing ideas to the repository.                                                   |

# Video

[![Video thumbnail](https://img.youtube.com/vi/UbJdAlyefow/hqdefault.jpg)](https://www.youtube.com/watch?v=UbJdAlyefow)

[Watch on YouTube](https://www.youtube.com/watch?v=UbJdAlyefow)
