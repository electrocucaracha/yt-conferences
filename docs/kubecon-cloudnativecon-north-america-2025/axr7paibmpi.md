---
layout: default
title:
  How Comcast Leverages Radius in Their Internal Developer Platform - Nick Beenham
  & Jonathan Smith
nav_order: 99
parent: Kubecon Cloudnativecon North America 2025
type: Video Note
description:
  Nick Beam, a distinguished engineer at Comcast, and Jonathan Smith from
  Microsoft’s Azure Open Source Incubations team discuss the integration and benefits
  of Radius, a cloud-native application platform contributed to the CNCF. Radius enabl...
resource: https://www.youtube.com/watch?v=axR7paIbmPI
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

Nick Beam, a distinguished engineer at Comcast, and Jonathan Smith from Microsoft’s Azure Open Source Incubations team discuss the integration and benefits of Radius, a cloud-native application platform contributed to the CNCF.
Radius enables developers to define applications and infrastructure in a unified, simplified manifest, allowing deployment across multiple cloud environments such as AWS, Azure, and on-premises systems.
Comcast adopted Radius to address the complexity and sprawl of Kubernetes and related tooling, collaborating closely with the Radius team to introduce custom resource types that fit their specific needs.
This partnership led to streamlined workflows, reduced cognitive load, and the ability to reuse existing tools like Terraform without significant migration costs.
The speakers highlight the value of open-source community engagement, the ease of contributing to Radius, and encourage others to participate, noting the platform’s extensibility, integration with popular DevOps tools, and the availability of a resource type repository for sharing and reusing components.

# Main Points

|   # | Main point                                                                                                                                                |
| --: | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Nick Beam, Distinguished Engineer at Comcast, became involved with the Radius program in late 2023.                                                       |
|   2 | Jonathan Smith leads product management for Azure Opensource Incubations, the team behind Radius and other CNCF-contributed projects.                     |
|   3 | Azure Incubations focuses on open source technologies to accelerate cloud migration industry-wide, partnering with CNCF for community and governance.     |
|   4 | Notable projects from the team include Keda, Dapr, Copacetic, DRSI, and Radius.                                                                           |
|   5 | Radius is a cloud-native application platform enabling applications to be defined once and deployed across multiple clouds (on-prem, AWS, Azure).         |
|   6 | Radius targets platform engineering teams, emphasizing extensibility, custom resources, and integration with existing developer platforms.                |
|   7 | Integrates with Kubernetes, Terraform, Dapr, GitOps tools (Flux, Argo CD), and has plugins in development for Backstage and Headlamp.                     |
|   8 | Radius aims to simplify Kubernetes complexity, enable seamless resource use across clouds, enforce security and cost controls, and provide AI guardrails. |
|   9 | Architecturally, Radius uses a Universal Control Plane (UCP) to deploy resources across clouds from a single application definition.                      |
|  10 | Comcast adopted Radius to address Kubernetes complexity, ecosystem sprawl, and configuration drift.                                                       |
|  11 | Custom resources in Radius allow defining any resource (e.g., databases, AI connections) simply and consistently.                                         |
|  12 | Supports managing multiple, geo-distributed clusters from a single control plane.                                                                         |
|  13 | Allows reuse of existing tools like Helm and Terraform, reducing migration costs.                                                                         |
|  14 | Recipes separate application manifests (by developers) from infrastructure modules (by platform engineers), promoting consistency and reducing drift.     |
|  15 | Creating and publishing custom resource types and recipes in Radius is straightforward, requiring minimal commands.                                       |
|  16 | Comcast saw benefits in open-source community engagement, feature feedback, and successful internal platform deployments.                                 |
|  17 | Lessons learned: start small,                                                                                                                             |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=axR7paIbmPI)
