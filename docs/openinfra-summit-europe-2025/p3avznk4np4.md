---
layout: default
title: OpenStack Demystified  A Practical Guide for VMware Admins
nav_order: 85
parent: OpenInfra Summit Europe 2025
type: Video Note
description: "Damian, a former VMware administrator now working at Platform 9, presents a comprehensive guide for IT professionals transitioning from VMware to OpenStack, driven largely by Broadcom’s aggressive ..."
resource: "https://www.youtube.com/watch?v=p3AvZNK4NP4"
youtube_stats:
  view_count: 81
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

Damian, a former VMware administrator now working at Platform 9, presents a comprehensive guide for IT professionals transitioning from VMware to OpenStack, driven largely by Broadcom’s aggressive post-acquisition pricing and community neglect.
He outlines three critical areas of change: technical, operational, and cultural.
Technically, the shift involves moving from a monolithic, GUI-centric environment to a modular, API-first architecture where components like Keystone, Nova, and Cinder replace VMware’s integrated services, requiring a new understanding of abstracted VMs, prescriptive networking, and distributed storage.
Operationally, the transition demands adapting to Linux-based command-line interfaces, distributed troubleshooting across multiple services, and a more complex risk model that relies on open-source drivers rather than a single vendor’s hardware compatibility list.
Culturally, Damian frames the migration as a growth opportunity, encouraging administrators to embrace new skills in infrastructure-as-code and open-source governance, while noting that the community and available training resources provide essential support for navigating this significant professional upheaval.

# Main Points

|   # | Main point                                                                                                                                                                                               |
| --: | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | The speaker, a former VMware administrator now working at Platform 9, shares insights on migrating to OpenStack.                                                                                         |
|   2 | Organizations are migrating primarily due to Broadcom’s acquisition of VMware, which has led to increased costs and a perceived abandonment of the community and partners.                               |
|   3 | The transition involves three major shifts: technical adaptation, operational changes, and organizational cultural adjustments.                                                                          |
|   4 | Technically, VMware is monolithic with GUI-centric management, while OpenStack is abstract, API-first, and CLI-driven.                                                                                   |
|   5 | VMware VMs are concrete file sets (VMDK/VMX), whereas OpenStack VMs are abstract entities with metadata stored in databases and storage handled by services like Cinder.                                 |
|   6 | Networking in VMware is less prescriptive, while OpenStack assigns IP, MAC, and security groups at the port level.                                                                                       |
|   7 | Storage differs significantly; VMware uses VMFS and vSAN, while OpenStack uses Cinder for block storage and Glance for images, offering more flexibility but requiring different operational approaches. |
|   8 | Identity and security are managed via Keystone in OpenStack, which is multi-tenant and flexible, compared to VMware’s role-based access control.                                                         |
|   9 | Backup and disaster recovery ecosystems are extensive in VMware but limited in OpenStack, though vendors like Rubrik and Cohesity are developing support.                                                |
|  10 | Operational challenges in OpenStack include distributed ownership, cross-functional triage, and monitoring via open-source tools like Prometheus and Grafana.                                            |
|  11 | Updates in OpenStack are semiannual and component-based, requiring blue-green or canary deployment strategies, unlike VMware’s integrated update model.                                                  |
|  12 | OpenStack emphasizes self-service provisioning from the start, leveraging multi-tenancy and APIs for automation.                                                                                         |
|  13 | Automation and orchestration are more modular and API-driven in OpenStack, avoiding the "shelfware" issue associated with VMware’s bundled products.                                                     |
|  14 | Governance and support in OpenStack rely on driver-based frameworks and open-source compliance, differing from VMware’s top-down commercial support and hardware compatibility lists.                    |
|  15 | Licensing risks shift from vendor audits in VMware to open-source compliance and management in OpenStack.                                                                                                |
|  16 | Culturally, the migration is viewed as a growth opportunity, requiring new skills in Linux, APIs, and distributed troubleshooting.                                                                       |
|  17 | Resources for learning include boot camps, certifications like Certified OpenStack Administrator, and community events such as OpenStack Days.                                                           |
|  18 | The openness of OpenStack, such as using Qcow2 images that work anywhere, is a key advantage over being beholden to a single vendor.                                                                     |

# Video

[![Video thumbnail](https://img.youtube.com/vi/p3AvZNK4NP4/hqdefault.jpg)](https://www.youtube.com/watch?v=p3AvZNK4NP4)

[Watch on YouTube](https://www.youtube.com/watch?v=p3AvZNK4NP4)
