---
layout: default
title: Sustainable Cloud Operations  Kubernetes is the GreenOps Framework You're Looking For
nav_order: 130
parent: OpenInfra Summit Europe 2025
type: Video Note
description: "A company from northern Italy has developed an open-source software application called Cartel, which applies DevOps methodologies to infrastructure automation and GreenOps practices to reduce carbo..."
resource: "https://www.youtube.com/watch?v=2ixv34R5YLw"
youtube_stats:
  view_count: 36
  channel_subscriber_count: 46800
tags:
  - openinfra-summit-europe-2025
  - video
  - learning
status: stable
generated:
  by: process:yt-summarizer-okf
  at: 2026-11-22T23:38:50+00:00
---

# Summary

A company from northern Italy has developed an open-source software application called Cartel, which applies DevOps methodologies to infrastructure automation and GreenOps practices to reduce carbon emissions.
The solution addresses the lack of visibility in resource usage by providing instant feedback on infrastructure efficiency, similar to how electric vehicles display driving efficiency metrics.
By leveraging Kubernetes, Prometheus, and Open Policy Agent, the system creates a closed-loop optimization process that continuously monitors resource consumption and grid carbon intensity data.
Key strategies include right-sizing virtual machines to prevent waste, automatically powering down unused development and test environments, and implementing geo-temporal shifting to run workloads when renewable energy sources are most abundant.
This approach not only reduces carbon emissions by approximately 13% through temporal shifting but also lowers operational costs, demonstrating a significant overlap between financial efficiency and environmental sustainability in infrastructure management.

# Main Points

|   # | Main point                                                                                                                                                            |
| --: | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | The company develops an open-source software application called Cartel that brings DevOps methodologies to infrastructure automation.                                 |
|   2 | The primary goal is to automate and compose actions on infrastructure, such as creating virtual machines or pipelines, rather than focusing solely on applications.   |
|   3 | GreenOps focuses on using energy efficiently, avoiding resource waste, and utilizing resources when grid energy is green.                                             |
|   4 | Visibility is identified as the starting point for efficiency, analogous to leaving lights on during a vacation or using an electric vehicle's efficiency gauge.      |
|   5 | Instant feedback on infrastructure usage, similar to a car's driving style indicator, encourages more efficient resource management without requiring complex AI.     |
|   6 | Cost reduction is a key driver for change in companies, and PhOps and GreenOps practices overlap significantly in improving infrastructure efficiency.                |
|   7 | The solution involves scaling infrastructure, decreasing hardware provisioning, and turning off unused development or test environments to save money and energy.     |
|   8 | The architecture uses Kubernetes as the backend, with declarative custom resources and operators to provision environments and monitoring.                            |
|   9 | Metrics are collected from resources, and carbon intensity data is gathered based on the location of on-premises or cloud data centers.                               |
|  10 | Open Policy Agent (OPA) policies are used to compute optimizations and apply them back to custom resources, creating a closed-loop optimization system.               |
|  11 | Right-sizing is the first step, where monitoring identifies wasted resources, such as oversized virtual machines, allowing for reduction or reallocation.             |
|  12 | Unused infrastructure, particularly development and testing environments running 24/7, should be turned off during nights and weekends to save costs and electricity. |
|  13 | Geo-shift involves moving workloads to locations with lower grid carbon intensity, such as regions with nuclear power, to reduce emissions.                           |
|  14 | Temporal shift involves delaying workloads to times when cleaner energy, such as solar power, is available, which can reduce carbon emissions by approximately 13%.   |
|  15 | The approach is not limited to Kubernetes and can interact with virtual machines on Azure or AWS through OPA policies.                                                |
|  16 | Carbon intensity data is sourced from Electricity Map, providing regional data updated every five minutes, combined with public data center locations.                |
|  17 | Tiny Time Mixers (TTMs) are used as efficient inference models to forecast future grid carbon intensity for optimization purposes.                                    |
|  18 | A scientific paper detailing the collaboration with the University of Torino and the Cartel platform is under review, with a preprint available.                      |

# Video

[![Video thumbnail](https://img.youtube.com/vi/2ixv34R5YLw/hqdefault.jpg)](https://www.youtube.com/watch?v=2ixv34R5YLw)

[Watch on YouTube](https://www.youtube.com/watch?v=2ixv34R5YLw)
