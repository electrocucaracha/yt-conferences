---
layout: default
title:
  Kubernetes Third Party Aud... Iain Smart, Amir Montazery, Rey Lejano, Tabitha
  Sable & Pietro Tirenna
nav_order: 196
parent: Kubecon Cloudnativecon Europe 2026
type: Video Note
description:
  The Kubernetes SIG Security team provided an update on their third-party
  audit efforts, highlighting the importance of external security reviews for such
  a large and complex open-source project. Previous audits in 2019 and 2022 uncovered
  a...
resource: https://www.youtube.com/watch?v=CThez9zBRlA
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

The Kubernetes SIG Security team provided an update on their third-party audit efforts, highlighting the importance of external security reviews for such a large and complex open-source project.
Previous audits in 2019 and 2022 uncovered a range of issues, from path traversal vulnerabilities to weak default credentials, many of which have been addressed, though some findings remain open and require further attention.
The most recent audit, coordinated by the Open Source Technology Improvement Fund and conducted by Shielder, focused on non-core components and used a threat modeling approach to identify actionable security findings.
Notable discoveries included a hardcoded Windows administrator password in images built for a specific cloud provider, weaknesses in AppArmor profile enforcement with Pod Security Standards, and supply chain risks in cluster template management.
The team emphasized that most issues stem from integration points and ecosystem complexity rather than poor coding, and they encouraged community involvement in addressing outstanding findings and improving security documentation.

# Main Points

|   # | Main point                                                                                                                             |
| --: | -------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Kubernetes SIG Security third-party audit subproject collaborates with external vendors for security audits.                           |
|   2 | Two major audits were conducted: Atredis and Trail of Bits (2019), NCC Group (2022).                                                   |
|   3 | Past audits identified issues such as path traversals, weak default credentials, cryptographic weaknesses, and architectural concerns. |
|   4 | High-severity findings are fixed before public release; some findings from previous audits remain open and need attention.             |
|   5 | The oldest unresolved issue is lack of Kubernetes certificate revocation for user identities (GitHub issue 18982).                     |
|   6 | Automation sometimes marks unresolved findings as stale; efforts are made to recover and triage these.                                 |
|   7 | Recent audit focused on non-core components, reviewing 665 features graduated to stable between versions 1.24 and 1.31.                |
|   8 | 93 features/areas were identified for audit; 17 labeled as high priority.                                                              |
|   9 | Audit scope included cluster API, pod security admission, and cgroup v2.                                                               |
|  10 | Open Source Technology Improvement Fund (OTF) managed vendor selection and audit administration.                                       |
|  11 | Security Response Committee (SRC) reviews audit findings privately before public release to ensure sensitive issues are fixed.         |
|  12 | Shielder performed the audit using a hybrid threat modeling and divide-and-conquer approach.                                           |
|  13 | Key audit findings:                                                                                                                    |
|  14 | Hardcoded Windows admin password in image builder for Nutanix provider, leading to a critical vulnerability (promptly fixed).          |
|  15 | AppArmor profiles bundled with unconfined aliases allowed bypassing pod security standards.                                            |
|  16 | Cluster API templates could be manipulated to inject privileged pods into management clusters, risking full compromise.                |
|  17 | Most issues stem from integration and configuration, not insecure coding.                                                              |
|  18 | Windows support introduces new security challenges due to OS-specific assumptions.                                                     |
|  19 | AI tools assist in codebase analysis and taint analysis but are not yet fully autonomous in finding all bugs.                          |
|  20 | Trust in the project is managed through private nomination and reputation w                                                            |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=CThez9zBRlA)
