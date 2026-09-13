---
layout: default
title:
  "The Cloud Is Lying To You: What It Really Takes To Run On-Prem - Paris Nakita
  Kejser, Terma A/S"
nav_order: 304
parent: Kubecon Cloudnativecon North America 2025
type: Video Note
description:
  Paris, an advanced platforms engineer at Turma, discusses his experience
  managing a large on-premises Kubernetes cluster and explores the reasons organizations
  may choose on-prem over cloud, such as compliance, control, and predictable cost...
resource: https://www.youtube.com/watch?v=K5Wh7dfbr4s
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

Paris, an advanced platforms engineer at Turma, discusses his experience managing a large on-premises Kubernetes cluster and explores the reasons organizations may choose on-prem over cloud, such as compliance, control, and predictable costs.
He highlights the trade-offs between cloud and on-premises solutions, noting that while the cloud offers convenience and managed services, it can lead to vendor lock-in, hidden complexity, and less control over data and security.
Paris emphasizes that running Kubernetes on-prem requires a shift in mindset, careful planning of hardware, networking, storage, and security, and the adoption of automation tools like Ansible and GitOps for effective management.
He recommends technologies such as Cilium for networking, Istio for service mesh, and Ceph for storage to build resilient, secure, and vendor-independent clusters, while stressing the importance of robust backup strategies and observability.
In the Q&A, Paris addresses challenges like DDoS protection, storage replication, automation from bare metal to Kubernetes, and the complexities of scaling and networking, ultimately advocating for ownership, transparency, and thoughtful design in on-premises infrastructure.

# Main Points

|   # | Main point                                                                                                                                                                    |
| --: | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Paris is an advanced platforms engineer at Turma, a Danish high-tech company specializing in mission-critical systems for defense, aerospace, security, and civilian sectors. |
|   2 | Manages a home Kubernetes cluster with over 100 cores, 200 GB memory, 200+ pods, and a Ceph cluster.                                                                          |
|   3 | Companies may move from cloud to on-prem for compliance, control, cost, and data regulations.                                                                                 |
|   4 | On-prem provides full ownership of hardware, network, storage, and keys, enabling easier compliance and predictable spending.                                                 |
|   5 | Hybrid solutions allow cloud bursting while keeping sensitive workloads on-prem.                                                                                              |
|   6 | Cloud offers convenience but hides complexity and can lead to vendor lock-in.                                                                                                 |
|   7 | On-prem requires managing all aspects: networking, storage, security, patching, scaling, and monitoring.                                                                      |
|   8 | Cloud outages can cause total loss of access; businesses must plan for provider dependency and disaster recovery.                                                             |
|   9 | True resilience means platform independence and having tested backup and recovery plans.                                                                                      |
|  10 | Running Kubernetes on-prem is a mindset shift; key areas: hardware, networking, storage, security, and automation.                                                            |
|  11 | Kubernetes prefers many small, stable nodes; dynamic networking (CNI, flexible routing) is essential.                                                                         |
|  12 | Persistent storage (volumes, CSI drivers, backups) is critical for stateful workloads.                                                                                        |
|  13 | On-prem security is fully owned: access control, image scanning, network policies, and secrets management.                                                                    |
|  14 | Automation and GitOps are vital for patching, scaling, and recovery.                                                                                                          |
|  15 | Infrastructure design choices: bare metal for control/performance, virtualization for flexibility, or hybrid.                                                                 |
|  16 | Networking and security must be designed intentionally; tools like Cilium (ebpf, Hubble, MTLS, cluster mesh) and Istio (traffic management, MTLS, observability) recommended. |
|  17 | Ceph is recommended for flexible, high-availability, vendor-independent storage (block, file, object).                                                                        |
|  18 | Backups must follow the 3-2-1 rule, be automated, encrypted, tested, and stored offsite.                                                                                      |
|  19 | Essential base services: secrets management                                                                                                                                   |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=K5Wh7dfbr4s)
