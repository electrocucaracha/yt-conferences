---
layout: default
title:
  "SIG-Node: Intro and Deep Dive - Sergey Kanzhelev, Google; Francesco Romani
  & Peter Hunt, Red Hat"
nav_order: 293
parent: Kubecon Cloudnativecon Europe 2025
type: Video Note
description: Here is a summary of the video transcript in 3-5 sentences.
resource: https://www.youtube.com/watch?v=7sr1eHJBXKs
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

Here is a summary of the video transcript in 3-5 sentences: Sergey Kangel from Google and Peter Hunt from Red Hat discuss the Sign Node project, which aims to improve resource management in Kubernetes.
They cover various topics, including resource allocation, device plug-in, DRA (Device Request Allocation), and CPU manager policies.
The team has made significant progress on these fronts, with features like in-place pod resize, structured parameters, and improved container stop signals.
They also discuss the challenges of managing resources efficiently and securely, particularly when it comes to devices and confidential containers.

# Main Points

|   # | Main point                                                                                                                                         |
| --: | -------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Sign Node is a part of Kubernetes that manages resources and provides features like admission control, resource allocation, and device management. |
|   2 | The goal of Sign Node is to provide a more efficient and scalable way to manage resources in Kubernetes.                                           |
|   3 | There are currently 24 caps (capabilities) being worked on for Sign Node, including:                                                               |
|   4 | In-place pod resize                                                                                                                                |
|   5 | Sidecar cars                                                                                                                                       |
|   6 | Structured parameters                                                                                                                              |
|   7 | CPU resource policy                                                                                                                                |
|   8 | VPA (Virtual Pod Autoscaling)                                                                                                                      |
|   9 | Confidential containers and rootless notes                                                                                                         |
|  10 | The team is working to improve the expressiveness of resource requests and make it easier for users to define their requirements.                  |
|  11 | There are plans to make Sign Node more modular and pluggable, allowing users to experiment with different allocation strategies.                   |
|  12 | The team is also working on improving the security features of Sign Node, including image verification and secure container execution.             |
|  13 | Users can help by providing feedback, attending meetings, and contributing to the development of Sign Node.                                        |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=7sr1eHJBXKs)
