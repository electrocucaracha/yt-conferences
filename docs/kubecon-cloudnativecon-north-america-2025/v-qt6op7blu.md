---
type: Video Note
title: "Design Patterns for Consistent Centralized Authorization - José Padilla & Alice Gibbons"
description: "In this session, Alice Gibbons from Diagrid and Jose Padija from Ozero discuss design patterns for centralized authorization in distributed systems, focusing on the challenges of maintaining consistency across multiple systems—known as the..."
resource: https://www.youtube.com/watch?v=v-Qt6op7BLU
tags: ["kubecon-cloudnativecon-north-america-2025", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

In this session, Alice Gibbons from Diagrid and Jose Padija from Ozero discuss design patterns for centralized authorization in distributed systems, focusing on the challenges of maintaining consistency across multiple systems—known as the "dual write problem." They explain that distributed systems are prone to failures due to unreliable networks, latency, and nonzero transport costs, which can lead to inconsistent states when updating both application databases and centralized authorization systems like OpenFGA.
To address these issues, they present several mitigation strategies, including sequential dual writes, transactional outbox, event sourcing, and durable execution engines.
The Dapr Workflow API is highlighted as a solution for achieving durable execution, enabling workflows to persist state and recover from failures automatically, thus ensuring atomicity and consistency across systems.
A live demo illustrates how Dapr workflows, combined with OpenFGA, can manage organization membership updates reliably, handle errors, and implement customizable retry and rollback policies, providing resilience and flexibility for developers working with distributed authorization patterns.
# Main Points

|   # | Main point                                                                                                                                                                                         |
| --: | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Session covers design patterns for centralized authorization, resiliency in computing, and Dapper workflow API.                                                                                    |
|   2 | Distributed systems remove bottlenecks but introduce challenges like unreliable networks, non-zero latency, and non-zero transport costs.                                                          |
|   3 | The "dual write problem" occurs when two external systems must be updated atomically; failure in one leads to inconsistent state.                                                                  |
|   4 | Examples: updating a database and messaging system, database and cache, inventory and payment, account creation and email verification, or application DB and centralized authorization (OpenFGA). |
|   5 | OpenFGA is a centralized, relationship-based access control system inspired by Google’s Zanzibar, now CNCF incubating.                                                                             |
|   6 | Dual write problem in authorization: updating both local app DB and OpenFGA can fail, causing inconsistencies.                                                                                     |
|   7 | Strategies to mitigate dual write:                                                                                                                                                                 |
|   8 | Sequential dual write with error handling and rollback.                                                                                                                                            |
|   9 | Transactional outbox pattern.                                                                                                                                                                      |
|  10 | Event sourcing pattern.                                                                                                                                                                            |
|  11 | Durable execution engine (workflow engine).                                                                                                                                                        |
|  12 | Durable execution: makes function calls persistent using append-only logs and checkpointing, enabling recovery from failures.                                                                      |
|  13 | Dapper is a CNCF project providing APIs for building microservices, including a workflow engine for durable execution.                                                                             |
|  14 | Dapper workflow API supports long-running processes, task chaining, fan-in/fan-out, external events, child workflows, retry policies, workflow versioning, and unique workflow identity.           |
|  15 | Workflow state is stored in a user-chosen state store (e.g., Postgres, MySQL, Redis).                                                                                                              |
|  16 | Grant organization membership workflow: checks permissions in OpenFGA, creates user locally, assigns permissions in OpenFGA, ensures atomicity and rollback on failure.                            |
|  17 | Demo: Python app using Dapper Workflow SDK and OpenFGA SDK; shows successful and failed permission scenarios, simulates network/database failures, demonstrates retry and rollback.                |
|  18 | Retry policies are customizable per activity; workflows can branch or handle errors as code.                                                                                                       |
|  19 | Per                                                                                                                                                                                                |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=v-Qt6op7BLU)