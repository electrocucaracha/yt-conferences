---
type: Video Note
title: "Beyond the Operators: The Full Strimzi Ecosystem for Kafka on... Paolo Patierno & Michael Morris"
description: "The session introduces StreamZ, a CNCF incubating project for running Apache Kafka on Kubernetes, and highlights its broader ecosystem beyond the core operators (cluster, topic, and user operators). The presenters, Paulo from IBM and Michae..."
resource: https://www.youtube.com/watch?v=mYt9C0YQxDY
tags: ["kubecon-cloudnativecon-north-america-2025", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

The session introduces StreamZ, a CNCF incubating project for running Apache Kafka on Kubernetes, and highlights its broader ecosystem beyond the core operators (cluster, topic, and user operators).
The presenters, Paulo from IBM and Michael from Ericsson, explain how various StreamZ components address key challenges in deploying and managing Kafka clusters.
These include the Access Operator for simplifying client configuration, HTTP and MQTT bridges for alternative connectivity, the Oauth library and quotas plugin for secure, token-based authentication and dynamic client throttling, and tools like the drain cleaner and Kubernetes config provider for safe maintenance and dynamic configuration.
Additionally, the session covers observability with the metrics reporter for Prometheus integration and the test container framework for streamlined testing.
The presenters emphasize community contributions and encourage engagement with the StreamZ ecosystem, which offers a comprehensive set of tools to enhance Kafka operations on Kubernetes.
# Main Points

|   # | Main point                                                                                                                                                            |
| --: | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Audience poll: most know Kafka, fewer know Strimzi.                                                                                                                   |
|   2 | Strimzi is a CNCF project for running Apache Kafka on Kubernetes.                                                                                                     |
|   3 | Strimzi provides operators for managing Kafka clusters, handling day 1 and day 2 operations (security, configuration, upgrades).                                      |
|   4 | Session focuses on the Strimzi ecosystem beyond core operators.                                                                                                       |
|   5 | Contributors, including students and community members, have developed many ecosystem components.                                                                     |
|   6 | Strimzi operators (cluster, topic, user) manage Kafka clusters via Kubernetes custom resources.                                                                       |
|   7 | Additional Strimzi components: Kafka Connect, Kafka MirrorMaker, Kafka clients.                                                                                       |
|   8 | Access Operator: creates Kubernetes secrets with Kafka connection details for clients.                                                                                |
|   9 | HTTP Bridge: exposes REST endpoints for producing/consuming/administering Kafka via HTTP; supports OpenTelemetry tracing and Prometheus metrics.                      |
|  10 | MQTT Bridge: allows IoT devices to send data to Kafka via MQTT; supports flexible topic mapping using regex.                                                          |
|  11 | OAuth Library: enables token-based authentication (e.g., OAuth, Keycloak) for Kafka clients and HTTP Bridge; supports local JWT and remote introspection validation.  |
|  12 | Quotas Plugin: provides dynamic, broker-level quota management and monitoring, distributing quotas among clients dynamically.                                         |
|  13 | Drain Cleaner: safely manages Kafka broker eviction during Kubernetes node draining, ensuring topic replication is not compromised.                                   |
|  14 | Kubernetes Config Provider: fetches configuration values for Kafka components from Kubernetes secrets/config maps via API, supports dynamic updates without restarts. |
|  15 | Metrics Reporter: exposes Kafka metrics directly in Prometheus format, bypassing JMX translation, configurable via allowlist.                                         |
|  16 | Test Container: framework for running Kafka in containers for unit/integration testing, supports various configurations and Kafka Connect.                            |
|  17 | Strimzi ecosystem addresses connectivity, security, governance, operations, reliability, observability, and testing.                                                  |
|  18 | All components are open source and available under the Strimzi orga                                                                                                   |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=mYt9C0YQxDY)