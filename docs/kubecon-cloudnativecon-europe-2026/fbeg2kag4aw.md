---
layout: default
title:
  "Kubernetes Security at Shopify Scale: Automating Security Across an Infrastr...
  Jie Wu & Pulkit Garg"
nav_order: 195
parent: Kubecon Cloudnativecon Europe 2026
type: Video Note
description:
  In this presentation, Jay and Pulkit from Shopify’s infrastructure security
  team describe how they secure Kubernetes at scale for millions of merchants. They
  explain that Shopify operates hundreds of Kubernetes clusters and processes nearly...
resource: https://www.youtube.com/watch?v=fBEG2kag4Aw
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

In this presentation, Jay and Pulkit from Shopify’s infrastructure security team describe how they secure Kubernetes at scale for millions of merchants.
They explain that Shopify operates hundreds of Kubernetes clusters and processes nearly 60,000 deploys weekly, with all configurations managed in a single monorepo, which poses significant risk if misconfigurations occur.
To address this, they implemented automated static code analysis using an open-source tool called Semgrep, which scans pull requests for critical misconfigurations—such as privileged containers, missing resource limits, and insecure host access—before code is merged.
They emphasize the importance of balancing security with developer productivity by providing clear, actionable guidance and documentation, and by iteratively refining rules with the help of AI to reduce false positives and ensure relevance.
The team also uses OPA for policy enforcement beyond Kubernetes, and highlights the value of collaboration, continuous improvement, and making the secure path the easiest for developers, resulting in a significant reduction in incidents and improved overall security posture.

# Main Points

|   # | Main point                                                                                                                                            |
| --: | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Presentation on securing Kubernetes at Shopify by Jay and Pulkit from the infrastructure security team                                                |
|   2 | Shopify runs hundreds of services on Kubernetes, with nearly 60,000 deploys weekly and about 500 clusters globally                                    |
|   3 | All Kubernetes manifests, Helm charts, and deploy configs are managed in a single infrastructure monorepo, creating a single source of truth and risk |
|   4 | Developers make frequent changes; misconfigurations can easily multiply across hundreds of manifest files via Helm                                    |
|   5 | Misconfigurations (e.g., privileged containers, missing resource limits) can slip through code reviews and reach production                           |
|   6 | Over 1,000 PRs merged weekly; manual review couldn't keep up, leading to incidents                                                                    |
|   7 | Team set goals: catch misconfigs in CI, add rules pre-deploy, maintain developer productivity, and educate developers with clear guidance             |
|   8 | Introduced "Samrap Cat," an open-source static code analysis tool (semgrep) to detect misconfigurations automatically in CI                           |
|   9 | Key rules: block privileged containers, require CPU/memory limits, prevent host access (hostNetwork, hostPID, hostIPC)                                |
|  10 | Additional rules address supply chain risks (e.g., image tags set to "latest") and missing authentication                                             |
|  11 | Developers receive clear, actionable feedback and guidance to remediate issues                                                                        |
|  12 | Good configurations are also multiplied across all manifests, improving security at scale                                                             |
|  13 | Rules are tested in warning/dry-run mode, monitored for false positives, and iterated with app teams                                                  |
|  14 | OPA/Gatekeeper used for cluster-level enforcement and Terraform; both semgrep and OPA complement each other                                           |
|  15 | AI used to refine rules, reduce false positives, and benchmark against security frameworks; reduced findings by 88%                                   |
|  16 | Over 50 rules and 13 OPA policies shipped in 6 weeks; zero incidents after rollout                                                                    |
|  17 | Key lessons: start in warn mode, address false positives quickly, provide clear remediation steps, make secure path the easiest path                  |
|  18 | Security is now built into the developer workflow, with continuous improvemen                                                                         |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=fBEG2kag4Aw)
