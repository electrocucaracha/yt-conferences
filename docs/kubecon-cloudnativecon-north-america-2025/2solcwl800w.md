---
type: Video Note
title: "Patch Me If You Can: Tackling Outdated Addons Before They Become... Stevie Caldwell & Andy Suderman"
description: "In this talk, Stevie Caldwell and Andy from Fairwinds discuss the critical role of Kubernetes add-ons, emphasizing that despite their name, add-ons are essential for cluster functionality, scalability, and security. They highlight the incre..."
resource: https://www.youtube.com/watch?v=2SoLCWl800w
tags: ["kubecon-cloudnativecon-north-america-2025", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

In this talk, Stevie Caldwell and Andy from Fairwinds discuss the critical role of Kubernetes add-ons, emphasizing that despite their name, add-ons are essential for cluster functionality, scalability, and security.
They highlight the increasing number and severity of vulnerabilities (CVEs) affecting these add-ons, the growing regulatory pressure to remediate them quickly, and the operational challenges in keeping add-ons updated, such as compatibility issues, manual processes, and lack of standardized release notes.
Drawing parallels to the evolution of Kubernetes upgrades, they advocate for a proactive, continuous upgrade approach—"bring the pain forward"—to minimize tech debt and security risks.
The speakers recommend leveraging automation and open source tools like Pluto, Nova, and Go No Go to streamline upgrades, monitor deprecated APIs, and assess upgrade safety, while also acknowledging the persistent challenges of time constraints and incomplete solutions for zero-CVE environments.
They conclude by encouraging regular research, staged testing, and frequent upgrades as best practices for managing Kubernetes add-ons effectively.
# Main Points

|   # | Main point                                                                                                                                                                            |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Fairwinds builds and manages Kubernetes clusters, add-ons, and infrastructure.                                                                                                        |
|   2 | Presenters: Stevie Caldwell (Tech Lead, author of Go No Go) and Andy (CTO, CNCF ambassador, author of Pluto and Goldilocks).                                                          |
|   3 | Agenda: why add-ons matter, vulnerability trends, operational struggles, best practices and tools.                                                                                    |
|   4 | Add-ons are essential for Kubernetes functionality (networking, ingress, TLS, monitoring).                                                                                            |
|   5 | Add-ons often require high-level permissions, increasing security risk.                                                                                                               |
|   6 | Vulnerabilities in add-ons are increasing; 86% of codebases scanned contain open source with vulnerabilities.                                                                         |
|   7 | From 2013 to 2023, CVEs increased by 463%.                                                                                                                                            |
|   8 | Time to remediate CVEs is rising, sometimes exceeding a year.                                                                                                                         |
|   9 | Regulatory pressure (executive orders, Cyber Resilience Act, NIST, ISO 2701) demands faster remediation.                                                                              |
|  10 | Operational challenges: "set it and forget it" syndrome, complex compatibility, manual upgrades, inconsistent release notes, testing and rollback requirements, and time constraints. |
|  11 | Managed Kubernetes services (e.g., AWS, GKE) force more frequent upgrades, improving cluster hygiene.                                                                                 |
|  12 | Add-on upgrades are hindered by lack of standardization and automation.                                                                                                               |
|  13 | Best practice: "Bring the pain forward"—upgrade add-ons continuously (Fairwinds upgrades all add-ons monthly).                                                                        |
|  14 | Continuous upgrades reduce tech debt and CVEs, and make maintenance easier.                                                                                                           |
|  15 | Tools mentioned: Pluto (API deprecation), Nova (Helm/image version alerts), Go No Go (upgrade safety validation), Renovate, Dependabot, managed add-ons.                              |
|  16 | Emphasize automation, regular upgrade cadence, staged testing before production.                                                                                                      |
|  17 | Research and analyze release notes; tooling and automation are key.                                                                                                                   |
|  18 | No complete solution for automated add-on conformance testing yet; end-to-end testing in staging is recommended.                                                                      |
|  19 | Upgrading images monthly reduces but does not eliminate CVEs; zero CVE may require patched images or third-party providers.                                                           |
|  20 | Budget constraints limit access to some solutions; the problem remains ongoing.                                                                                                       |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=2SoLCWl800w)