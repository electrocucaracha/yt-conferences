---
type: Video Note
title: "GAMMA in Action: How Careem Migrated To Istio Without Downtime - Suren Raju & Sergey Marunich"
description: "The presentation details Kareem’s migration of its critical digital platform, which supports millions of users and partners across the Middle East, from a fragmented traffic management system using multiple service meshes to a unified archi..."
resource: https://www.youtube.com/watch?v=igJXmbwMYAc
tags: ["kubecon-cloudnativecon-north-america-2025", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

The presentation details Kareem’s migration of its critical digital platform, which supports millions of users and partners across the Middle East, from a fragmented traffic management system using multiple service meshes to a unified architecture based on Istio and Envoy, leveraging the Gateway API and Flagger for safe, invisible, and zero-downtime migration.
The team faced challenges due to operational friction from maintaining different stacks and sought a solution that provided cohesive architecture, advanced features, extensibility, and strong open-source community support.
The migration process was carefully designed to be fast, safe, and transparent, utilizing canary deployments, automated rollbacks, and extensive observability to ensure reliability for users who depend on the platform for essential services.
Key learnings included the importance of planning, testing, and understanding differences in data plane behavior, as well as the evolving nature of the Gateway API ecosystem and the need for ongoing reliability improvements post-migration.
The migration was completed in six weeks across five clusters and 700 services without downtime or major rewrites, but the team continues to address new challenges and refine their processes for future upgrades.
# Main Points

|   # | Main point                                                                                                                        |
| --: | --------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Presentation covers Kareem's migration to Istio service mesh without downtime                                                     |
|   2 | Kareem is a Middle East super app serving 75M+ customers, 3.5M+ captains, 10K+ restaurant partners in 70 cities, 10 countries     |
|   3 | Infrastructure: 700 active services, 5 EKS clusters, 2 AWS regions, 1B public API requests, 5B internal API requests daily        |
|   4 | Previous traffic platform was fragmented (Linkerd, Kong, other proxies), causing operational friction and inconsistent policies   |
|   5 | Migration goals: single cohesive architecture, more mesh features, extensible data plane, open source foundation                  |
|   6 | Chose Istio and Envoy for unified traffic management, reliability, and community support                                          |
|   7 | Migration needed to be fast, safe, and invisible to users and service owners                                                      |
|   8 | Considered parallel clusters but opted for in-cluster, gradual, batch-by-batch migration during low-traffic hours (3-6am)         |
|   9 | Used Gateway API (Gamma) and Flagger for automated, canary-based, safe migration                                                  |
|  10 | Flagger managed canary deployments, gradually shifting traffic and rolling back on failure                                        |
|  11 | Migration process: create DNS record, enable Istio injection, disable Linkerd, Flagger handles rollout and rollback if needed     |
|  12 | Observability: unified dashboards, anomaly alerts, access logs, extensive testing and dry runs                                    |
|  13 | Migration completed in 6 weeks across 5 clusters, 700 services, no downtime, no major deployment script changes                   |
|  14 | Key learnings: Gateway API simplifies migration but runtime parity issues exist (latency measurement, HTTP header handling, etc.) |
|  15 | Ecosystem is evolving; different Gateway API implementations support different spec versions                                      |
|  16 | Post-migration challenges: proxy OOM kills, ongoing reliability improvements, gateway migration still in progress                 |
|  17 | Flagger canary rollout used existing deployment process; canary and primary run at equal scale during rollout                     |
|  18 | Team handles 1B northbound and 5B mesh transactions daily                                                                         |
|  19 | Continuous improvement and upgrade procedures established for future migrations and revisions                                     |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=igJXmbwMYAc)