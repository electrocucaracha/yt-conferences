---
layout: default
title:
  "Platform Engineering in Action: Test-Driven Development App... Charles-Edouard
  Brétéché & Sara Qasmi"
nav_order: 199
parent: Kubecon Cloudnativecon North America 2025
type: Video Note
description:
  In this session, the speakers discuss the often-overlooked importance
  of testability in platform engineering, specifically focusing on applying test-driven
  development (TDD) to developer platforms. They demonstrate building a Kubernetes-bas...
resource: https://www.youtube.com/watch?v=p2QPtjHp77I
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

In this session, the speakers discuss the often-overlooked importance of testability in platform engineering, specifically focusing on applying test-driven development (TDD) to developer platforms.
They demonstrate building a Kubernetes-based platform to run a Drupal application, initially without tests, which leads to a critical issue when a platform change breaks the contract between the platform and development teams—specifically, a secret name change that causes the application to fail.
The presenters then rebuild the platform using TDD, writing tests to ensure that such contracts remain valid and that changes do not inadvertently break functionality.
They show how these tests can be automated and integrated into CI pipelines using tools like Chainsaw, making it easier to catch errors early and maintain confidence in platform changes.
The key takeaway is that TDD is not just for application development but is also essential for platform engineering, enabling better collaboration and reliability between platform and development teams.

# Main Points

|   # | Main point                                                                                                                                            |
| --: | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Session focuses on applying test-driven development (TDD) to platform engineering.                                                                    |
|   2 | Initial platform is built without tests; issues are expected to arise.                                                                                |
|   3 | Two teams involved: platform team (manages Kubernetes, database, networking, CI/CD) and development team (needs environment to run Drupal app).       |
|   4 | Platform stack includes Kubernetes cluster, Argo CD for GitOps-driven deployment, and Crossplane for infrastructure services.                         |
|   5 | Crossplane provides an interface/contract for services like databases, allowing platform engineers to change implementations without affecting users. |
|   6 | Developers request databases via a MariaDB instance resource; platform team ensures implementation.                                                   |
|   7 | Output of the composition includes a secret with database credentials for the application.                                                            |
|   8 | Changing the secret name in the platform without informing developers breaks the application, especially when scaling.                                |
|   9 | Lack of tests means such contract changes can cause production failures that are hard to trace.                                                       |
|  10 | TDD is proposed to maintain contract validity and reduce errors.                                                                                      |
|  11 | Tests are added to the CI pipeline using Chainsaw, a declarative testing tool.                                                                        |
|  12 | Tests check for the existence and correctness of the secret (e.g., name and password field).                                                          |
|  13 | Failing tests prevent merging breaking changes.                                                                                                       |
|  14 | Fixing the secret name and rerunning tests ensures contract is maintained.                                                                            |
|  15 | Chainsaw tests can be run locally or in CI, and are not limited to any Kubernetes distribution.                                                       |
|  16 | TDD helps both platform and development teams maintain confidence in changes.                                                                         |
|  17 | Chainsaw enables writing tests without advanced programming knowledge.                                                                                |
|  18 | Documentation and further resources are available on GitHub.                                                                                          |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=p2QPtjHp77I)
