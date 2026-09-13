---
type: Video Note
title: "Optimizing Model Serving on Kubernetes With Model Streaming - Ekin Karabulut & Ronen Dar, Run:ai"
description: "The speaker discusses optimizing model serving inference on a Kubernetes cluster with model weight streaming. They introduce Rani Model Weight Streamer, an open-source project that accelerates the process of loading model weights onto GPUs..."
resource: https://www.youtube.com/watch?v=qH5djJlbodY
tags: ["kubecon-cloudnativecon-europe-2025", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

The speaker discusses optimizing model serving inference on a Kubernetes cluster with model weight streaming.
They introduce Rani Model Weight Streamer, an open-source project that accelerates the process of loading model weights onto GPUs from various storage types.
The streamer uses concurrency and adjustable parameters to balance workload distribution, which is crucial for optimal performance.
Benchmarks show significant improvements in loading times, especially when using high-performance storage like SSDs or S3.
The speaker highlights the importance of considering storage bandwidth and practical limits, as well as the need for a cooldown period between cloud tests.
Future versions will support sharded models, multi-GPU model loading, parallel file loading, and GPU direct storage, with promising results from collaborations with GKE teams.
# Main Points

|   # | Main point |
| --: | ---------- |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=qH5djJlbodY)