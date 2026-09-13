---
layout: default
title:
  "Getting up To Date With Docsy: The Ku... Natali Vlatko, Rey Lejano, Divya
  Mohan & Sayak Mukhopadhyay"
nav_order: 90
parent: Kubecon Cloudnativecon North America 2025
type: Video Note
description:
  The video features members of the Kubernetes SIG Docs team—Ray Laano,
  Natalie Latco, and Da Muan—discussing the ongoing upgrade of the Kubernetes documentation
  site, specifically the transition to newer versions of the Doxy theme and Hugo s...
resource: https://www.youtube.com/watch?v=lOQBleJBMdY
tags:
  - kubecon-cloudnativecon-north-america-2025
  - video
  - learning
status: stable
generated:
  by: process:yt-conferences-okf
  at: 2026-09-12 00:00:00+00:00
---

# Summary

The video features members of the Kubernetes SIG Docs team—Ray Laano, Natalie Latco, and Da Muan—discussing the ongoing upgrade of the Kubernetes documentation site, specifically the transition to newer versions of the Doxy theme and Hugo static site generator.
They explain the importance of up-to-date, high-quality documentation for user adoption, support, and the global community, noting past migrations from Jekyll to Hugo and the adoption of Doxy for improved localization and user experience.
The upgrade process is incremental, focusing on small, manageable pull requests to minimize disruption, ensure compatibility across multiple languages, and maintain site stability during frequent Kubernetes releases.
The team emphasizes the need for community involvement in reviewing, testing, and providing feedback on documentation changes, highlighting the challenges of maintaining such a large, volunteer-driven project and inviting contributors to participate through GitHub, Slack, and regular meetings.
They also address questions about testing, noting that while build and deployment checks exist, there are currently no end-to-end automated tests, and they welcome contributions in this area.

# Main Points

|   # | Main point                                                                                                                                                                                                                                                                  |
| --: | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Introduction of speakers: Ray Laano (Red Hat, Kubernetes maintainer, SIGDOCs co-chair), Natalie Latco (Cisco, Kubernetes maintainer, open source director), Da Muan (SUZA, Kubernetes docs maintainer), Saiak (not present due to visa issues, key contributor to upgrade). |
|   2 | Focus of talk: Kubernetes documentation upgrade, specifically upgrading the Doxy theme and Hugo static site generator.                                                                                                                                                      |
|   3 | Importance of documentation: Drives open source adoption, supports users, and is critical for troubleshooting.                                                                                                                                                              |
|   4 | Current tech stack: GitHub for source control, Prow for CI/CD, Netlify for hosting, Hugo as static site generator, Doxy as theme, Mermaid.js for diagrams.                                                                                                                  |
|   5 | Reasons for upgrade: Security, compatibility, access to new features (e.g., dark mode, modern icons), improved performance, easier maintenance, and contribution.                                                                                                           |
|   6 | History: Started with Jekyll, migrated to Hugo in 2018 for flexibility and localization, adopted Doxy theme in 2020.                                                                                                                                                        |
|   7 | Challenges: Volunteer-driven, lagging behind on Hugo and Doxy releases, compatibility and security issues, complex customizations.                                                                                                                                          |
|   8 | Upgrade approach:                                                                                                                                                                                                                                                           |
|   9 | Small, incremental pull requests.                                                                                                                                                                                                                                           |
|  10 | One layout/shortcode at a time to avoid breaking localization.                                                                                                                                                                                                              |
|  11 | Continuous cleanup and testing.                                                                                                                                                                                                                                             |
|  12 | Rebasing frequently to keep up with Kubernetes releases.                                                                                                                                                                                                                    |
|  13 | Collaboration with SIG Contributor Experience for contributor site upgrades.                                                                                                                                                                                                |
|  14 | Upgrade process:                                                                                                                                                                                                                                                            |
|  15 | Audit current site and dependencies.                                                                                                                                                                                                                                        |
|  16 | Compare with latest Doxy versions.                                                                                                                                                                                                                                          |
|  17 | Incremental template/layout updates.                                                                                                                                                                                                                                        |
|  18 | Test changes and gather feedback.                                                                                                                                                                                                                                           |
|  19 | Update dependency versions after testing.                                                                                                                                                                                                                                   |
|  20 | Progress:                                                                                                                                                                                                                                                                   |
|  21 | Upgrade to Doxy 0.6.0 complete, 0.7.0 in progress, aiming for 0.12.0.                                                                                                                                                                                                       |
|  22 | Incremental progress, prioritizing minimal customizations for easier contributions.                                                                                                                                                                                         |
|  23 | How to contribute:                                                                                                                                                                                                                                                          |
|  24 | File issues, join Slack channel (#sig-docs), review PRs (formal/informal), test documentation, submit feedback, attend meetings.                                                                                                                                            |
|  25 | New contributor meet-and-greet sessions available.                                                                                                                                                                                                                          |
|  26 | Testing:                                                                                                                                                                                                                                                                    |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=lOQBleJBMdY)
