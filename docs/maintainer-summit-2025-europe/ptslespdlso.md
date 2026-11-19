---
layout: default
title: "Subproject Struggles: Community Vs Company - Michael McCune, Red Hat & Davanum Srinivas, AWS"
nav_order: 17
parent: "Maintainer Summit 2025 - Europe"
type: Video Note
description: "This interactive session, led by Michael McHune and Dims, addresses the complex dynamics between community ownership and corporate interests in Kubernetes sub-projects, specifically focusing on the..."
resource: "https://www.youtube.com/watch?v=ptsLespDlSo"
tags:
  - maintainer-summit-2025-europe
  - video
  - learning
status: stable
generated:
  by: process:yt-summarizer-okf
  at: 2026-11-15T22:30:54+00:00
---

# Summary

This interactive session, led by Michael McHune and Dims, addresses the complex dynamics between community ownership and corporate interests in Kubernetes sub-projects, specifically focusing on the tension between the Cloud Controller Manager (CCM) and the AWS Load Balancer Controller.
The speakers highlight a recurring issue where feature development is fragmented across repositories with convoluted histories, leading to confusion for users and contributors who lack clear documentation or migration paths between these components.
A key example discussed is the difficulty Red Hat developers faced in proposing features to the CCM when the active maintenance had shifted to a separate, vendor-specific controller, illustrating the broader challenge of defining project ownership and maintenance responsibilities within SIGs.
The discussion emphasizes the need for better community practices, such as standardized tooling, transparent CI/CD infrastructure, and robust disaster recovery plans for shared resources like Google Docs, to prevent knowledge loss and ensure project continuity.
Ultimately, the session advocates for a healthier ecosystem where corporate sponsors actively contribute to and maintain community-owned code, fostering a culture of shared responsibility and open collaboration that benefits all users, regardless of their affiliation.

# Main Points

|   # | Main point                                                                                                                                                                                                                                  |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | The session addresses community versus company struggles in Kubernetes sub-project maintenance, focusing on ownership, feature placement, and collaboration.                                                                                |
|   2 | A key issue involves the AWS cloud controller manager and load balancer controller, where specific features exist in one repository but not the other, causing confusion for users.                                                         |
|   3 | The AWS cloud provider repository is treated as a snapshot of code extracted from Kubernetes, while new load balancer features are developed in a separate, long-existing AWS load balancer controller repository.                          |
|   4 | Red Hat developers sought to add a network load balancer security group feature to the cloud controller manager but were directed to the separate load balancer controller, highlighting a lack of clear documentation and migration paths. |
|   5 | The community lacks a documented migration pattern for users moving services from the cloud controller manager to the load balancer controller, exacerbating the confusion.                                                                 |
|   6 | New community members face barriers to contribution due to non-standardized tooling and complex CI/CD infrastructure, such as Prow and test grids, which are difficult to navigate without prior experience.                                |
|   7 | Project documentation and agendas stored in corporate-owned Google Docs have been lost when employees changed jobs, necessitating a shift to community-owned shared directories to prevent data loss.                                       |
|   8 | There is a debate over whether corporate sponsors have a moral obligation to maintain code that primarily benefits their specific cloud platform, versus the community's responsibility to maintain shared infrastructure.                  |
|   9 | Maintainers emphasize the importance of clearly distinguishing between acting as a community leader and representing a corporate employer to ensure fair and transparent decision-making.                                                   |
|  10 | Early diversification of the maintainer list is recommended to prevent projects from becoming dominated by a single corporation, which can make later community engagement difficult.                                                       |
|  11 | The community aims to create a more inviting space for new contributors by improving onboarding, standardizing tooling, and encouraging corporate sponsors to invest in shared maintenance and migration efforts.                           |

# Video

[![Video thumbnail](https://img.youtube.com/vi/ptsLespDlSo/hqdefault.jpg)](https://www.youtube.com/watch?v=ptsLespDlSo)

[Watch on YouTube](https://www.youtube.com/watch?v=ptsLespDlSo)
