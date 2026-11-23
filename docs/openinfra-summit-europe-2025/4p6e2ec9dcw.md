---
layout: default
title: "Building a CSP with OpenStack & Kubernetes  Pain, Power, and Progress"
nav_order: 46
parent: OpenInfra Summit Europe 2025
type: Video Note
description: "KT Cloud, South Korea’s leading data center operator, presented its initiative to rearchitect its traditional cloud platform into a cloud-native infrastructure using Kubernetes and OpenStack."
resource: "https://www.youtube.com/watch?v=4p6e2EC9DCw"
youtube_stats:
  view_count: 167
  like_count: 8
  channel_subscriber_count: 46800
tags:
  - openinfra-summit-europe-2025
  - video
  - learning
status: stable
generated:
  by: process:yt-summarizer-okf
  at: 2026-11-22T23:38:50+00:00
---

# Summary

KT Cloud, South Korea’s leading data center operator, presented its initiative to rearchitect its traditional cloud platform into a cloud-native infrastructure using Kubernetes and OpenStack.
The transition was driven by the need to overcome the scalability limits of hardware-based tenant isolation and to reduce dependency on external vendors by leveraging and contributing to open-source technologies.
The new foundation platform utilizes a three-cluster architecture—admin, stack, and management—to ensure operational stability and loose coupling, with OpenStack services running on top of Kubernetes.
A key innovation is the unified networking layer where OVN serves as the shared backend for both Kubernetes (via the kube-ovn CNI) and OpenStack Neutron, enabling seamless communication between containerized workloads and virtual machines.
This integrated approach supports the launch of a new VPC service that provides customers with fully isolated, customizable private networks, along with enhanced CI/CD pipelines, observability tools, and a redesigned customer console.
Looking ahead, KT Cloud plans to integrate AI capabilities into the platform, including GPU orchestration and AI-optimized hardware, to further expand its service offerings.

# Main Points

|   # | Main point                                                                                                                                                                    |
| --: | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | KT Cloud is the first public cloud provider and top data center operator in South Korea, operating 15 data centers with over 20 years of experience.                          |
|   2 | The company initiated a next-generation cloud-native platform to rearchitect its classic cloud using open-source technologies and standard cloud architectures.               |
|   3 | The traditional model faced scalability limits due to hardware-based tenant isolation and suffered from vendor lock-in that weakened in-house technical capabilities.         |
|   4 | To overcome hardware isolation limits, the new platform layers Neutron on OVN and OVS to implement VPCs, achieving tenant isolation at the virtualization layer.              |
|   5 | Leveraging and contributing to open-source projects allows KT Cloud to avoid vendor lock-in, maintain internal expertise, and respond agilely to market changes.              |
|   6 | The foundation platform consists of three distinct clusters: Admin, Stack, and Management, ensuring separation of roles and loose coupling for stability.                     |
|   7 | The Admin cluster manages the platform lifecycle using Cluster API and serves as a central hub for GitOps deployment, container registry, and secret management.              |
|   8 | The Stack cluster runs OpenStack services on top of Kubernetes, sharing a single OVS and OVN to enable native communication between pods and VMs.                             |
|   9 | The Management cluster hosts customer-facing services, including the customer portal and core cloud service features.                                                         |
|  10 | OVN is an open-source network virtualization solution built on OVS that creates logical virtual networks through a control plane and data plane model.                        |
|  11 | Kube-ovn acts as a CNI plugin for Kubernetes, using OVN as its backend to provide networking functions and actively managing the OVN cluster lifecycle.                       |
|  12 | Neutron in the OpenStack environment uses the same OVN backend as Kubernetes, with logical resources like routers and networks mapping one-to-one to OVN entities.            |
|  13 | This integrated networking approach enables seamless communication between Kubernetes pods and OpenStack VMs, laying the foundation for microVM-based offerings.              |
|  14 | The Next VPC service provides fully isolated, customizable private networks, allowing customers to define IP ranges, subnets, and security policies autonomously.             |
|  15 | Unlike the classic shared network model, Next VPC offers multi-tenant management with unique IP ranges, stronger security, and greater scalability across availability zones. |
|  16 | The VPC architecture includes layers for IP management, traffic flow, and external routing, ensuring modular and scalable network design.                                     |
|  17 | VPC interconnections support secure peering between VPCs and external connectivity via internet and NAT gateways, allowing precise traffic control and policy application.    |
|  18 | The platform unifies CI/CD processes into a single pipeline for automated deployment and validation of OpenStack and KT Cloud services.                                       |
|  19 | Observability is enhanced through a unified platform built on Grafana and LGTM, integrating metrics, logs, and traces for both internal and external visibility.              |
|  20 | The customer console has been redesigned to improve usability and address pain points from the previous classic system.                                                       |
|  21 | Future plans include integrating AI features such as GPU orchestration and AI-optimized storage, alongside hardware upgrades to ARM CPUs and DPUs.                            |
|  22 | The company is expanding its service portfolio to include GPU as a Service, bare metal as a Service, and microVM offerings.                                                   |

# Video

[![Video thumbnail](https://img.youtube.com/vi/4p6e2EC9DCw/hqdefault.jpg)](https://www.youtube.com/watch?v=4p6e2EC9DCw)

[Watch on YouTube](https://www.youtube.com/watch?v=4p6e2EC9DCw)
