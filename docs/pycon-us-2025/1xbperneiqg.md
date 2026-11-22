---
layout: default
title: "PSF - Update from our Security Engineers"
nav_order: 104
parent: PyCon US 2025
type: Video Note
description: "Mike Fedler and Seth Larson, the Python Software Foundation’s security engineers, presented an update on their recent security initiatives, highlighting their complementary expertise in PyPI and br..."
resource: "https://www.youtube.com/watch?v=1xbPerneIqg"
youtube_stats:
  view_count: 411
  like_count: 17
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

Mike Fedler and Seth Larson, the Python Software Foundation’s security engineers, presented an update on their recent security initiatives, highlighting their complementary expertise in PyPI and broader Python ecosystem security.
Fedler detailed efforts to enhance software supply chain transparency by developing software bills of materials for Python packages and implementing default system certificate usage in PyPI to improve corporate proxy compatibility.
He also discussed the automation of the security response team’s advisory process and preparation for the upcoming Cyber Resilience Act, emphasizing a "security in a box" approach to share best practices with the wider community.
Larson focused on PyPI-specific improvements, including the implementation of package quarantine capabilities to safely investigate malicious uploads without immediate deletion, and the full enforcement of two-factor authentication for all PyPI uploads to mitigate account takeover risks.
Additionally, Larson addressed ongoing work to prevent domain resurrection attacks by managing email deliverability for expired domains and improving the detection of typo-squatting, while encouraging the community to stay informed through the PyPI and PSF blogs.

# Main Points

|   # | Main point                                                                                                                                                           |
| --: | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Mike Fedler and Seth Larson are the Python Software Foundation security engineers presenting their annual update.                                                    |
|   2 | Seth focuses on the breadth of Python security, while Mike focuses on the depth of PyPI security.                                                                    |
|   3 | A new project is developing software bills of materials for Python packages to help machines parse complex dependencies like C, Rust, and JavaScript.                |
|   4 | This SBOM initiative aims to improve the accuracy of vulnerability scanners and compliance tools for Python applications.                                            |
|   5 | PyPI now uses system certificates by default, which allows users behind corporate proxies to maintain secure connections without disabling certificate verification. |
|   6 | The security response team published 16 advisories in the past year and automated the alerting and record-keeping processes for new fixes.                           |
|   7 | The team is preparing the Python ecosystem for the Cyber Resilience Act, with key requirements taking effect in 2026.                                                |
|   8 | Mike promotes a "security in a box" approach, creating guides and tools that other communities like Django and scientific projects can remix.                        |
|   9 | Seth implemented a quarantine feature for PyPI to temporarily remove malicious packages from installation while allowing time for investigation.                     |
|  10 | Automated quarantine now triggers based on trusted inbound reports, reducing the time malicious packages remain live on the index.                                   |
|  11 | Full enforcement of two-factor authentication for all PyPI uploads became mandatory on January 1st of this year.                                                     |
|  12 | This 2FA requirement significantly reduces the risk of account takeovers through stolen credentials and unauthorized API token creation.                             |
|  13 | Seth is working on email deliverability improvements to prevent domain resurrection attacks where attackers exploit expired domains to hijack packages.              |
|  14 | New detection systems for typo squatting are being deployed to identify suspicious package names, though they currently generate some false positives.               |
|  15 | The team encourages users to subscribe to the PyPI and PSF blogs to stay updated on security features and guides released incrementally.                             |
|  16 | Alpha Omega is acknowledged as the sponsor supporting the Python Software Foundation security developers and residents.                                              |

# Video

[![Video thumbnail](https://img.youtube.com/vi/1xbPerneIqg/hqdefault.jpg)](https://www.youtube.com/watch?v=1xbPerneIqg)

[Watch on YouTube](https://www.youtube.com/watch?v=1xbPerneIqg)
