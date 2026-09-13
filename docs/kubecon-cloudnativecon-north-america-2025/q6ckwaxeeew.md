---
layout: default
title:
  "Red Vs. Blue: A Live Attacker-Defender Showdown in Kubernetes Securi... Lucy
  Sweet & Sandeep Kanabar"
nav_order: 256
parent: Kubecon Cloudnativecon North America 2025
type: Video Note
description:
  In this live "Red Versus Blue" Kubernetes security demo, Lucy and Sandeep
  demonstrate common attack and defense scenarios within a Kubernetes cluster. Lucy,
  representing the defender, deploys a database application with default, permissive...
resource: https://www.youtube.com/watch?v=q6ckwAXeeew
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

In this live "Red Versus Blue" Kubernetes security demo, Lucy and Sandeep demonstrate common attack and defense scenarios within a Kubernetes cluster.
Lucy, representing the defender, deploys a database application with default, permissive configurations, while Sandeep, as the attacker, exploits vulnerabilities such as deploying a malicious image, escalating privileges, abusing service accounts, consuming excessive resources, and performing lateral movement across namespaces.
Throughout the session, Lucy responds by applying Kubernetes security features like pod security policies, tightening service account permissions, setting resource quotas and limit ranges, and enforcing network policies to restrict unauthorized access and resource abuse.
The demo highlights how misconfigurations and lack of restrictions can lead to cluster compromise, and emphasizes the importance of layered security controls.
The session concludes with a discussion on additional tools like admission webhooks and the importance of community initiatives supporting underrepresented groups in tech.

# Main Points

|   # | Main point                                                                                                        |
| --: | ----------------------------------------------------------------------------------------------------------------- |
|   1 | Live Kubernetes security demo: attacker (Sandeep) vs. defender (Lucy)                                             |
|   2 | Lucy: platform engineering at Uber, Kubernetes node lifecycle working group lead                                  |
|   3 | Sandeep: engineer often tasked with root cause analysis, member of deaf and hard of hearing working group         |
|   4 | Demo is live, tested once before; prepared files and commands for efficiency                                      |
|   5 | Local kind cluster used, 100% offline for safety                                                                  |
|   6 | Sandeep (attacker) uses a malicious image instead of TIDB, gains reverse shell access                             |
|   7 | Attacker escalates privileges, accesses kubeconfig, certificates, and host filesystem                             |
|   8 | Lucy identifies over-permissive pod privileges (privileged: true, allowPrivilegeEscalation: true)                 |
|   9 | Applies Kubernetes Pod Security Admission (PSA) to restrict privileged pods                                       |
|  10 | Sandeep exploits over-permissive service account, accesses secrets, creates malicious pods                        |
|  11 | Lucy tightens service account permissions, deletes backdoor pods                                                  |
|  12 | Sandeep starts resource abuse (CPU/memory hogging) due to lack of resource quotas/limits                          |
|  13 | Lucy applies resource quotas and limit ranges to restrict resource usage per namespace and pod                    |
|  14 | Sandeep attempts lateral movement: accesses internal services (admin dashboard) from compromised pod              |
|  15 | Lucy applies Kubernetes network policies to restrict cross-namespace communication                                |
|  16 | Discussion on importance of resource quotas, even for honest users, to prevent accidental abuse and cost overruns |
|  17 | Final attack: lateral movement blocked by network policies                                                        |
|  18 | Merge Forward initiative highlighted: support for underrepresented groups in tech                                 |
|  19 | Q&A:                                                                                                              |
|  20 | Red team enumeration: use KubeDNS, service account introspection, DNS brute-forcing                               |
|  21 | GitOps/continuous delivery can help enforce security but may not prevent fast attacks                             |
|  22 | Demo files/commands will be uploaded to GitHub                                                                    |
|  23 | Beyond PSA: admission webhooks and validating admission policies can prevent bad pods                             |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=q6ckwAXeeew)
