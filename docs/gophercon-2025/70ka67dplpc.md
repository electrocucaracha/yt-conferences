---
layout: default
title: "GopherCon 2025: The Code You Reviewed is Not the Code You Built - Jess McClintock"
nav_order: 7
parent: GopherCon 2025
type: Video Note
description: "Jess Pentok from Google Cloud presents a critical analysis of the security gaps between reviewed source code and final build artifacts, arguing that traditional human code review is increasingly vu..."
resource: "https://www.youtube.com/watch?v=70ka67DpLPc"
youtube_stats:
  view_count: 1111
  like_count: 18
  channel_subscriber_count: 41100
tags:
  - gophercon-2025
  - video
  - learning
status: stable
generated:
  by: process:yt-summarizer-okf
  at: 2026-11-21T05:22:37+00:00
---

# Summary

Jess Pentok from Google Cloud presents a critical analysis of the security gaps between reviewed source code and final build artifacts, arguing that traditional human code review is increasingly vulnerable to sophisticated supply chain attacks.
Through detailed case studies of the Bolt DB Go, EventStream, TJ Actions, and XZ incidents, the talk demonstrates how malicious actors exploit ecosystem-specific behaviors—such as mutable Git tags, versioning discrepancies, and complex build rules—to hide backdoors and exfiltrate data while maintaining a clean appearance in public repositories.
To address these risks, Pentok introduces a capability-based security model that treats software permissions similarly to mobile app consent, emphasizing that the build artifact, not the source code, is the true source of security truth.
She presents CapSock, an open-source tool that performs call graph analysis on build artifacts to identify unexpected capabilities like network access or file system usage, thereby detecting malicious changes that evade source-level inspection.
The presentation concludes by urging developers to pin dependencies to specific commits rather than mutable tags and to adopt proactive, artifact-level analysis tools to bridge the trust gap in open source software.

# Main Points

|   # | Main point                                                                                                                                                                           |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   1 | A malicious package named Bolt DB Go persisted on the Go module proxy for years, containing a backdoor that allowed remote command execution.                                        |
|   2 | Attackers used typosquatting and large, noisy pull requests to hide malicious dependencies from human code reviewers.                                                                |
|   3 | The Go module proxy caches immutable copies of source code, meaning malicious versions remain available even after the original repository is cleaned or archived.                   |
|   4 | In the EventStream npm attack, a new maintainer injected a payload that stole Bitcoin from Copay Dash users by exploiting versioning rules to hide the malicious code from auditors. |
|   5 | The TJ Actions GitHub Action compromise involved leaking maintainer tokens to override Git tags, redirecting CI/CD pipelines to a malicious fork that exfiltrated secrets.           |
|   6 | Attackers exploited the temporal gap between tag verification and code retrieval, highlighting the risk of mutable Git tags in dependency management.                                |
|   7 | The XZ Utils incident demonstrated how complex build tools and obfuscated test files can hide backdoors in source code that are not visible during standard review.                  |
|   8 | The source of truth for security is the build artifact, not the source code, because the compiled output may differ from what was reviewed.                                          |
|   9 | Capability analysis treats software permissions like mobile app permissions, flagging unexpected access to network, file system, or code execution resources.                        |
|  10 | Capsock is a tool that analyzes Go build artifacts using call graph analysis to identify specific capabilities and transitive dependencies.                                          |
|  11 | Capsock uses SSA and VTA algorithms to trace function calls to standard library functions, reducing false positives compared to simple import analysis.                              |
|  12 | Only 3% of Go package updates add new capabilities, making such changes a strong indicator of potential security issues that warrant scrutiny.                                       |
|  13 | The capsock Git diff tool compares capabilities between two commits to detect new or changed behaviors in dependencies.                                                              |
|  14 | Capability analysis provides a proactive security approach by identifying potential harm from unexpected behavior changes, unlike reactive vulnerability scanners.                   |
|  15 | Analysis of the Go module proxy shows that 8.5% of packages with modified Git tags have capability differences, often due to dependency changes or accidental leaks.                 |
|  16 | Developers should pin dependencies to specific commit hashes rather than mutable tags to prevent tag manipulation attacks.                                                           |
|  17 | Capsock is available for Go and is currently in pilot for Rust, with plans to expand to other languages and ecosystems.                                                              |

# Video

[![Video thumbnail](https://img.youtube.com/vi/70ka67DpLPc/hqdefault.jpg)](https://www.youtube.com/watch?v=70ka67DpLPc)

[Watch on YouTube](https://www.youtube.com/watch?v=70ka67DpLPc)
