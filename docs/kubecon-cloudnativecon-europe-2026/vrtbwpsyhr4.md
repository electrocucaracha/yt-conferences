---
type: Video Note
title: "Kill the Ticket Queue: A CNCF Blueprint for Self-Service Platfor... Bhavani Indukuri & Aparna Prabhu"
description: "In this talk, Bhavani Indukuri and Aparna Prabhu from DigitalOcean describe how their team transformed the developer experience by replacing a slow, ticket-based environment provisioning process with a self-service platform. Previously, dev..."
resource: https://www.youtube.com/watch?v=vrtBWPSyhr4
tags: ["kubecon-cloudnativecon-europe-2026", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

In this talk, Bhavani Indukuri and Aparna Prabhu from DigitalOcean describe how their team transformed the developer experience by replacing a slow, ticket-based environment provisioning process with a self-service platform.
Previously, developers faced long delays—up to seven days—due to manual back-and-forth between multiple teams and lack of automation, resulting in high ticket volumes and inefficient use of platform team resources.
By leveraging CNCF projects such as Backstage for a unified developer portal, Argo Events and Argo Workflows for event-driven automation, vcluster for lightweight, isolated Kubernetes environments, and Kyverno for automated policy enforcement and guardrails, they built a scalable, declarative, and observable platform.
This new system enables developers to provision environments in under ten minutes, enforces resource and security policies automatically, and provides robust observability with Prometheus and Grafana.
As a result, they achieved a 90% reduction in infrastructure tickets, significant cost savings, and freed platform teams to focus on innovation rather than support, ultimately delivering a much improved developer experience.
# Main Points

|   # | Main point                                                                                                                                                                                                 |
| --: | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | The previous environment provisioning process was manual, slow, and required multiple teams, taking up to seven days per request.                                                                          |
|   2 | Over 200 tickets per month overwhelmed the platform team, reducing time for innovation.                                                                                                                    |
|   3 | Manual security reviews and lack of automation made the process unscalable and inefficient.                                                                                                                |
|   4 | A self-service platform was built using DigitalOcean Kubernetes clusters, with a control plane and worker clusters.                                                                                        |
|   5 | Developers use Backstage as a unified portal to request environments via templates.                                                                                                                        |
|   6 | Backstage emits webhook events, triggering Argo Events and Argo Workflows for event-driven automation.                                                                                                     |
|   7 | Argo Events decouples UI from orchestration, supports multiple event sources, and ensures reliable event processing.                                                                                       |
|   8 | Argo Workflows orchestrates the provisioning process, supports DAGs, retries, idempotency, and is fully declarative for GitOps.                                                                            |
|   9 | vcluster provides lightweight, cost-effective, and isolated Kubernetes environments for multi-tenancy.                                                                                                     |
|  10 | Kyverno enforces guardrails as code, including CPU/memory limits, ownership, label enforcement, trusted registries, blocking privileged containers, network isolation, and TTL-based lifecycle management. |
|  11 | Observability is implemented using Prometheus, Grafana, and VictoriaMetrics, with ongoing improvements and integration with OpenTelemetry.                                                                 |
|  12 | Key lessons learned: design for failure, automate lifecycle management, and evolve policies to balance security and developer freedom.                                                                     |
|  13 | Provisioning time reduced from days to under 10 minutes; 90% reduction in infra tickets; infrastructure costs reduced by over 50%.                                                                         |
|  14 | Platform teams are freed from support tasks, enabling more innovation.                                                                                                                                     |
|  15 | The system is scalable, automated, and provides a better developer experience.                                                                                                                             |
|  16 | The platform supports further automation and unified experiences beyond environment provisioning.                                                                                                          |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=vrtBWPSyhr4)