---
layout: default
title: How to support life science research projects on cloud infrastructures
nav_order: 80
parent: OpenInfra Summit Europe 2025
type: Video Note
description: "Deasti from the CINECA Supercomputer Center in Italy presented on how the facility supports life science research projects on the cloud, addressing specific challenges related to sensitive data and..."
resource: "https://www.youtube.com/watch?v=rQpFcnYYnvk"
youtube_stats:
  view_count: 83
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

Deasti from the CINECA Supercomputer Center in Italy presented on how the facility supports life science research projects on the cloud, addressing specific challenges related to sensitive data and GDPR compliance.
Since traditional high-performance computing clusters are not inherently designed for data isolation, CINECA deployed an HPC cloud infrastructure based on OpenStack to combine computational power with the flexibility and security features of cloud computing.
The presentation detailed a dual approach to security, involving strict organizational procedures such as formal data processing agreements and internal policies for account management, alongside technical measures like two-factor authentication, volume encryption, and privacy-by-design software development.
Practical examples included the Italian Genome Network and the Orchestra project, where architectures used isolated virtual machines and encrypted file systems to ensure that only aggregated, anonymized data was accessible to researchers.
CINECA has been ISO 27001 certified for life science projects since 2022, a status that enhances user trust and provides a competitive advantage, with plans to extend this certification to all infrastructure-as-a-service projects.

# Main Points

|   # | Main point                                                                                                                                                              |
| --: | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | The presenter from CINECA, Italy's primary supercomputing center, discusses supporting life science research on cloud infrastructure.                                   |
|   2 | CINECA is a consortium of university research centers founded in 1969 to manage high-performance computing facilities in Italy.                                         |
|   3 | Life science users require computational capacity, model optimization, and data management workflows for sensitive data such as genomics and clinical information.      |
|   4 | Strict regulations like GDPR pose security and privacy challenges that traditional HPC clusters are not designed to handle due to their shared resource nature.         |
|   5 | CINECA deployed an HPC cloud infrastructure starting ten years ago, combining HPC performance with cloud flexibility using OpenStack.                                   |
|   6 | The approach to securing sensitive data involves both technical security measures and organizational administrative processes.                                          |
|   7 | Organizational procedures include formal agreements with researchers, appointing CINECA as a data processor under GDPR, and defining roles and responsibilities.        |
|   8 | Internal policies cover account creation, privilege management, log access, backup procedures, disaster recovery, and change management.                                |
|   9 | Technical security measures include access control, two-factor authentication, and the use of the Barbican key manager for encrypted volumes.                           |
|  10 | A privacy by design approach is applied, including risk identification, data protection impact assessments, and sharing results with users before production.           |
|  11 | Vulnerability assessments and penetration testing are performed before production and at least annually or upon major updates.                                          |
|  12 | An example project for the Italian genome network uses three virtual machines to isolate data, with only aggregated and anonymized results shared with researchers.     |
|  13 | Another example for the Orchestra project uses specific tokens for controlled data access and encrypted volumes for backend analysis.                                   |
|  14 | CINECA has been certified ISO 27001 for life science projects on cloud since 2022, with verification for extension to all IaaS projects upcoming.                       |
|  15 | Certification benefits include increased user trust, competitive advantage for specific funding calls, and improved internal staff awareness of data risks.             |
|  16 | User removal policies involve disabling accounts after inactivity and closing them after a grace period, with data associated to projects rather than individual users. |
|  17 | The current system supports approximately ten life science projects and scales effectively, though paperwork remains a slow process.                                    |
|  18 | Encryption is applied at the volume level and for secure communications, requiring trust in the administrator for data at rest.                                         |

# Video

[![Video thumbnail](https://img.youtube.com/vi/rQpFcnYYnvk/hqdefault.jpg)](https://www.youtube.com/watch?v=rQpFcnYYnvk)

[Watch on YouTube](https://www.youtube.com/watch?v=rQpFcnYYnvk)
