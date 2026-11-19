---
layout: default
title: "Unconference Session: How ​Should ​Maintainers ​Navigate (and ​Review) AI-based PRs?​"
nav_order: 13
parent: "Maintainer Summit 2026 - Europe"
type: Video Note
description: 'Natalie Blatzko, a maintainer in the Kubernetes SIG Docs, facilitated an unconference session to address the growing burden of AI-generated pull requests (PRs) and "AI slop" on open-source maintain...'
resource: "https://www.youtube.com/watch?v=5FiAnB8Preo"
tags:
  - maintainer-summit-2026-europe
  - video
  - learning
status: stable
generated:
  by: process:yt-summarizer-okf
  at: 2026-11-16T15:59:05+00:00
---

# Summary

Natalie Blatzko, a maintainer in the Kubernetes SIG Docs, facilitated an unconference session to address the growing burden of AI-generated pull requests (PRs) and "AI slop" on open-source maintainers.
Participants from various CNCF projects, including Kubernetes, Cilium, Harbor, and K3s, confirmed that they face significant challenges distinguishing between genuine human contributions and low-effort, undisclosed AI submissions, which often result in unresponsive or bot-like interactions during code reviews.
The discussion highlighted that while using AI tools is not inherently banned, the lack of transparency and the resulting maintenance toil are critical issues, with some maintainers noting that AI-generated code can even introduce security vulnerabilities.
Proposed solutions included implementing stricter disclosure requirements in PR templates, enforcing code of conduct violations for dishonesty, and adopting a "one-strike" or timeout policy for bad-faith actors, though there was debate over whether such rules should be mandated at the CNCF level or left to individual projects.
The session concluded with a commitment to draft improved guidelines and engage with other projects to create flexible, project-specific policies that balance the need for quality contributions with the reality of AI-assisted development.

# Main Points

|   # | Main point                                                                                                                                                                                                                    |
| --: | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Kubernetes SIG Docs receives a high volume of AI-generated pull requests, with approximately 150 open PRs at any given time, many of which are not disclosed as AI-assisted.                                                  |
|   2 | A significant portion of review comments in these PRs are also AI-generated, creating a burden where maintainers interact with bots rather than human contributors.                                                           |
|   3 | Current Kubernetes guidance requires contributors to disclose AI use in PR descriptions and prohibits using AI to respond to review comments, but enforcement remains challenging.                                            |
|   4 | Maintainers struggle to distinguish between genuine new contributors using AI to lower entry barriers and bad-faith actors submitting low-effort, automated PRs.                                                              |
|   5 | There is a lack of universal CNCF-level guidance on AI usage, with projects like Kubernetes, Cilium, Harbor, and K3s facing similar issues but developing different internal policies.                                        |
|   6 | Cilium recommends asking "why" questions during reviews to verify human understanding and explicitly discourages using LLMs to edit responses for non-native English speakers to preserve authenticity.                       |
|   7 | Security concerns include AI-generated code introducing vulnerabilities and an increase in low-effort spam in bug bounty programs, overwhelming security teams.                                                               |
|   8 | Proposed solutions include implementing a "one-strike" or timeout policy for violations, requiring mandatory AI disclosure in PR templates, and potentially using prompt injection techniques to detect AI-generated reviews. |
|   9 | Some maintainers suggest leveraging AI for pre-filtering and initial code reviews to reduce human toil, while keeping final approval with humans.                                                                             |
|  10 | There is debate over whether a global CNCF policy is necessary or if projects should retain the freedom to define their own AI guidelines based on their specific capacity and needs.                                         |
|  11 | The consensus is that banning AI entirely is not feasible, but stricter enforcement of honesty and human interaction is required to protect maintainer time and project quality.                                              |
|  12 | Follow-up actions include opening discussions in the Kubernetes project to refine guidance and collaborating with other CNCF projects to share best practices.                                                                |

# Video

[![Video thumbnail](https://img.youtube.com/vi/5FiAnB8Preo/hqdefault.jpg)](https://www.youtube.com/watch?v=5FiAnB8Preo)

[Watch on YouTube](https://www.youtube.com/watch?v=5FiAnB8Preo)
