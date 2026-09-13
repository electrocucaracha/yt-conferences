---
type: Video Note
title: "Inside Saxo Service Blueprint: Implementing Kubernetes Operators for Legacy Ent... Oskar Kristiansen"
description: "Oscar Christensen, a senior enterprise platform engineer at Saxo Bank, describes the development of the Saxo service blueprint, a system designed to modernize and automate infrastructure and IAM provisioning using Kubernetes operators and G..."
resource: https://www.youtube.com/watch?v=D6c5lsOz38U
tags: ["kubecon-cloudnativecon-europe-2026", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

Oscar Christensen, a senior enterprise platform engineer at Saxo Bank, describes the development of the Saxo service blueprint, a system designed to modernize and automate infrastructure and IAM provisioning using Kubernetes operators and GitOps.
Saxo Bank, a complex and highly regulated financial institution with a mix of legacy and modern systems, previously relied on a manual, ticket-based process for provisioning services, which was slow and lacked transparency.
The new approach allows developers to define service requirements in a YAML file, submit a pull request, and have the platform automatically handle provisioning across all environments, integrating with both cloud-native and traditional infrastructure.
The system uses custom operators to manage resources such as namespaces, service accounts, Kafka ACLs, app registrations, and network policies, ensuring idempotency and supporting disaster recovery by leveraging Git as the source of truth.
Transparency and developer experience are enhanced through integration with Backstage and an AI assistant, Eva, which provides real-time status and guidance, enabling a small team to efficiently manage complex infrastructure across multiple domains.
# Main Points

|   # | Main point                                                                                                                                        |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Saxo Bank is a systemically important financial institution in Denmark with 1.4 million clients, 12 offices, and over 2,400 employees.            |
|   2 | The bank offers complex financial products, operates globally, and manages over 71,000 financial instruments.                                     |
|   3 | Legacy infrastructure and applications, along with compliance demands, create challenges for modernization.                                       |
|   4 | Previously, infrastructure provisioning required multiple tickets/emails across five teams, causing delays and lack of transparency.              |
|   5 | The new system uses Kubernetes operators and GitOps to automate and modernize infrastructure and IAM provisioning.                                |
|   6 | Developers now write a YAML file describing service needs, open a PR, and after approval, the platform provisions all dependencies automatically. |
|   7 | The platform supports both cloud-native (Kubernetes) and traditional workloads, accommodating legacy systems that can't be containerized.         |
|   8 | All service definitions are stored in a single Git repository, with environment-specific overrides.                                               |
|   9 | A verifier service checks PRs for structure, uniqueness, and security, and assigns appropriate reviewers.                                         |
|  10 | Lifecycle management allows lightweight reviews for dev/test and stricter reviews for production deployment.                                      |
|  11 | Operators consume both service and infrastructure catalogs to automate provisioning.                                                              |
|  12 | The blueprint engine converts YAML files into Kubernetes custom resources, which are reconciled by operators.                                     |
|  13 | Operators handle namespace creation, service accounts, AD groups, Kafka ACLs, app registrations, network policies, and more.                      |
|  14 | Custom operators are used for internal systems where standard tools like Crossplane or Terraform are insufficient.                                |
|  15 | The system is designed for idempotency and disaster recovery; clusters can be rebuilt from Git repositories.                                      |
|  16 | Small team automates across many domains by integrating with existing expert team interfaces.                                                     |
|  17 | Some resources (e.g., microservice DB access, DNS, certificates) are managed by dev teams using Helm charts and cloud-native too                  |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=D6c5lsOz38U)