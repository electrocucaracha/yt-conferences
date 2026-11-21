---
layout: default
title: "Asleep at the Wheel: Getting your SBOMs to pay attention... - Sanchit Sahay, Abhishek Reddypalle"
nav_order: 77
parent: PyCon US 2026
type: Video Note
description: "Abhishek and Sanchit, PhD students from Purdue and NYU, address the critical issue of hidden native dependencies in Python software builds, which often cause runtime failures and security vulnerabi..."
resource: "https://www.youtube.com/watch?v=VYY3HnRtV6U"
youtube_stats:
  view_count: 174
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

Abhishek and Sanchit, PhD students from Purdue and NYU, address the critical issue of hidden native dependencies in Python software builds, which often cause runtime failures and security vulnerabilities despite successful package manager installations.
They argue that traditional Software Bills of Materials (SBOMs) are frequently inaccurate because they are generated before or after the build process, relying on static manifest files that miss dynamic elements like shared libraries, network calls, and build-time artifacts.
To solve this, they introduce SBOMit, an open-source tool that integrates with the Witness framework to observe the build process in real-time, capturing cryptographic attestations of file access, process execution, and network activity.
By enriching standard SBOMs with this live build data, SBOMit provides a verifiable and complete inventory of software components, effectively turning supply chain investigations into rapid database lookups and mitigating risks from compromised build pipelines.
The speakers conclude by encouraging developers to adopt these tools and standards like PEP 770 to ensure their SBOMs are accurate, secure, and compliant with emerging government regulations.

# Main Points

|   # | Main point |
| --: | ---------- |
|   1 | PhD students Abhishek from Purdue and Sanchit from NYU address the issue of non-reproducible Python builds caused by hidden native dependencies. |
|   2 | Common installation failures occur when pip reports success but imports fail due to missing shared objects or CUDA mismatches, as seen in libraries like vLLM and cryptography. |
|   3 | Pip metadata and requirements files only capture explicit Python packages, leaving invisible native libraries like OpenSSL and Rust code untracked. |
|   4 | These hidden dependencies create significant security risks, as evidenced by attacks like SolarWinds and Log4Shell where compromised build processes went undetected. |
|   5 | Software Bill of Materials (SBOMs) are required by US and EU governments to provide a machine-readable inventory of all software components. |
|   6 | Current SBOM generation tools often produce inaccurate data because they rely on stale manifest files or scan outputs after the build, missing transitive dependencies and build-time artifacts. |
|   7 | Analysis of 5,000 Docker Hub images revealed that 30% of files are untracked by package managers, a systemic issue also found in Maven Central, Jenkins, and VS Code extensions. |
|   8 | The proposed solution, SBOMit, moves SBOM generation to the build time to capture real-time data on file access, network calls, and spawned processes. |
|   9 | SBOMit uses the Witness tool and in-toto specifications to record cryptographically signed attestations of build activities, ensuring data integrity and verifiability. |
|  10 | Witness monitors system calls using strace and network traffic using eBPF to detect unexpected registry access or malicious network calls during the build. |
|  11 | The enriched SBOM combines traditional software composition analysis with in-toto attestations to reveal missed packages, shared object files, and accurate version information. |
|  12 | A demonstration using a Rust-based Python wheel showed that SBOMit identified cargo packages and shared libraries that standard tools like Sift and Trivy missed. |
|  13 | SBOMit is an open-source project supported by the OpenSSF, encouraging users to verify their packaging contents and contribute to the tool’s development. |
|  14 | The project advocates for treating SBOMs as active security tools rather than mere compliance documents to effectively combat supply chain vulnerabilities. |
|  15 | Users are advised to inspect wheel files for unlisted dependencies and adopt PEP 770 standards to improve package detection and SBOM accuracy. |

# Video

[![Video thumbnail](https://img.youtube.com/vi/VYY3HnRtV6U/hqdefault.jpg)](https://www.youtube.com/watch?v=VYY3HnRtV6U)

[Watch on YouTube](https://www.youtube.com/watch?v=VYY3HnRtV6U)
