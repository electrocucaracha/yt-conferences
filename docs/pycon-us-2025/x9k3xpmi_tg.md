---
layout: default
title: "Phantom Dependencies: is your requirements.txt haunted? - Seth Michael Larson"
nav_order: 12
parent: PyCon US 2025
type: Video Note
description: 'Seth, a security engineer at the Python Software Foundation, presents a talk on "phantom dependencies," which are software components used by an application but not declared in its manifest, often ...'
resource: "https://www.youtube.com/watch?v=x9K3xPmi_tg"
youtube_stats:
  view_count: 1627
  like_count: 35
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

Seth, a security engineer at the Python Software Foundation, presents a talk on "phantom dependencies," which are software components used by an application but not declared in its manifest, often resulting from bundling, static linking, or the inclusion of non-Python code like C or Rust.
These dependencies pose a significant security risk because standard vulnerability scanners rely on metadata to identify software, and phantom dependencies often lack the necessary labels, leading to false negatives where vulnerabilities go undetected.
To address this, Seth introduces PEP 770, a standard he authored that reserves a new `dist-info/sboms` directory within Python wheels to store Software Bill of Materials (SBOM) data, thereby providing ecosystem-agnostic metadata that scanners can utilize.
He demonstrates how tools like Auditwheel can automatically generate these SBOMs during the build process, allowing scanners to accurately detect and analyze all bundled libraries.
The talk concludes with practical advice for developers to create high-quality manifests, verify scanner capabilities across different packaging ecosystems, and support the PSF’s efforts to improve Python’s supply chain security.

# Main Points

|   # | Main point                                                                                                                                   |
| --: | -------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Phantom dependencies are software components used by code but not declared in the manifest, creating security blind spots.                   |
|   2 | The term was coined by Endor Labs in their 2023 supply chain security report.                                                                |
|   3 | Standard Python manifests like requirements.txt and pip freeze often miss bundled libraries such as libwebp or libjpeg.                      |
|   4 | Software Bill of Materials (SBOMs) are ecosystem-agnostic manifests that provide a comprehensive list of all software components.            |
|   5 | SBOMs are crucial for compliance, vulnerability scanning, and meeting regulations like the Cyber Resilience Act.                             |
|   6 | Scanners typically rely on metadata rather than analyzing file contents, so unlabeled software remains undetected.                           |
|   7 | Phantom dependencies often arise from deliberate practices like bundling, vendoring, and static linking for portability.                     |
|   8 | Python wheels frequently bundle non-Python code, including C, C++, Rust, and JavaScript, which standard packaging metadata cannot represent. |
|   9 | PEP 770, authored by Seth, reserves a dist-info/sboms directory in Python wheels to store SBOM documents.                                    |
|  10 | Tools like auditwheel can automatically generate CycloneDX SBOMs when bundling libraries into manylinux wheels.                              |
|  11 | Implementing PEP 770 allows scanners to detect previously invisible dependencies without requiring changes to the application code.          |
|  12 | Users should create manifests using tools like Sift to verify that scanners are detecting all software components.                           |
|  13 | It is recommended to use scanners that support non-Python ecosystems, such as Grype or Trivy, rather than relying solely on pip audit.       |
|  14 | Pip audit is only effective for pure Python dependencies and should be combined with other scanners for comprehensive coverage.              |
|  15 | To ensure vulnerability data availability, users should test scanners against known vulnerabilities in each packaging ecosystem.             |
|  16 | The Python Software Foundation offers developer and resident programs to support critical ecosystem work like security.                      |
|  17 | SBOM formats support signatures and download URLs, which can be used to verify the integrity of bundled software.                            |
|  18 | Rebuilding wheels from source or verifying checksums can help mitigate risks associated with untrusted bundled libraries.                    |
|  19 | Large application stacks should prioritize investigating compiled libraries and non-Python dependencies to identify security gaps.           |
|  20 | Package managers like UV may not natively generate SBOMs, but external tools can scan virtual environments and container images directly.    |

# Video

[![Video thumbnail](https://img.youtube.com/vi/x9K3xPmi_tg/hqdefault.jpg)](https://www.youtube.com/watch?v=x9K3xPmi_tg)

[Watch on YouTube](https://www.youtube.com/watch?v=x9K3xPmi_tg)
