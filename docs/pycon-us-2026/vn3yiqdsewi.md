---
layout: default
title: "GitHub Actions Security in Python Packages - Andrew Nesbitt"
nav_order: 80
parent: PyCon US 2026
type: Video Note
description: "Andrew Nesbitt, creator of the Ecosystems project, presented a critical analysis of GitHub Actions security vulnerabilities within the Python package ecosystem."
resource: "https://www.youtube.com/watch?v=vn3YIqdseWI"
youtube_stats:
  view_count: 222
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

Andrew Nesbitt, creator of the Ecosystems project, presented a critical analysis of GitHub Actions security vulnerabilities within the Python package ecosystem.
By mining data from over 864,000 PyPI packages, he identified widespread security footguns, including excessive default permissions, unpinned mutable action tags, and dangerous "pull request target" triggers that allow attackers to execute arbitrary code and steal credentials.
Nesbitt highlighted the "Ultralytics" attack as a prime example of how these configuration flaws can be chained to publish malicious packages, noting that thousands of repositories remain vulnerable to similar exploits.
To mitigate these risks, he strongly recommended adopting trusted publishing to eliminate long-lived tokens and integrating the Zizmore linter into CI pipelines to automatically detect and block insecure workflow configurations.
Although GitHub has announced plans to improve security features such as lock files and restricted triggers, Nesbitt emphasized that these changes are not yet fully implemented, urging developers to proactively harden their workflows immediately.

# Main Points

|   # | Main point |
| --: | ---------- |
|   1 | Andrew Nesbbit presented on GitHub Actions security for Python packages, highlighting risks in CI/CD workflows. |
|   2 | Approximately 44,000 Python repositories still use long-lived PyPI tokens instead of the more secure trusted publishing method. |
|   3 | GitHub Actions functions like a package manager but lacks critical features such as lock files and immutable versioning. |
|   4 | Mutable tags allow maintainers to force-push changes to existing versions, enabling silent supply chain attacks. |
|   5 | The Ultralytics attack demonstrated how forked repositories and pull request triggers can expose PyPI API keys for malicious package publishing. |
|   6 | 1,300 other repositories were identified with the same vulnerable configuration as the compromised Ultralytics project. |
|   7 | The Zizmore tool was used to audit 150,000 repositories, revealing widespread security misconfigurations in workflow files. |
|   8 | 100,000 repositories have excessive permissions enabled due to legacy default settings from before February 2023. |
|   9 | 85,000 repositories use unpinned action versions, creating vulnerability to tag manipulation and dependency confusion. |
|  10 | 21,000 repositories are susceptible to template injection, where untrusted input like pull request titles is executed in bash. |
|  11 | 15,000 repositories are vulnerable to cache poisoning, allowing one workflow to inject data into another workflow's execution. |
|  12 | Dangerous triggers, specifically pull_request_target, allow attackers to run code from forks with access to repository secrets. |
|  13 | 3,000 workflows reference archived actions that are no longer maintained and may break or become insecure. |
|  14 | Third-party actions often contain unpinned internal dependencies and reach out to multiple external hosts, increasing attack surface. |
|  15 | GitHub has announced plans to add lock files and ban pull_request_target, but these features are not yet fully implemented. |
|  16 | Recommended hardening measures include using trusted publishing, integrating Zizmore into CI, and removing pull_request_target triggers. |
|  17 | Data mining showed a temporary 15% drop in dangerous feature usage after the Trivy vulnerability, but new packages continue to adopt insecure patterns. |

# Video

[![Video thumbnail](https://img.youtube.com/vi/vn3YIqdseWI/hqdefault.jpg)](https://www.youtube.com/watch?v=vn3YIqdseWI)

[Watch on YouTube](https://www.youtube.com/watch?v=vn3YIqdseWI)
