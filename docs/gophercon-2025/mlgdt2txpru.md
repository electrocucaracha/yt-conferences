---
layout: default
title: "GopherCon 2025: Supercharging ML Pipelines with Go - Vaidehi Thete"
nav_order: 3
parent: GopherCon 2025
type: Video Note
description: "Vide, a machine learning engineer at The New York Times, explains how the team leveraged Go to streamline machine learning inference pipelines by utilizing interprocess communication via shared mem..."
resource: "https://www.youtube.com/watch?v=mLGDT2TxPrU"
youtube_stats:
  view_count: 1716
  like_count: 43
  channel_subscriber_count: 41100
tags:
  - gophercon-2025
  - video
  - learning
status: stable
generated:
  by: process:yt-summarizer-okf
  at: 2026-11-21T05:22:37+00:00
---

# Summary

Vide, a machine learning engineer at The New York Times, explains how the team leveraged Go to streamline machine learning inference pipelines by utilizing interprocess communication via shared memory.
The platform, built-in Go for its concurrency and type safety, hosts various models to drive user engagement, manage paywalls, and power targeted email campaigns.
To integrate a Python-based ranking model into this Go-centric infrastructure, the team adopted a separation of concerns approach, using shared memory regions to facilitate high-speed data transfer between the Go service and the inference server.
By batching multi-dimensional tensors and writing them to shared memory, the system efficiently processes over 40 million user-content recommendations, reducing the time to generate email cohorts from hours to minutes.
This architecture ensures data integrity through checksums and allows for rapid prototyping and scaling, ultimately enabling the successful launch of targeted email programs and supporting future multi-variant model experiments.

# Main Points

|   # | Main point                                                                                                                                                      |
| --: | --------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | The New York Times machine learning platform team uses Go to productionize models for real-time, low-latency inference with high fault tolerance.               |
|   2 | The platform supports various use cases, including article recommendations, paywall optimization, subscriber retention, and targeted email campaigns.           |
|   3 | Targeted emails identify user bases for specific content to boost on-site traffic and engagement by sending curated messages.                                   |
|   4 | The system generates over 40 million user-content recommendations by deploying multiple replicas of recommendation services to avoid compute bottlenecks.       |
|   5 | A second ranking model aggregates these recommendations to curate specific user audiences for each content ID.                                                  |
|   6 | The ranking model is written in Python by data scientists, while the platform infrastructure is built-in Go.                                                    |
|   7 | Guiding principles for integration include separation of concerns, fast data stream processing with integrity, and system resilience through stateless ranking. |
|   8 | The solution leverages interprocess communication via shared memory, allowing two processes on the same machine to access the same RAM address space.           |
|   9 | Go simplifies shared memory setup by initializing file objects, setting sizes, and mapping memory regions with minimal code.                                    |
|  10 | Data is written to shared memory using native Go copy methods while tracking address space size to prevent storage issues.                                      |
|  11 | Reading from shared memory involves iterating through byte streams to reconstruct integer representations.                                                      |
|  12 | The ranking model is hosted behind NVIDIA Triton, an open-source inference serving software, which communicates with the Go application via shared memory.      |
|  13 | Data is structured as tensors, which are multi-dimensional arrays of numerical values, packed onto shared memory regions.                                       |
|  14 | The recommendation system output comprises four distinct tensors with varying dimensions and types, such as int64, float32, and int8.                           |
|  15 | Each user record occupies approximately 57 bytes, requiring the writing of 40 million records to shared memory in a real-time stream.                           |
|  16 | Tensors are batched by type rather than end-to-end records to capitalize on high throughput and ensure predictability.                                          |
|  17 | Data integrity is validated by comparing checksums of batches before they are passed to shared memory.                                                          |
|  18 | The Go service uses worker pools and channels to distribute tasks across goroutines for populating shared memory regions.                                       |
|  19 | Benchmarking shows that writing over 40 million records or 4 GB of data takes approximately 50 seconds, allowing for quick restarts after failures.             |
|  20 | The system deploys two processes as containers within a Kubernetes pod with a shared memory volume mount.                                                       |
|  21 | Triton handles reading input tensors from shared memory and writing output tensors, requiring no additional code from data scientists or platform engineers.    |
|  22 | The Go service reads the output tensors, adds business logic metadata, and sends the results to downstream services for email dispatch.                         |
|  23 | Go interfaces facilitated rapid prototyping with in-memory implementations before integrating production services.                                              |
|  24 | The new pipeline reduced cohort generation time from hours to minutes, leading to increased active users and clicks.                                            |
|  25 | Future plans include launching a multi-variant version of the service to concurrently test multiple ranking models for experimentation.                         |

# Video

[![Video thumbnail](https://img.youtube.com/vi/mLGDT2TxPrU/hqdefault.jpg)](https://www.youtube.com/watch?v=mLGDT2TxPrU)

[Watch on YouTube](https://www.youtube.com/watch?v=mLGDT2TxPrU)
