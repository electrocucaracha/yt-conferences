---
layout: default
title: "Fine-grained and centralized authorization for OpenStack with Open Policy Agent"
nav_order: 47
parent: OpenInfra Summit Europe 2025
type: Video Note
description: "This presentation by C7 details the implementation of Open Policy Agent (OPA) to provide fine-grained, centralized authorization for OpenStack, addressing the limitations of traditional Oslo policy..."
resource: "https://www.youtube.com/watch?v=_B4Zsd8RG88"
youtube_stats:
  view_count: 163
  like_count: 1
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

This presentation by C7 details the implementation of Open Policy Agent (OPA) to provide fine-grained, centralized authorization for OpenStack, addressing the limitations of traditional Oslo policy files which are difficult to maintain and test.
The team integrated OPA via a custom Oslo policy plugin that invokes OPA’s REST API, deploying OPA instances as local sidecars to minimize latency and ensuring low overhead, with most decisions processed in under two milliseconds.
A significant challenge was encountered with Neutron, whose unique policy evaluation logic caused severe performance bottlenecks; this was mitigated by introducing a lightweight database proxy with caching to reduce redundant policy checks.
The production rollout was executed carefully to avoid service disruption, utilizing automated policy generation from source code, comprehensive testing, and custom monitoring tools to track decision times and ensure accuracy.
Although a rare timeout issue between OpenStack services and OPA remains under investigation, the solution successfully enables flexible role management and improved security without significant performance impact.

# Main Points

|   # | Main point                                                                                                                                                                        |
| --: | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | The session presents a solution for fine-grained and centralized authorization in OpenStack using Open Policy Agent (OPA).                                                        |
|   2 | Presenters from C7, a public cloud provider, developed this solution to meet customer needs for flexible access control in production environments.                               |
|   3 | Standard OpenStack authorization uses a mix of role-based and attribute-based access control, with policies defined in code and overridden via configuration files.               |
|   4 | Current policy management is difficult to maintain, test, and deploy, as changes require manual redistribution to all nodes and can cause service restarts.                       |
|   5 | OPA is a CNCF-graduated policy engine that evaluates policies via a REST API, offering a centralized location for policy storage and management.                                  |
|   6 | The integration involves a custom Oslo policy plugin that invokes OPA, replacing the broken native HTTP check support in OpenStack.                                               |
|   7 | OPA instances are deployed as local containers on the same host as each OpenStack service to minimize latency and avoid network overhead.                                         |
|   8 | A generator tool converts existing OpenStack policy files into Rego format, automatically creating both the policies and their corresponding unit tests.                          |
|   9 | Policies are managed in a single Git repository, with CI/CD pipelines building OPA bundles that are fetched locally by services, eliminating manual file distribution.            |
|  10 | Neutron presents unique challenges because it evaluates policies after database queries and performs custom ownership checks, leading to significant performance overhead.        |
|  11 | To optimize Neutron performance, a database proxy with caching was implemented to fetch parent resource data once, reducing repeated policy evaluations.                          |
|  12 | The production rollout strategy involved deploying OPA with identical policies first to ensure no functional changes, followed by the introduction of new service-specific roles. |
|  13 | Monitoring is enhanced by an OPA decision exporter service that logs decisions and exposes metrics such as decision time and request size.                                        |
|  14 | Performance impact is minimal, with most policy decisions taking less than one millisecond, though some services like Neutron may take up to two milliseconds.                    |
|  15 | A persistent timeout issue between OpenStack services and OPA was mitigated by increasing timeouts and implementing a retry mechanism, though the root cause remains unresolved.  |
|  16 | Future plans include adding TLS support, integrating policy fetching directly with Keystone, and enabling customers to create self-service roles.                                 |

# Video

[![Video thumbnail](https://img.youtube.com/vi/_B4Zsd8RG88/hqdefault.jpg)](https://www.youtube.com/watch?v=_B4Zsd8RG88)

[Watch on YouTube](https://www.youtube.com/watch?v=_B4Zsd8RG88)
