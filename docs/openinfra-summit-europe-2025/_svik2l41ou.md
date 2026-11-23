---
layout: default
title: "Expanded Blueprint: Best Practice Reference Architecture for AI-enabled Workloads"
nav_order: 131
parent: OpenInfra Summit Europe 2025
type: Video Note
description: "Niels Maukner, a principal cloud architect at Open Telekom Cloud, presented a conceptual framework for standardizing an AI-enabled infrastructure stack based on Linux, OpenStack, Kubernetes, and AI..."
resource: "https://www.youtube.com/watch?v=_sViK2l41oU"
youtube_stats:
  view_count: 32
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

Niels Maukner, a principal cloud architect at Open Telekom Cloud, presented a conceptual framework for standardizing an AI-enabled infrastructure stack based on Linux, OpenStack, Kubernetes, and AI components.
He argued that while the diversity of cloud providers creates interoperability challenges due to differing authentication methods and resource semantics, a unified platform layer like Kubernetes can help abstract these infrastructure differences.
Maukner suggested that AI could be leveraged to standardize container building practices and repository structures, addressing the current lack of consensus in best practices for application packaging.
Drawing a parallel to the historical LAMP stack, he proposed a modern equivalent that simplifies complex configuration choices by relying on sensible defaults, allowing developers to focus on application logic rather than infrastructure management.
The presentation concluded with the recommendation to embrace default configurations and make firm decisions to avoid being overwhelmed by the excessive number of available options in the current cloud and AI landscape.

# Main Points

|   # | Main point                                                                                                                                                                |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | The speaker, Niels Maukner from Open Telekom Cloud, presents a requirements engineering path for a standardized AI-enabled stack rather than a finished product.          |
|   2 | The original goal was to extend a white paper on reference architectures to include AI, aiming for a standard stack based on Linux, OpenStack, and Kubernetes.            |
|   3 | Standardization is valuable for users because it allows recycling of previous work and ensures interoperability across different cloud providers.                         |
|   4 | Many cloud providers, including OTC, Clara, SysEleven, OVH, and Stackit, run on OpenStack, demonstrating the platform's adaptability from private to large public clouds. |
|   5 | Moving applications between OpenStack-based clouds is often complex due to differences in authentication methods, resource labeling, and flavor semantics.                |
|   6 | In multi-cloud scenarios, users must solve the same problems multiple times, such as adapting to different object store implementations like Swift versus S3.             |
|   7 | Diversity in cloud implementations is a strength of the landscape, but it requires tools to select available features and manage differences effectively.                 |
|   8 | Using the platform layer, such as Kubernetes, as a unification layer can abstract hardware and IaaS resources, potentially simplifying deployments.                       |
|   9 | It is unclear if fine-grained resource selectors are necessary for real-world workloads or if simpler Kubernetes deployment definitions suffice.                          |
|  10 | Containers are powerful but often misunderstood, leading to poor reusability; there is a need for defined best practices to standardize container structure.              |
|  11 | Git repositories lack a strictly enforced standard format, making it difficult to understand build processes without extensive documentation.                             |
|  12 | AI could be utilized to define and specify container packaging based on recommended target pictures, though this idea requires further development.                       |
|  13 | The software lifecycle involves build pipelines and container registries, with GitOps principles connecting repositories to DevOps methodologies.                         |
|  14 | The concept of a modern LAMP stack is proposed, evolving into a stack of Linux, OpenStack, Kubernetes, Infrastructure, and AI.                                            |
|  15 | Linux is self-adaptable with few configuration needs, while OpenStack setup lacks agreed best practices, with various installation methods like Colossus or packages.     |
|  16 | Kubernetes offers a unified description model but remains complex, with ongoing debates about its relationship with OpenStack.                                            |
|  17 | Infrastructure solutions for networking and storage are relatively settled, whereas AI lacks consensus due to its novelty and rapid evolution.                            |
|  18 | For AI integration, the speaker suggests starting with simple open-source models to design applications, allowing for easy model replacement later.                       |
|  19 | Users must address the indeterminism of AI when using it as a feature for workload definition.                                                                            |
|  20 | The summary emphasizes embracing default configurations and being humble with assumptions while being firm with decisions to avoid drowning in options.                   |

# Video

[![Video thumbnail](https://img.youtube.com/vi/_sViK2l41oU/hqdefault.jpg)](https://www.youtube.com/watch?v=_sViK2l41oU)

[Watch on YouTube](https://www.youtube.com/watch?v=_sViK2l41oU)
