---
type: Video Note
title: "Unveiling Automation: How Mercantil Transformed Data Streaming With Strimzi, Argo... Marcelo Costa"
description: "Marcelo Costa, Head of Data at Mechanu Bank in Brazil, discusses how his team addressed the challenges of scaling real-time data access as the bank grew. Previously, data requests were slow and error-prone, taking up to seven days and relyi..."
resource: https://www.youtube.com/watch?v=tWpspU_9ClE
tags: ["kubecon-cloudnativecon-north-america-2025", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

Marcelo Costa, Head of Data at Mechanu Bank in Brazil, discusses how his team addressed the challenges of scaling real-time data access as the bank grew.
Previously, data requests were slow and error-prone, taking up to seven days and relying on manual processes.
To solve this, they implemented an "integration hub" built around Kafka, Kubernetes, and automated DevOps pipelines, enabling efficient, standardized, and auditable data movement across legacy and modern systems.
By automating connector creation through GitOps and declarative configuration, they reduced lead times from days to just four hours, minimized incidents, and eliminated licensing costs from previous solutions.
This transformation not only improved speed and reliability but also fostered collaboration between engineering, operations, and business teams, demonstrating that with the right architecture and automation, Kafka can be a powerful and manageable ally for enterprise data needs.
# Main Points

|   # | Main point                                                                                                                                                                                                            |
| --: | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Marcelo Costa, Head of Data at Mechanu Bank, Brazil, presents on simplifying data operations using software engineering.                                                                                              |
|   2 | Running Kafka is often seen as complex, expensive, and challenging.                                                                                                                                                   |
|   3 | Mechanu Bank is an 80-year-old, medium-sized, fast-growing bank in Brazil.                                                                                                                                            |
|   4 | Growth led to challenges in providing real-time data access; previous data requests took up to seven business days.                                                                                                   |
|   5 | Legacy methods for moving data were too slow for business needs.                                                                                                                                                      |
|   6 | Implemented an "integration hub" data architecture, built on Kafka, to connect on-prem systems like mainframes.                                                                                                       |
|   7 | The architecture aims for easy governance, administration, and standardization, but initial setup is complex.                                                                                                         |
|   8 | Challenges included manual management of Kafka Connect, high risk of human error, slow connector creation (7-10 days), lack of versioning, traceability, scalability, and low standardization.                        |
|   9 | Mainframes are powerful but difficult to extract data from affordably.                                                                                                                                                |
|  10 | The integration hub is a layered architecture with nine core technologies, including Kubernetes, DevOps pipelines, and Argo CD.                                                                                       |
|  11 | Focus on three components that help manage the architecture, especially for creating connectors between systems.                                                                                                      |
|  12 | Connector creation process: developer writes code, packages it as a YAML file, pushes to Azure repository, Argo CD detects changes and reconciles the desired state, operator creates and optimizes Kafka connectors. |
|  13 | Automation balances load across Kafka Connect pods and optimizes performance.                                                                                                                                         |
|  14 | Demonstrated connector creation from Snowflake to Kafka, with observability on the platform.                                                                                                                          |
|  15 | Platform stats: 8 billion records moved in one week, 134 connectors running, managed by a small team.                                                                                                                 |
|  16 | Currently 400 connectors, 32 projects using the solution, only five Kafka Connect pods, and just three incidents (all human error) since launch.                                                                      |
|  17 | Automation and new architecture reduced lead time for connectors from days/weeks to four hours.                                                                                                                       |
|  18 | Transitioned from manual, error-prone processes to automated, audi                                                                                                                                                    |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=tWpspU_9ClE)