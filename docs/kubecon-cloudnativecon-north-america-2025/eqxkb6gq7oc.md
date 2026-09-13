---
layout: default
title:
  "Tutorial: Build Your Internal Developer Platform With the Experts: A Hands-On...
  Multiple Speakers"
nav_order: 324
parent: Kubecon Cloudnativecon North America 2025
type: Video Note
description:
  'The workshop introduces participants to building an internal developer
  platform using the "backstack," which includes Backstage, Argo CD, Crossplane, and
  Kyverno. The session begins with an overview of each project: Backstage is presented
  a...'
resource: https://www.youtube.com/watch?v=eqxKB6Gq7oc
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

The workshop introduces participants to building an internal developer platform using the "backstack," which includes Backstage, Argo CD, Crossplane, and Kyverno.
The session begins with an overview of each project: Backstage is presented as a customizable framework for building internal developer portals, not a product, enabling organizations to centralize software management and developer collaboration.
Argo CD is described as a GitOps tool for Kubernetes, automating application deployment and synchronization from version-controlled sources, with a comparison to Flux highlighting their different approaches.
Crossplane extends Kubernetes to manage infrastructure and applications declaratively, allowing platform teams to expose APIs for developers and supporting a wide range of resources and compositions.
Kyverno is introduced as a Kubernetes-native policy engine that enforces policies as code, automating governance, security, and operational standards.
The hands-on portion guides attendees through setting up their environment, configuring authentication, and using Backstage to create and manage applications, demonstrating how these tools integrate to provide a self-service, feedback-driven developer experience.
The workshop concludes by emphasizing the power of combining these open-source projects to streamline platform engineering, improve developer autonomy, and ensure compliance, while encouraging participants to engage with the respective communities for further learning and contribution.

# Main Points

|   # | Main point                                                                                                                                                      |
| --: | --------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Workshop focuses on building an internal developer platform using the "backstack": Backstage, Argo, Crossplane, and Kyverno.                                    |
|   2 | Presenters: Margarita Medina (Upbound, Kubernetes), Christian Hernandez (Cisco, Argo CD), Courtney Nickerson (Nermatada, Kyverno), Scott Rosenberg (Teras Sky). |
|   3 | Workshop agenda: slides on platform engineering and project intros, hands-on guided workshop, free time for labs, wrap-up.                                      |
|   4 | Participants instructed to fork a GitHub repository, open a 4-core Codespace (web version recommended), and set up environment.                                 |
|   5 | Backstage:                                                                                                                                                      |
|   6 | Framework for building internal developer portals, not a product.                                                                                               |
|   7 | Powered by a central software catalog; enables software creation, management, and exploration.                                                                  |
|   8 | Highly customizable with 250+ official plugins and 100+ community plugins.                                                                                      |
|   9 | New frontend system allows no-code plugin integration; switched from webpack to RSpack for faster builds.                                                       |
|  10 | Argo:                                                                                                                                                           |
|  11 | Suite of DevOps tools for Kubernetes: Argo Workflows, Argo CD, Argo Rollouts, Argo Events, Argo Helm.                                                           |
|  12 | Argo CD is a GitOps tool for declarative, versioned, and continuously reconciled application deployment.                                                        |
|  13 | Comparison with Flux: Argo CD is monolithic with built-in UI and RBAC; Flux is modular, uses Kubernetes RBAC.                                                   |
|  14 | Argo CD supports Git, Helm, OCI, and Customize as sources.                                                                                                      |
|  15 | Crossplane:                                                                                                                                                     |
|  16 | Control plane framework extending Kubernetes to manage any resource (cloud, on-prem, third-party).                                                              |
|  17 | Enables platform teams to expose infrastructure and application APIs for developers.                                                                            |
|  18 | Key concepts: managed resources, composite resource definitions, compositions, packages, configurations, operations.                                            |
|  19 | Integrates with developer portals (e.g., Backstage) and GitOps tools (Argo CD, Flux).                                                                           |
|  20 | Kyverno:                                                                                                                                                        |
|  21 | Open-source Kubernetes-native policy engine, now supports JSON payloads and CEL.                                                                                |
|  22 | Manages resource lifecycle, integrates with reporting tools.                                                                                                    |
|  23 | Policy-as-code: declarative, human-readable, version-controlled, automates enforcement for security, operati                                                    |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=eqxKB6Gq7oc)
