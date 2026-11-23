---
layout: default
title: Building a Sovereign DBaaS supporting OpenStack
nav_order: 106
parent: OpenInfra Summit Europe 2025
type: Video Note
description: "The speaker presents CX, a Database-as-a-Service (DBaaS) solution built for OpenStack, designed to help cloud service providers compete with hyperscalers by offering a user-friendly, secure, and sc..."
resource: "https://www.youtube.com/watch?v=hb9RTaqAHko"
youtube_stats:
  view_count: 58
  like_count: 1
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

The speaker presents CX, a Database-as-a-Service (DBaaS) solution built for OpenStack, designed to help cloud service providers compete with hyperscalers by offering a user-friendly, secure, and scalable database management platform.
The architecture utilizes a Kubernetes-based control plane to manage a data plane consisting of virtual machines, supporting popular open-source databases like PostgreSQL and MySQL with features such as parameter groups, automated backups, and point-in-time recovery.
The system provides multiple access methods, including a web UI, Terraform provider, and public API, while ensuring multi-tenancy through JWT-based authentication linked to OpenStack projects.
Key operational principles include immutable infrastructure, where failed nodes are replaced rather than repaired, and the use of external DNS for single-endpoint access to database clusters.
The presentation concludes by highlighting the platform’s support for various cloud infrastructures and its focus on simplifying database operations for end users who expect an experience similar to Amazon RDS.

# Main Points

|   # | Main point                                                                                                                                                                                        |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | The presentation introduces a Database-as-a-Service (DBaaS) solution built for OpenStack, designed to compete with hyperscalers and meet customer expectations similar to Amazon RDS.             |
|   2 | Key requirements include a simple UI, single endpoint access, security, scalability, parameter groups for configuration replication, and backup/restore capabilities with point-in-time recovery. |
|   3 | The architecture separates the control plane, which runs on Kubernetes, from the data plane, which currently operates on virtual machines.                                                        |
|   4 | The system supports common open-source databases and multiple cloud infrastructures, including AWS, Google Cloud, and OpenStack, with multi-region and availability zone support.                 |
|   5 | Deployment is configured via Helm charts, allowing administrators to define supported database types, instance flavors, and volume types within the control plane.                                |
|   6 | Users can access the service through a web UI, Terraform provider, or public API to provision data stores with specific configurations.                                                           |
|   7 | The provisioning workflow involves creating infrastructure resources like VMs and storage, followed by software provisioning using Cloud-Init for certificates and database setup.                |
|   8 | Database clusters are established with primary and replica nodes using streaming replication, and backup schedules are automatically created.                                                     |
|   9 | Monitoring and logging are handled by Fluent Bit forwarding logs to Loki and exporters sending metrics to Victoria Metrics.                                                                       |
|  10 | The data plane currently uses VMs running Ubuntu 22.04, with containerized database support planned for the future roadmap.                                                                       |
|  11 | Licensing for commercial databases like Microsoft SQL Server is managed externally, as the platform does not enforce license checks or accept bring-your-own-license keys.                        |
|  12 | Single endpoint access is achieved using External DNS to create records that route traffic to the primary node of the database cluster.                                                           |
|  13 | Metadata is stored in separate repositories for MySQL, PostgreSQL, and the control plane runtime to manage state and configuration.                                                               |
|  14 | Backups are uploaded to user-provided S3-compatible storage, and point-in-time recovery utilizes binary logs.                                                                                     |
|  15 | Multi-tenancy is supported by deploying resources into a specific OpenStack project owned by the control plane, isolating users via security groups.                                              |
|  16 | Authentication integrates with existing identity providers like Keystone, using JWT tokens to map users to their respective OpenStack projects.                                                   |
|  17 | Operations follow an immutable infrastructure principle, where failed nodes are replaced rather than repaired, and DNS records are updated to reflect changes.                                    |

# Video

[![Video thumbnail](https://img.youtube.com/vi/hb9RTaqAHko/hqdefault.jpg)](https://www.youtube.com/watch?v=hb9RTaqAHko)

[Watch on YouTube](https://www.youtube.com/watch?v=hb9RTaqAHko)
