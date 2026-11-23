---
layout: default
title: Manage your OpenStack resources from Kubernetes with ORC
nav_order: 38
parent: OpenInfra Summit Europe 2025
type: Video Note
description: "The OpenStack Resource Controller (ORC) is a Kubernetes-native project that provides a declarative API for managing OpenStack resources, addressing the imperative nature of traditional OpenStack in..."
resource: "https://www.youtube.com/watch?v=c1AHmV0DDGo"
youtube_stats:
  view_count: 187
  like_count: 4
  channel_subscriber_count: 46800
tags:
  - openinfra-summit-europe-2025
  - video
  - learning
status: stable
generated:
  by: process:yt-summarizer-okf
  at: 2026-11-22T23:38:50+00:00
---

# Summary

The OpenStack Resource Controller (ORC) is a Kubernetes-native project that provides a declarative API for managing OpenStack resources, addressing the imperative nature of traditional OpenStack interfaces.
Built on the Go for Cloud SDK, ORC allows users to define desired infrastructure states using Custom Resource Definitions, which the controller reconciles against the actual cloud environment.
The system enforces strict dependency management by referencing resources via Kubernetes names rather than OpenStack IDs, ensuring that operations like subnet creation or network deletion occur in the correct sequence and preventing unintended changes.
ORC distinguishes between managed resources, where it controls the full lifecycle, and unmanaged resources, which are imported via filters to represent externally created shared infrastructure.
While similar to other cloud orchestration tools like Crossplane or AWS ASO, ORC offers a streamlined, OpenStack-specific solution that is already used in production by projects such as CAPO and Red Hat’s HyperShift to manage complex resource lifecycles like images.

# Main Points

|   # | Main point                                                                                                                                                              |
| --: | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | OpenStack Resource Controller (ORC) is a Kubernetes-native set of controllers and custom resource definitions for managing OpenStack resources declaratively.           |
|   2 | ORC is built on top of the Go for Cloud SDK and follows Kubernetes conventions, including semantic versioning and deterministic operations.                             |
|   3 | The project originated from a prototype by K and engineers, was integrated into the Cluster API Provider OpenStack (CAPO), and later split out as a standalone project. |
|   4 | ORC distinguishes between managed resources, where it controls the full lifecycle, and unmanaged resources, which are imported via filters and managed externally.      |
|   5 | Dependency management is handled by referencing resources by Kubernetes name, ensuring objects exist before dependent resources are created or deleted.                 |
|   6 | ORC avoids unnecessary API calls to OpenStack, only interacting when Kubernetes objects are created, updated, or deleted, and does not currently detect external drift. |
|   7 | Users can define resources like networks and subnets using YAML, where ORC ensures consistency, retries failures, and enforces dependency order.                        |
|   8 | ORC supports GitOps workflows, such as integration with Argo CD, to reconcile infrastructure definitions against the underlying cloud state.                            |
|   9 | The tool can be used as an orchestrator to create complex OpenStack environments in the correct sequence, potentially replacing tools like Heat or Terraform.           |
|  10 | ORC can be embedded as a library in other controllers, such as CAPO and Red Hat HyperShift, to manage image lifecycles and handle complex API corner cases.             |
|  11 | Compared to AWS and GCP equivalents, ORC currently lacks drift detection and multi-instance controller support but aims to adopt similar features.                      |
|  12 | Unlike Crossplane, which uses Terraform, ORC interacts directly with OpenStack via Go for Cloud, reducing complexity and allowing direct bugfixes in the SDK.           |
|  13 | ORC currently has controllers for most core OpenStack resources, and a generator tool simplifies the creation of new controllers.                                       |
|  14 | The project team is small but active, with maintainers also contributing to Go for Cloud to fix issues discovered during ORC development.                               |
|  15 | The community is encouraged to provide feedback, contribute code, and help develop Helm charts, with support available via the OpenStack Slack channel.                 |
|  16 | Cascading deletions are handled using finalizers, preventing the deletion of parent resources like projects until all dependent resources are removed.                  |

# Video

[![Video thumbnail](https://img.youtube.com/vi/c1AHmV0DDGo/hqdefault.jpg)](https://www.youtube.com/watch?v=c1AHmV0DDGo)

[Watch on YouTube](https://www.youtube.com/watch?v=c1AHmV0DDGo)
