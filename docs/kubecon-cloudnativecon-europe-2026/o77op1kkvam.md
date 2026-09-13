---
layout: default
title:
  To Upstream or Not? Why Becoming the Maintainer of Your Dependencies Matters
  - Christos Markou
nav_order: 374
parent: Kubecon Cloudnativecon Europe 2026
type: Video Note
description:
  Christo Marco, a software engineer at Elastic and maintainer in the OpenTelemetry
  project, discusses the importance of becoming maintainers of open source dependencies,
  especially for companies that rely heavily on such projects. He highlig...
resource: https://www.youtube.com/watch?v=O77op1kKvaM
tags:
  - kubecon-cloudnativecon-europe-2026
  - video
  - learning
status: stable
generated:
  by: process:yt-conferences-okf
  at: 2026-09-12 00:00:00+00:00
---

# Summary

Christo Marco, a software engineer at Elastic and maintainer in the OpenTelemetry project, discusses the importance of becoming maintainers of open source dependencies, especially for companies that rely heavily on such projects.
He highlights how open source technologies underpin much of the digital world, yet are often maintained by a small group of individuals, which can lead to issues if projects become understaffed, as seen with the deprecation of the Kubernetes ingress-nginx project.
Using the analogy of an open source garden, Marco explains the roles of maintainers, vendors, and community users, emphasizing the need for proper governance, transparency, and collaboration.
He shares a real-world example involving the OpenTelemetry Collector and Kubernetes events, illustrating how active upstream involvement allowed his team to resolve technical debt and improve both the upstream project and their downstream distribution, ultimately benefiting users, maintainers, and vendors alike.
Marco concludes by encouraging organizations to invest in open source maintenance, start small, build trust within the community, and contribute meaningfully, as this collective effort ensures the sustainability and success of open source projects.

# Main Points

|   # | Main point                                                                                                                                                       |
| --: | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | The talk addresses why becoming maintainers of open source dependencies is important.                                                                            |
|   2 | Open source technologies underpin much of the digital world and rely on global contributors.                                                                     |
|   3 | Many critical projects are maintained by a small number of people, sometimes leading to issues if not well-staffed.                                              |
|   4 | Example: The Kubernetes ingress-nginx project was deprecated due to lack of maintainers, causing migration pain for users.                                       |
|   5 | Stakeholders in open source include companies/vendors, maintainers, and community users.                                                                         |
|   6 | Companies often hire maintainers to ensure project health and influence roadmaps, but governance and transparency are essential.                                 |
|   7 | Maintainers have long-term technical ownership, approve/review/reject changes, and ensure quality and accountability.                                            |
|   8 | Community users provide feedback, report bugs, and influence project relevance through their needs and trust.                                                    |
|   9 | Successful open source projects require alignment among maintainers, users, and vendors.                                                                         |
|  10 | The "open source garden" analogy illustrates shared responsibility and governance in open source.                                                                |
|  11 | Vendors cannot bypass processes for their own needs; they must follow established rules.                                                                         |
|  12 | OpenTelemetry is a major CNCF project for vendor-neutral telemetry collection.                                                                                   |
|  13 | The OpenTelemetry Collector is a vendor-neutral agent; vendors often create their own distributions.                                                             |
|  14 | Elastic’s distribution (edot collector) is downstream from the upstream collector and includes upstream components.                                              |
|  15 | A real-world issue arose around collecting Kubernetes events using two components: k8s_events_receiver (specific) and k8s_object_receiver (generic).             |
|  16 | The team chose the generic component due to planned deprecation of the specific one, but deprecation stalled, causing confusion and extra maintenance for users. |
|  17 | As a code owner, the speaker investigated, engaged with maintainers, and helped resolve the issue by keeping both components and improving guidance.             |
|  18 | Downstream, Elastic customers faced visualization issues; switching b                                                                                            |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=O77op1kKvaM)
