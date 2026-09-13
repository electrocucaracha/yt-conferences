---
type: Video Note
title: "Ghost in the Platform: How the Dutch Tax Authority Built a Servi... Jerry van Hulst, & Marcel Kerker"
description: "The presentation introduces the Coina platform, developed by the Dutch tax authority (Belastingdienst), which manages tax collection, benefits, and customs in the Netherlands. The platform’s journey began in 2017 with the goal of maximizing..."
resource: https://www.youtube.com/watch?v=PUHAYSM_jGI
tags: ["kubecon-cloudnativecon-europe-2026", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

The presentation introduces the Coina platform, developed by the Dutch tax authority (Belastingdienst), which manages tax collection, benefits, and customs in the Netherlands.
The platform’s journey began in 2017 with the goal of maximizing developer autonomy through a Kubernetes-based container hosting solution.
Early adoption saw rapid growth, but challenges emerged as developers faced high cognitive load and a lack of standardization, leading to slower onboarding.
To address this, the team created a structured onboarding process, a comprehensive manifesto, and the open-source Project as a Service (Paas) operator, enabling developers to provision fully configured Kubernetes environments with a single YAML request.
The platform also offers a “golden path” of best practices, extensive documentation, workshops, and a strong community of practice, supporting over 80 teams and 160 applications across 78 OpenShift clusters.
Looking ahead, the team aims to expand integrations, enhance automation with AI, and continue empowering developers toward self-sufficiency and standardization.
# Main Points

|   # | Main point                                                                                                                                                                                         |
| --: | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Presentation about the Coina platform by the Dutch tax authority (Belastingdienst)                                                                                                                 |
|   2 | Dutch tax authority: 28,000 employees, 4,000 IT staff, collects over 300 billion euros annually                                                                                                    |
|   3 | IT landscape spans 60 years; focus on last 10 years                                                                                                                                                |
|   4 | Mission: empower staff with a platform and tools for digital ownership                                                                                                                             |
|   5 | Journey began in 2017 with Kubernetes adoption, aiming for maximum developer autonomy                                                                                                              |
|   6 | Early years focused on building and automating infrastructure; first customers joined in 2019                                                                                                      |
|   7 | Initial success: high enthusiasm, rapid adoption, increased developer velocity                                                                                                                     |
|   8 | Challenges emerged: high cognitive load for developers, lack of standardization, slow onboarding, enablement team couldn't keep up                                                                 |
|   9 | Main problem: reduce cognitive load and increase standardization to speed up workflows                                                                                                             |
|  10 | Onboarding process: DevOps teams prepare architecture, replatform applications, complete intake questionnaire (~50 questions), receive go/no-go for non-production, then production environments   |
|  11 | Manifesto: 70 points teams must accept (e.g., application resettable, redeploy containers, environment parity, team responsibility)                                                                |
|  12 | Project as a Service (PaaS): open-source Kubernetes operator for creating full environments with one YAML request, GitOps interface, preconfigured capabilities (Argo CD, Keycloak, Grafana, etc.) |
|  13 | Automated validation and approval process for pull requests to manage cluster resources                                                                                                            |
|  14 | Starter kit built with Backstage: generates repos, CI/CD pipelines, manifests, documentation, and pull requests                                                                                    |
|  15 | Golden Path: opinionated guidance with 50+ white papers covering design, deployment, and operations                                                                                                |
|  16 | Community of Practice and user groups for knowledge sharing, demos, and workshops                                                                                                                  |
|  17 | Over 80 teams, 160+ applications, 78 OpenShift clusters, 900+ worker nodes                                                                                                                         |
|  18 | Recent exponential growth in clusters and adoption                                                                                                                                                 |
|  19 | Future plans: more Backstage integration, expand starter kit, more white papers, AI integration for support and automation                                                                         |
|  20 | Key lessons: platform is an ec                                                                                                                                                                     |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=PUHAYSM_jGI)