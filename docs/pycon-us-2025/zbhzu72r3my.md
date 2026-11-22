---
layout: default
title: "Reviewing another year of security partnership between the PSF & Alpha-Omega (Sponsor: Alpha-Omega)"
nav_order: 72
parent: PyCon US 2025
type: Video Note
description: "Michael Windsor, co-founder of Alpha Omega, outlines the organization’s strategy to address open-source supply chain risks by funding security work and catalyzing systemic change rather than just p..."
resource: "https://www.youtube.com/watch?v=ZbHzU72r3mY"
youtube_stats:
  view_count: 231
  like_count: 4
  channel_subscriber_count: 34500
tags:
  - pycon-us-2025
  - video
  - learning
status: stable
generated:
  by: process:yt-summarizer-okf
  at: 2026-11-22T01:39:37+00:00
---

# Summary

Michael Windsor, co-founder of Alpha Omega, outlines the organization’s strategy to address open-source supply chain risks by funding security work and catalyzing systemic change rather than just patching individual vulnerabilities.
He emphasizes the importance of treating dependencies as active components requiring intentional management, using the Airflow project as a successful case study where prioritized security efforts led to improved community engagement and dependency health.
Seth, a security developer at the Python Software Foundation (PSF), details recent advancements in the Python ecosystem, including the implementation of Software Bill of Materials (SBOMs) for all Python packages, the migration from PGP to Sigstore for secure signing, and the adoption of system trust stores in pip to simplify corporate proxy configurations.
He also highlights the creation of standards for CVE numbering authorities and the ongoing efforts to mitigate novel threats like GitHub Actions attacks and AI-generated security noise.
Mike Fedler, the PyPI Safety and Security Engineer, discusses critical platform enhancements such as the mandatory enforcement of two-factor authentication (2FA) for all users, the introduction of a quarantine mechanism to safely isolate malicious packages, and the deployment of automated typo-squatting detection tools.
He further explains efforts to prevent domain resurrection attacks by validating email domains and improving the performance and security of the PyPI warehouse codebase, underscoring the PSF’s commitment to normalizing security as a core function of open-source stewardship.

# Main Points

|   # | Main point                                                                                                                                                |
| --: | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Alpha Omega was founded in 2022 to address open-source supply chain security risks and has raised approximately $23 million from sponsors.                |
|   2 | The organization’s strategy focuses on creating leverage points and scaling security improvements rather than simply funding individual projects.         |
|   3 | Funding is allocated to four main categories: staffing, package repositories, audits, and other security initiatives.                                     |
|   4 | The Airflow project served as a case study for prioritizing security by reviewing dependencies and establishing a clear security posture.                 |
|   5 | Maintainers are encouraged to treat dependencies as active components requiring attention, testing, and intentional management rather than static assets. |
|   6 | A dedicated security leadership role is essential for creating prioritization, momentum, and cultural change within open-source projects.                 |
|   7 | Seth, a security engineer at the Python Software Foundation, focuses on CPython, pip, and ecosystem-wide standards.                                       |
|   8 | The Python ecosystem has adopted Software Bill of Materials (SBOMs) to standardize software composition data across different ecosystems.                 |
|   9 | The Python Security Response Team has formalized processes for triaging vulnerabilities and automating CVE record management.                             |
|  10 | The ecosystem is migrating from PGP signatures to Sigstore to enable workload identity and improve build provenance.                                      |
|  11 | Pip now uses system trust stores by default, resolving certificate verification issues in corporate proxy environments.                                   |
|  12 | AI-generated code introduces new challenges, including hallucinated security reports and "slop squatting," which burden maintainers.                      |
|  13 | The EU Cyber Resilience Act is a major upcoming regulatory driver requiring compliance from both open-source stewards and manufacturers.                  |
|  14 | Mike, the PyPI Safety and Security Engineer, highlights the enforcement of mandatory two-factor authentication for all PyPI users.                        |
|  15 | PyPI has implemented a quarantine mechanism to temporarily suspend suspicious projects, allowing for investigation without immediate deletion.            |
|  16 | Automated quarantine systems use trusted external security partners to flag and isolate malicious packages in real-time.                                  |
|  17 | A "typo sniper" tool detects potential typosquatting attacks by analyzing package name patterns and registration behavior.                                |
|  18 | PyPI validates email addresses and blocks disposable or expiring domains to mitigate account takeover and domain resurrection attacks.                    |
|  19 | Performance optimizations have significantly reduced PyPI CI test times and improved database query efficiency for mirroring protocols.                   |
|  20 | The team is working on a cohesive user account workflow, pruning incomplete registrations, and developing a management API for better security controls.  |
|  21 | Trusted publishing and Salsa source provenance are being advanced to ensure end-to-end supply chain integrity for Python packages.                        |

# Video

[![Video thumbnail](https://img.youtube.com/vi/ZbHzU72r3mY/hqdefault.jpg)](https://www.youtube.com/watch?v=ZbHzU72r3mY)

[Watch on YouTube](https://www.youtube.com/watch?v=ZbHzU72r3mY)
