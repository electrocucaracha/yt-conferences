---
type: Video Note
title: "From Projects to Products: The Sociotechnical Journey Behind Sony... Eugenia Bergman & Hagen Tonnies"
description: "In this talk, the speakers from Sony PlayStation describe their journey in building and scaling an internal cloud platform, highlighting the challenges of moving from a project-oriented to a product-oriented approach. Initially, their platf..."
resource: https://www.youtube.com/watch?v=zrXvt9DXQ3U
tags: ["kubecon-cloudnativecon-europe-2026", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

In this talk, the speakers from Sony PlayStation describe their journey in building and scaling an internal cloud platform, highlighting the challenges of moving from a project-oriented to a product-oriented approach.
Initially, their platform appeared mature but struggled to meet diverse team needs, leading to workarounds and growing backlogs.
As the organization expanded, coordination became complex, prompting them to adopt clearer capability boundaries, modular architecture, and explicit contracts between teams.
They shifted their focus from infrastructure metrics and project completion to user adoption, value delivery, and feedback loops, redefining "done" as delivering integrated, supported, and actually used capabilities.
Ultimately, aligning architectural, organizational, and feedback processes enabled them to transition from simply shipping projects to building a platform as a product, emphasizing continuous learning, clear ownership, and leadership support.
# Main Points

|   # | Main point                                                                                                                             |
| --: | -------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Sony PlayStation's internal cloud platform evolved from supporting a single tenant to multiple internal teams with diverse needs.      |
|   2 | Initial platform appeared mature but backlog kept growing due to varying team requirements and workarounds.                            |
|   3 | Teams often bypassed the platform or requested exceptions, leading to custom deployments and fragmentation.                            |
|   4 | Shifted focus from project-oriented delivery to product-oriented approaches, emphasizing customer needs and user experience.           |
|   5 | Platform team lacked dedicated product managers, requiring engineers to empathize with users directly.                                 |
|   6 | Platform started as a simple internal runtime for the game streaming service, managed by cross-functional teams.                       |
|   7 | As more teams onboarded, demands became unpredictable and complex, with different workloads, security needs, and Kubernetes maturity.  |
|   8 | Tension arose between teams wanting direct infrastructure control and the platform team's push for abstraction and standardization.    |
|   9 | Traditional yearly project planning cycles became misaligned with the fast-changing environment and growing complexity.                |
|  10 | Accumulated a mix of modern and legacy systems, increasing operational challenges.                                                     |
|  11 | Sought external knowledge from books and industry experts but found practical steps lacking.                                           |
|  12 | Emphasized the importance of reconciliation loops, controller patterns, and clear component boundaries to manage drift and complexity. |
|  13 | Highlighted the need for multi-tenancy, cost-effectiveness, and user-friendly onboarding for internal teams.                           |
|  14 | Legal compliance, governance, and policy enforcement became critical as the platform scaled.                                           |
|  15 | Mapped team interactions to clarify dependencies, but initial centralization around an enablement team created bottlenecks.            |
|  16 | Redefined team boundaries using APIs, CRDs, and explicit interfaces to empower local decision-making.                                  |
|  17 | Adopted producer-consumer models to clarify ownership, dependencies, and reduce unnecessary coordination.                              |
|  18 | Shifted success metrics from project completio                                                                                         |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=zrXvt9DXQ3U)