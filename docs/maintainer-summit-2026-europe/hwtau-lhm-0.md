---
layout: default
title: "The Practices That Made Me Go 'Wow': What Every CNCF Project Ca... Rohit Agrawal & Kateryna Nezdolii"
nav_order: 21
parent: "Maintainer Summit 2026 - Europe"
type: Video Note
description: "Rohit and Katrina, maintainers of the Envoy proxy, present a comprehensive overview of the project’s governance, security, and automation practices designed to ensure stability and maintainability."
resource: "https://www.youtube.com/watch?v=hwTaU-lHm-0"
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

Rohit and Katrina, maintainers of the Envoy proxy, present a comprehensive overview of the project’s governance, security, and automation practices designed to ensure stability and maintainability.
They detail a tiered maintenance structure that includes domain experts, maintainers, and senior maintainers, supported by a strict code ownership model and a weekly on-call rotation to prevent the bystander effect and ensure timely issue triage.
To manage risk in a large C++ codebase, Envoy employs runtime guards for secure feature rollouts, a three-phase deprecation process, and rigorous testing standards that include nearly 100% test coverage, fuzzing, and various sanitizers to catch memory and thread-related bugs.
The project also emphasizes supply chain accountability through named shepherds for API and dependencies, dependency scorecards, and automated tools that handle stale PRs and dependency updates.
Finally, the speakers offer actionable takeaways for other open-source projects, recommending the adoption of CI-validated documentation, automated stale PR closing, and structured deprecation cycles to improve project health and reduce maintenance burden.

# Main Points

|   # | Main point                                                                                                                                                            |
| --: | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Envoy Proxy is a cloud-native L7 load balancer with 350k lines of C++ code, roughly 1,000 contributors, and 400 extensions.                                           |
|   2 | Governance uses a tiered structure: domain experts, maintainers, and senior maintainers, with explicit responsibilities and voting rights.                            |
|   3 | Code reviews follow a one-day SLA, achieved by limiting review scope to specific domains via a strict code owners file.                                               |
|   4 | New extensions require cross-company approval to prevent single-vendor capture of subsystems.                                                                         |
|   5 | Extension PRs cannot modify core code; core changes require separate PRs reviewed by senior maintainers.                                                              |
|   6 | Stale PRs are automatically closed after seven days of inactivity to keep the queue clean.                                                                            |
|   7 | Nearly 100% test coverage is strictly enforced for new code, with no exceptions.                                                                                      |
|   8 | A weekly on-call rotation handles triage, unblocks stalled PRs, and monitors CI flakiness, acting as project management rather than firefighting.                     |
|   9 | Community meetings occur bi-weekly only if there is a concrete agenda; otherwise, they are canceled.                                                                  |
|  10 | Extension sponsorship is a four-step process: issue discussion, maintainer sponsorship, named reviewers, and collective maintenance.                                  |
|  11 | Abandoned extensions are removed after a six-month deprecation window following a maintainer vote.                                                                    |
|  12 | Contrib extensions require an end user sponsor running at scale and are excluded from the main build and security team coverage.                                      |
|  13 | Risky changes are hidden behind runtime flags (reloadable features) to allow safe rollback without restarting the process.                                            |
|  14 | Deprecation follows a three-phase cycle over three to six months: warning logs, hard fail with override, and final code removal.                                      |
|  15 | Testing includes unit, integration, config example validation, compile-time checks, memory/performance tracking, and fuzzing.                                         |
|  16 | Fuzzing uses 50 targets running 24/7 via OSS-Fuzz to catch bugs in parsers, codecs, and routing logic.                                                                |
|  17 | Sanitizers (Address, Memory, Thread) are run in CI to catch buffer overflows, uninitialized memory, and data races.                                                   |
|  18 | Bots automate chores such as deprecation cleanup tracking, stale PR closing, and dependency update PRs.                                                               |
|  19 | Named shepherds are assigned for API compatibility, dependency management, and security triage to ensure accountability.                                              |
|  20 | External dependencies are evaluated against scorecards for maintenance, license, security, binary size, and test coverage.                                            |
|  21 | Dependency health is monitored continuously, and patches are treated as liabilities to be upstreamed whenever possible.                                               |
|  22 | Recommended practices for other projects include validating doc configs in CI, automating stale PRs, documenting review policies, and implementing on-call rotations. |
|  23 | Introducing sanitizers, three-phase deprecations, and fuzzing can significantly improve project quality and security posture.                                         |
|  24 | CI performance is actively managed to keep PR feedback times around 40 minutes by optimizing parallelism and test targets.                                            |
|  25 | Geographical diversity is managed through asynchronous communication and flexible meeting times to accommodate different time zones.                                  |

# Video

[![Video thumbnail](https://img.youtube.com/vi/hwTaU-lHm-0/hqdefault.jpg)](https://www.youtube.com/watch?v=hwTaU-lHm-0)

[Watch on YouTube](https://www.youtube.com/watch?v=hwTaU-lHm-0)
