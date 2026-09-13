---
layout: default
title:
  Rabobank’s Path to Secure, Fast Kubernetes Delivery - Beatrice Forslund & Koshin
  Verberne, Rabobank
nav_order: 305
parent: Kubecon Cloudnativecon Europe 2026
type: Video Note
description:
  In this presentation, Kosher Fern and Petris from Rabo Bank’s container
  platform team describe their journey in delivering secure and efficient Kubernetes
  clusters to internal tenants. They explain the bank’s strict regulatory requirements...
resource: https://www.youtube.com/watch?v=cznwYOK3TtY
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

In this presentation, Kosher Fern and Petris from Rabo Bank’s container platform team describe their journey in delivering secure and efficient Kubernetes clusters to internal tenants.
They explain the bank’s strict regulatory requirements, which necessitate rigorous security controls, compliance checks, and thorough documentation for all deployments.
To streamline and standardize Kubernetes adoption, the team established a central platform (Qup) that provides tenants with dedicated clusters—prioritizing security and network isolation over cost efficiency—using tools like Terraform, Argo CD, and Kyverno for automation, compliance, and policy enforcement.
The platform enables rapid, compliant cluster provisioning, reducing setup time from 54 days to just a few hours, while also offering tenants near-admin access within defined security boundaries.
The team emphasizes the importance of clear responsibilities, the right tooling, and ongoing dialogue with tenants to balance innovation with regulatory compliance, sharing key lessons learned for others facing similar challenges.

# Main Points

|   # | Main point                                                                                                                                                               |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   1 | Presentation on secure and fast Kubernetes delivery at Rabo Bank by Kosher Fern and Petris from the container platform team                                              |
|   2 | Rabo Bank serves nearly 9 million customers globally, with infrastructure across three landing zones: Azure, AWS, and on-premise                                         |
|   3 | Current Kubernetes landscape: ~150 Azure Kubernetes Service clusters, 473 Azure container apps, 40+ AWS EKS clusters, 12 on-prem OpenShift clusters                      |
|   4 | Shift from teams creating their own clusters to a more controlled, mature platform approach with increased security restrictions                                         |
|   5 | Strict financial cybersecurity and anti-crime laws from Dutch and European regulators; regular audits require documented controls and evidence                           |
|   6 | Security measures include MFA, modern encryption, threat detection, network segmentation, and operational checks for all deployments                                     |
|   7 | Established a container platform team (Qup) to centralize Kubernetes security, compliance, and infrastructure, enabling tenants to focus on their applications           |
|   8 | Standardized monitoring with hotel agent and Splunk across all landing zones; vulnerability management with Microsoft Defender (Azure) and Inspector (AWS)               |
|   9 | Evaluated namespace-as-a-service (shared clusters) vs. cluster-as-a-service (dedicated clusters); chose dedicated clusters for stronger network isolation and compliance |
|  10 | On AWS, each tenant gets a separate account and EKS cluster for control plane and resource isolation                                                                     |
|  11 | Infrastructure provisioned with Terraform; Argo CD used for continuous deployment                                                                                        |
|  12 | Security pipeline includes code quality scanning (curcube), vulnerability scanning (Checkmarx), and secret scanning; dependencies updated with Renovate                  |
|  13 | Argo CD adapted to comply with IT change management by triggering deployments via Git tags and change tasks                                                              |
|  14 | Governance enforced with Kyverno for policy boundaries and compliance reporting; tenants receive feedback via internal developer portal                                  |
|  15 | Managed platform reduced cluster delivery time from 54 days to 4 hours                                                                                                   |
|  16 | Internal portal (Nexa, built                                                                                                                                             |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=cznwYOK3TtY)
