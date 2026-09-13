---
type: Video Note
title: "Flip That Stack: Renovating Edge Infrastructure at the Home Depot - Dillon TenBrink, The Home Depot"
description: "Dylan Timberink, a distinguished engineer at The Home Depot, shares insights from building the edge platform that powers the company’s retail experience across over 2,300 locations. He emphasizes the importance of understanding the right ti..."
resource: https://www.youtube.com/watch?v=p5Vca4BoiJw
tags: ["kubecon-cloudnativecon-north-america-2025", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

Dylan Timberink, a distinguished engineer at The Home Depot, shares insights from building the edge platform that powers the company’s retail experience across over 2,300 locations.
He emphasizes the importance of understanding the right timing for transformation, designing specifically for edge constraints rather than simply replicating cloud solutions, and adopting eventual consistency for reliable operations at scale.
Key lessons include reducing developer toil through composable infrastructure and templating, implementing robust data caching and messaging services for offline and resilient operations, and investing early in observability and testability to manage edge cases and system health.
Timberink also highlights ongoing challenges with storage solutions at the edge and stresses the need to actively manage the transition from legacy to new platforms to avoid operational bottlenecks, concluding with encouragement to learn from these experiences and resources like the Edgemonsters working group.
# Main Points

|   # | Main point                                                                                                                                                        |
| --: | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Dylan Timberink, Distinguished Engineer at The Home Depot, shares lessons from building the edge platform powering Home Depot stores.                             |
|   2 | Home Depot is the world’s largest home improvement retailer with over 2,300 locations in North America and a major retail website.                                |
|   3 | The legacy edge platform was store-centric, built for unreliable connectivity and batch data synchronization.                                                     |
|   4 | Retail transformation around 2015-2016 shifted focus from store-centric to customer-centric, driven by omnichannel expectations and agile development needs.      |
|   5 | Hardware and software refresh cycles aligned around 2019, creating an opportunity for a new platform.                                                             |
|   6 | Core design goals: resilient, stable, fit within existing store footprint, real-time observability, support for modern data services, and platform composability. |
|   7 | Edge platform built on Kubernetes, emphasizing composability to allow easy updates and scalability.                                                               |
|   8 | Adopted an eventually consistent, pull-based model (GitOps/Flux) for configuration management, using a templating engine to reduce developer toil.                |
|   9 | Main goals: make developers’ lives easier and provide needed business services.                                                                                   |
|  10 | Introduced a data cache service at the edge for frequently accessed data (e.g., pricing, inventory), supporting offline operation and fast access.                |
|  11 | Messaging service ensures guaranteed delivery of data back to the cloud, focusing on reliability over speed.                                                      |
|  12 | Developed replication tracking and observability tools for real-time fleet visibility and self-service for developers and operators.                              |
|  13 | Created edge test environments for scalable, on-demand testing and troubleshooting.                                                                               |
|  14 | Observability was implemented later than ideal; now provides real-time insights and value-added services.                                                         |
|  15 | Developer experience enhanced with self-service plugins and control planes for deployment visibility.                                                             |
|  16 | Storage at the edge remains a major challenge; most solutions are not edge-optimized.                                                                             |
|  17 | Managing the transformation timeline is critical—actively control migration                                                                                       |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=p5Vca4BoiJw)