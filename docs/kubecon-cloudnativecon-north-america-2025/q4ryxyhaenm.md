---
layout: default
title:
  "Butterfly Effect: What Kubernetes SIG Security Has in F... I. Coldwater, S.
  Raghunathan, C. Valencia"
nav_order: 36
parent: Kubecon Cloudnativecon North America 2025
type: Video Note
description:
  The SIG Security Maintainer Track talk introduces the Kubernetes SIG
  Security group, established in 2020 to provide a dedicated, inclusive space for
  security within the Kubernetes project. The group oversees several subprojects,
  including p...
resource: https://www.youtube.com/watch?v=q4ryxYhAenM
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

The SIG Security Maintainer Track talk introduces the Kubernetes SIG Security group, established in 2020 to provide a dedicated, inclusive space for security within the Kubernetes project.
The group oversees several subprojects, including periodic third-party security audits—recently shifting focus to widely used non-core components—and the SIG Security Documentation project, which aims to update resources like the OWASP Kubernetes Top 10 and develop in-depth hardening guides for cluster operators.
The SIG Security Tooling subproject maintains tools such as the official CVE feed, collaborates on vulnerability scanning, and works to improve infrastructure security, while also hosting educational sessions.
Another key initiative is the self-assessments subproject, which helps Kubernetes components conduct threat modeling and security reviews, encouraging participation from contributors of all backgrounds.
Throughout, the group emphasizes a welcoming, collaborative environment where both newcomers and experienced professionals can contribute and grow, highlighting the ripple effect of individual contributions within the open source community.

# Main Points

|   # | Main point                                                                                                                                        |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | SIG Security has been a Kubernetes Special Interest Group (SIG) since 2020.                                                                       |
|   2 | Kubernetes governance is organized by SIGs, each responsible for a specific area.                                                                 |
|   3 | Before SIG Security, security was considered everyone's responsibility, leading to fragmentation.                                                 |
|   4 | Working Group Audit led to the formation of SIG Security.                                                                                         |
|   5 | SIG Security aims to create a welcoming, inclusive space for contributors of all skill levels.                                                    |
|   6 | Participation is based on those who show up and contribute, not formal membership.                                                                |
|   7 | Subprojects include documentation, tooling, and self-assessments.                                                                                 |
|   8 | The periodic third-party audit recently focused on widely used non-core components, not just the core codebase.                                   |
|   9 | The audit process involves external teams, findings triaged by the Security Response Committee, and eventual public disclosure.                   |
|  10 | One disclosed finding: CVE-20257342 (hardcoded credentials in Windows OVA/NANX images).                                                           |
|  11 | SIG Security Documentation subproject focuses on security awareness through tutorials, blogs, examples, and hardening guides.                     |
|  12 | Current documentation projects: updating the OWASP Kubernetes Top 10 (community input invited) and developing a detailed hardening guide.         |
|  13 | Contributors are encouraged to collaborate and bring new topics or sections.                                                                      |
|  14 | SIG Security Tooling subproject started in 2021, maintains the official CVE feed, scans for vulnerabilities, and improves infrastructure as code. |
|  15 | Recent tooling work includes migrating tools to Google Cloud Build and improving CVE data structure and publication.                              |
|  16 | Learning sessions are hosted on security tools like Cubound.                                                                                      |
|  17 | Self-assessments subproject helps projects threat model and assess security, using data flow diagrams and STRIDE framework.                       |
|  18 | Self-assessments completed for Cluster API, started for vSphere and etcd.                                                                         |
|  19 | All contributors, regardless of background, are encouraged to join and participate.                                                               |
|  20 | Meetings are held every other Friday at 11:00 a.m. Eastern; information available via mailing list and Slack.                                     |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=q4ryxYhAenM)
