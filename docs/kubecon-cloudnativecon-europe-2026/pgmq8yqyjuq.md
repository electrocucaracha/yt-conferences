---
type: Video Note
title: "Banking on Reliability: Cloud Native SRE Practices in Financial Services - Clément Nussbaumer"
description: "The speaker, a systems engineer at Post Finance, a major Swiss bank, discusses the implementation of site reliability engineering (SRE) principles to improve service reliability, particularly focusing on Kubernetes clusters. Initially, the..."
resource: https://www.youtube.com/watch?v=pgmQ8YqyjUQ
tags: ["kubecon-cloudnativecon-europe-2026", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

The speaker, a systems engineer at Post Finance, a major Swiss bank, discusses the implementation of site reliability engineering (SRE) principles to improve service reliability, particularly focusing on Kubernetes clusters.
Initially, the team lacked clear service level objectives (SLOs), leading to subjective assessments of system performance.
By defining and monitoring SLOs, they identified and addressed issues such as unbalanced API server loads, which were resolved by configuring HTTP2 connection handling to ensure proper load distribution.
The talk also covers the development and open-sourcing of monitoring tools like Cubers, which performs health checks and neighbor latency detection, and the importance of efficient end-to-end testing to proactively catch service failures.
A case study on sporadic 502 errors reveals the significance of aligning backend and ingress timeout settings, illustrating how even rare errors can uncover critical system insights.
The speaker concludes by emphasizing the value of SLOs, open-source collaboration, comprehensive testing, and attention to every error, no matter how infrequent.
# Main Points

|   # | Main point                                                                                                                                                |
| --: | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Speaker is a Swiss systems engineer at Post Finance, a large Swiss bank operating on-prem Kubernetes clusters.                                            |
|   2 | Migration from kubeadm to Talos is ongoing; most Kubernetes solutions are built in-house.                                                                 |
|   3 | Reliability is critical; failed requests directly impact customers at ATMs or shops.                                                                      |
|   4 | Initially, no Service Level Objectives (SLOs) were defined; issues were identified subjectively and often ignored.                                        |
|   5 | Adoption of SLOs (e.g., <0.1% API server request failure) enabled objective monitoring and improvement.                                                   |
|   6 | Used open-source tool SLOs to define and monitor metrics, correlating incidents with cluster events.                                                      |
|   7 | Identified upgrade-related latency issues; improved by switching to stacked etcd topology (API server talks to local etcd).                               |
|   8 | Further improvements included transferring etcd leadership before maintenance, but issues persisted.                                                      |
|   9 | Discovered load imbalance among API servers due to persistent HTTP2 connections; one server handled most traffic.                                         |
|  10 | Resolved by setting the API server’s goaway-chance flag, forcing clients to reconnect and balancing load.                                                 |
|  11 | Developed and open-sourced monitoring tools: hosters (DNS troubleshooting) and cubers (continuous health checks).                                         |
|  12 | Cubers performs multiple checks (API server via IP/DNS, CNI, ingress, neighbor latency) and records detailed metrics.                                     |
|  13 | Addressed scalability issue in cubers by implementing a hash ring to limit neighbor checks, reducing metric load.                                         |
|  14 | Implemented SLO for cubers; fixed request loss during pod shutdown by adding a 5-second graceful shutdown.                                                |
|  15 | Developed end-to-end tests (in Go) for cluster services (e.g., PVC creation, deployment), running as cronjobs and reporting to VictoriaMetrics.           |
|  16 | End-to-end tests help quickly identify and correlate service failures with recent changes.                                                                |
|  17 | Investigated rare 502 errors; root cause was mismatched keepalive timeouts between NGINX ingress (60s) and Tomcat backend (20s), causing race conditions. |
|  18 | Fix: Set backend keepalive timeout longer than ingress timeout.                                                                                           |
|  19 | Key t                                                                                                                                                     |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=pgmQ8YqyjUQ)