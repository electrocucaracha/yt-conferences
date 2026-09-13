---
type: Video Note
title: "When Multitenancy Goes Wrong: A Deep Dive Into Kcp’s First CVE - Marvin Beckers, ClickHouse"
description: "Marvin Beckers, a maintainer of the CNCF sandbox project KCP, discusses the project's first official CVE and the lessons learned from addressing it. KCP is a multi-tenant, horizontally scalable control plane for Kubernetes-like APIs, design..."
resource: https://www.youtube.com/watch?v=6pFY8lrTOKw
tags: ["kubecon-cloudnativecon-europe-2026", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

Marvin Beckers, a maintainer of the CNCF sandbox project KCP, discusses the project's first official CVE and the lessons learned from addressing it.
KCP is a multi-tenant, horizontally scalable control plane for Kubernetes-like APIs, designed to provide logical separation through workspaces and virtual workspaces, enabling API providers and consumers to interact securely.
The vulnerability arose because an authorizer in the virtual workspace failed to check API bindings on the consumer side, allowing users with certain permissions to perform unauthorized create and delete operations, potentially escalating privileges by creating cluster-admin bindings.
The issue was discovered while extending permission claims functionality, and although mitigated by some architectural constraints, it was serious enough to warrant a coordinated disclosure and rapid patching process using GitHub's security advisory tools.
Beckers emphasizes the importance of maintaining a robust security process, transparent communication, and continuous vigilance, encouraging other open source projects to prepare for similar incidents and leverage available security infrastructure.
# Main Points

|   # | Main point                                                                                                                                   |
| --: | -------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Presentation covers the first official CVE in the CNCF sandbox project KCP.                                                                  |
|   2 | Marvin Beckers is a KCP maintainer and cloud software engineer at Click House.                                                               |
|   3 | KCP is a multi-tenant, horizontally scalable control plane for Kubernetes-like APIs.                                                         |
|   4 | KCP is not Kubernetes; it's a standalone API server using the Kubernetes resource model and libraries.                                       |
|   5 | KCP enables clients familiar with Kubernetes APIs to interact with it.                                                                       |
|   6 | Typical use cases: internal developer platforms, orchestrating global SaaS/PaaS solutions, and exposing APIs to external customers.          |
|   7 | KCP introduces multi-tenancy via workspaces and virtual workspaces, providing logical separation within a single API server.                 |
|   8 | Virtual workspaces offer filtered views of data, allowing API providers to access only relevant objects for reconciliation.                  |
|   9 | Dynamic virtual workspaces are built on Kubernetes libraries and use API definition sets to serve APIs.                                      |
|  10 | Authorization and admission are implemented in virtual workspaces for security.                                                              |
|  11 | The CVE was discovered while extending virtual workspace functionality to restrict permission claims by verbs.                               |
|  12 | Documentation claimed an authorizer checked API bindings, but the actual check was missing.                                                  |
|  13 | The missing check allowed API providers to perform create and delete operations in arbitrary workspaces if they knew the logical cluster ID. |
|  14 | List and get operations were protected by a labeling mechanism, but create/delete were not.                                                  |
|  15 | The vulnerability allowed privilege escalation by creating cluster-admin role bindings.                                                      |
|  16 | The CVSS score was revised to 9.6 due to the potential for privilege escalation.                                                             |
|  17 | The fix involved extending the authorizer to check API bindings and verbs.                                                                   |
|  18 | GitHub security advisories were used for private reporting, triage, and coordinated disclosure.                                              |
|  19 | Pre-announcements were sent to users before the patch release.                                                                               |
|  20 | Recommendation: projects should have a security process and use GitHub advisories for CVEs.                                                  |
|  21 | Future improvements include building a trusted v                                                                                             |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=6pFY8lrTOKw)