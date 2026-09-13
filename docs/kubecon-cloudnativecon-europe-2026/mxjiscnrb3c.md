---
layout: default
title:
  "Invisible Guardrails: Enabling Developer Velocity W... James Elías Sigurðarson
  & Vignir Hafsteinsson"
nav_order: 157
parent: Kubecon Cloudnativecon Europe 2026
type: Video Note
description:
  In this talk, James and Vign from Asana describe their journey in building
  a secure, scalable infrastructure platform with security as a first-class feature.
  Initially, Asana’s centralized security model created bottlenecks and friction,
  as...
resource: https://www.youtube.com/watch?v=mxjiSCnrb3c
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

In this talk, James and Vign from Asana describe their journey in building a secure, scalable infrastructure platform with security as a first-class feature.
Initially, Asana’s centralized security model created bottlenecks and friction, as all security changes had to be reviewed and deployed by a single team, slowing developer velocity and leading to operational challenges as the company scaled.
To address this, they transitioned to a multi-tenant Kubernetes architecture called "cells," enabling more granular, application-level permissions and network policies managed alongside application code using tools like Crossplane and Cilium.
Automation and observability were emphasized to streamline permission management, enforce least privilege, and provide auditability, while guardrails such as permission boundaries and policy validation were implemented to prevent misconfigurations and restrict dangerous actions.
The team learned the importance of clear responsibility boundaries, early investment in tooling and education, and shifting both security controls and conversations left to empower developers without sacrificing security or velocity.

# Main Points

|   # | Main point                                                                                                                                                        |
| --: | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Asana is a work management platform serving over 170,000 organizations and millions of users.                                                                     |
|   2 | Security, stability, and velocity are prioritized in that order for infrastructure development.                                                                   |
|   3 | Historically, security was centralized, creating bottlenecks and slowing developer velocity.                                                                      |
|   4 | Single-tenant Kubernetes clusters (cube apps) led to scaling and operational challenges, including single points of failure and high operational burden on teams. |
|   5 | Transitioned to a multi-tenant architecture called "cells," with isolated failure domains and dedicated platform teams.                                           |
|   6 | Shifted from cluster-level to application-level permissions, adhering to the principle of least privilege.                                                        |
|   7 | Adopted GitOps for deploying permissions and used automation to reduce human error.                                                                               |
|   8 | Implemented pod-level IAM permissions using Crossplane, placing permission definitions alongside application code.                                                |
|   9 | Network security moved from cluster-level to pod-level using Cilium network policies, enforcing deny-by-default and explicit segmentation.                        |
|  10 | Application developers now define permissions and network policies within the same PR as code changes, improving clarity and reducing deployment cycles.          |
|  11 | Automation and observability tools (Hubble, AWS client-side monitoring) are used to capture and generate least-privilege policies iteratively.                    |
|  12 | AWS permission boundaries and security groups set maximum permission scopes; guardrails are validated and shifted left for earlier feedback.                      |
|  13 | Platform uses AWS Bottlerocket OS, Istio for ingress/egress and MTLS, and Kyverno for runtime policy enforcement and validation.                                  |
|  14 | Guardrails are tested and validated locally before enforcement; invisible guardrails can cause silent failures if not permissive enough.                          |
|  15 | Clear distinction of responsibilities between platform and application teams is emphasized.                                                                       |
|  16 | Early investment in tooling, automation, observability, and communication is recommended.                                                                         |
|  17 | All configuration changes go through GitOps pipelines; human actions ar                                                                                           |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=mxjiSCnrb3c)
