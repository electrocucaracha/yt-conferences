---
layout: default
title: Explain How Kubernetes Works With GPU Like I’m 5 - Carlos Santana, AWS
nav_order: 91
parent: Kubecon Cloudnativecon Europe 2025
type: Video Note
description:
  Carlos Santana, a CNCF ambassador, shares his experience of learning
  Kubernetes with GPUs at home using an Nvidia Jetson device. He explains that to
  get started, one needs the device driver, CUDA toolkit, and container toolkit, which
  can be...
resource: https://www.youtube.com/watch?v=bQvrutQO3-c
tags:
  - kubecon-cloudnativecon-europe-2025
  - video
  - learning
status: stable
generated:
  by: process:yt-conferences-okf
  at: 2026-09-12 00:00:00+00:00
---

# Summary

Carlos Santana, a CNCF ambassador, shares his experience of learning Kubernetes with GPUs at home using an Nvidia Jetson device.
He explains that to get started, one needs the device driver, CUDA toolkit, and container toolkit, which can be installed through Helm charts.
The device plug-in is also required for scheduling pods on the GPU.
Carlos demonstrates a setup where he runs a Kubernetes cluster at home with a Jetson device and uses it to deploy a deep learning model.
He emphasizes that while small devices like Jetsons can run models, they may not reach full potential when deployed in the cloud due to quantization.

# Main Points

|   # | Main point |
| --: | ---------- |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=bQvrutQO3-c)
