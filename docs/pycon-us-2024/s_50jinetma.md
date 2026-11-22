---
layout: default
title: "Python Software Foundation - Meet our Security Engineers"
nav_order: 122
parent: PyCon US 2024
type: Video Note
description: "Seth Larson and Mike Fiedler, the Python Software Foundation’s new full-time security engineers, presented their efforts to enhance supply chain security and protect the PyPI ecosystem."
resource: "https://www.youtube.com/watch?v=S_50jInetMA"
youtube_stats:
  view_count: 385
  like_count: 8
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

Seth Larson and Mike Fiedler, the Python Software Foundation’s new full-time security engineers, presented their efforts to enhance supply chain security and protect the PyPI ecosystem.
Mike highlighted the successful completion of PyPI’s first-ever security audit, which yielded no critical findings, and detailed the implementation of a new API integration with security researchers to rapidly detect and remove malicious packages, such as those used for Discord credential theft.
Seth discussed his focus on CPython vulnerabilities and the promotion of "provenance" to verify the origin of software artifacts, while Mike emphasized the growing adoption of "trusted publishers" to eliminate the need for long-lived API tokens during package uploads.
Both engineers stressed that security is an evolving discipline requiring dedicated resources rather than volunteer efforts, citing their ability to respond swiftly to significant threats like the XZ backdoor.
They concluded by encouraging the community to utilize secure packaging tools and follow the PSF’s security blogs to stay informed about best practices and ongoing improvements.

# Main Points

|   # | Main point                                                                                                                                                |
| --: | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Seth Larson serves as a developer-in-residence sponsored by Alpha-Omega, focusing on supply chain security to ensure developer intent matches execution.  |
|   2 | Seth collaborates with various security communities to identify critical issues and teaches security practices to Python teams and maintainers.           |
|   3 | Seth’s recent work involves the Python Security Response Team, handling vulnerabilities, setting up CVEs, and ensuring facility reliability.              |
|   4 | Mike Fiedler is the PyPI safety and security engineer sponsored by Amazon Web Services, focusing on securing the package index.                           |
|   5 | PyPI hosts over half a million packages, serves over 800,000 users, and handles approximately 50,000 requests per second.                                 |
|   6 | A security audit of PyPI funded by the Open Technology Fund resulted in no critical findings, with reports and remediation steps made public.             |
|   7 | A common recent threat involves Discord credential stealers distributed via malicious packages recommended in the Python Discord community.               |
|   8 | Mike works with a community of researchers who evaluate uploaded packages for malicious signals and report findings to the PSF.                           |
|   9 | An integration API in private beta allows security researchers to send structured data to PyPI for automated decision-making and removal of bad packages. |
|  10 | Seth is shifting focus to package maintainers, promoting secure tooling and workflows against supply chain attacks.                                       |
|  11 | Seth is working on implementing provenance for packages to tie source code origin to artifacts for better policy enforcement.                             |
|  12 | Mike is improving malware response times to minimize the proliferation window for malicious packages and disincentivize attackers.                        |
|  13 | Mike is working on improving account management and developing API-driven actions for organizations to manage users and roles more effectively.           |
|  14 | Seth recommends users check the security features of packaging tools like PIP and Poetry to ensure the most secure experience.                            |
|  15 | Trusted publishers allow CI/CD providers like GitHub Actions to upload packages using short-lived tokens, eliminating the need for long-term credentials. |
|  16 | Over 11,000 projects currently use the trusted publishers feature to secure their package upload processes.                                               |
|  17 | Seth highlights the importance of full-time security staffing, citing the rapid response to the XZ backdoor incident as a key benefit.                    |
|  18 | The PSF security team relies on community trust to effectively manage security incidents and communicate with the Python ecosystem.                       |
|  19 | Both engineers emphasize that their roles build upon previous volunteer efforts to provide more consistent and focused security support.                  |

# Video

[![Video thumbnail](https://img.youtube.com/vi/S_50jInetMA/hqdefault.jpg)](https://www.youtube.com/watch?v=S_50jInetMA)

[Watch on YouTube](https://www.youtube.com/watch?v=S_50jInetMA)
