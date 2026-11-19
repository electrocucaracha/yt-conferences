---
layout: default
title: "Guidelines for Achieving Project Release Maturity - Andrew Block, Carol Valencia & Nabarun Pal"
nav_order: 15
parent: "Maintainer Summit 2026 - Europe"
type: Video Note
description: "This presentation outlines guidelines for achieving project release maturity within the CNCF, focusing on a checklist for maintainers to ensure governance and security as projects transition from s..."
resource: "https://www.youtube.com/watch?v=sNSK6IExIFI"
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

This presentation outlines guidelines for achieving project release maturity within the CNCF, focusing on a checklist for maintainers to ensure governance and security as projects transition from sandbox to graduated status.
The speakers, representing Kubernetes and Helm, discuss seven key topics, including source code management, versioning, documentation, licensing, testing, security, and release distribution.
They highlight how Kubernetes manages its monorepo structure and complex CI pipelines via Prow, while Helm emphasizes strict semantic versioning, community documentation, and automated license compliance checks.
Both projects detail their security practices, such as vulnerability disclosure processes, artifact signing, and supply chain integrity measures, aiming to provide a robust baseline for other open-source initiatives.
The session concludes with an invitation for the community to contribute to the final white paper and checklist, ensuring the guidelines remain adaptable and inclusive of diverse project needs.

# Main Points

|   # | Main point                                                                                                                                                        |
| --: | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | The initiative aims to create a project release maturity checklist and white paper for CNCF projects to guide governance and security practices.                  |
|   2 | The presentation covers seven key topics: source code management, versioning, documentation, licensing, testing, security, and release management.                |
|   3 | Kubernetes manages its monorepo by staging external dependencies in separate repositories to prevent consumers from importing millions of lines of code directly. |
|   4 | Kubernetes utilizes a contribution ladder where contributors progress from non-members to reviewers, approvers, and eventually SIG chairs or tech leads.          |
|   5 | Kubernetes follows Semantic Versioning technically but deviates by allowing breaking changes in alpha and beta features within minor versions.                    |
|   6 | Kubernetes uses a single main branch for development and cherry-picks changes into release branches, requiring changes to land in main first.                     |
|   7 | Helm strictly enforces Semantic Versioning and backward compatibility, using major releases to remove dead code and implement breaking API changes.               |
|   8 | Kubernetes maintains two documentation pillars: end user documentation on kubernetes.io and contributor-focused documentation on kubernetes.dev.                  |
|   9 | Helm provides a comprehensive documentation site with user and contributor guides, translated into multiple languages to support a global community.              |
|  10 | CNCF projects follow Apache licensing, and Helm uses automation to validate license headers on all source code before commits are accepted.                       |
|  11 | Kubernetes scans its entire dependency graph to ensure all licenses conform to CNCF approved lists, removing non-compliant dependencies when found.               |
|  12 | Kubernetes uses Prow, a complex CI system, to manage merge queues and test code, with components that are pluggable for other projects to adopt.                  |
|  13 | Helm integrates external tools like Go lint, CodeQL, and Go vault check into its CI pipeline to detect vulnerabilities and ensure code quality.                   |
|  14 | Kubernetes operates a private and public vulnerability disclosure process, including a HackerOne bounty program and a public CVE feed.                            |
|  15 | Helm maintains a documented security policy with a dedicated security team, GPG-signed artifacts, and OSSF scorecard generation.                                  |
|  16 | Kubernetes uses the krel tool to automate release processes, including building binaries, generating packages, and signing artifacts.                             |
|  17 | Kubernetes replicates container images across various cloud providers to reduce egress fees for users creating clusters in specific regions.                      |
|  18 | Helm has a well-established release process that publishes to GitHub, Homebrew, and other package managers with human-written release notes.                      |
|  19 | The initiative invites CNCF project maintainers to contribute case studies and feedback to the white paper via the TAC Operational Resilience channel.            |
|  20 | Future plans include integrating the checklist with AI agents and GitHub workflows to automate compliance checks for project graduation.                          |
|  21 | The TAC Security and Compliance group will review the security aspects of the checklist to ensure robust vulnerability management standards.                      |

# Video

[![Video thumbnail](https://img.youtube.com/vi/sNSK6IExIFI/hqdefault.jpg)](https://www.youtube.com/watch?v=sNSK6IExIFI)

[Watch on YouTube](https://www.youtube.com/watch?v=sNSK6IExIFI)
