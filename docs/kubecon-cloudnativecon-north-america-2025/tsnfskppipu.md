---
layout: default
title:
  Integrating Data Center Observability Into Cloud Native Envi... Pedro Célestin
  & Julia Furst Morgado
nav_order: 105
parent: Kubecon Cloudnativecon North America 2025
type: Video Note
description:
  In this talk, Julia and Pedro discuss the challenges and solutions involved
  in bridging the gap between traditional on-premises data center monitoring and modern
  cloud-native observability, particularly within the legislative chamber in Bra...
resource: https://www.youtube.com/watch?v=TsNfSKppiPU
tags:
  - kubecon-cloudnativecon-north-america-2025
  - video
  - learning
status: stable
generated:
  by: process:yt-conferences-okf
  at: 2026-09-12 00:00:00+00:00
---

# Summary

In this talk, Julia and Pedro discuss the challenges and solutions involved in bridging the gap between traditional on-premises data center monitoring and modern cloud-native observability, particularly within the legislative chamber in Brazil.
They highlight issues such as fragmented telemetry formats, lack of shared context, tool sprawl, and the absence of a common observability language, which hinder effective troubleshooting and collaboration between infrastructure and platform teams.
Their solution centers on adopting OpenTelemetry and its semantic conventions to unify data collection and normalization across both legacy and cloud environments, enabling consistent, vendor-neutral telemetry pipelines.
Pedro details their open-source framework, which integrates data from SNMP, syslogs, Redfish APIs, and cloud-native sources using OpenTelemetry collectors, Kafka for buffering, and backends like Prometheus and OpenSearch, with additional strategies for long-term log retention and cost management.
The key benefits include improved data ownership, flexibility in backend choice, cost reduction, and the ability to correlate metrics across all infrastructure layers, ultimately enhancing end user experience and organizational observability maturity.

# Main Points

|   # | Main point                                                                                                                                  |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Julia and Pedro are principal engineers and CNCF ambassadors, active in Kubernetes and cloud native communities.                            |
|   2 | The talk addresses bridging the gap between legacy on-premises telemetry and modern cloud observability pipelines.                          |
|   3 | Main challenges identified:                                                                                                                 |
|   4 | Fragmented telemetry formats (SNMP, syslog, vCenter APIs vs. PromQL, OpenTelemetry, JSON logs).                                             |
|   5 | Lack of shared context between infrastructure and platform teams.                                                                           |
|   6 | Tool sprawl: multiple observability stacks with different data stores and rules.                                                            |
|   7 | No common language or conventions for observability across teams.                                                                           |
|   8 | OpenTelemetry is highlighted as a universal, vendor-neutral standard for collecting, processing, and exporting telemetry data.              |
|   9 | Pedro’s organization (Brazilian legislative chamber) implemented an open-source observability framework using OpenTelemetry and CNCF tools. |
|  10 | Architecture overview:                                                                                                                      |
|  11 | Data collected from data center (SNMP, syslog, Redfish) and cloud-native layers.                                                            |
|  12 | OpenTelemetry Collector sits at the center, extended with contrib receivers and semantic conventions.                                       |
|  13 | Data flows into unified pipelines, with Prometheus for metrics, OpenSearch for logs, and dashboards for unified views.                      |
|  14 | Apache Kafka used as a buffer for resilience and to handle telemetry data spikes.                                                           |
|  15 | Apache Flink processes logs for long-term retention, storing compressed Parquet files in S3.                                                |
|  16 | Key benefits:                                                                                                                               |
|  17 | Data ownership and vendor lock-in avoidance.                                                                                                |
|  18 | Cost reduction by choosing appropriate backends per environment.                                                                            |
|  19 | Unified analysis and correlation across all infrastructure layers.                                                                          |
|  20 | Manual mapping required for SNMP exporter; homogeneous hardware simplified integration.                                                     |
|  21 | Correlation between workloads and infrastructure achieved by using unified resource attributes across layers.                               |
|  22 | The approach is adaptable to different scopes, from full-stack to partial layers.                                                           |
|  23 | Recommendations for managing AWS log ingress costs: filter data, use hybrid storage, and leverage tools for telemetry insights.             |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=TsNfSKppiPU)
