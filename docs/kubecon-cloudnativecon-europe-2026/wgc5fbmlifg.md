---
layout: default
title:
  "Lightning Talk: KRafting the Cloud: Building a Free, Open, and Accessible
  Cloud - Alex Bissessur"
nav_order: 208
parent: Kubecon Cloudnativecon Europe 2026
type: Video Note
description:
  Alex discusses the challenges of cloud infrastructure in Mauritius, where
  major providers like AWS and Azure have limited presence, leading to reliance on
  local cloud service providers that often lack modern features and automation. To
  addr...
resource: https://www.youtube.com/watch?v=wgc5fBmlIFg
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

Alex discusses the challenges of cloud infrastructure in Mauritius, where major providers like AWS and Azure have limited presence, leading to reliance on local cloud service providers that often lack modern features and automation.
To address this, Alex describes building a cloud platform called Craft, which leverages virtual clusters (vclusters) within Kubernetes to provide isolated, self-managed environments for users.
The system is composed of several microservices, including authentication, cluster management, and a frontend, and utilizes Rust for interacting with Kubernetes resources, offering convenience and security through namespace isolation, network policies, and pod security.
Craft has enabled social benefits in Mauritius by providing free, open-source hosting for community projects and educational workshops, making cloud-native technologies more accessible.
The project is available on GitHub and aims to empower others to deploy similar solutions in their own communities.

# Main Points

|   # | Main point                                                                                                                         |
| --: | ---------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Presenter: Alex from Mauritius                                                                                                     |
|   2 | Mauritius lacks major cloud service providers (CSPs) and has limited connectivity                                                  |
|   3 | Local CSPs are often overpriced, outdated, and not cloud-native                                                                    |
|   4 | Manual processes dominate; lack of managed services and automation                                                                 |
|   5 | Motivation: Need to build a cloud-native solution locally                                                                          |
|   6 | Key requirements for a cloud provider: user isolation, runs on remote hardware, self-managed provisioning                          |
|   7 | Introduced virtual clusters (vclusters) within Kubernetes clusters                                                                 |
|   8 | Implementations used: Vcluster and K3K                                                                                             |
|   9 | Virtual clusters run inside pods, expose their own API servers, and support storage/ingress class passthrough                      |
|  10 | Isolation achieved via namespaces, network policies, and pod security admission levels                                             |
|  11 | Project "Craft" architecture: microservices, authentication, cluster services, frontend, PostgreSQL                                |
|  12 | UI provides logs and cluster details                                                                                               |
|  13 | Used Rust (with QRS crate) for Kubernetes interaction; reimplemented K3K CRDs as Rust types for convenience                        |
|  14 | Simple Rust code enables listing and creating clusters                                                                             |
|  15 | Each cluster has its own CoreDNS instance                                                                                          |
|  16 | Project benefits: enables learning Kubernetes, supports workshops, provides free hosting for community projects and personal sites |
|  17 | Open source: manifests can be reused by others for their own hardware and communities                                              |
|  18 | Positive user feedback and 100% customer satisfaction reported                                                                     |
|  19 | Project available on GitHub and craftcloud.dev                                                                                     |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=wgc5fBmlIFg)
