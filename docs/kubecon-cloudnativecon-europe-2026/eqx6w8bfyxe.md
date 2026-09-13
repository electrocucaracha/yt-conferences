---
layout: default
title:
  "From Open Source To Enterprise Scale and Back: A Journey... Michael Kuhnt
  & Gabriel Adrian Samfira"
nav_order: 124
parent: Kubecon Cloudnativecon Europe 2026
type: Video Note
description:
  In this talk, Michael from Mercedes-Benz Tech Innovation and Gabriel
  from Cloud Base Solutions share their experience building a large-scale managed
  CI/CD runner platform for internal teams at Mercedes-Benz, leveraging the open source
  proje...
resource: https://www.youtube.com/watch?v=eqX6w8bFyxE
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

In this talk, Michael from Mercedes-Benz Tech Innovation and Gabriel from Cloud Base Solutions share their experience building a large-scale managed CI/CD runner platform for internal teams at Mercedes-Benz, leveraging the open source project Garm.
Initially, teams at Mercedes-Benz faced challenges with fragmented and insecure self-hosted runner setups for GitHub Enterprise, prompting the creation of a unified, ephemeral VM-based runner platform to reduce duplication and improve security.
After documenting their vision and gathering feedback, they adopted and contributed to Garm, which offered a flexible, pluggable architecture for managing runners across various clouds and infrastructures.
Key lessons included the importance of clearly articulating and sharing the project vision, actively engaging users and minimizing adoption friction, learning transparently from failures through postmortems, and giving back to the open source community.
The session concluded with a live demo of Garm’s Kubernetes operator, showcasing its integration capabilities and scalability, and emphasized that small teams can achieve significant impact by building on and contributing to open source solutions.

# Main Points

|   # | Main point                                                                                                                                                       |
| --: | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Michael and Gabriel shared lessons from building a managed shared service for internal development teams at Mercedes-Benz using the open source project Garm.    |
|   2 | The initial challenge was the lack of managed runners for GitHub Enterprise, leading to duplicate efforts and security concerns as teams built their own setups. |
|   3 | The team created a design document outlining the vision, goals, and approach for a common managed CI/CD runner platform.                                         |
|   4 | Sharing the vision document internally helped gather feedback and refine the idea.                                                                               |
|   5 | Research led to discovering Garm, an open source GitHub Action Runner Manager with a pluggable architecture, written in Go.                                      |
|   6 | The team contributed to Garm and established collaboration with its creator, Gabriel.                                                                            |
|   7 | Garm was originally built to help the Flatcar Linux project move from Jenkins to GitHub workflows, requiring VM-based runners.                                   |
|   8 | Garm supports multiple providers (Azure, OpenStack, LXD, Kubernetes, Incus, Akamai) and can be extended with custom providers.                                   |
|   9 | Mercedes-Benz added a Kubernetes provider and contributed back to the project.                                                                                   |
|  10 | Garm can now connect to multiple source forges (GitHub, Gitea, Forgejo).                                                                                         |
|  11 | Onboarding users required extensive outreach and minimizing friction; using the "self-hosted" label enabled seamless adoption.                                   |
|  12 | Features added included transparent proxy configuration and remote shell access for debugging workflows.                                                         |
|  13 | The team experienced a major outage due to infrastructure issues, wrote a postmortem, and emphasized transparency to build trust.                                |
|  14 | The platform scaled to over 12 million workflow runs and 700,000 runs per month.                                                                                 |
|  15 | Open source and Garm were crucial to the platform's success; the team contributed bug fixes, insights, and a Kubernetes operator back to the community.          |
|  16 | A live demo showcased the Kubernetes operator integration, multi-provider support, and runner pool management in Garm.                                           |
|  17 | The talk concluded with an invitation to explore helpful links and a Q&A session.                                                                                |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=eqX6w8bFyxE)
