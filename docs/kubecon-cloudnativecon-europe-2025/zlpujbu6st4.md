---
type: Video Note
title: "Orchestrating AI Models in Kubernetes: Deploying Ollama as a Nati... Samuel Veloso & Lucas Fernández"
description: "Samuel Beloso from Cast AI and Lucas from Red Hat discuss deploying Olama, a native container runtime, in Kubernetes. They explore how to run models locally with Olama and deploy it in a Kubernetes-native way using a custom runtime class. T..."
resource: https://www.youtube.com/watch?v=zLpUJBU6sT4
tags: ["kubecon-cloudnativecon-europe-2025", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

Samuel Beloso from Cast AI and Lucas from Red Hat discuss deploying Olama, a native container runtime, in Kubernetes.
They explore how to run models locally with Olama and deploy it in a Kubernetes-native way using a custom runtime class.
The process involves creating a custom runtime class that uses the containerd library, implementing the TTRPC task interface, and registering the runtime class with containerd.
They also demonstrate how to integrate this with QFlow, a CNCF project for ML workflows, by deploying everything into QFlow with a modular architecture.
# Main Points

|   # | Main point |
| --: | ---------- |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=zLpUJBU6sT4)