---
type: Video Note
title: "Crossplane - The Cloud Native Framework for Platform Engineering - Jared Watts & Nic Cope, Upbound"
description: "In this twice-annual update, Nick and Jared, maintainers of Crossplane, introduce the project as a framework for building control planes and custom Kubernetes APIs without writing controllers, enabling platform teams to provide developer se..."
resource: https://www.youtube.com/watch?v=XKUi8xxkyjM
tags: ["kubecon-cloudnativecon-north-america-2025", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

In this twice-annual update, Nick and Jared, maintainers of Crossplane, introduce the project as a framework for building control planes and custom Kubernetes APIs without writing controllers, enabling platform teams to provide developer self-service with guardrails.
They highlight Crossplane’s recent graduation as a CNCF project, its widespread adoption, and the release of Crossplane v2, which brings major changes such as namespaced resources by default, simplified composition, removal of claims, and activation policies for more granular CRD management.
Nick demonstrates how to define and compose custom resources using various languages, emphasizing Crossplane’s flexibility and ease of use.
Jared then introduces new features in v2, including "operations" for day-2 management tasks and "circuit breakers" to prevent reconciliation loops that can overload clusters.
The session concludes with a discussion of future plans, such as improving the package manager, enhancing developer tooling, supporting migration from v1 to v2, and maturing new features, followed by a Q&A addressing technical details about managed resources, activation policies, metrics, and the adoption of alpha features.
# Main Points

|   # | Main point                                                                                                                                                                                                     |
| --: | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Crossplane is a framework for building control planes and custom Kubernetes APIs without writing controllers.                                                                                                  |
|   2 | Enables platform engineering teams to create abstractions for developer self-service, reducing reliance on ticket ops or giving full admin access.                                                             |
|   3 | Crossplane is now a CNCF graduated project, in the top 10% for contributors, and widely adopted in production.                                                                                                 |
|   4 | Control planes provide continuous reconciliation, declarative APIs, and developer self-service with guardrails.                                                                                                |
|   5 | Crossplane v2 released (and v2.1), backward compatible with v1.x.                                                                                                                                              |
|   6 | Major v2 changes: resources are namespaced by default, can compose any resources (not just Crossplane), less opinionated usage, claims removed, activation policies introduced for selective CRD installation. |
|   7 | Composition allows users to define composite resources (XRs) that abstract lower-level resources (e.g., deployment, service, RDS instance).                                                                    |
|   8 | Supports multiple configuration languages for compositions (YAML, templated YAML, Python, KCL).                                                                                                                |
|   9 | Crossplane provides a large library of managed resources (controllers for cloud resources, etc.), all namespaced in v2.                                                                                        |
|  10 | Package manager enables easy installation of functions, providers, and configurations.                                                                                                                         |
|  11 | Operations: new alpha feature in v2 for day-2 management tasks (backups, upgrades, maintenance) via function pipelines; supports vanilla, cron, and watch operations.                                          |
|  12 | Circuit breakers (introduced in v2.1) prevent runaway reconciliation loops by throttling excessive updates, protecting the API server.                                                                         |
|  13 | Future plans: improve package manager reliability, enhance developer tooling, provide migration guidance from v1 to v2, mature features to GA.                                                                 |
|  14 | Namespaced resources in v2 use "M" in API group for "managed."                                                                                                                                                 |
|  15 | Managed resource activation policies allow selective CRD installation; must be set before provider install.                                                                                                    |
|  16 | Circuit breaker emits Prometheus metrics.                                                                                                                                                                      |
|  17 | Operations feature is alpha; enable via feature flag; functions for operations are organization-specific.                                                                                                      |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=XKUi8xxkyjM)