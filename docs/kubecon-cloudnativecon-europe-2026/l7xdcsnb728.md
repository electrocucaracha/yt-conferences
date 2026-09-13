---
layout: default
title:
  "Automate Once, Run Anywhere: The Docker Moment for Security Workflows - Nancy
  Chauhan & Aseem Shrey"
nav_order: 22
parent: Kubecon Cloudnativecon Europe 2026
type: Video Note
description:
  The presenters introduce "Ships Studio," an open-source project designed
  to bring the robust practices of software engineering—such as observability, traceability,
  and modular workflows—to the field of security engineering, which often reli...
resource: https://www.youtube.com/watch?v=l7XdCSNb728
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

The presenters introduce "Ships Studio," an open-source project designed to bring the robust practices of software engineering—such as observability, traceability, and modular workflows—to the field of security engineering, which often relies on fragile, script-based automations that lack these features.
They highlight the common challenges faced by security teams at organizations of all sizes, including tool sprawl, lack of ownership, unreliable scripts, and difficulties in scaling and auditing security processes.
Ships Studio addresses these issues by providing a visual, drag-and-drop interface for building containerized security workflows, leveraging technologies like Temporal for reliable execution, ClickHouse for analytics, and Kafka for event streaming.
The platform enables users to compose, version, and audit security workflows, integrate with existing tools like Prowler and Trivy, and share standardized workflows across teams, reducing vendor dependency and manual effort.
The demo showcases how Ships Studio simplifies building and managing security automations, supports integration with CI/CD pipelines, and includes features for managing and routing security findings, ultimately aiming to make security automation more scalable, reliable, and accessible.

# Main Points

|   # | Main point                                                                                                                                    |
| --: | --------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Presentation introduces an open-source project aimed at bringing software engineering best practices to security engineering.                 |
|   2 | Security automation in organizations often relies on fragile, unreliable scripts glued together, regardless of company size.                  |
|   3 | Security engineering has not evolved as much as software engineering in terms of automation, observability, and ownership.                    |
|   4 | Current security automation lacks observability, ownership, alerting, traceability, and is difficult to audit.                                |
|   5 | Companies often experience tool sprawl, buying multiple vendor tools for different security needs, leading to increased costs and complexity. |
|   6 | Engineering effort is wasted managing unfriendly tools; open-source tools are underutilized due to maintenance challenges.                    |
|   7 | Security engineers are strong problem solvers but may lack software development skills needed for scalable solutions.                         |
|   8 | Scripts do not scale well for large organizations or complex environments.                                                                    |
|   9 | Proposed solution: containerized, modular workflows instead of scripts.                                                                       |
|  10 | Ships Studio is introduced as an open-source platform with a drag-and-drop UI for building security workflows.                                |
|  11 | Components (e.g., Nmap, Prowler) are dockerized and can be visually composed; users can add custom components.                                |
|  12 | Backend uses Temporal for workflow management, retries, and fault tolerance; runs on Kubernetes.                                              |
|  13 | ClickHouse and Kafka are used for analytics and event streaming; all logs and workflow data are stored and auditable.                         |
|  14 | Versioning ensures traceability and compliance; every change creates a new version for audit purposes.                                        |
|  15 | Visual builder allows users to create, run, and monitor workflows without writing code.                                                       |
|  16 | Example use case: building a cloud security posture management tool using Prowler.                                                            |
|  17 | Ships Studio provides observability, retries, alerting, full visibility, and auditability for security workflows.                             |
|  18 | Enables reusable, composable security workflows, reducing tool sprawl and vendor dependencies.                                                |
|  19 | Teams can share standardize                                                                                                                   |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=l7XdCSNb728)
