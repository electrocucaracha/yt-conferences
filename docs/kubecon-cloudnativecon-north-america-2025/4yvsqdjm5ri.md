---
layout: default
title:
  "One Dozen To One Thousand Clusters: How Argo Kept up as We Scaled - Jérémy
  Albuixech & Kahou Lei"
nav_order: 187
parent: Kubecon Cloudnativecon North America 2025
type: Video Note
description:
  Kahal and Jeremy, engineers at Octa, discuss how their Ozero platform
  evolved to support large-scale, automated deployments using Argo CD and Argo Workflows.
  Initially, their platform was manually operated and not designed for scale, but
  gr...
resource: https://www.youtube.com/watch?v=4yVSqDJm5RI
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

Kahal and Jeremy, engineers at Octa, discuss how their Ozero platform evolved to support large-scale, automated deployments using Argo CD and Argo Workflows.
Initially, their platform was manually operated and not designed for scale, but growing demand led them to adopt cloud-native tools, with Argo CD handling service provisioning and Argo Workflows managing deployments.
They highlight the benefits of Argo, such as ease of installation, flexible integration, strong dependency management, and a robust open-source community, but also explain why they cannot use Argo CD’s auto-sync feature due to their custom release model and customer-specific deployment windows.
To address performance and reliability challenges at scale, they developed homegrown plugins, optimized the use of Customize, and implemented a CLI wrapper to handle transient errors and retries.
The team also describes their approach to workflow orchestration, state management, and collaboration across teams, as well as UI limitations and workarounds.
Throughout, they emphasize the importance of stability, automation, and incremental improvements to keep their deployment pipeline reliable and efficient.

# Main Points

|   # | Main point                                                                                                                                                                  |
| --: | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Introduced presenters: Kahal (Principal Software Engineer, OCO platform) and Jeremy (Staff Engineer, Ozero platform) at Octa.                                               |
|   2 | Agenda: platform history and design, deep dive on Argo CD, Argo Workflows, Q&A.                                                                                             |
|   3 | Initial platform was manual, low-scale, with snowflake infra and configs, and limited automation/security.                                                                  |
|   4 | New platform leverages cloud-native tech: Argo CD (service provisioning), Argo Workflows (deployments), Terraform (infra code), all orchestrated by control plane services. |
|   5 | Argo chosen for easy installation, flexible integration, strong API/CI integration, robust dependency model, and strong open-source community.                              |
|   6 | Current scale: 1,000-2,000 Argo CD applications, 2-3 million Kubernetes resources, 32 application controller pods, 24 repository server pods, one control plane instance.   |
|   7 | Argo CD auto-sync ensures cluster state matches Git repository, but not used due to custom release model and deployment windows.                                            |
|   8 | Release manifest bundles all microservice versions, Terraform code, and plugins; one Argo application per cluster.                                                          |
|   9 | Custom deployment process: scheduler and deploy manager submit Argo Workflows during customer-defined deploy windows.                                                       |
|  10 | Workflow steps: preflight checks, Terraform plan/apply, config/secrets generation, Argo CD sync via custom plugins.                                                         |
|  11 | Benefits: better error control, flexible deployment priorities, reduced blast radius, controlled upgrades, avoids overloading Argo CD components.                           |
|  12 | Homegrown application X plugin generates Kubernetes resources from minimal YAML, ensuring security and autoscaling best practices.                                          |
|  13 | Performance issue with Kustomize plugins solved by forking Kustomize and embedding plugins, reducing refresh time from minutes to seconds.                                  |
|  14 | Docker-in-Docker used in plugins to ensure correct versioning per customer environment.                                                                                     |
|  15 | Built CLI wrapper for Argo CD to categorize failures, enable retries, set timeouts, and avoid stuck/conflicting syncs.                                                      |
|  16 | UI and scaling challenges: slow/unusable UI at scale, misleading app statuses, co                                                                                           |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=4yVSqDJm5RI)
