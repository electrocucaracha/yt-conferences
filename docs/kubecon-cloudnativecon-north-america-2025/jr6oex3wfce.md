---
type: Video Note
title: "Zero Downtime Migration of Monolith To K8s Using Sidecar and Contai... Deepak Kosaraju & James Dabbs"
description: "James and Deepak from Procore shared their experience migrating a large, legacy Rails monolith and its surrounding microservices to Kubernetes, highlighting both the challenges and solutions they encountered. They described the initial pain..."
resource: https://www.youtube.com/watch?v=jR6Oex3wFCE
tags: ["kubecon-cloudnativecon-north-america-2025", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

James and Deepak from Procore shared their experience migrating a large, legacy Rails monolith and its surrounding microservices to Kubernetes, highlighting both the challenges and solutions they encountered.
They described the initial pain points of their autoscaling group-based deployments, which were inefficient and difficult to change due to bespoke scripts and accumulated technical debt.
Their migration strategy focused on using open-source, CNCF-aligned tools, GitOps practices with Argo CD, and consistent declarative tagging for observability and auditing.
Key technical lessons included tuning deployment and health check settings to accommodate slow application startup and shutdown, iterating on pod termination strategies to achieve zero-downtime rollouts, and adapting autoscaling behaviors to match dynamic traffic patterns.
They emphasized the importance of executive support, robust observability, and iterative testing in lower environments, ultimately achieving reliable, rapid deployments across multiple clusters with minimal customer impact.
The team also contributed improvements back to open-source projects and encouraged others to experiment with their shared demo code.
# Main Points

|   # | Main point                                                                                                                                                                                                                                   |
| --: | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | James and Deepak from Procore shared their journey migrating a legacy Rails monolith (Cornerstone) to Kubernetes.                                                                                                                            |
|   2 | Procore serves a wide range of construction customers; Cornerstone is core, with 90+ teams and ~9 deploys/day.                                                                                                                               |
|   3 | Legacy deployment used autoscaling groups with inefficient, wasteful scaling only at deploy time.                                                                                                                                            |
|   4 | Legacy system relied on bespoke, hard-to-change scripts, leading to technical debt and fear of change.                                                                                                                                       |
|   5 | The migration aimed to improve scaling behavior without impacting deploy cadence or causing outages/incidents.                                                                                                                               |
|   6 | Executive support was crucial for foundational rework, but required careful risk management.                                                                                                                                                 |
|   7 | Six-month timeline: five months on foundational work, then iterative improvements.                                                                                                                                                           |
|   8 | Design principles: use CNCF/open-source components, avoid bespoke solutions, prioritize agility and flexibility, GitOps-first (Argo CD), minimal Terraform for control plane, consistent declarative tagging for observability and auditing. |
|   9 | Deployment uses Helm for overrides, Argo CD for bootstrapping controllers/CRDs, and homegrown solutions for app deployment.                                                                                                                  |
|  10 | Key Kubernetes primitives: pods, services, ingress/gateway controllers, endpoint slices.                                                                                                                                                     |
|  11 | Learned to tune maxSurge, maxUnavailable, rollout strategy, and Karpenter batch idle duration to optimize deploys and avoid unnecessary node creation.                                                                                       |
|  12 | Health probes: startup probe failure threshold set to 2x average boot time; liveness probe period not more frequent than readiness.                                                                                                          |
|  13 | Leveraged container lifecycle hooks for graceful connection termination; iterated preStop logic to avoid 503 errors during deploys.                                                                                                          |
|  14 | Migrated from static sleep-based preStop to dynamic Envoy health check fail, ensuring zero-downtime rolling updates.                                                                                                                         |
|  15 | Moved from ingress controllers to Gateway API (Envoy Gateway), reducing endpoint update time from 30s to <3s.                                                                                                                                |
|  16 | Adopted KEDA for dynamic scaling; observed HPA sync period limitations in EKS; fallback set to 80% of max replicas for reliability.                                                                                                          |
|  17 | Use Argo Rollouts for canary                                                                                                                                                                                                                 |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=jR6Oex3wFCE)