---
type: Video Note
title: "Spin-Up, Test, Tear-Down: How Trivago Runs Developer Preview Environm... Armin Aminian & Jan Wozniak"
description: "In this presentation, Armen, S, and Jan from Trivago discuss how they manage developer preview environments at scale to support over 200 engineers and hundreds of pull requests daily. Trivago, a travel meta-search engine with over 100 micro..."
resource: https://www.youtube.com/watch?v=_stuEBA4nK0
tags: ["kubecon-cloudnativecon-europe-2026", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

In this presentation, Armen, S, and Jan from Trivago discuss how they manage developer preview environments at scale to support over 200 engineers and hundreds of pull requests daily.
Trivago, a travel meta-search engine with over 100 microservices deployed across three regions on GKE Kubernetes, faced challenges with traditional staging environments, such as resource contention and unreliable tests.
To address this, they implemented automated, isolated preview environments for each pull request, leveraging Kubernetes, Argo CD, and KEDA for cost-efficient scaling, including scale-to-zero capabilities.
The team details their journey from using GCP Cloud Run for frontend previews to unifying their platform on Kubernetes, overcoming technical hurdles with KEDA’s HTTP add-on, and collaborating with the open-source community to improve scaling for both backend and frontend services.
Their solution enables rapid, confident feature delivery, minimizes incidents, and maintains cost efficiency, with all processes automated through CI/CD pipelines and dynamic environment provisioning.
# Main Points

|   # | Main point                                                                                                                             |
| --: | -------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Trivago is a travel meta search engine comparing accommodation prices across multiple OTAs.                                            |
|   2 | Infrastructure consists of 100+ microservices deployed across three regions on GKE Kubernetes clusters.                                |
|   3 | Developer preview environments are used to test changes before merging to production.                                                  |
|   4 | Traditional staging environments are inefficient at scale due to conflicts and blocking among 200+ developers and 100+ active PRs.     |
|   5 | Preview environments are automatically deployed per pull request via CI pipelines, providing isolated testing and integration.         |
|   6 | Only the changed service is deployed in the preview environment, connecting to dependencies in staging.                                |
|   7 | Preview environments enable early issue detection, easy sharing with QA/stakeholders, and confident merges.                            |
|   8 | Initial frontend previews ran on GCP Cloud Run (cost-effective, request-based billing, but expensive at scale and split architecture). |
|   9 | Goal: unify all previews on Kubernetes for both frontend and backend, but Kubernetes doesn’t natively scale to zero.                   |
|  10 | KEDA (Kubernetes Event-driven Autoscaling) is used to enable scale-to-zero for preview environments.                                   |
|  11 | HTTP add-on for KEDA allows scaling based on HTTP traffic, using an interceptor to proxy requests and manage cold starts.              |
|  12 | Trivago contributed to the HTTP add-on project, adding gRPC support via their Go Zero tool.                                            |
|  13 | Preview environments are managed with Argo CD ApplicationSet, using PR and generator triggers for dynamic deployment.                  |
|  14 | PR environments are created on PR open, deleted on merge, and idle environments scale to zero automatically.                           |
|  15 | Stack includes Argo CD, KEDA, Helm, and automated workflows; no more Cloud Run.                                                        |
|  16 | Over 200 engineers can work simultaneously with cost-efficient, unified preview environments.                                          |
|  17 | KEDA is also used for Kafka-based autoscaling in production.                                                                           |
|  18 | Most preview environments are stateless; data is read-only from databases.                                                             |
|  19 | CI/CD is used for building, testing, and deploying previews to ensure parity with production processes.                                |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=_stuEBA4nK0)