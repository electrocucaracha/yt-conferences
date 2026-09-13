---
layout: default
title:
  "From “It Works!” to “It’s Secure!”: Hardening Your First Kub... Paul Zerdilas-Herrera
  & Leon Schulze"
nav_order: 127
parent: Kubecon Cloudnativecon Europe 2026
type: Video Note
description:
  In this presentation at CubeCon, Paul from Nutanix and Leon from Palo
  Alto Networks share a cautionary tale about Kubernetes security through the story
  of Dave, a junior developer who unknowingly exposes his application and cluster
  to the i...
resource: https://www.youtube.com/watch?v=oW946hLuKNc
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

In this presentation at CubeCon, Paul from Nutanix and Leon from Palo Alto Networks share a cautionary tale about Kubernetes security through the story of Dave, a junior developer who unknowingly exposes his application and cluster to the internet, leading to a security breach.
They explain how attackers commonly scan for open ports and vulnerable services, and how default Kubernetes configurations—such as overly permissive service account tokens and lack of network isolation—can make clusters easy targets.
The speakers emphasize that security is a layered process, not a binary state, and recommend practical steps like limiting attack surfaces, enforcing role-based access control, running containers as non-root, and using open-source tools to automate security checks.
They stress that default settings are often insecure due to the complexity and learning curve of Kubernetes, and urge developers to proactively secure their environments from the outset.
The session concludes with the reminder that learning from mistakes—both one’s own and others’—is crucial in the rapidly evolving cloud-native ecosystem.

# Main Points

|   # | Main point                                                                                                                                  |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Paul (Nutanix, Kubernetes platform) and Leon (Palo Alto Networks, security) present a session at CubeCon.                                   |
|   2 | The session is based on a real-life inspired story about Kubernetes security.                                                               |
|   3 | Dave, a junior developer at a fintech startup, is tasked with deploying an internal support tool on Kubernetes with a tight deadline.       |
|   4 | Dave, inexperienced with Kubernetes and security, follows online tutorials and deploys his first application.                               |
|   5 | Dave exposes his app via a load balancer, leaving the cluster open to the internet.                                                         |
|   6 | Over the weekend, attackers discover the open cluster, scan it, and exploit vulnerabilities.                                                |
|   7 | Attackers use tools like Shodan and NMAP to find and analyze exposed Kubernetes clusters.                                                   |
|   8 | 33% of intrusions start with exposed services as the initial attack vector.                                                                 |
|   9 | Attackers exploit command injection vulnerabilities in Dave’s app to gain access.                                                           |
|  10 | Attackers steal Kubernetes service account tokens, which act as digital passports for pods.                                                 |
|  11 | 70% of users leave service account tokens accessible by default.                                                                            |
|  12 | Attackers use stolen tokens to escalate privileges and deploy crypto miners disguised as system monitors.                                   |
|  13 | Kubernetes secrets are often only encoded, not encrypted, making them easy to access.                                                       |
|  14 | 89% of companies deploying clusters have experienced some form of attack or probing.                                                        |
|  15 | Security is a spectrum; layered defense is necessary (not just one wall).                                                                   |
|  16 | Key security steps: limit attack surface, restrict API access, use least privilege, implement role-based access control, contain workloads. |
|  17 | Disable anonymous authentication and automounting of service account tokens.                                                                |
|  18 | Use network isolation, private clusters, and IP allow lists.                                                                                |
|  19 | Run containers as non-root, use read-only file systems, disable privilege escalation, and drop unnecessary Linux capabilities.              |
|  20 | Use open source tools to scan for vulnerabilities, enforce secure YAMLs, monitor for anomalies, and benchmark compliance.                   |
|  21 | Real-world vulnerabilities (e.g., React to Shell) are exploited within                                                                      |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=oW946hLuKNc)
