---
layout: default
title:
  "Durable Execution in DevOps: How Uniphar Built Reliable Syst... Alice Gibbons
  & Vaclav (Oisin) Haken"
nav_order: 97
parent: Kubecon Cloudnativecon Europe 2026
type: Video Note
description:
  In this presentation, Alice Gibbons from DiGrid and Oshin from UniFar
  discuss how UniFar modernized its cost management systems using Dapper, an open-source
  distributed application runtime. UniFar, originally a small pharmacy co-op, now
  ope...
resource: https://www.youtube.com/watch?v=REp5yMgy7UQ
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

In this presentation, Alice Gibbons from DiGrid and Oshin from UniFar discuss how UniFar modernized its cost management systems using Dapper, an open-source distributed application runtime.
UniFar, originally a small pharmacy co-op, now operates globally and needed to manage complex, distributed IT systems after multiple acquisitions and cloud migrations.
Their solution leverages Dapper workflows to automate and reliably track cloud resource costs, enabling flexible cost splitting and reporting through a hierarchy that mirrors Azure’s structure.
The system uses durable execution, allowing workflows to resume after failures, and outputs standardized CSV reports for accounting.
They highlight the benefits of Dapper’s modularity, extensibility, and durability, share lessons learned in workflow design and parallelization, and note successful adoption of Dapper for other mission-critical applications at UniFar.

# Main Points

|   # | Main point                                                                                                                                           |
| --: | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Presentation focused on durable execution in DevOps, reliability in distributed systems, and workflow management using Dapper.                       |
|   2 | UniFar evolved from a small pharmacy co-op to a global company in 160+ countries with 200+ partners, modernizing operations from manual to digital.  |
|   3 | Cost management is critical during cloud migration, especially with diverse, acquired IT systems and shared infrastructure.                          |
|   4 | Need for extensible, distributed solutions to handle growing numbers of resources and projects, with support for splitting costs across initiatives. |
|   5 | Monthly cost tracking implemented using workflows, with business users able to define cost center rules for flexibility.                             |
|   6 | Output is a CSV file for accounting, bridging business and technology needs.                                                                         |
|   7 | Solution mirrors Azure’s resource hierarchy: tenant → subscription → resource group → resources.                                                     |
|   8 | Specialized workflows created for unique scenarios (e.g., AKS splitting, VDI workflows), easily extendable for new logic.                            |
|   9 | Workflows fan out for data discovery and crunching, then fan in for reporting.                                                                       |
|  10 | Durable execution achieved via Dapper workflow engine, with checkpointing and replaying for resilience against failures.                             |
|  11 | Parent workflow triggers child workflows for each Azure resource, each running as a separate process.                                                |
|  12 | Business logic wrapped in Dapper.NET SDK for durable execution; supports stopping and resuming workflows without data loss.                          |
|  13 | Dapper acts as an abstraction layer between application code and infrastructure, supporting modularity, resiliency, observability, and security.     |
|  14 | Supports parallel and sequential workflows, child workflows, external event handling, workflow versioning, and identity management.                  |
|  15 | Resiliency and retry policies can be set per activity.                                                                                               |
|  16 | Workflow state is checkpointed to a state store, enabling recovery and completion after failures.                                                    |
|  17 | Workflow abstraction builds on the actor pattern, managing state and lifecycle for scalability.                                                      |
|  18 | Lessons learned: parallelize subscriptions, run                                                                                                      |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=REp5yMgy7UQ)
