---
layout: default
title: "Growing Your Design Proposal Process To Meet Your Needs - Fabian Deutsch & Dipesh Rawat"
nav_order: 6
parent: "Maintainer Summit 2025 - Europe"
type: Video Note
description: "This presentation by IBM software developer and Kubernetes enhancement team lead, along with Kubermatic maintainer Fabian, details how to tailor design proposal processes to project needs by compar..."
resource: "https://www.youtube.com/watch?v=qTCjmsYMM1A"
tags:
  - maintainer-summit-2025-europe
  - video
  - learning
status: stable
generated:
  by: process:yt-summarizer-okf
  at: 2026-11-15T22:30:54+00:00
---

# Summary

This presentation by IBM software developer and Kubernetes enhancement team lead, along with Kubermatic maintainer Fabian, details how to tailor design proposal processes to project needs by comparing the mature Kubernetes KEP process with the evolving Kubermatic enhancement workflow.
The speakers explain that Kubernetes adopted a formal KEP process, inspired by Python PEPs, to manage its massive scale by requiring comprehensive documentation, metadata files, and production readiness reviews to ensure transparency and build confidence in changes.
In contrast, Kubermatic, a smaller CNCF project, initially relied on informal PRs but evolved into a structured process using a dedicated repository and GitHub issues to track feature maturity, assign ownership, and route proposals to specific Special Interest Groups (SIGs) to reduce reliance on personal relationships.
Both projects emphasize that while formal processes improve traceability and inclusivity, they introduce maintenance overhead, requiring a balance between rigorous documentation and lean workflows to avoid slowing down development velocity.
The speakers advise new projects to start with simple, low-friction processes to attract contributors and gradually scale complexity, noting that Kubermatic follows a time-based release schedule trailing Kubernetes by two months, with exceptions handled on a case-by-case basis to maintain stability.

# Main Points

|   # | Main point                                                                                                                                                    |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Kubernetes celebrated its 10th anniversary in 2024, marking its first commit in June 2014 with 250 lines of code.                                             |
|   2 | As the first CNCF graduated project in 2018, Kubernetes has over 95,000 contributors and 1.5 million contributions.                                           |
|   3 | Early feature discussions occurred on Slack, mailing lists, and GitHub issues, which became difficult to track as the project scaled.                         |
|   4 | The Kubernetes Enhancement Proposal (KEP) process was inspired by Python PEPs and R requests for comments to ensure transferable skills.                      |
|   5 | A KEP is a version-controlled document in Git that tracks motivation, testing impact, and feature maturity across releases.                                   |
|   6 | The core goal of the KEP process is to build confidence around changes rather than simply merging code.                                                       |
|   7 | Changes qualifying as KEPs include user-visible changes, major refactors, cross-SIG collaborations, and API or architectural shifts.                          |
|   8 | The KEP process consists of three artifacts: the KEP template, a metadata YAML file, and a Production Readiness Review (PRR).                                 |
|   9 | The metadata file uses a DACI model to define drivers, approvers, contributors, and informed parties for transparency.                                        |
|  10 | The PRR is a questionnaire reviewed by an independent team to ensure proposed features do not break production environments.                                  |
|  11 | Kubernetes releases twice a year over 15 to 16 weeks, with feature opt-in occurring in the first four weeks.                                                  |
|  12 | Automation via Prow moves opted-in KEPs to a tracking board where the enhancement team verifies metadata and template compliance.                             |
|  13 | Two key checkpoints are enforced: an enhancement freeze to lock scope and a code/test freeze for approved implementation PRs.                                 |
|  14 | KEPs missing deadlines are removed from the release, though exceptions can be requested for additional time.                                                  |
|  15 | Benefits of the KEP process include improved transparency, traceability, aligned cross-SIG collaboration, and easier onboarding for new contributors.         |
|  16 | Challenges include high documentation overhead, outdated KEPs, and potential slowdowns in project velocity due to unclear scopes.                             |
|  17 | Lessons learned suggest that not every change requires a KEP, and processes should start small and evolve iteratively.                                        |
|  18 | Clear metadata files are essential for external tooling integration and project health monitoring.                                                            |
|  19 | Kubewarden is a CNCF project for managing virtual machines alongside container workloads, aiming for graduation in 2025.                                      |
|  20 | Early Kubewarden development relied on simple PRs with minimal documentation, which was effective for a small contributor base.                               |
|  21 | As the project approached 1.0, large PRs without prior alignment caused challenges, prompting the need for a formal process.                                  |
|  22 | Kubewarden initially used a community repository with a slimmed-down design template inspired by Kubernetes but lacked defined ownership and status tracking. |
|  23 | Problems included lack of transparency, missing team ownership, untracked feature states, and misalignment between compute, storage, and network teams.       |
|  24 | The process was difficult for new contributors to navigate and relied heavily on personal relationships for feature progression.                              |
|  25 | Kubewarden adopted a dedicated enhancements repository and requires a GitHub issue with a template before submitting a feature PR.                            |
|  26 | The issue template defines the purpose, primary contact, maturity level, and the Kubewarden-side maintainer responsible for the feature.                      |
|  27 | Special Interest Groups (SIGs) were introduced to decentralize decision-making and reduce reliance on personal relationships.                                 |
|  28 | Kubewarden follows a time-based release schedule trailing Kubernetes by two months to allow for stabilization and integration testing.                        |
|  29 | Exceptions to the release schedule are handled case-by-case, allowing for minor delays if a critical feature is nearly complete.                              |
|  30 | For new projects, it is recommended to start with a lean process using GitHub issues to attract contributors before scaling up complexity.                    |
|  31 | Balancing process rigor with contributor accessibility is crucial to avoid scaring off new participants in early-stage projects.                              |

# Video

[![Video thumbnail](https://img.youtube.com/vi/qTCjmsYMM1A/hqdefault.jpg)](https://www.youtube.com/watch?v=qTCjmsYMM1A)

[Watch on YouTube](https://www.youtube.com/watch?v=qTCjmsYMM1A)
