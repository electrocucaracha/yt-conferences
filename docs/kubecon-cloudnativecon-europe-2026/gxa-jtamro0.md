---
type: Video Note
title: "Cloud Native Non-Functional Requirements: Building Scalable, Resilient and Secure... Jakub Krzywda"
description: "In this talk, Yakub Shiva, a cloud native architect at Elasticis, discusses the importance of considering non-functional requirements—such as scalability, resilience, and security—when designing application architectures, beyond just the ba..."
resource: https://www.youtube.com/watch?v=GXa_jTamRo0
tags: ["kubecon-cloudnativecon-europe-2026", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

In this talk, Yakub Shiva, a cloud native architect at Elasticis, discusses the importance of considering non-functional requirements—such as scalability, resilience, and security—when designing application architectures, beyond just the basic functional flow.
He explains that while functional requirements define what a system should do, non-functional requirements determine whether it can operate effectively under load, during failures, and against security threats.
Shiva outlines key qualities for cloud native systems, including loose coupling, observability, automation (CI/CD), and security by design, emphasizing the shared responsibilities between application platforms and developers.
He provides practical insights into how platforms should offer robust infrastructure—like replicated databases, logging stacks, and automated deployment pipelines—while developers must implement best practices in areas such as logging, security, and resource management.
The talk concludes by stressing that leveraging cloud native platforms can greatly aid in meeting non-functional requirements, but developers must actively collaborate with these platforms and continually assess how to best utilize their capabilities during the design process.
# Main Points

|   # | Main point                                                                                                                                            |
| --: | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Designing application architecture often starts with drawing functional components: frontend, API, database.                                          |
|   2 | Functional requirements describe what the system does; non-functional requirements (NFRs) determine if it can handle scale, resilience, and security. |
|   3 | NFRs are critical for real-world performance under load, failure, and attack.                                                                         |
|   4 | Cloud native technologies enable scalable, resilient, manageable, and observable applications in dynamic cloud environments.                          |
|   5 | NFRs include qualities like performance, scalability, security, usability, and maintainability.                                                       |
|   6 | Application platforms streamline the application lifecycle from development to management.                                                            |
|   7 | NFRs define qualities; cloud native technologies fulfill them; platforms combine these into a coherent system.                                        |
|   8 | Key architectural qualities:                                                                                                                          |
|   9 | Loose coupling: Components (microservices) are independent, enabling faster iteration and scaling.                                                    |
|  10 | Observability: Systems generate actionable insights via logs, metrics, and traces for faster incident response.                                       |
|  11 | Automation: Continuous integration (CI), continuous delivery (CD), and continuous deployment automate testing and releases, reducing risk.            |
|  12 | Cloud native security: Security is integrated throughout the lifecycle, with automated scans and rapid updates.                                       |
|  13 | Security principles: Security by design, minimal need to know, defense in depth, redundancy.                                                          |
|  14 | Don’t repeat yourself: Reuse platform functionality and automate processes to reduce duplication.                                                     |
|  15 | Practical NFR implementations:                                                                                                                        |
|  16 | State management: Platforms provide replicated, backed-up databases; developers manage credentials, migrations, and use platform databases.           |
|  17 | Observability: Platforms offer centralized logging; developers log errors, use structured logs, and create dashboards.                                |
|  18 | Automation: Platforms provide CI/CD tools and registries; developers write tests and follow platform deployment paths.                                |
|  19 | Security: Platforms enforce hardened configurations and guardrails; developers follow best                                                            |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=GXa_jTamRo0)