---
layout: default
title: "PSF - Update from our Security Engineers"
nav_order: 11
parent: PyCon US 2026
type: Video Note
description: "Seth Larson and Mike Fiedler from the Python Software Foundation presented an update on the evolving security landscape of the Python ecosystem, highlighting a significant increase in supply chain ..."
resource: "https://www.youtube.com/watch?v=PtMysG7aAO0"
youtube_stats:
  view_count: 273
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

Seth Larson and Mike Fiedler from the Python Software Foundation presented an update on the evolving security landscape of the Python ecosystem, highlighting a significant increase in supply chain attacks and software vulnerabilities.
Mike detailed the rise of persistent malware targeting transitive dependencies and cross-ecosystem secrets, emphasizing the critical importance of auditing dependencies and adopting trusted publishers to minimize token exposure.
He also reported on PyPI’s successful second security audit by Trail of Bits, which identified and remediated high-severity bugs, including a silent permission transfer issue.
Seth discussed the growing volume of CVEs, attributing the trend to the integration of large language models with traditional security tools, and highlighted efforts to standardize Software Bill of Materials (SBOMs) to improve vulnerability detection across diverse package formats.
Additionally, he outlined the formalization of the Python Security Response Team through PEP 811, which has facilitated the addition of new members and improved coordination for vulnerability disclosure.
The speakers concluded by urging the community to support the Python Software Foundation and its sponsors, such as Google and Anthropic, to sustain these critical security initiatives.

# Main Points

|   # | Main point                                                                                                                                                                                   |
| --: | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Seth Larson and Mike Fiedler from the Python Software Foundation presented on evolving security threats and recent infrastructure improvements.                                              |
|   2 | Malware attacks are increasingly targeting upstream dependencies to exploit transitive blast radius issues, affecting projects like num2words and light-llm.                                 |
|   3 | Attackers utilize lateral movement to compromise secrets stored in monorepos that manage multiple language SDKs and CI systems.                                                              |
|   4 | Recent incidents include the Shai Hulud worm, which has been made public and is being improved via community pull requests.                                                                  |
|   5 | PyPI has implemented trusted publishers to minimize token exposure, ensuring tokens are short-lived, cryptographically bound to repositories, and eliminating the risk of credential replay. |
|   6 | The Python Software Foundation passed its second security audit conducted by Trail of Bits, funded by the Sovereign Tech Agency.                                                             |
|   7 | The audit identified and fixed high-severity bugs, including a silent permission transfer issue during project ownership changes.                                                            |
|   8 | Trail of Bits contributed CodeQL queries to the CI/CD pipeline to prevent future occurrences of identified vulnerabilities.                                                                  |
|   9 | The number of published CVEs for Python and pip is rising, with approximately 65 vulnerabilities expected in the current year.                                                               |
|  10 | A white paper identified seven vulnerabilities related to ZIP and tar archive format inconsistencies that could cause different tools to interpret packages differently.                     |
|  11 | The Python Security Response Team established governance through PEP 811, enabling the addition of nine new team members to handle increased reporting volumes.                              |
|  12 | Software Bill of Materials (SBOM) adoption is expanding, with around 300 packages explicitly adding SBOMs to improve vulnerability detection across ecosystems.                              |
|  13 | The new PyCon US security talk track received high attendance, reflecting strong community interest in security education.                                                                   |
|  14 | Supporting the Python Software Foundation through sponsorship is crucial for maintaining the security of the Python ecosystem.                                                               |
|  15 | Security news and updates are regularly published on the PyPI and Python Software Foundation blogs.                                                                                          |

# Video

[![Video thumbnail](https://img.youtube.com/vi/PtMysG7aAO0/hqdefault.jpg)](https://www.youtube.com/watch?v=PtMysG7aAO0)

[Watch on YouTube](https://www.youtube.com/watch?v=PtMysG7aAO0)
