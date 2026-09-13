---
layout: default
title:
  "Reimagining Insurance Infrastructure: CopperPoint's Cloud Native Blueprint
  - Sid Dixit & Sham Rao"
nav_order: 257
parent: Kubecon Cloudnativecon North America 2025
type: Video Note
description:
  In this presentation, Sid Dixit and Shamar Rao from Copper Point Insurance
  discuss their company’s transition to a cloud native architecture, emphasizing the
  unique challenges of operating in the regulated insurance industry. They detail
  Co...
resource: https://www.youtube.com/watch?v=jQRpHOm4Vts
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

In this presentation, Sid Dixit and Shamar Rao from Copper Point Insurance discuss their company’s transition to a cloud native architecture, emphasizing the unique challenges of operating in the regulated insurance industry.
They detail Copper Point’s growth from a single-state insurer to a multi-state, multi-product company, and their recent migration from on-premises systems to the cloud, leveraging CNCF principles such as containerization, microservices, and event-driven design.
The team highlights the development of a modular integration layer called Wild Donkey, extensive use of reusable APIs and data pipelines, and a hybrid architecture that balances cloud flexibility with core system reliability.
They share lessons learned from past missteps with vendor lock-in and overly granular microservices, advocating for a pragmatic, “molecular” approach to architecture, heavy automation, and in-house expertise development.
The speakers recommend starting simple, empowering teams, avoiding vendor lock-in, leveraging AI and automation, and abstracting cloud dependencies to ensure scalability, cost-effectiveness, and maintainability as the company continues to grow.

# Main Points

|   # | Main point                                                                                                                                                                                                                     |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   1 | Copper Point is an insurance company, originally a single-state, single-line business from Phoenix, Arizona, founded in 1925.                                                                                                  |
|   2 | Became privatized, mutualized, and expanded through acquisitions: Pacific Compensation (2017) and Alaska National Corporation (2019).                                                                                          |
|   3 | Expanded to multiple states and business lines beyond workers compensation, including property and commercial auto.                                                                                                            |
|   4 | In 2023, migrated all workloads from on-premises to cloud, integrating acquired systems.                                                                                                                                       |
|   5 | Aims to remain cost-effective, unlock cloud innovation (including AI/GenAI), and provide superior experiences to agents, brokers, and policyholders.                                                                           |
|   6 | Cloud-native architecture designed for compliance, resilience, and trust, adhering to CNCF principles: containerization, microservices, composable and event-driven design.                                                    |
|   7 | Production environment includes 100+ integrations, 100+ reusable APIs, 600+ job pipelines, and 500+ data pipelines.                                                                                                            |
|   8 | Core systems use Guidewire (SaaS), with integrations powered by an in-house layer called Wild Donkey.                                                                                                                          |
|   9 | Real-time data streaming via Kafka to Databricks, with data replicated to on-prem EDW using Fivetran.                                                                                                                          |
|  10 | Uses AWS EKS for microservices (Quarkus), Jenkins for CI/CD, Grafana for logging, Cast AI for autoscaling, Octa for authentication, Keeper for secrets, Amazon Aurora for database, S3 for storage, and SNS for notifications. |
|  11 | Hybrid architecture combines cloud flexibility and core system reliability, starting simple and modular for future scalability.                                                                                                |
|  12 | Past challenges included legacy monolithic Java app, vendor PaaS limitations, and high licensing costs.                                                                                                                        |
|  13 | Migrated to Kubernetes, requiring organizational change and upskilling.                                                                                                                                                        |
|  14 | Focus on building reusable components (database, message queues, secrets, storage, integration patterns).                                                                                                                      |
|  15 | Strives to bring expertise in-house, reduce vendor lock-in, and empower teams.                                                                                                                                                 |
|  16 | Lessons learned: avoid overcomplicating with microservices, automate developer environments, use Linux and Visual Studio Code, and script everything (preferably                                                               |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=jQRpHOm4Vts)
