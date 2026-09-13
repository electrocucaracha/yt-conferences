---
type: Video Note
title: "Taking Care of Your Control Plane With API Priority and Fairness an... Matteo Ruina & Ayaz Badouraly"
description: "The speaker, Mateo, discusses the importance of taking care of the Kubernetes control plane and shares two techniques: API Priority and Fairness (APF) and Resource Quota. APF helps prevent a single user from affecting the stability of the p..."
resource: https://www.youtube.com/watch?v=c73SzCKx-OY
tags: ["kubecon-cloudnativecon-europe-2025", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

The speaker, Mateo, discusses the importance of taking care of the Kubernetes control plane and shares two techniques: API Priority and Fairness (APF) and Resource Quota.
APF helps prevent a single user from affecting the stability of the platform by prioritizing requests based on their priority level.
However, it can be challenging to configure and may not work as expected in certain scenarios.
Resource Quota provides a more robust solution by limiting the consumption of resources per namespace, allowing for better scalability and resource management.
The speaker shares his team's experience with implementing these techniques, including challenges and lessons learned, and emphasizes the importance of continuous monitoring and improvement to ensure optimal performance and reliability of the Kubernetes control plane.
# Main Points

|   # | Main point |
| --: | ---------- |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=c73SzCKx-OY)