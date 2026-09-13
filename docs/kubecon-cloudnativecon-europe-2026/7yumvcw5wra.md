---
layout: default
title:
  "Advanced Kyverno Patterns : Automating Platform Security and Ope... Frank
  Jogeleit & Johannes Sonner"
nav_order: 16
parent: Kubecon Cloudnativecon Europe 2026
type: Video Note
description:
  In this session, Frank and Johannes introduce Kyverno, a Kubernetes-native
  policy engine, highlighting its advanced features for automating platform security
  and operations. Kyverno extends beyond Kubernetes’ built-in admission policies by...
resource: https://www.youtube.com/watch?v=7YuMvcW5wRA
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

In this session, Frank and Johannes introduce Kyverno, a Kubernetes-native policy engine, highlighting its advanced features for automating platform security and operations.
Kyverno extends beyond Kubernetes’ built-in admission policies by offering robust reporting, resource generation, cleanup, and fine-grained exception handling, all using familiar YAML and CEL expressions.
Johannes shares practical use cases from Deutsche Telekom, such as automating namespace role bindings based on labels for self-service access control, integrating with tools like Crossplane and Pulumi to automate infrastructure tasks without custom scripts, and leveraging Kyverno’s mutating policies to optimize workflows like dependency caching.
The speakers emphasize Kyverno’s value not only for security but also for holistic infrastructure automation and compliance reporting, enabling scalable governance and self-service in large organizations.
They conclude with a roadmap update, mentioning improvements to the CLI, a new reporting standard, and the deprecation of older policy formats, inviting users to engage with the project and its community.

# Main Points

|   # | Main point                                                                                                                                             |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   1 | Kyverno is an admission controller for Kubernetes, acting as a validating and mutating webhook.                                                        |
|   2 | It can validate, mutate, generate, and clean up resources, including existing workloads.                                                               |
|   3 | Kyverno offers advanced reporting to track policy compliance over time.                                                                                |
|   4 | Supports resource generation, such as auto-generating quotas and synchronizing secrets across namespaces.                                              |
|   5 | Provides cleanup policies to remove unnecessary resources based on labels or expressions.                                                              |
|   6 | API and expression language (CEL) are similar to Kubernetes built-in policies, with additional libraries for extended use cases.                       |
|   7 | Enables image verification and HTTP requests in policy execution.                                                                                      |
|   8 | Can be used as a command-line tool for validating any JSON payload, including Dockerfiles and Terraform files.                                         |
|   9 | Offers an OPA-Envoy plugin for validating Envoy requests and HTTP requests.                                                                            |
|  10 | Easy to learn for Kubernetes users, uses YAML and CEL for policy definitions.                                                                          |
|  11 | Fine-grained exception handling allows excluding resources from policies without changing the policy itself.                                           |
|  12 | Designed specifically for Kubernetes environments.                                                                                                     |
|  13 | Use case: Automates RBAC role bindings in ephemeral namespaces based on labels, enabling teams to manage access dynamically.                           |
|  14 | Use case: Automates certificate chain updates in Crossplane resources by mutating resources to fetch and inject certificates, avoiding custom scripts. |
|  15 | Use case: Injects persistent volumes into Pulumi stacks for dependency caching, speeding up deployments.                                               |
|  16 | Enables mutating Kubernetes resources for configuration, scaling, and labeling without manual intervention.                                            |
|  17 | Provides compliance and reporting through Policy Reporter, integrating with observability stacks like Grafana.                                         |
|  18 | Policies can run in audit mode for non-enforcing compliance checks.                                                                                    |
|  19 | Supports tiered compliance reporting with opt-in/opt-out via labels.                                                                                   |
|  20 | Policies are distributed via Helm charts and GitOps workflows.                                                                                         |
|  21 | Kyverno is not just a security tool; it is used for holistic infrastructure automation.                                                                |
|  22 | Emph                                                                                                                                                   |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=7YuMvcW5wRA)
