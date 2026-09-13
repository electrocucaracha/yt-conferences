---
layout: default
title:
  Crossplane - The Cloud Native Framework for Platform Engineering - Jared Watts
  & Adam Wolfe Gordon
nav_order: 79
parent: Kubecon Cloudnativecon Europe 2026
type: Video Note
description:
  Jared and Adam, core maintainers of the Crossplane project, introduce
  Crossplane as a control plane framework that enables platform teams to build self-service
  infrastructure APIs for developers, reducing deployment wait times and complexit...
resource: https://www.youtube.com/watch?v=zu6V34BFksk
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

Jared and Adam, core maintainers of the Crossplane project, introduce Crossplane as a control plane framework that enables platform teams to build self-service infrastructure APIs for developers, reducing deployment wait times and complexity.
They explain key Crossplane concepts such as composite resource definitions (XRDs), compositions, and managed resources, which allow developers to request infrastructure through simple APIs while the platform team ensures best practices and compliance.
The session highlights recent milestones, including Crossplane’s graduation within CNCF and the release of Crossplane V2, which introduces improvements like default namespacing and broader composability.
Adam demonstrates new developer experience enhancements, particularly control plane projects, which streamline the development, testing, and packaging of Crossplane platforms by consolidating APIs, compositions, and functions—now writable in various languages—into a single project structure.
Jared then showcases advancements in Crossplane metrics, detailing a new, flexible approach to observability that allows users to monitor resources at granular levels without overwhelming monitoring systems, thanks to integration with the resource state metrics project.
The session concludes with an invitation for community contributions and engagement.

# Main Points

|   # | Main point                                                                                                                                                                                         |
| --: | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Jared and Adam are core maintainers of the Crossplane project.                                                                                                                                     |
|   2 | Session covers foundational knowledge and latest developments in Crossplane.                                                                                                                       |
|   3 | Developers often face delays and complexity when deploying new services due to infrastructure and compliance requirements.                                                                         |
|   4 | Crossplane enables building platforms that expose simple APIs for developers to request infrastructure.                                                                                            |
|   5 | Crossplane is a control plane framework for building platforms and control planes, emphasizing self-service with guardrails.                                                                       |
|   6 | Crossplane extends Kubernetes to manage resources beyond containers.                                                                                                                               |
|   7 | Crossplane is now a CNCF graduated project with over 3,000 contributors.                                                                                                                           |
|   8 | Crossplane v2 released; resources are namespaced by default, and composition is more flexible.                                                                                                     |
|   9 | Crossplane 1.20 is the last supported 1.x release.                                                                                                                                                 |
|  10 | Key Crossplane concepts: XRD (Composite Resource Definition) defines platform APIs; Composition implements logic for resource creation; Managed Resources represent cloud or Kubernetes resources. |
|  11 | Crossplane transforms cloud provider services into Kubernetes API objects managed by controllers.                                                                                                  |
|  12 | XRDs define the schema and experience exposed to developers.                                                                                                                                       |
|  13 | Compositions are pipelines of functions that configure and declare resources.                                                                                                                      |
|  14 | Functions in compositions can be written in any GRPC-supported language (Go, Python, KCL, Q, HCL, YAML).                                                                                           |
|  15 | Crossplane handles Kubernetes controller complexities; functions focus on business logic.                                                                                                          |
|  16 | Developer experience improvements: control plane projects unify functions, compositions, and XRDs in one place for easier management and versioning.                                               |
|  17 | Command-line tools support initializing projects, generating XRDs, compositions, and functions, and running local clusters for testing.                                                            |
|  18 | XPRN is a test framework for writing and running composition tests locally.                                                                                                                        |
|  19 | New metrics capabilities allow detailed, flexible monitoring of Crossplane resources, leveraging resource state metrics.                                                                           |
|  20 | Resource metrics monitors enable custom metrics and labeling, with controls to a                                                                                                                   |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=zu6V34BFksk)
