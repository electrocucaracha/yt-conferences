---
type: Video Note
title: "The Journey of Deploying Backstage in a Large Organization - Mathieu Girard & Teddy Poingt, Beneva"
description: "The presenters describe their experience deploying Backstage, an open-source developer portal framework, at Beneva, a large Canadian insurance company formed from a merger. Facing challenges from duplicated tools, inconsistent practices, an..."
resource: https://www.youtube.com/watch?v=l7OQdrUkoVI
tags: ["kubecon-cloudnativecon-north-america-2025", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

The presenters describe their experience deploying Backstage, an open-source developer portal framework, at Beneva, a large Canadian insurance company formed from a merger.
Facing challenges from duplicated tools, inconsistent practices, and developer confusion after the merger, they launched a software development industrialization program to improve efficiency and developer experience.
They advocated for Backstage by demonstrating potential time savings and return on investment to leadership, emphasizing the value of a unified portal for developers.
The implementation involved assembling a small DevOps team, naming the portal "DevConnect," integrating essential tools (identity provider, Git, documentation), and automating onboarding through pull requests and templates.
They focused on two main goals: improving access to information/tools and accelerating best practice adoption, leveraging Backstage’s catalog and scaffolder features.
Adoption was encouraged through communication, demos, and monitoring usage, while ongoing improvements included adding plugins, integrations, and automation.
Key takeaways highlight the importance of aligning with leadership priorities, addressing developer pain points, treating the portal as a product, and engaging both the developer community and open-source contributors.
# Main Points

|   # | Main point                                                                                                                                              |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Presented the journey of deploying Backstage in a large organization (Benva, Canada’s largest mutual insurance company, 6,000+ employees, $27B assets). |
|   2 | Benva formed in 2020 from a merger of SSQ and La Capitale, resulting in duplicated IT systems, many technologies, and initial chaos.                    |
|   3 | Development was fragmented, with little governance, duplicated efforts, and high cognitive load for developers.                                         |
|   4 | Launched a “software development industrialization” program to improve efficiency, standardize tools, and enhance developer experience (DevX).          |
|   5 | Defined efficiency as a function of productivity and developer happiness.                                                                               |
|   6 | Developers faced confusion and repetitive questions about deployment, testing, and tooling.                                                             |
|   7 | Identified the need for a developer portal; chose Backstage as the solution.                                                                            |
|   8 | Advocated for Backstage by quantifying small time savings (e.g., 5 minutes/day/developer) to demonstrate ROI to leadership.                             |
|   9 | Adapted messaging for different audiences: technical details for developers, ROI and value for leadership.                                              |
|  10 | Assembled a 3-4 person DevOps team with TypeScript, React, and Kubernetes skills.                                                                       |
|  11 | Named the portal “DevConnect” via a developer poll; created a logo for identity.                                                                        |
|  12 | Main goals: better access to information/tools and accelerating best practices adoption.                                                                |
|  13 | Integrated identity provider, Git repository, and documentation as initial steps.                                                                       |
|  14 | Used Backstage’s software catalog to centralize components, systems, domains, and APIs, described via YAML manifests.                                   |
|  15 | Automated onboarding with pull requests for catalog entries; set a goal for 90% repository coverage.                                                    |
|  16 | Added plugins for technology tracking (end-of-life, language), and tooling for validation and error reporting.                                          |
|  17 | Leveraged Backstage’s scaffolder to standardize project templates and best practices.                                                                   |
|  18 | Communicated via short videos, demos, and monitored adoption with analytics plugins.                                                                    |
|  19 | Encouraged inner sourcing for plugin and template contributions.                                                                                        |
|  20 | Integrated with CI/CD, artifact repositories,                                                                                                           |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=l7OQdrUkoVI)