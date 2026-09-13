---
type: Video Note
title: "The KEP Lifecycle: How the Release Team Guides Enhanceme... Kat C, Sreeram V, Rayan D & Subhasmita S"
description: "The video features a panel of Kubernetes release team members who explain the Kubernetes Enhancement Proposal (KEP) process and how the release team ensures enhancements contribute to project stability. They introduce themselves and outline..."
resource: https://www.youtube.com/watch?v=4if9UBP-NKQ
tags: ["kubecon-cloudnativecon-europe-2026", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

The video features a panel of Kubernetes release team members who explain the Kubernetes Enhancement Proposal (KEP) process and how the release team ensures enhancements contribute to project stability.
They introduce themselves and outline the role of KEPs, which are design documents used to propose new features or deprecations, and describe how these are tracked in the k/enhancements GitHub repository.
The panel details the step-by-step lifecycle of a KEP from both contributor and release team perspectives, including SIG sponsorship, PR requirements, production readiness reviews, and the structured 15-week release cycle with key milestones like PR freeze, enhancement freeze, and code freeze.
They discuss recent process improvements, such as moving from Google Sheets to automated GitHub tracking and instituting hard deadlines for PR submissions to improve efficiency and reduce confusion.
The session concludes with encouragement for new contributors to join the release team, an overview of the tracking board’s automation, and a Q&A addressing process automation and documentation.
# Main Points

|   # | Main point                                                                                                                                                                                                                     |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   1 | Introduction of speakers: Ryan Das (Digital Ocean, SIG Release), Cat Cosgrove (Minimus, Kubernetes Steering Committee), Freda Madesh (Digital Ocean, Release Branch Management Lead), Subashmita (Enhancement Subteam Shadow). |
|   2 | The talk covers the Kubernetes Enhancement Proposal (KEP) lifecycle and the release team's role in guiding enhancements to stability.                                                                                          |
|   3 | KEPs (Kubernetes Enhancement Proposals) are design documents for new features and deprecations in Kubernetes, stored in the k/enhancements GitHub repo.                                                                        |
|   4 | KEPs were introduced in 2017, inspired by Rust RFCs and Python PEPs.                                                                                                                                                           |
|   5 | Kubernetes SIGs (Special Interest Groups) are dedicated teams for different components; SIG Release manages the release process.                                                                                               |
|   6 | The enhancements subproject of SIG Architecture manages KEPs, with biweekly meetings.                                                                                                                                          |
|   7 | To propose a KEP, contributors fill out a template, get SIG lead review, and submit to the k/enhancements repo.                                                                                                                |
|   8 | Each KEP must be sponsored and approved by a SIG.                                                                                                                                                                              |
|   9 | The release team tracks KEPs through the release cycle, requiring an "opted-in" label from SIG maintainers.                                                                                                                    |
|  10 | KEPs must include a kep.yaml file and a README, and pass a Production Readiness Review (PRR) questionnaire.                                                                                                                    |
|  11 | The release process includes several freezes: PRR freeze, enhancements freeze, code freeze, and docs/test freeze.                                                                                                              |
|  12 | The release cycle is 15 weeks, with three releases per year.                                                                                                                                                                   |
|  13 | The release team assembles, tracks, and manages KEPs through milestones and deadlines.                                                                                                                                         |
|  14 | Hard deadlines (e.g., PRR freeze) are now enforced to improve efficiency and reduce confusion.                                                                                                                                 |
|  15 | Exception requests can be filed in advance if deadlines cannot be met.                                                                                                                                                         |
|  16 | The enhancements tracking process moved from Google Sheets to GitHub for better automation and efficiency.                                                                                                                     |
|  17 | The release team has a shadow program open to contributors, with structured onboarding and documentation.                                                                                                                      |
|  18 | The enhancements tracking board is label-driven and used by multiple subteams for release management.                                                                                                                          |
|  19 | KEPs are essential for tracking all updates, dep                                                                                                                                                                               |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=4if9UBP-NKQ)