---
layout: default
title:
  "From Bespoke To Bulletproof: SPIFFE/SPIRE With ESO for Enterprise Zero...
  May Large & Ivy Alkhaz"
nav_order: 82
parent: Kubecon Cloudnativecon North America 2025
type: Video Note
description:
  At CubeCon, Ivy Alcaz and May Large from State Farm shared their journey
  implementing Spire for Enterprise Zero Trust, detailing their transition from a
  bespoke, out-of-the-box Spire deployment to a scalable, highly available nested
  Spire a...
resource: https://www.youtube.com/watch?v=EVbFeCipis8
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

At CubeCon, Ivy Alcaz and May Large from State Farm shared their journey implementing Spire for Enterprise Zero Trust, detailing their transition from a bespoke, out-of-the-box Spire deployment to a scalable, highly available nested Spire architecture across multiple AWS regions and clusters.
They described initial challenges with static secrets, scaling issues, and consumer experience, which led them to adopt a nested topology with a root "mom" Spire server and child servers for each business cluster, replacing SQLite with RDS Postgres and centralizing OIDC discovery.
Leveraging the hardened Helm chart and strong community support, they streamlined deployment, managed cross-account secrets securely using External Secrets Operator (ESO), and ensured a smooth rollout with minimal consumer disruption by overlapping token validity periods and addressing AWS and Kubernetes constraints.
The move to nested Spire simplified JWT issuer management, improved workload API availability, and enabled easier SVID consumption, while future plans include expanding UI capabilities, service mesh integration, federation, and broader platform support.
Throughout, they emphasized the value of community collaboration, automation, and practical lessons learned for large-scale, secure Spire adoption.

# Main Points

|   # | Main point                                                                                                                             |
| --: | -------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Ivy Alcaz and May Large presented on moving from bespoke to bulletproof Spiffy/Spire for Enterprise Zero Trust at CubeCon.             |
|   2 | Both are platform engineers at State Farm, responsible for Spire across a large AWS-based Kubernetes cluster fleet.                    |
|   3 | Initial implementation used out-of-the-box Spire with ArgoCD, SQLite, AWS Private CA, and Key Management Store.                        |
|   4 | Challenges included scaling issues, maintenance of manifests/YAML, SQLite storage loss, and too many OIDC endpoints.                   |
|   5 | Transitioned to a nested Spire architecture:                                                                                           |
|   6 | Management cluster (“mom”) became the root Spire server.                                                                               |
|   7 | Child clusters became independent Spire servers with RDS Postgres replacing SQLite.                                                    |
|   8 | OIDC discovery service centralized to mom, replaced with AWS S3 bundle publisher and CloudFront for public keys.                       |
|   9 | Intermediate CA path length set to two for independence of child clusters.                                                             |
|  10 | Used Spiffy Hardened Helm Chart for deployment, leveraging community-tested defaults and monthly updates.                              |
|  11 | Community support via Slack and GitHub was crucial for troubleshooting and feature requests.                                           |
|  12 | External Secrets Operator (ESO) used for secure cross-account secret management, with Terraform for AWS resource policies and tagging. |
|  13 | Rollout strategy:                                                                                                                      |
|  14 | Started with passive region clusters to test and learn.                                                                                |
|  15 | Shortened cluster names to fit 15-character service name constraint.                                                                   |
|  16 | Managed AWS 100 assume role key limit by reducing replicas and extending intermediate CA TTL.                                          |
|  17 | Nested Spire reduced root server dependency, improving high availability.                                                              |
|  18 | Overlapped JWT SVID validity to ensure zero consumer downtime during migration.                                                        |
|  19 | Consumption improvements:                                                                                                              |
|  20 | Reduced to a single JWT issuer.                                                                                                        |
|  21 | Workload API available on all nodes.                                                                                                   |
|  22 | Provided exemplars (cron job, sidecar) and recommended spiffy helper for SVID consumption.                                             |
|  23 | Future plans: UI improvements, more exemplars, service mesh integration, X509, federation, and multi-cloud trust domains.              |
|  24 | Currently, only Kubernetes is supported, but non-Kube                                                                                  |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=EVbFeCipis8)
