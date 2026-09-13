---
layout: default
title:
  "On the Origin of Platforms: Evolution of a Capital One Enterprise. Bradley
  Whitfield & Jacob Walden"
nav_order: 185
parent: Kubecon Cloudnativecon North America 2025
type: Video Note
description:
  "In this talk, Brad Whitfield and Jake Walden from Capital One describe
  the evolution of their internal multi-tenant compute platform, Dragon, built on
  Kubernetes. They outline five stages of platform development: inception, stabilization,
  m..."
resource: https://www.youtube.com/watch?v=BY-mQH9VKAo
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

In this talk, Brad Whitfield and Jake Walden from Capital One describe the evolution of their internal multi-tenant compute platform, Dragon, built on Kubernetes.
They outline five stages of platform development: inception, stabilization, multi-tenancy, rewrite, and exponential growth, emphasizing how each stage brings new external pressures and requires specific adaptations.
Initially, they prioritized speed and simplicity, limiting features and documentation, but faced challenges as the platform scaled, such as lack of automation and increased support demands.
The migration from ECS to Kubernetes enabled greater flexibility, automation, and tenant isolation, while partnerships with internal teams improved efficiency and compliance.
As the platform matured, they adopted custom resource definitions and operators to manage complexity, supported advanced use cases, and scaled rapidly, highlighting the importance of automation, robust testing, and strong feedback loops with users.
The presenters stress that platform evolution is a gradual, ongoing process shaped by both technical and organizational factors, and encourage teams to celebrate incremental progress and maintain open communication with stakeholders.

# Main Points

|   # | Main point                                                                                                                         |
| --: | ---------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Capital One’s internal multi-tenant compute platform is called Dragon, built on Kubernetes.                                        |
|   2 | Platform evolution is compared to artificial vs. natural selection: initial rigid builds vs. organic, adaptive growth.             |
|   3 | Stage 1 (Inception): Main external pressures were speed (MVP delivery) and distractions (avoiding unnecessary features/tools).     |
|   4 | Early platform built on ECS EC2 for quick MVP; minimal automation and documentation led to later operational challenges.           |
|   5 | Technical weaknesses included lack of automation, insufficient documentation, ALB maintenance complexity, and API rate limits.     |
|   6 | Stage 2 (Stabilization): Tech debt from stage 1 required focus on operations, SRE principles, and transparent incident management. |
|   7 | Noted inverse relationship between platform trust and support/toil required.                                                       |
|   8 | Migration from ECS to Kubernetes enabled DNS-based service discovery, improved secrets management, and overcame ALB rule limits.   |
|   9 | Initial Kubernetes deployments used Go templates; later evolved to controllers, admission hooks, and operators for automation.     |
|  10 | Stage 3 (Multi-tenancy): Focused on tenant isolation, auditing, secure pipelines, resource control, and scalable support.          |
|  11 | Partnerships with other internal teams (security, audit, IM) improved efficiency and compliance.                                   |
|  12 | Used controllers for network policies and secure cross-account role assumption.                                                    |
|  13 | Stage 4 (Rewrite): Moved to CRDs and operators (Dragon operator) for better scalability, flexibility, and automation.              |
|  14 | Codified standards into three main CRDs; minimal tenant input required for onboarding.                                             |
|  15 | Centralized cluster provisioning with “one cube” streamlined compliance and maintenance.                                           |
|  16 | Stage 5 (Exponential Growth): Rapid cluster growth, platforms on platforms, need for treating clusters as cattle.                  |
|  17 | Adaptations include cluster proxies, service mesh for service discovery, and automation to scale without increasing headcount.     |
|  18 | Future focus: hub-and-spoke cluster management, centralized control planes, and                                                    |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=BY-mQH9VKAo)
