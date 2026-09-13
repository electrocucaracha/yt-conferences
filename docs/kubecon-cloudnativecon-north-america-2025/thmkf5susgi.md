---
layout: default
title:
  "Project Lightning Talk: Multi-Cluster Configuration Management With KubeStellar
  - Andy Anderson"
nav_order: 232
parent: Kubecon Cloudnativecon North America 2025
type: Video Note
description:
  Andy Anderson, a software architect at IBM Research, introduces Coupe
  Stellar, a multicluster configuration management tool within the CNCF ecosystem.
  Coupe Stellar enables users to manage an inventory of remote clusters, stage workloads
  in...
resource: https://www.youtube.com/watch?v=tHMKF5sUSgI
tags:
  - kubecon-cloudnativecon-north-america-2025
  - video
  - learning
status: stable
generated:
  by: process:yt-conferences-okf
  at: 2026-09-12 00:00:00+00:00
---

# Summary

Andy Anderson, a software architect at IBM Research, introduces Coupe Stellar, a multicluster configuration management tool within the CNCF ecosystem.
Coupe Stellar enables users to manage an inventory of remote clusters, stage workloads in centralized namespaces, and distribute them to execution clusters via binding policies, overcoming Kubernetes limitations such as cluster timeouts.
Recent developments include extensive localization, a new site with a sandbox environment, a plugin framework for custom UI extensions, automated multi-browser UI testing, and a multiplugin for the command line to streamline cluster management.
The ADA project integrates AI-driven automation for provisioning and workload assignment, and the team emphasizes community involvement through a contributor ladder, mentorship program, and collaborations like the software-defined farm project with Cornell University.
Anderson invites attendees to upcoming sessions and encourages participation in the Coupe Stellar community.

# Main Points

|   # | Main point                                                                                                                                          |
| --: | --------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Coupe Stellar is a multicluster configuration management tool.                                                                                      |
|   2 | Part of CNCF; presented by Andy Anderson, IBM Research.                                                                                             |
|   3 | Manages an inventory of remote clusters and workload namespaces.                                                                                    |
|   4 | Workloads are staged in namespaces where pods don't run, then assigned to clusters via binding policy.                                              |
|   5 | Uses SIG M multiclusters workload API for communication between inventory, transport, and definition spaces.                                        |
|   6 | Overcomes Kubernetes limitations, such as clusters being marked unschedulable after going offline.                                                  |
|   7 | Recently added localization in English, French, Italian, German, Spanish, Japanese, Hindi, traditional and simplified Chinese, and Portuguese.      |
|   8 | New site launching in December with enhanced sandbox for free trials.                                                                               |
|   9 | Plug-in framework allows creation and distribution of UI plugins.                                                                                   |
|  10 | Automated multi-browser UI testing implemented with Playwright.                                                                                     |
|  11 | Multi-plugin for kubectl enables working with multiple clusters from the command line (e.g., "kubectl get pods -A" shows pods across all clusters). |
|  12 | 8A project automates provisioning, pod, workload, and binding policies across clusters using AI tools like Gemini and OpenAI.                       |
|  13 | Seamless integration with Argo.                                                                                                                     |
|  14 | Focus on increasing product quality and adopter support.                                                                                            |
|  15 | Plug-in API supports building plugins with Wom and Node code for multicluster operations.                                                           |
|  16 | Output enhancements include extra columns for clusters in command-line results.                                                                     |
|  17 | Easy installation via brew formula.                                                                                                                 |
|  18 | 8A project enables prompt-based workload assignment to clusters using Python libraries.                                                             |
|  19 | Contributor ladder and mentor program established; 12 mentees graduated.                                                                            |
|  20 | Issues and help wanted available on Cloud Tributor; contributor resources on YouTube.                                                               |
|  21 | Joint studies agreement with Cornell University on software defined farm for edge computing in agriculture.                                         |
|  22 | Poster session and booth scheduled at upcoming events for further engagement.                                                                       |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=tHMKF5sUSgI)
