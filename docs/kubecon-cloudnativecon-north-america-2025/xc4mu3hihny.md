---
layout: default
title:
  "Upgrade Nightmare To Uptime Dream: The Cloud Provider's Playbook for... Yuchen
  Zhou & Uttam Kumar"
nav_order: 336
parent: Kubecon Cloudnativecon North America 2025
type: Video Note
description:
  In this presentation, Utam Kumar from Salesforce and a representative
  from Google discuss the complexities and solutions involved in upgrading Kubernetes
  minor versions at scale, particularly for critical platforms like Salesforce Hyperforc...
resource: https://www.youtube.com/watch?v=xc4MU3HiHnY
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

In this presentation, Utam Kumar from Salesforce and a representative from Google discuss the complexities and solutions involved in upgrading Kubernetes minor versions at scale, particularly for critical platforms like Salesforce Hyperforce.
They explain that Hyperforce operates thousands of Kubernetes clusters across multiple clouds, supporting millions of pods and requiring robust, automated processes for safe upgrades.
The speakers highlight the challenges of Kubernetes upgrades, including interconnected dependencies, rapid release cycles, and the risk of outages, and describe Salesforce’s approach of extensive changelog analysis, automated fleet scanning, rigorous performance and validation testing, and staggered rollouts with rollback support.
Google’s representative details their strategy for safer upgrades in Google Kubernetes Engine (GKE), emphasizing automation, control over upgrade timing and grouping, observability, and a new two-step upgrade process using an emulator version to enable safe rollbacks.
Both organizations stress the importance of comprehensive testing, customer collaboration, and new tooling to minimize risk and maintain high uptime during Kubernetes upgrades.

# Main Points

|   # | Main point                                                                                                                                                                       |
| --: | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Utam Kumar (Salesforce) and a Google engineer discuss Kubernetes minor version upgrades.                                                                                         |
|   2 | Salesforce Hyperforce is a large-scale, multi-cloud platform with 1,000+ Kubernetes clusters and millions of pods.                                                               |
|   3 | Hyperforce uses Kubernetes with Google Cloud and other vendors, Istio service mesh, CSI add-ons, autoscaling controllers, and custom integration services.                       |
|   4 | Fleet management and APIs enable abstracted, fleetwide releases using Argo, Spree, Terraform, and AI-powered troubleshooting.                                                    |
|   5 | Kubernetes upgrades are critical for new features and security but are complex and risky due to interconnected dependencies and lack of rollback support.                        |
|   6 | Upgrades require prepping and certification: analyzing changelogs, automated fleet scans, dev cluster testing, and performance testing.                                          |
|   7 | Deprecated APIs are flagged early via CI policies; warnings escalate to failures as removal nears.                                                                               |
|   8 | Validation frameworks require customers to submit tests, which run in upgrade pipelines; failures halt upgrades for investigation.                                               |
|   9 | Staggered upgrades are based on cluster criticality, with soak/bake periods to catch issues in lower environments.                                                               |
|  10 | Examples of upgrade issues: API server concurrency changes (429 errors), containerd IPv6 changes affecting sidecars.                                                             |
|  11 | Rollback support is essential for safe upgrades; previously, only disaster recovery was possible.                                                                                |
|  12 | Google’s GKE approach: automation, control (grouping, soak time, maintenance windows/exclusions), observability, and reliability pillars.                                        |
|  13 | Two-step upgrade process: first upgrade binaries and add-ons with emulator version set to previous minor; after soak period and verification, bump compatibility to new version. |
|  14 | Emulator version allows clusters to emulate previous API behavior, enabling safe rollback during soak.                                                                           |
|  15 | Performance testing is done at production scale and for individual add-ons; both homegrown and standardized frameworks are used.                                                 |
|  16 | Add-on upgrades are tested with each minor version; GKE bundles and tests 100+ add-ons                                                                                           |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=xc4MU3HiHnY)
