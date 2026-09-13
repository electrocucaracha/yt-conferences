---
layout: default
title:
  How Statistical Offices Move to Cloud Native Technology - Frédéric Comte &
  Trygve Tatsuya Falch
nav_order: 143
parent: Kubecon Cloudnativecon Europe 2026
type: Video Note
description:
  The speakers, representing Statistics Norway and the French national
  statistical office, discuss the challenges and solutions involved in moving national
  statistical offices (NSOs) to cloud-native infrastructures. They highlight the institu...
resource: https://www.youtube.com/watch?v=JD8qIJuEfEA
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

The speakers, representing Statistics Norway and the French national statistical office, discuss the challenges and solutions involved in moving national statistical offices (NSOs) to cloud-native infrastructures.
They highlight the institutional tension between maintaining strict security and enabling innovation, noting that traditional IT processes often slow down experimentation and development.
By adopting Kubernetes, containers, and open-source platforms like NICE and Onyxia, they have created flexible, secure, and user-friendly environments that allow data scientists—who often work with sensitive real data and are not traditional developers—to efficiently analyze data and build statistical products.
These platforms provide standardized tools, secure access, and resource management while supporting a wide range of analytical workflows, from one-off explorations to production pipelines.
The speakers emphasize the importance of collaboration, guidance over abstraction, and ongoing training to ensure that statisticians can leverage modern technologies while maintaining data security and methodological rigor.

# Main Points

|   # | Main point                                                                                                                                                            |
| --: | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Statistical offices are moving to cloud-native solutions to address challenges in producing official statistics.                                                      |
|   2 | National statistical offices (NSOs) must balance data protection with enabling innovation, often hindered by centralized IT processes.                                |
|   3 | Cloud-native and self-service platforms aim to reduce institutional bottlenecks and ticket-based cultures.                                                            |
|   4 | Statistics Norway modernized infrastructure by moving from on-premise legacy systems to Kubernetes and cloud-native technologies.                                     |
|   5 | NICE (NAV's Application Infrastructure Service) provides secure, ready-made building blocks for software development, reducing the need to build everything in-house. |
|   6 | Collaboration exists between Norwegian and French statistical offices, including the open-source Onyxia project.                                                      |
|   7 | Data scientists in NSOs often act as developers but have unique needs: they work with real, sensitive data and require secure, centralized platforms.                 |
|   8 | Containers and object storage (e.g., Parquet format) provide scalable, flexible foundations for both exploration and production.                                      |
|   9 | Secret management is handled with Vault; data warehouse uses Iceberg for flexible, open access.                                                                       |
|  10 | The architecture supports an ecosystem of tools (e.g., DuckDB, Spark, Trino) rather than a single solution.                                                           |
|  11 | User experience is prioritized through guidance over abstraction, maintaining standard tools and avoiding lock-in.                                                    |
|  12 | Onyxia provides a unified, transparent user interface, leveraging OpenID Connect for access and automating resource provisioning.                                     |
|  13 | Features include emulated terminals, automatic configuration, S3 browser, and file explorers.                                                                         |
|  14 | Statisticians are trained in Python and responsible for end-to-end statistical pipelines.                                                                             |
|  15 | Onyxia launches services via Helm charts, with user-friendly interfaces for resource configuration.                                                                   |
|  16 | Maintenance includes pausing unused containers and aggressive cleanup, especially for GPU resources.                                                                  |
|  17 | Data isolation is managed via S3 access policies and group-based permissions.                                                                                         |
|  18 | Onyxia is                                                                                                                                                             |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=JD8qIJuEfEA)
