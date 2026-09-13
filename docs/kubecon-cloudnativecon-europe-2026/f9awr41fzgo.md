---
layout: default
title:
  "Project Lightning Talk: Beyond Guardrails: Resource Lifecycle Automation With
  Kyverno - Ammar Yasser"
nav_order: 253
parent: Kubecon Cloudnativecon Europe 2026
type: Video Note
description:
  Luke Mowski, a maintainer for Keveno, presents on behalf of a colleague
  at CubeCon, explaining how Keveno has evolved beyond its original use for blocking
  bad configurations. Using the example of "namespace as a service," he describes
  how K...
resource: https://www.youtube.com/watch?v=F9AwR41FzGo
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

Luke Mowski, a maintainer for Keveno, presents on behalf of a colleague at CubeCon, explaining how Keveno has evolved beyond its original use for blocking bad configurations.
Using the example of "namespace as a service," he describes how Keveno now supports advanced automation tasks such as creating ephemeral namespaces for testing, enforcing best practices, and managing resource lifecycles.
Recent updates have introduced new policy types: mutating policies to modify resources before they are stored, generating policies to automatically create related resources, and deleting policies to automate cleanup, such as implementing TTL-based deletions.
These YAML-based policies can be integrated into GitHub pipelines and repositories, providing auditable, code-free automation compared to custom controllers.
Luke emphasizes that Keveno is now a comprehensive platform automation tool, not just a guardrail solution, and invites attendees to a deeper session at Kanukon.

# Main Points

|   # | Main point                                                                                                                                                              |
| --: | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Luke Mowski is a maintainer for Keveno, presenting in place of Amaya Sir.                                                                                               |
|   2 | Keveno is commonly used for blocking bad configurations.                                                                                                                |
|   3 | Recent updates allow Keveno to do more than just blocking, including automation tasks.                                                                                  |
|   4 | Example use case: namespace as a service for creating ephemeral namespaces to test pull requests.                                                                       |
|   5 | Platform engineers want to follow best practices, create intermediate resources, and clean up after pull requests.                                                      |
|   6 | Traditional solution involves custom controllers, which require scalability, monitoring, and reporting.                                                                 |
|   7 | Keveno is a policy engine based on YAML and CEL, originally built for Kubernetes.                                                                                       |
|   8 | Keveno now supports use cases beyond Kubernetes, such as authorization.                                                                                                 |
|   9 | Integrated features include validation, reporting, and fine-grained exceptions.                                                                                         |
|  10 | Three main policies introduced:                                                                                                                                         |
|  11 | Mutating policy (stable in version 1.17): mutates resources before they reach the Kubernetes database to ensure compliance.                                             |
|  12 | Generating policy: creates specified resources (e.g., network policies, role bindings) when a namespace is created; updates or deletes resources if the policy changes. |
|  13 | Deleting policy: automates cleanup, such as deleting namespaces after a TTL, similar to a cleanup cron job.                                                             |
|  14 | These YAML policies can be managed in GitHub pipelines and repositories for auditing.                                                                                   |
|  15 | Keveno enables platform automation and complex workflows, not just guardrails.                                                                                          |
|  16 | Invitation to Kanukon event for a deeper talk on the topic.                                                                                                             |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=F9AwR41FzGo)
