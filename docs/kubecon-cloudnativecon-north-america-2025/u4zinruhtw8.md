---
layout: default
title:
  Shipping Secure, Reusable, and Composable Infrastructure as Code... Feynman
  Zhou & Katherine Pitz
nav_order: 279
parent: Kubecon Cloudnativecon North America 2025
type: Video Note
description:
  In this presentation, Feman from Microsoft Azure and Katie Pittz from
  GE Healthcare discuss how GE Healthcare addressed challenges in deploying cloud-native
  patient care applications by centralizing and automating their infrastructure provi...
resource: https://www.youtube.com/watch?v=u4zinRUhtw8
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

In this presentation, Feman from Microsoft Azure and Katie Pittz from GE Healthcare discuss how GE Healthcare addressed challenges in deploying cloud-native patient care applications by centralizing and automating their infrastructure provisioning process.
Previously, each application team managed deployments independently, resulting in manual, time-consuming, and inconsistent processes that delayed hospital access to new software.
To solve this, GE Healthcare’s platform team developed a digital provisioning tool based on infrastructure as code (IaC) and OCI (Open Container Initiative) artifacts, leveraging the ORAS project to package, publish, and deliver reusable, composable software packages with custom configurations.
This approach streamlined deployments, reduced manual steps, and enabled faster, more reliable delivery of applications to hospitals.
The presentation also highlights how ORAS and OCI artifacts support secure, flexible artifact management and versioning, and outlines future plans to further optimize package structure and align with updated OCI specifications.

# Main Points

|   # | Main point                                                                                                                                                               |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   1 | Presentation began without slides due to technical issues; slides available online for reference.                                                                        |
|   2 | Speakers: Feman (Microsoft Azure, CNCF maintainer) and Katie Pittz (GE Healthcare, software engineer).                                                                   |
|   3 | GE Healthcare faced challenges with decentralized, manual, and inconsistent deployment of patient care applications.                                                     |
|   4 | Each application team managed its own infrastructure, leading to varied processes and heavy administrative burden.                                                       |
|   5 | Deployments were slow, sometimes taking days to weeks, delaying hospital access to applications.                                                                         |
|   6 | Problems included custom infrastructure per hospital, manual steps, inconsistent deployment/versioning practices, and increasing complexity with more cloud-native apps. |
|   7 | GE Healthcare’s platform team built a digital provisioning service to centralize and automate deployments.                                                               |
|   8 | Solution uses reusable base packages with custom configuration, automating installations and reducing manual runbooks.                                                   |
|   9 | Deployment time reduced to a few hours, depending on application complexity.                                                                                             |
|  10 | ORAS standardizes packaging, publishing, and delivery of cloud-native software infrastructure.                                                                           |
|  11 | ORAS project started in 2019, joined CNCF in 2021; enables storing any artifact (AI models, Helm charts, signatures, etc.) in container registries.                      |
|  12 | ORAS provides command-line tools and SDKs (C#, Java, Python, Go, Rust); widely adopted in open source and enterprise.                                                    |
|  13 | Key ORAS scenarios: content distribution, content promotion, supply chain security, multi-architecture artifact management, registry backup/restore.                     |
|  14 | GE Healthcare uses infrastructure as code (IaC) as the foundation for reusable packages, supporting tools like Terraform, Helm, Open Tofu, and cloud-specific IaC.       |
|  15 | OCI artifacts are used to package IaC files, metadata, and annotations, enabling composable, reusable, and versioned deployments.                                        |
|  16 | Application teams build packages to platform standards, publish to OCI registries, and automate deployment via the provisioning tool.                                    |
|  17 | Workflow: service engineers select p                                                                                                                                     |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=u4zinRUhtw8)
