---
layout: default
title: "Talks - Cheuk Ting Ho: Making Python safer than ever"
nav_order: 160
parent: PyCon US 2024
type: Video Note
description: "Chum, a PSF director and fellow, delivered a talk emphasizing the critical importance of security in the Python community, drawing an analogy between physical neighborhood safety and cybersecurity ..."
resource: "https://www.youtube.com/watch?v=FxHuHT12UH8"
youtube_stats:
  view_count: 352
  like_count: 5
  channel_subscriber_count: 34500
tags:
  - pycon-us-2024
  - video
  - learning
status: stable
generated:
  by: process:yt-summarizer-okf
  at: 2026-11-22T10:18:11+00:00
---

# Summary

Chum, a PSF director and fellow, delivered a talk emphasizing the critical importance of security in the Python community, drawing an analogy between physical neighborhood safety and cybersecurity to highlight the vulnerability of Python’s diverse user base, which includes researchers, financial institutions, and schools.
She outlined top open-source risks, such as known vulnerabilities, package compromise, and name confusion attacks, while noting that Python’s status as a first programming language for many users increases the need for robust security measures.
The presentation detailed significant efforts by the Python Software Foundation, including the hiring of two full-time security engineers funded by Alpha Omega and AWS, who have implemented keyless signing for CPython releases, enforced two-factor authentication on PyPI, and improved malware reporting response times to under an hour.
Additionally, the PSF has become a CVE Numbering Authority, established a security advisory database, and commissioned a security audit of the PyPI infrastructure to ensure the legitimacy and safety of the ecosystem.
Chum concluded by urging maintainers to enable two-factor authentication and use trusted publishing, advising users to keep dependencies updated and locked, and encouraging corporate leaders to support the PSF financially and educate their employees on security best practices.

# Main Points

|   # | Main point                                                                                                                                                  |
| --: | ----------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | The speaker, a PSF director, emphasizes the critical importance of security in the Python community, comparing it to personal safety.                       |
|   2 | Python's diverse user base, including researchers, banks, governments, and students, makes the ecosystem uniquely vulnerable to security threats.           |
|   3 | Many Python users lack deep engineering backgrounds, increasing the risk of security oversights in code and dependency management.                          |
|   4 | Global regulations like the US Executive Order on Cybersecurity and the EU Cyber Resilience Act highlight the growing need for software security standards. |
|   5 | Key open-source risks include known vulnerabilities, compromised packages, name confusion attacks, and unmaintained or outdated software.                   |
|   6 | The PSF has hired two full-time security engineers: Seth for CPython and pip, funded by Alpha Omega, and Mike for PyPI, funded by AWS.                      |
|   7 | All Python releases since version 3.11 are signed using Sigstore, a keyless signing technology that enhances transparency and verification.                 |
|   8 | The PSF became a CVE Numbering Authority to assign unique identifiers to vulnerabilities in CPython and pip, improving tracking and communication.          |
|   9 | A PSF advisory database and mailing list provide notifications for security issues, with data available in the OSV format for tool integration.             |
|  10 | PyPI now enforces two-factor authentication for all users to prevent account compromises and malicious package uploads.                                     |
|  11 | The PyPI malware reporting system was improved with a new help desk tool, reducing average response time from eight hours to under one hour.                |
|  12 | A security audit of the Warehouse and Capage codebases was conducted by Trail of Bits, funded by the Open Technology Fund.                                  |
|  13 | The Python Security Response Team handles vulnerability reports privately, ensuring patches are developed before public disclosure.                         |
|  14 | Maintainers are urged to enable two-factor authentication, use trusted publishing, and follow best practices for secure software release.                   |
|  15 | Users should lock dependencies, keep packages updated, and use tools like pip-audit to check for vulnerabilities.                                           |
|  16 | Companies are encouraged to support the PSF financially and educate employees on security best practices to strengthen the ecosystem.                       |
|  17 | A security open space session led by Seth is scheduled for attendees to discuss vulnerability handling and community contributions.                         |

# Video

[![Video thumbnail](https://img.youtube.com/vi/FxHuHT12UH8/hqdefault.jpg)](https://www.youtube.com/watch?v=FxHuHT12UH8)

[Watch on YouTube](https://www.youtube.com/watch?v=FxHuHT12UH8)
