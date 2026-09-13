---
layout: default
title:
  Extending Kubernetes for AI | Lessons Learned From Platform... - Susan, Lucy,
  Andrea, Etienne, Tim
nav_order: 93
parent: Kubecon Cloudnativecon Europe 2025
type: Video Note
description:
  The panel discussion focuses on extending Kubernetes for AI workloads,
  with experts from Google Cloud, Uber, and Overstory sharing their experiences and
  insights. They discuss the challenges of managing stateful loads, such as databases,
  an...
resource: https://www.youtube.com/watch?v=d9K5PSsHtDg
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

The panel discussion focuses on extending Kubernetes for AI workloads, with experts from Google Cloud, Uber, and Overstory sharing their experiences and insights.
They discuss the challenges of managing stateful loads, such as databases, and the importance of dynamic resource allocation to optimize GPU utilization.
The panelists also touch on the need for more checkpointing and disruption tolerance in batch training, particularly with expensive GPUs.
They share their strategies for making compute choices, including using specialized compute variations and collocation to improve resource overcommitting.

# Main Points

|   # | Main point                                                                                                                                                                    |
| --: | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Susan Woo is a product manager at Google Cloud, focusing on cloud networking, GKE networking, and network security.                                                           |
|   2 | The panel discussion focuses on extending Kubernetes for AI workloads.                                                                                                        |
|   3 | Weeb8's Lucy explains that they use a stateless compute platform to deploy services, with a team of engineers building platforms for deployment and data pipeline management. |
|   4 | Uber's Andrea discusses using satellite images to prevent wildfires, utilizing Google Cloud and GKE for risk assessment and data processing.                                  |
|   5 | Skidmd's Tim Wickberg talks about in-place pod vertical scaling, allowing for dynamic resource allocation and improved AI workloads.                                          |
|   6 | Overstory's Andrea mentions the importance of checkpointing and disruption tolerance in GPU management, as GPUs are expensive and finite resources.                           |
|   7 | The panelists discuss compute choices, including using specialized compute like GPUs and TPUs, and collocation to improve resource overcommitting.                            |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=d9K5PSsHtDg)
