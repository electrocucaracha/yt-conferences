---
type: Video Note
title: "Lightning Talk: Kueue: Save Some QPS for the Rest of Us! How To Manage 100k Updates Pe... P. Bundyra"
description: "Google engineers have been developing Q, a cloud-native queuing system for AI workloads since 2022. Q acts as a bouncer deciding which job or workload can enter a Kubernetes cluster and cues them accordingly. To expose the queue information..."
resource: https://www.youtube.com/watch?v=njNXlZNT3dw
tags: ["kubecon-cloudnativecon-europe-2025", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

Google engineers have been developing Q, a cloud-native queuing system for AI workloads since 2022.
Q acts as a bouncer deciding which job or workload can enter a Kubernetes cluster and cues them accordingly.
To expose the queue information to users, the team initially considered extending the workload object with its position but found it unsuitable for large-scale use due to API server limitations.
Instead, they used the Kubernetes API aggregation layer to store the order of workloads in Q, leveraging its performance benefits while still relying on CRDs for most logic.
# Main Points

|   # | Main point |
| --: | ---------- |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=njNXlZNT3dw)