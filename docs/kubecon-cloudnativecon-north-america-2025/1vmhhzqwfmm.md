---
layout: default
title:
  "Kubernetes Infra SIG: Intro and Updates - Mahamed Ali, Arab Center for Research
  & Policy Studies"
nav_order: 140
parent: Kubecon Cloudnativecon North America 2025
type: Video Note
description:
  Muhammad, a senior DevOps engineer and Kubernetes maintainer, provides
  an update on the SIG Kubernetes infrastructure, which manages the Kubernetes project's
  cloud infrastructure with support from major vendors. He highlights key services
  s...
resource: https://www.youtube.com/watch?v=1VMhhZQWFmM
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

Muhammad, a senior DevOps engineer and Kubernetes maintainer, provides an update on the SIG Kubernetes infrastructure, which manages the Kubernetes project's cloud infrastructure with support from major vendors.
He highlights key services such as the image registry, CI, and download service, sharing usage statistics and recent leadership changes.
This year, IBM and Datadog joined as new vendors, with IBM providing build clusters for additional architectures and Datadog offering cloud cost observability and testing tools.
The team has improved CI performance by upgrading to newer VM types and continues to seek contributors, especially those interested in cloud infrastructure and SRE roles.
Muhammad encourages interested individuals to join the SIG's Slack channel or meetings to get involved.

# Main Points

|   # | Main point                                                                                                                                                        |
| --: | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Muhammad is a senior DevOps engineer at DR Center for Research and Policy Studies, Kubernetes maintainer, Sikkate infra lead, Kative maintainer, CNCF ambassador. |
|   2 | Sikkate infra manages Kubernetes project's cloud infrastructure, funded by multiple vendors.                                                                      |
|   3 | Three key services: image registry, CI, and download service.                                                                                                     |
|   4 | Leadership changes: Benjamin Elder and Dims stepped down; new chairs are Dylan Paige and Crian Hackman.                                                           |
|   5 | dl.k.io hosts Kubernetes binaries; serves about 3.5 PB/month, 120 requests/sec, 11.5 GB/sec traffic, 95% cache hit ratio.                                         |
|   6 | registry.io hosts all Kubernetes project images; served from 22 Google Cloud regions and 11 AWS regions; about 500 requests/sec; 2.22 PB served from S3.          |
|   7 | Current cloud vendors: Google, Amazon, Fastly, Microsoft Azure, and this lotion.                                                                                  |
|   8 | New vendors: IBM and Datadog.                                                                                                                                     |
|   9 | IBM provided Kubernetes build clusters for S390X and PPC64 architectures; now running tests on four main architectures: S390X, PPC64, AMD64, ARM64.               |
|  10 | Build clusters: 10 nodes each, running core Kubernetes and etcd tests, catching bugs previously unseen.                                                           |
|  11 | Thanks to Mju, Praio, Raja, and Sail from IBM.                                                                                                                    |
|  12 | Datadog partnership provides cloud cost observability, security tooling, and synthetic testing.                                                                   |
|  13 | Public dashboard shows cloud spend across Azure, AWS, and Google Cloud; Azure integration pending.                                                                |
|  14 | CI clusters: ~20 TB memory, ~3,000 cores, latest hardware.                                                                                                        |
|  15 | Synthetic testing: image pulls from 29 regions every 30 seconds; registry performance tested.                                                                     |
|  16 | No SLA for registry service; only OCI compliance guaranteed.                                                                                                      |
|  17 | CI speed improvements: migrating from N1 VMs to latest VMs, reducing job time from 1 hour to 45 minutes.                                                          |
|  18 | Plan to upgrade EKS clusters to newer generations next year.                                                                                                      |
|  19 | Seeking more maintainers and contributors, especially SREs.                                                                                                       |
|  20 | SIG meets biweekly; contact via Kubernetes Slack in the Sikkate infra channel.                                                                                    |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=1VMhhZQWFmM)
