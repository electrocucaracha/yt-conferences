---
layout: default
title:
  "Project Lightning Talk: What Can Crossplane Actually Do? A Real World Fiel...
  Jonasz Łasut-Balcerzak"
nav_order: 295
parent: Kubecon Cloudnativecon Europe 2026
type: Video Note
description:
  Yonwas Baleshak from the Swiss insurance company Baloas discusses the
  advantages of using Crossplane for platform APIs, emphasizing its integration with
  the Kubernetes control plane and ecosystem. Crossplane allows users to leverage
  familia...
resource: https://www.youtube.com/watch?v=l1LICWLtXIE
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

Yonwas Baleshak from the Swiss insurance company Baloas discusses the advantages of using Crossplane for platform APIs, emphasizing its integration with the Kubernetes control plane and ecosystem.
Crossplane allows users to leverage familiar Kubernetes tools, policies, and RBAC for both application and infrastructure deployments, providing a unified workflow and single pane of glass.
It offers flexibility in implementation, supporting simple YAML templating, Go templates, and general-purpose programming languages like Go, TypeScript, and Python, along with a wide range of cloud providers.
Crossplane addresses challenges in self-service for highly regulated, multi-tenant environments by enabling compliance updates, extending cloud provider products, and building abstractions over complex configurations.
Real-world examples include managing DNS ownership, enhancing API gateways, and simplifying application deployment for developers, ultimately abstracting platform complexity and enabling safer, faster development.

# Main Points

|   # | Main point                                                                                                                                             |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   1 | Crossplane integrates with the Kubernetes control plane and ecosystem.                                                                                 |
|   2 | Supports use of Kubernetes policies (Kyverno, OPA Gatekeeper) and admission policies.                                                                  |
|   3 | Enables reuse of Kubernetes RBAC for both application and infrastructure deployments.                                                                  |
|   4 | Provides a single pane of glass for managing application and infrastructure deployments.                                                               |
|   5 | Allows reuse of GitHub flows and promotion flows for both apps and infrastructure.                                                                     |
|   6 | Offers implementation flexibility: start with YAML templating, Go templates, or use general-purpose languages (Go, TypeScript, Python) with functions. |
|   7 | Supports a wide array of providers, including Azure and other major cloud providers.                                                                   |
|   8 | Addresses self-service challenges in highly regulated, multi-tenant environments.                                                                      |
|   9 | Facilitates compliance by allowing creation of new composition revisions to update all cloud resources for evolving security requirements.             |
|  10 | Enables extension of cloud provider products to meet compliance or domain-specific needs.                                                              |
|  11 | Allows building abstractions over complex configurations spanning multiple providers or tenant boundaries.                                             |
|  12 | Example: Enables shared usage without shared responsibility, such as DNS, by building validation and ownership into the platform.                      |
|  13 | Example: Extends cloud provider products (e.g., API gateways) by adding missing capabilities using Go or TypeScript functions.                         |
|  14 | Example: Simplifies deployment for developers by abstracting complex configurations, such as enabling SSO with a simple flag.                          |
|  15 | Helps developers deploy applications safely without deep infrastructure knowledge.                                                                     |
|  16 | Abstracts platform complexity and provides guardrails for faster and safer developer workflows.                                                        |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=l1LICWLtXIE)
