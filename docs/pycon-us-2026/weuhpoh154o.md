---
layout: default
title: "Breaking Bad (Packages): Why Traditional Vulnerability... - Shelby Cunningham and Madison Ficorilli"
nav_order: 130
parent: PyCon US 2026
type: Video Note
description: Shelby Cunningham and Madison Figurelli from GitHub’s Advisory Database and OSS CNA team present a critical analysis of why traditional vulnerability tracking mechanisms often fail to address moder...
resource: "https://www.youtube.com/watch?v=wEUHpOH154o"
youtube_stats:
  view_count: 611
  like_count: 3
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

Shelby Cunningham and Madison Figurelli from GitHub’s Advisory Database and OSS CNA team present a critical analysis of why traditional vulnerability tracking mechanisms often fail to address modern supply chain attacks.
They argue that current systems, such as the CVE framework, are ill-suited for tracking malware because CVE rules explicitly prohibit assigning IDs to deliberately malicious code, creating a significant gap in security visibility.
Through case studies of the XZ Utils backdoor, the TJ Actions compromise, and the large-scale ShyHollude campaign, the speakers demonstrate that tracking systems are heavily registry-centric and rely on fragile, human-dependent processes that break down when maintainers lose account access or when attacks span multiple ecosystems.
The discussion highlights that while mature registries like npm have established advisory workflows, less mature ecosystems and cross-ecosystem attacks, such as the Trivy compromise affecting PyPI, result in delayed alerts and inconsistent visibility for defenders.
Ultimately, the team concludes that supply chain attacks are graph-shaped and interconnected, whereas current tracking mechanisms remain siloed, necessitating improved automation, better cross-ecosystem coordination, and a shift toward more resilient, automated alerting systems to effectively protect the open-source software supply chain.

# Main Points

|   # | Main point |
| --: | ---------- |
|   1 | The GitHub Advisory Database and OSS CNA team track software vulnerabilities, malicious packages, and compromised versions using CVEs and ecosystem-specific databases. |
|   2 | CVE rules explicitly prohibit assigning IDs to deliberately malicious code, creating a gap in tracking pure malware compared to vulnerabilities. |
|   3 | The XZ Utils backdoor case highlighted that tracking systems are registry-centric, causing C libraries and tarballs to fall through the cracks of modern supply chain security tooling. |
|   4 | In the XZ Utils incident, the lack of a package registry anchor and ecosystem-native alerting forced defenders to rely on out-of-band intelligence for delayed awareness. |
|   5 | The TJ Actions compromise demonstrated that current systems have a critical human dependency, as the alert pipeline broke when the maintainer lost account access. |
|   6 | Miter had to manually issue a CVE for the TJ Actions incident because the standard GitHub advisory creation process was unavailable due to the maintainer's lockout. |
|   7 | The Shy Hallude malware campaign on npm involved hundreds of packages, making it difficult to track with individual CVEs due to varying vectors and the need for campaign-level context. |
|   8 | Defenders struggle to assess the impact of large-scale malware campaigns because individual package IDs lack the connections needed to understand the broader threat. |
|   9 | The Trivy compromise showed that cross-ecosystem attacks require fragile bridges like PySEC and the GitHub Advisory Database to propagate alerts from GitHub Actions to PyPI. |
|  10 | Cross-ecosystem alert propagation is not automatic and requires multiple manual steps, creating a risk of silent failure if any part of the chain breaks. |
|  11 | The Tanstack compromise marked one of the first documented cases of a malicious npm package carrying valid Salsa provenance through the entire pipeline. |
|  12 | The Tanstack incident involved chaining three separate vulnerabilities and affected both npm and PyPI packages, raising questions about the adequacy of single CVEs for multi-ecosystem campaigns. |
|  13 | The OpenSSF malicious packages database is currently the most mature central repository for tracking open-source malware, including PyPI packages. |
|  14 | Technical controls such as dependency cooldowns and pinning actions can help mitigate the impact of rapid supply chain compromises. |
|  15 | Establishing out-of-band communication channels and trust networks with maintainers is crucial for incident response when primary accounts are compromised. |
|  16 | Mentioning nation-state actors like North Korea targeting open source developers is an effective way to convey the severity of supply chain risks to non-technical stakeholders. |

# Video

[![Video thumbnail](https://img.youtube.com/vi/wEUHpOH154o/hqdefault.jpg)](https://www.youtube.com/watch?v=wEUHpOH154o)

[Watch on YouTube](https://www.youtube.com/watch?v=wEUHpOH154o)
