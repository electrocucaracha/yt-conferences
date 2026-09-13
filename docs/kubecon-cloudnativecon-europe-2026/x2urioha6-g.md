---
layout: default
title:
  "API-Driven Infrastructure as Code: Kubernetes APIs as the Con... Florian Hopfensperger
  & Yury Tsarev"
nav_order: 12
parent: Kubecon Cloudnativecon Europe 2026
type: Video Note
description:
  In this talk, Florian Hoffinsburgger and Yuri from Abound discuss building
  API-driven infrastructure using Kubernetes APIs as a contract bridge between internal
  teams. They describe their platform, which enables multiple product teams to of...
resource: https://www.youtube.com/watch?v=X2URIOhA6_g
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

In this talk, Florian Hoffinsburgger and Yuri from Abound discuss building API-driven infrastructure using Kubernetes APIs as a contract bridge between internal teams.
They describe their platform, which enables multiple product teams to offer automation products to internal application teams via a unified interface, leveraging Kubernetes APIs and Crossplane for infrastructure management.
The presenters emphasize the importance of well-defined API contracts to address challenges such as unclear ownership, tightly coupled super compositions, breaking changes, and documentation drift.
They demonstrate how strong API contracts facilitate loose coupling between teams, enable automated testing and validation, and support scalable, reliable infrastructure provisioning.
The session concludes with lessons learned, including the value of clear contract boundaries, careful versioning, documentation as code, and robust testing practices, as well as a Q&A addressing topics like resource sharing, versioning strategies, migration to Crossplane v2, and disaster recovery.

# Main Points

|   # | Main point                                                                                                                        |
| --: | --------------------------------------------------------------------------------------------------------------------------------- |
|   1 | The platform uses Kubernetes APIs as a contract bridge between teams.                                                             |
|   2 | The platform serves only internal customers within the enterprise.                                                                |
|   3 | Product teams create automation products; application teams consume them.                                                         |
|   4 | The platform team operates and develops the platform, supporting multiple product teams.                                          |
|   5 | Achievements include enabling self-service signup and managing 1,000+ control planes.                                             |
|   6 | A unified interface replaces disparate team-specific interfaces, using Kubernetes and GitHub.                                     |
|   7 | Over 20,000 infrastructure claims are managed, covering 90+ products by 15 teams.                                                 |
|   8 | Crossplane is used to power the platform, leveraging crossplane providers for enterprise API integration.                         |
|   9 | Each customer has a dedicated control plane for infrastructure management.                                                        |
|  10 | Product teams use a GitOps approach for platform and product deployment.                                                          |
|  11 | Product teams define APIs for their automation products, focusing on usability and clarity.                                       |
|  12 | API contracts are central, defined via XRDs with schema, validation, documentation, versioning, and tests.                        |
|  13 | Canary deployments are used to safely roll out changes to subsets of customers.                                                   |
|  14 | Challenges include unclear ownership, super compositions, breaking changes, and undocumented assumptions.                         |
|  15 | API contracts clarify boundaries, responsibilities, and expected behaviors.                                                       |
|  16 | Crossplane features like required resources/importers enable integration across providers without tight coupling.                 |
|  17 | Consumers interact with products via API contracts, with automated validation and additional safeguards.                          |
|  18 | Both providers (product teams) and consumers (application teams) can test API contracts locally and in CI.                        |
|  19 | Local composition tests and tools like crossplane render enable rapid, reliable development and validation.                       |
|  20 | Lessons learned: clear contract boundaries, versioning to avoid breaking changes, documentation as code, and high adoption rates. |
|  21 | For versioning, avoid breaking changes by designing evolvable APIs and using tools like kube API linter.                          |
|  22 | Migration                                                                                                                         |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=X2URIOhA6_g)
