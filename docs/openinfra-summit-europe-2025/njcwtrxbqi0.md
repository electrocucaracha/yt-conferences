---
layout: default
title: United Nations International Computing Centre's Journey with OpenStack
nav_order: 31
parent: OpenInfra Summit Europe 2025
type: Video Note
description: 'Paula, an infrastructure and platform engineering engineer at the United Nations International Computing Center (UNICC), presented the organization’s journey in building "UniCloud," a private cloud...'
resource: "https://www.youtube.com/watch?v=njCwTRXBqI0"
youtube_stats:
  view_count: 211
  like_count: 4
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

Paula, an infrastructure and platform engineering engineer at the United Nations International Computing Center (UNICC), presented the organization’s journey in building "UniCloud," a private cloud solution developed around OpenStack to serve the UN family.
UNICC, which provides IT services to various UN agencies globally, established this cloud to meet specific principles including open-source adoption, data sovereignty, cost transparency, self-service capabilities, and high automation.
The architecture is strictly divided into a core domain, housing management infrastructure and security services built on LXC and Kubernetes, and a cloud domain that offers Infrastructure as a Service and container layers to end users, ensuring hard isolation between these domains and from existing on-premises systems.
The team, comprising over 50 engineers, utilized Terraform, Ansible, and CI/CD pipelines to automate deployment and operations, while addressing technical challenges such as multi-tenancy isolation by switching storage drivers to ensure robust data separation.
Looking ahead, UNICC is expanding UniCloud by adding a second region, integrating specialized compute for artificial intelligence, and exploring hyperconverged computing to further enhance its sovereign and secure cloud services.

# Main Points

|   # | Main point                                                                                                                                                  |
| --: | ----------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | UNICC is the IT service provider for the United Nations system, supporting agencies globally from offices in Valencia, Brindisi, New York, and Geneva.      |
|   2 | The organization built UniCloud, a private cloud product based on OpenStack, to provide reliable, transparent, and cost-predictable services.               |
|   3 | Key design principles include using open source solutions, ensuring data sovereignty, enabling self-service, and maximizing automation and availability.    |
|   4 | A 2019 Joint Inspection Unit report identified UNICC as the best-positioned entity to provide cloud services for the UN ecosystem.                          |
|   5 | The architecture enforces strict segregation between the core domain (infrastructure and platform) and the cloud domain (customer-facing services).         |
|   6 | The core domain infrastructure is isolated from existing UNICC on-premises systems, requiring the construction of dedicated management infrastructure.      |
|   7 | Management infrastructure was built using LXC system containers and Kubernetes, hosting essential services like DNS, NTP, and network tools.                |
|   8 | Three availability zones were established in the Valencia data center to ensure high availability and network isolation.                                    |
|   9 | Observability and alerting are managed on separate external servers running Prometheus and Grafana to prevent loss of monitoring during core failures.      |
|  10 | Dedicated infrastructure supports security operations, including EDR, vulnerability management, and penetration testing.                                    |
|  11 | The entire stack is managed using Infrastructure as Code with Terraform and Ansible, integrated into CI/CD pipelines for automated deployment and patching. |
|  12 | Access control relies on pull request reviews in Bitbucket rather than direct administrator access, enhancing security and auditability.                    |
|  13 | The cloud domain offers Infrastructure as a Service and container layers via Kubernetes clusters, integrated with CI/CD tools for customer convenience.     |
|  14 | Over 50 engineers from more than 50 teams collaborate on the stack, including SOC, developers, administrators, and data center staff.                       |
|  15 | Challenges included migrating from port forwards to OVN load balancers and adopting Cluster API for better Kubernetes management.                           |
|  16 | FinOps requirements led to the use of Prometheus exporters for fine-grained metrics beyond standard tools like OMeter.                                      |
|  17 | Multi-tenancy and data isolation required moving from CephFS to a different storage array to ensure hard isolation for shared file systems.                 |
|  18 | Future plans include adding a second region, specialized compute for artificial intelligence, and exploring hyperconverged computing.                       |
|  19 | The initiative emphasizes sovereignty over both data and knowledge, keeping expertise in-house to drive organizational efficiency and growth.               |

# Video

[![Video thumbnail](https://img.youtube.com/vi/njCwTRXBqI0/hqdefault.jpg)](https://www.youtube.com/watch?v=njCwTRXBqI0)

[Watch on YouTube](https://www.youtube.com/watch?v=njCwTRXBqI0)
