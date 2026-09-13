---
layout: default
title:
  "Advancing Kubernetes AI Conformance: Current State and Road... Yuan Tang,
  Mario Fahlandt & Janet Kuo"
nav_order: 17
parent: Kubecon Cloudnativecon Europe 2026
type: Video Note
description:
  The Kubernetes AI Conformance program, led by representatives from Google,
  Red Hat, and Curomedic, aims to establish standardized requirements and APIs for
  running AI and ML workloads on Kubernetes platforms. Recognizing that traditional
  Ku...
resource: https://www.youtube.com/watch?v=EdgyyJpauKU
tags:
  - kubecon-cloudnativecon-europe-2026
  - video
  - learning
status: stable
generated:
  by: process:yt-conferences-okf
  at: 2026-09-12 00:00:00+00:00
---

# Summary

The Kubernetes AI Conformance program, led by representatives from Google, Red Hat, and Curomedic, aims to establish standardized requirements and APIs for running AI and ML workloads on Kubernetes platforms.
Recognizing that traditional Kubernetes conformance does not fully address the unique needs of AI workloads—such as specialized hardware, GPU support, and advanced networking—the group developed additional requirements, categorized as "should" (recommended) and "must" (mandatory), which platforms must meet on top of existing Kubernetes conformance.
The program, now a permanent subproject under SIG Architecture, maintains its requirements and automated tests in a public GitHub repository and has introduced a structured process for managing and evolving these standards.
Since its launch at KubeCon North America, the initiative has seen broad community involvement, with regular meetings and open calls for input, especially from end users, to ensure the standards address diverse real-world scenarios.
The overarching goal is to enable interoperability and portability of AI workloads across different Kubernetes vendors and environments, fostering industry-wide collaboration and preventing vendor lock-in.

# Main Points

|   # | Main point                                                                                                                                        |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Introduction of Kubernetes AI Conformance leads: Janet Quo (Google), Yan Tang (Red Hat), Mario Farland (Curomedic), Rita Sang (Microsoft, absent) |
|   2 | AI workloads introduce new requirements and challenges for Kubernetes, such as GPU usage, specialized hardware, networking, and security          |
|   3 | Existing Kubernetes conformance is insufficient for AI workloads; need for faster iteration and additional standards                              |
|   4 | Kubernetes AI Conformance Working Group started in 2025, sponsored by SIG Architecture                                                            |
|   5 | Requirements are categorized as "should" (recommended) and "must" (mandatory)                                                                     |
|   6 | Kubernetes AI conformance adds requirements on top of existing Kubernetes conformance; platforms must be Kubernetes conformant first              |
|   7 | The program defines standardized capabilities and APIs for running AI/ML workloads, aiming for interoperability and portability                   |
|   8 | Transitioned from a working group to a SIG Architecture official subproject for long-term maintenance                                             |
|   9 | All design, requirements, discussions, code, and automated tests are available in the GitHub repo                                                 |
|  10 | Program launched at KubeCon North America; initial adopters and contributors recognized                                                           |
|  11 | Certified platforms are listed in the CNCF landscape; checklist available for Kubernetes versions 1.33 to 1.35                                    |
|  12 | Requirement tracking moved from Google Docs to a structured GitHub project board                                                                  |
|  13 | Introduced a Kubernetes AI Conformance Requirement (K) process, similar to Kubernetes Enhancement Proposal process                                |
|  14 | Upcoming releases (1.36, 1.37) will introduce new requirements, especially around inferencing and agents                                          |
|  15 | Automated test framework in Go supports specifying different accelerator types for certification                                                  |
|  16 | Plan to add more conformance tests for specific areas, e.g., DRA drivers                                                                          |
|  17 | Conformance program ensures consistent experience across vendors and platforms, preventing vendor lock-in                                         |
|  18 | Community-driven process with input from vendors, end users, and organizations like Nvidia                                                        |
|  19 | Meetings are bi-weekly, with communication via mailing list and Slack                                                                             |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=EdgyyJpauKU)
