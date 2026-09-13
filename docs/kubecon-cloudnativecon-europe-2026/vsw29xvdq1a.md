---
layout: default
title:
  "Schema Inference and Automation: A New Era for Telemetry Mana... Nicolas Takashi
  & Arthur Silva Sens"
nav_order: 328
parent: Kubecon Cloudnativecon Europe 2026
type: Video Note
description:
  In this talk, Arthur Silva Sense and Nico Takash introduce OpenTelemetry
  Weaver, a tool designed to automate schema inference and enable "Observability by
  Design" without requiring large, specialized teams. They explain that Observability
  b...
resource: https://www.youtube.com/watch?v=vSW29xvdq1A
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

In this talk, Arthur Silva Sense and Nico Takash introduce OpenTelemetry Weaver, a tool designed to automate schema inference and enable "Observability by Design" without requiring large, specialized teams.
They explain that Observability by Design treats telemetry as an API, allowing organizations to define schemas that can be used for contract testing, code generation, policy enforcement, and artifact creation such as dashboards and alerts.
Through a live demo, they show how Weaver can infer telemetry schemas from live data, validate compatibility between code and schema, and generate client SDKs and documentation, thus reducing manual errors and ensuring consistency.
The presenters emphasize the importance of schema-driven observability for maintaining reliable systems, discuss plans for standardization and template improvements, and address audience questions about managing metric standards and gradual rollouts.
They conclude by highlighting ongoing efforts to integrate schema awareness into Prometheus and encourage adoption of automated, schema-based observability practices.

# Main Points

|   # | Main point                                                                                                                                                             |
| --: | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | The talk focuses on schema inference automation, specifically not related to AI.                                                                                       |
|   2 | Presenters: Arthur Silva Sense (Grafana Labs, Prometheus maintainer) and Nico Takash (Coralogix, Perseus maintainer).                                                  |
|   3 | Topic centers on OpenTelemetry Weaver, a tool managed by the OpenTelemetry organization.                                                                               |
|   4 | Observability by Design treats telemetry as an API, using declarative schemas to enable contract testing, code generation, dashboards, alerts, and policy enforcement. |
|   5 | Weaver receives schemas as input and outputs various artifacts, supporting automation and policy enforcement.                                                          |
|   6 | Schema example: a metric with description, units, and examples; enables renaming, policy enforcement, and artifact generation.                                         |
|   7 | Real-world adoption is challenging; organizations often accumulate metrics ad hoc or by copying others.                                                                |
|   8 | Manual schema creation is error-prone and time-consuming, especially for large codebases like Prometheus.                                                              |
|   9 | Weaver introduced a command called "registry infer" to automate schema generation from live telemetry.                                                                 |
|  10 | Demo: Go application exposes metrics; Weaver infers schema from live telemetry using OTLP and OpenTelemetry Collector.                                                 |
|  11 | Load generator simulates user behavior to produce diverse telemetry for schema inference.                                                                              |
|  12 | Generated schema enables further automation: client SDKs, documentation, dashboards, and alerts.                                                                       |
|  13 | Weaver provides "live check" command to validate that live telemetry matches the schema, ensuring contract compliance.                                                 |
|  14 | Changing a metric without updating the schema triggers a violation, preventing unnoticed breaking changes.                                                             |
|  15 | Integration with CI/CD (e.g., GitHub Actions) can block PRs with breaking telemetry changes.                                                                           |
|  16 | Once schema and contract testing are in place, organizations can move to automated client instrumentation generation.                                                  |
|  17 | Weaver uses Jinja templates for flexible artifact generation (SDKs, docs, dashboards) in multiple languages.                                                           |
|  18 | Process for adoption: infer schema from live telemetry, validate with live check, generate artifacts, and e                                                            |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=vSW29xvdq1A)
