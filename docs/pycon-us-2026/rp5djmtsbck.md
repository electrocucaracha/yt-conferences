---
layout: default
title: "Python Security: What we've done, now AI & Glasswing are changing everything (Sponsor: Alpha-Omega)"
nav_order: 120
parent: PyCon US 2026
type: Video Note
description: "This presentation by Mike Fiedler and Seth from the Python Software Foundation (PSF) and Alpha Omega addresses the escalating security challenges in the Python ecosystem, driven by the integration ..."
resource: "https://www.youtube.com/watch?v=RP5djmTSbCk"
youtube_stats:
  view_count: 341
  like_count: 2
  channel_subscriber_count: 34500
tags:
  - pycon-us-2026
  - video
  - learning
status: stable
generated:
  by: process:yt-summarizer-okf
  at: 2026-11-20T08:08:06+00:00
---

# Summary

This presentation by Mike Fiedler and Seth from the Python Software Foundation (PSF) and Alpha Omega addresses the escalating security challenges in the Python ecosystem, driven by the integration of AI with existing security tools.
The speakers highlight a fourfold increase in malware reports and vulnerability disclosures, noting that AI has significantly reduced the cost and time required for attackers to identify and exploit vulnerabilities, thereby intensifying the asymmetry between defenders and attackers.
To combat this, the PSF has implemented rapid response mechanisms such as automatic quarantine of malicious packages, trusted reporter programs, and dependency cooldowns, which prevent the installation of recently published packages to mitigate "watering hole" attacks.
The talk also details the formalization of the Python Security Response Team through PEP 811 and the coordinated remediation of critical vulnerabilities in archive handling across CPython, pip, and uv.
Finally, the presenters provide actionable advice for maintainers and users, recommending the adoption of dependency locking, security scanning tools like Zizmore and CodeQL, the creation of comprehensive threat models, and the establishment of clear security policies to prepare for a future of accelerated vulnerability discovery and exploitation.

# Main Points

|   # | Main point                                                                                                                                           |
| --: | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Alpha Omega sponsors the Python Software Foundation, providing staff roles and cross-ecosystem security collaboration.                               |
|   2 | The PSF is a small nonprofit with approximately 13 staff members, including dedicated security engineers for PyPI and CPython.                       |
|   3 | AI and LLMs combined with deterministic security tools have significantly reduced the cost and time required to find vulnerabilities.                |
|   4 | Inbound malware reports to PyPI have increased fourfold year-over-year, while the number of security staff has remained constant.                    |
|   5 | Watering hole attacks target established projects to exploit user trust, distinct from new malicious package creation.                               |
|   6 | The ShyHulu worm exploited insecure GitHub Actions settings in the Trivy scanner to exfiltrate CI environment tokens.                                |
|   7 | Attackers use compromised tokens to publish malicious packages, exfiltrate cryptocurrency wallets, or move laterally across ecosystems.              |
|   8 | The LightLLM exploit demonstrated that unpinned dependencies allow rapid malware propagation, with 40-50% of downloads being unpinned.               |
|   9 | PyPI implemented a quarantine feature to remove malicious releases from the index while keeping them visible for investigation.                      |
|  10 | Trusted reporters with low false-positive rates can trigger automatic quarantine actions, reducing response time during off-hours.                   |
|  11 | A new feature allows quarantining specific releases rather than entire projects, preserving access to safe versions for existing users.              |
|  12 | PyPI underwent a second security audit funded by the German Sovereign Tech Agency, with findings addressed by Alpha Omega staff.                     |
|  13 | Dependency cooldowns in installers like pip and uv prevent installation of packages published within a recent timeframe, mitigating fresh attacks.   |
|  14 | The volume of vulnerability reports to the Python Security Response Team is expected to reach 400 in 2026, a fourfold increase.                      |
|  15 | PEP 811 formalized the governance and membership process for the Python Security Response Team to handle increased workload.                         |
|  16 | Coordinated fixes were implemented for tar and ZIP archive vulnerabilities across CPython, pip, and uv, with mitigations deployed at the PyPI level. |
|  17 | Future plans include evolving trusted publishing to limit token scope and duration, reducing the impact of CI credential theft.                      |
|  18 | A staged release process is being considered to allow time for security scanning before new packages become globally available.                      |
|  19 | CPython aims to extend verification materials to downstream redistributors like Docker images and Linux distros to ensure integrity.                 |
|  20 | Maintainers are advised to use security tools like Zizmor, CodeQL, and Semgrep to scan repositories and workflows.                                   |
|  21 | Writing a threat model helps contextualize known risks and reduces false positive reports from automated security scanners.                          |
|  22 | Projects should publish a security policy and security.txt file to provide secure reporting channels and clear guidelines.                           |
|  23 | Users should lock dependencies using tools like uv lock or pip compile to ensure reproducibility and prevent supply chain attacks.                   |
|  24 | Implementing dependency cooldowns and vulnerability scanning helps users protect against rapid exploitation of new advisories.                       |
|  25 | The time to exploit vulnerabilities is decreasing, requiring users to prepare for faster patching cycles and defense in depth.                       |
|  26 | A new security track at PyCon US features eight talks by security experts to further educate the community.                                          |
|  27 | Trusted publishers are vetted for security practices and infrastructure stability before being approved on PyPI.                                     |
|  28 | The PSF encourages community involvement in security response but requires careful vetting due to the sensitivity of unpatched vulnerabilities.      |

# Video

[![Video thumbnail](https://img.youtube.com/vi/RP5djmTSbCk/hqdefault.jpg)](https://www.youtube.com/watch?v=RP5djmTSbCk)

[Watch on YouTube](https://www.youtube.com/watch?v=RP5djmTSbCk)
