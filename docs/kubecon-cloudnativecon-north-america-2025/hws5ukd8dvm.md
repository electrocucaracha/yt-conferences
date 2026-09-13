---
layout: default
title:
  "No Joke: Two Security Maintainers Walk Into a Cluster - Jackie Maertens &
  Nilekh Chaudhari"
nav_order: 177
parent: Kubecon Cloudnativecon North America 2025
type: Video Note
description:
  In this talk, Jackie Martins and Nilik, both senior software engineers
  at Microsoft and security maintainers, guide the audience through essential Kubernetes
  cluster security practices. They emphasize the principle of least privilege, start...
resource: https://www.youtube.com/watch?v=HwS5UKD8dVM
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

In this talk, Jackie Martins and Nilik, both senior software engineers at Microsoft and security maintainers, guide the audience through essential Kubernetes cluster security practices.
They emphasize the principle of least privilege, starting with proper configuration of RBAC (Role-Based Access Control) to avoid overly broad permissions and common pitfalls like using cluster-admin roles or forgetting to remove test permissions.
The speakers demonstrate the importance of encrypting secrets at rest—preferably using KMSv2—and highlight that Kubernetes secrets are not encrypted by default, urging the use of external secret management solutions like the Secret Store CSI driver to avoid storing sensitive data in etcd.
They also cover the necessity of network policies to restrict pod communication, recommending a default deny-all approach and careful management of ingress and egress rules.
Pod security standards are discussed, with advice to enforce restrictive profiles and avoid running pods as root, and the importance of using vulnerability scanning tools and up-to-date images is underscored to prevent exploitation of known flaws.
Throughout, they provide demos, share common misconfigurations, and encourage integrating security checks throughout the development lifecycle, referencing additional resources and their GitHub for further guidance.

# Main Points

|   # | Main point                                                                                                                                                                                                            |
| --: | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Presenters: Jackie Martins and Nilik, senior software engineers at Microsoft, Azure Kubernetes team, ISTIO security maintainers.                                                                                      |
|   2 | Security goals: protect data at rest, enforce least privilege, minimize open doors, remove unnecessary permissions, ensure cluster resilience.                                                                        |
|   3 | Key Kubernetes security components/tools discussed: RBAC, encryption at rest, secrets management, network policies, pod security standards, image vulnerability scanning.                                             |
|   4 | RBAC (Role-Based Access Control):                                                                                                                                                                                     |
|   5 | Controls who can access what in the cluster.                                                                                                                                                                          |
|   6 | Four components: roles, role bindings, cluster roles, cluster role bindings.                                                                                                                                          |
|   7 | Common pitfalls: granting cluster-admin to everything, using wildcard permissions, forgetting to remove test permissions, using cluster role bindings instead of role bindings, unnecessary service account mounting. |
|   8 | Use validating admission policies to enforce RBAC best practices.                                                                                                                                                     |
|   9 | Encryption at Rest:                                                                                                                                                                                                   |
|  10 | By default, Kubernetes secrets are only base64 encoded, not encrypted.                                                                                                                                                |
|  11 | Use KMSv2 for encrypting etcd data.                                                                                                                                                                                   |
|  12 | Common pitfalls: not re-encrypting old secrets, losing encryption keys, using local keys in production, not testing encryption.                                                                                       |
|  13 | Secrets Management:                                                                                                                                                                                                   |
|  14 | Avoid storing application secrets in Kubernetes secrets; use external secret stores (e.g., Vault, AWS Secrets Manager, Azure Key Vault) via Secret Store CSI driver.                                                  |
|  15 | Supports secret rotation and logging.                                                                                                                                                                                 |
|  16 | Common pitfalls: mixing Kubernetes and external secrets, exposing secrets via environment variables, not enabling secret rotation.                                                                                    |
|  17 | Network Policies:                                                                                                                                                                                                     |
|  18 | Control pod-to-pod and pod-to-external communication.                                                                                                                                                                 |
|  19 | Default is allow-all; recommend default deny-all and add specific policies.                                                                                                                                           |
|  20 | Common pitfalls: forgetting egress rules, misconfiguring additive policies, hardcoding IPs, not testing policies.                                                                                                     |
|  21 | Pod Security Standards:                                                                                                                                                                                               |
|  22 | Three levels: privileged, baseline, restricted.                                                                                                                                                                       |
|  23 | Restrict namespace sharing, privilege escalation, Linux capabilities, volume types, hostport access, pr                                                                                                               |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=HwS5UKD8dVM)
