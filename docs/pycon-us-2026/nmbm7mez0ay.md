---
layout: default
title: "From Cheese Shop to Fortress: Building Secure, Production-Ready Python Wheels (Sponsor: Chainguard)"
nav_order: 94
parent: PyCon US 2026
type: Video Note
description: "Dan Fraser, a principal engineer at Chainguard, delivered a talk at PyCon 2026 on the escalating threat of malware in the software supply chain, highlighting how low-cost AI tools have lowered the ..."
resource: "https://www.youtube.com/watch?v=NmBm7MeZ0aY"
youtube_stats:
  view_count: 346
  like_count: 1
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

Dan Fraser, a principal engineer at Chainguard, delivered a talk at PyCon 2026 on the escalating threat of malware in the software supply chain, highlighting how low-cost AI tools have lowered the barrier for attacks such as typosquatting, dependency confusion, and account takeovers.
He detailed recent high-profile incidents, including the Trivy scanner compromise and the LightLLM infection, which exploited stolen credentials to inject malicious payloads into popular Python packages.
To mitigate these risks, Fraser recommended best practices such as scanning dependencies for malware, using PyPI trusted publishing, implementing cooldown periods for new package versions, and avoiding long-lived tokens in CI/CD pipelines.
He then introduced Chainguard Libraries, a product that provides hardened, source-built Python wheels with SLSA provenance and SBOMs to ensure supply chain integrity and offer optional CVE remediation.
Finally, Fraser shared technical lessons learned from building complex libraries like PyTorch, emphasizing the importance of matching upstream build configurations, such as static linking strategies and toolchain compatibility, to ensure functional parity and security.

# Main Points

|   # | Main point |
| --: | ---------- |
|   1 | The speaker, Dan Fraser, is a principal engineer at Chainguard working on Python libraries and has a background in Linux distributions like Debian and Ubuntu. |
|   2 | Chainguard aims to be a safe source for open source, providing hardened container images and libraries built from upstream source code with Salsa V3 provenance. |
|   3 | The software supply chain is vulnerable to attacks such as typosquatting, dependency confusion, tag hijacking, account takeovers, and brand jacking. |
|   4 | PyPI is a significant target for malware due to its scale, with 40 terabytes of data and 4.4 billion daily downloads. |
|   5 | Recent high-profile attacks include the Trivy scanner compromise, the LightLLM malware injection, and the Mini Worm attack on TanStack CI/CD. |
|   6 | AI tools like Claude and ChatGPT are increasingly used by attackers to automate malware creation, data theft, and ransomware drafting. |
|   7 | Recommended security practices include scanning for malware, verifying signatures, using cooldown periods for new packages, and limiting dependency surface area. |
|   8 | Developers should use PyPI trusted publishing, CI/CD for builds, and avoid long-lived tokens to reduce security risks. |
|   9 | Chainguard libraries provide two indexes: one for malware-resistant builds matching PyPI and another for CVE remediation with backported patches. |
|  10 | Building Python wheels correctly requires matching upstream build practices, such as static linking decisions for libraries like MKL and OpenSSL. |
|  11 | Statically linking libstdc++ can cause crashes due to global state conflicts; the solution involves using compatibility layers similar to manylinux images. |
|  12 | Chainguard uses automated parity testing to compare their wheels against upstream versions, checking shared libraries, ABIs, and runtime test results. |
|  13 | S-bombs and Salsa provenance files allow users to trace the exact source code, build environment, and dependencies used to create a library. |
|  14 | The team discovered that opportunistic linking of libraries like OpenBLAS during builds can introduce duplicate dependencies and crashes. |
|  15 | Chainguard libraries are currently freely available until the end of June, and the company is hiring for various roles. |
|  16 | For libraries built in private mirrors, signing artifacts and including S-bombs are recommended to prove integrity and provenance. |
|  17 | A cooldown period of 2 to 3 days is advised for pulling new packages to allow time for malware detection, while monitoring for critical CVEs. |

# Video

[![Video thumbnail](https://img.youtube.com/vi/NmBm7MeZ0aY/hqdefault.jpg)](https://www.youtube.com/watch?v=NmBm7MeZ0aY)

[Watch on YouTube](https://www.youtube.com/watch?v=NmBm7MeZ0aY)
