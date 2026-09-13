---
layout: default
title:
  "Tutorial: Hacking up a Storm With Kubernetes - Rory McCune, Datadog; Marion
  McCune & Iain Smart"
nav_order: 351
parent: Kubecon Cloudnativecon Europe 2025
type: Video Note
description:
  The tutorial demonstrated how to bypass Kubernetes security controls
  by exploiting vulnerabilities in the system. The presenter used a service account
  token to gain elevated privileges and create a new role with "star" rights, which
  allowed...
resource: https://www.youtube.com/watch?v=8Q8sFzODEUo
tags:
  - kubecon-cloudnativecon-europe-2025
  - video
  - learning
status: stable
generated:
  by: process:yt-conferences-okf
  at: 2026-09-12 00:00:00+00:00
---

# Summary

The tutorial demonstrated how to bypass Kubernetes security controls by exploiting vulnerabilities in the system.
The presenter used a service account token to gain elevated privileges and create a new role with "star" rights, which allowed them to access any resource in the cluster.
They also exploited an unpatchable CVE to hijack traffic between namespaces, demonstrating the importance of network policies and admission control.
The presenter emphasized the need for careful permission management, minimal access, and segregation of resources to prevent similar vulnerabilities.

# Main Points

|   # | Main point                                                                                                                      |
| --: | ------------------------------------------------------------------------------------------------------------------------------- |
|   1 | The speaker has 9 years of experience in container security and is part of the Kubernetes SIG security team.                    |
|   2 | The tutorial will follow an attack path in Kubernetes to show how someone might be able to escalate privileges.                 |
|   3 | The speaker recommends using Kind to spin up a test cluster for the tutorial.                                                   |
|   4 | The tutorial will cover authentication, authorization, and admission control in Kubernetes.                                     |
|   5 | The speaker will demonstrate how to bypass pod security admission controls using service accounts and JWT tokens.               |
|   6 | The tutorial will also cover exploiting unpatchable Kubernetes CVEs.                                                            |
|   7 | The speaker recommends being careful with permissions, minimizing access, and segregating resources to prevent security issues. |
|   8 | The tutorial is available on the speaker's blog and on the Kubernetes Slack channel.                                            |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=8Q8sFzODEUo)
