---
layout: default
title: "Cheese Must Stand: Defending the Python Library Ecosystem in 2025 - Patrick Smyth & Srishti Hegde"
nav_order: 117
parent: PyCon US 2025
type: Video Note
description: "Patrick Smith and Shisty Hegda from Chain Guard presented on defending the Python library ecosystem in 2025, highlighting the increasing threats to supply chain security."
resource: "https://www.youtube.com/watch?v=5cdC5pVkCvU"
youtube_stats:
  view_count: 1133
  like_count: 13
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

Patrick Smith and Shisty Hegda from Chain Guard presented on defending the Python library ecosystem in 2025, highlighting the increasing threats to supply chain security.
They discussed recent incidents, including a dependency confusion attack on PyTorch and a compromised GitHub Actions workflow affecting Ultralytics, which underscore the risks of malicious actors injecting malware into popular packages.
The speakers emphasized that Python’s widespread use in critical sectors like banking and healthcare makes it a high-value target for sophisticated attacks, such as typo squatting and credential theft.
To mitigate these risks, they recommended adopting trusted publishing, signing software artifacts with provenance data, and utilizing tools like SLSA to verify the integrity of dependencies.
Additionally, they introduced Chain Guard Libraries for Python, a service that rebuilds packages in a hardened environment to eliminate "software dark matter" and secure the build and distribution stages of the supply chain.

# Main Points

|   # | Main point                                                                                                                                     |
| --: | ---------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Patrick Smith and Shisty Hegda from Chain Guard presented on defending the Python library ecosystem in 2025.                                   |
|   2 | The Python ecosystem has evolved from early challenges like Python 2 vs 3 to a modern infrastructure supporting over 630,000 projects.         |
|   3 | PyPI hosts nearly 28 terabytes of packages and records 1.6 billion daily downloads.                                                            |
|   4 | The software supply chain environment has become more adverse due to AI-generated spam and sophisticated targeted attacks.                     |
|   5 | Python is now used in high-sensitivity sectors such as banking, healthcare, and government, increasing the stakes for security.                |
|   6 | Installing a single package often pulls in a complex graph of transitive dependencies, creating multiple points of attack.                     |
|   7 | Attackers can inject malware at various stages including source code, build, dependency resolution, and distribution.                          |
|   8 | Recent incidents include cross-index attacks on npm and PyPI, malicious packages stealing cloud credentials, and dependency confusion attacks. |
|   9 | A December 2022 PyTorch incident involved a malicious torch triton package that harvested sensitive data and transmitted it via DNS.           |
|  10 | Remediation for the PyTorch attack included removing the package, clearing caches, and renaming internal dependencies to prevent recurrence.   |
|  11 | The Ultralytics YOLO project suffered a supply chain attack where compromised GitHub Actions allowed bad distributions and API token theft.    |
|  12 | PyPI has implemented trusted publishing to replace long-lived API tokens with identity providers like GitHub.                                  |
|  13 | PyPI maintainers have introduced quarantine processes, two-factor authentication, and a reporting API for trusted reporters.                   |
|  14 | Tools like Snyk, Grype, and Trivy can scan software artifacts for known vulnerabilities in CI/CD workflows.                                    |
|  15 | The SLSA framework encourages signing software artifacts and adding provenance to verify integrity and origin.                                 |
|  16 | Chain Guard Libraries for Python secures the build and distribution stages by rebuilding packages in a protected factory environment.          |
|  17 | Building from source helps mitigate risks associated with "software dark matter," which refers to untraceable native binaries in wheels.       |
|  18 | Maintainers should use trusted publishing, sign artifacts with Sigstore, and scan upstream dependencies regularly.                             |
|  19 | Consumers should treat missing source links as a yellow flag and consider using repository managers to control package sources.                |
|  20 | Evaluating and minimizing dependencies is crucial because developers often overlook the security implications of transitive packages.          |

# Video

[![Video thumbnail](https://img.youtube.com/vi/5cdC5pVkCvU/hqdefault.jpg)](https://www.youtube.com/watch?v=5cdC5pVkCvU)

[Watch on YouTube](https://www.youtube.com/watch?v=5cdC5pVkCvU)
