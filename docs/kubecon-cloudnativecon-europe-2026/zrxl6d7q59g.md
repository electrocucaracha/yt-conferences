---
layout: default
title:
  "Pay Less for More: A Practitioner's Playbook for Kubern... Malgorzata Widelicka
  & Lukasz Ogrodowczyk"
nav_order: 240
parent: Kubecon Cloudnativecon Europe 2026
type: Video Note
description:
  Ma Gojata and Gash, DevOps specialists at Roche, discuss their experiences
  managing large-scale cloud platforms in the highly regulated pharmaceutical sector,
  focusing on Kubernetes autoscaling. They describe the challenges of financial was...
resource: https://www.youtube.com/watch?v=ZRXl6d7Q59g
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

Ma Gojata and Gash, DevOps specialists at Roche, discuss their experiences managing large-scale cloud platforms in the highly regulated pharmaceutical sector, focusing on Kubernetes autoscaling.
They describe the challenges of financial waste from over-provisioned infrastructure, stability issues due to improper resource settings, and the complexities of maintaining compliance alongside DevOps agility.
By adopting the open-source Carpenter project for autoscaling, they optimized costs—achieving up to 90% reduction—by provisioning resources only when needed and tailoring node pools to workload requirements.
They emphasize the importance of observability, careful configuration, and aligning infrastructure scaling with application logic, sharing practical examples and lessons learned, such as managing node churn, optimizing cold starts, and balancing cost with performance and compliance.
The session concludes with key takeaways: customize configurations to workload needs, leverage observability for insights, and prioritize paying for execution over readiness.

# Main Points

|   # | Main point                                                                                                                                                                                                      |
| --: | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Ma Gojata and Gash are DevOps at Roche, specializing in cloud platforms and pharma R&D.                                                                                                                         |
|   2 | Roche is a global pharma company with over 100,000 employees, founded in Basel 130 years ago.                                                                                                                   |
|   3 | Ma works on the Envelope platform supporting data scientists in drug discovery, generating 150 million predictions and retraining 300 models monthly.                                                           |
|   4 | Gash works on the Ocean platform for data and analytics in GXP and non-GXP clinical trials, processing about half a petabyte of data.                                                                           |
|   5 | Both platforms contribute to different stages of drug development: discovery and clinical trials.                                                                                                               |
|   6 | Main infrastructure pain points: financial waste (paying for readiness), stability failures (out of memory), lack of flexibility (spot instances, quotas), and maintenance challenges (multi-cluster upgrades). |
|   7 | DevOps and compliance have conflicting priorities; CNCF tools bridge the gap.                                                                                                                                   |
|   8 | Heavy workloads (e.g., backup jobs) require proper requests/limits and are good candidates for cluster autoscaling.                                                                                             |
|   9 | Moved from static node groups to provisioning infrastructure only for job execution, scaling to zero between runs.                                                                                              |
|  10 | Use Carpenter (CNCF project) for autoscaling; key concepts include node pools, expire_after, instance types, and consolidation.                                                                                 |
|  11 | On-demand instances for critical workloads; spot instances for fault-tolerant workloads; node weights set priorities.                                                                                           |
|  12 | Carpenter's consolidation engine optimizes costs by bin-packing and removing underutilized nodes.                                                                                                               |
|  13 | Observability is crucial; capacity vs. utilization shows waste; aim for 90% utilization.                                                                                                                        |
|  14 | Carpenter reduced pod pending time from ~5 minutes to ~1 minute compared to Cluster Autoscaler.                                                                                                                 |
|  15 | Optimized startup time by shrinking Docker images, optimizing code, upgrading Kubernetes/Carpenter, and using optimized AMIs.                                                                                   |
|  16 | Achieved up to 90% cost reduction, mainly by right-sizing Carpenter and paying for execution, not readiness.                                                                                                    |
|  17 | Observability platforms can incur high costs due to Carpenter metrics (metric cardinality).                                                                                                                     |
|  18 | Node churn (frequent node c                                                                                                                                                                                     |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=ZRXl6d7Q59g)
