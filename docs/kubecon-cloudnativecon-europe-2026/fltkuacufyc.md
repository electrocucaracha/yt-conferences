---
layout: default
title:
  "Locking Down Ray Serve: How to Secure Ur ML Models? - Kateryna Hrytsaienko,
  Valtech"
nav_order: 213
parent: Kubecon Cloudnativecon Europe 2026
type: Video Note
description:
  Katina begins by sharing her personal experience with learning to secure
  Ray models and emphasizes the importance of robust security practices in MLOps environments.
  She introduces Ray as an open-source tool for distributed computing, highl...
resource: https://www.youtube.com/watch?v=FLTKUAcuFyc
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

Katina begins by sharing her personal experience with learning to secure Ray models and emphasizes the importance of robust security practices in MLOps environments.
She introduces Ray as an open-source tool for distributed computing, highlighting its integration with Kubernetes and the security risks inherent in its default flat, permissionless architecture.
The talk covers best practices for securing Ray clusters, including using namespaces, virtual clusters, and policy engines like Kyverno to enforce boundaries and resource limits.
Katina also discusses strategies for managing inbound and outbound traffic, such as leveraging private APIs, identity-aware proxies, and mutual TLS—preferably via service meshes like Istio or managed cloud solutions—while noting the limitations of Ray’s own token authentication.
She concludes by recommending continuous monitoring tools like Prowler to detect misconfigurations and encourages attendees to access her runbook and resources for further guidance.

# Main Points

|   # | Main point                                                                                                                                                                    |
| --: | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | The talk focuses on securing Ray models and clusters, sharing lessons learned from experience.                                                                                |
|   2 | Ray is an open-source tool for distributed computing, integrating with Kubernetes via KubeRay and custom resources.                                                           |
|   3 | Ray clusters consist of a head node and worker nodes; the head node can act as a worker, which is not recommended for security.                                               |
|   4 | By default, Ray clusters have no security mechanisms; all nodes have access to everything, making them vulnerable to abuse and remote code execution.                         |
|   5 | ML security concerns include not just data, but also resource abuse, leading to high cloud costs.                                                                             |
|   6 | MLOps apps face similar vulnerabilities as regular apps, plus ML-specific risks like input manipulation and privilege violations.                                             |
|   7 | Security should be layered: infrastructure hardening, identity management, mutual TLS, and compliance/governance.                                                             |
|   8 | Namespaces can limit Ray’s permissions, but managing multiple teams and upgrades is challenging.                                                                              |
|   9 | Virtual clusters (e.g., vcluster) allow teams to have isolated environments within a shared GKE cluster, supporting custom policies and resource control.                     |
|  10 | Policy engines like Kyverno can enforce security rules, such as preventing worker processes on the head node and limiting communication.                                      |
|  11 | LimitRange can be used to prevent resource abuse within clusters.                                                                                                             |
|  12 | For inbound traffic, prefer internal networking (private API, internal load balancer); for external access, use Identity Aware Proxy with proper firewall and authentication. |
|  13 | Inference Gateway and Cloud Armor can protect against malicious input and provide advanced routing and caching.                                                               |
|  14 | Outbound traffic should use cloud identity mapping (Google account to Kubernetes service account) for secure resource access.                                                 |
|  15 | Mutual TLS is recommended for worker-to-worker communication; options include service mesh (sidecar or ambient), but Ray’s own mTLS implementation is complex and not ideal.  |
|  16 | Ray tokens are not granular, not secure by default, and require additional proxies; not recommende                                                                            |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=FLTKUAcuFyc)
