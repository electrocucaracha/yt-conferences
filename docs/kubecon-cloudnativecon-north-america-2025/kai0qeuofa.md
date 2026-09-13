---
type: Video Note
title: "Node Manager - How Yahoo Manages Thousands of Nodes at Scale? - Payal Patel, Yahoo"
description: "Piyal Patel, a principal software development engineer at Yahoo, presents on Yahoo's Node Manager, a Kubernetes operator designed to automate and control maintenance and remediation tasks across thousands of on-premises and cloud-based Kube..."
resource: https://www.youtube.com/watch?v=_kAI0qEuoFA
tags: ["kubecon-cloudnativecon-north-america-2025", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

Piyal Patel, a principal software development engineer at Yahoo, presents on Yahoo's Node Manager, a Kubernetes operator designed to automate and control maintenance and remediation tasks across thousands of on-premises and cloud-based Kubernetes nodes.
She explains that Yahoo manages over 8,000 physical hosts and hundreds of clusters, making manual node management error-prone and time-consuming.
Node Manager enables administrators to specify nodes for maintenance, set concurrency and failure thresholds, and pause or resume tasks as needed, all while maintaining healthy cluster capacity.
The system consists of a custom resource for configuration, a controller for orchestration, and a node agent for task execution, with security ensured through encrypted annotations.
For auto-remediation, Yahoo leverages the open-source Node Problem Detector to identify issues, then uses the same operator framework to cordon, drain, and repair nodes in a controlled manner, with metrics and visualizations provided via Prometheus and Grafana.
Patel highlights that automation has significantly reduced maintenance time, improved reliability, and provided valuable operational insights, while also addressing challenges such as pod disruption budgets, stateful workloads, and debugging failed actions.
The session concludes with a Q&A covering technical details, open sourcing plans, and operational best practices.
# Main Points

|   # | Main point                                                                                                                                         |
| --: | -------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Yahoo manages 35+ on-prem Kubernetes clusters (8,000+ physical hosts, 2,400+ applications) and 35+ EKS, 16+ GKE clusters (1,000+ nodes).           |
|   2 | Node Manager is a Kubernetes operator for automated, controlled node maintenance at scale.                                                         |
|   3 | Key requirements: specify node list, configure concurrency, set failure thresholds.                                                                |
|   4 | Node Manager architecture: custom resource (defines maintenance), controller (orchestrates tasks), node agent (executes tasks on nodes).           |
|   5 | Custom resource allows configuration of node selection, concurrency, failure thresholds, pause, timeout, and maintenance blueprint via config map. |
|   6 | Supports node group-specific concurrency, failure thresholds, pause, and execution order (weight).                                                 |
|   7 | Status of maintenance tasks is visible via kubectl commands; supports live monitoring.                                                             |
|   8 | Controller ensures checks/conditions, groups nodes by rack to minimize workload impact, and manages task dispatch.                                 |
|   9 | Node agent listens for annotations, executes tasks, and updates status (success/error/timeout).                                                    |
|  10 | Annotations are encrypted as JWT tokens for security.                                                                                              |
|  11 | Node auto-remediation includes issue detection (Node Problem Detector), isolation (cordon/drain), hardware tagging, and controlled remediation.    |
|  12 | Node Problem Detector (NPD) detects 25+ node issues via pattern matching, creates Kubernetes events.                                               |
|  13 | Remediation actions are triggered based on event thresholds, with configurable actions and retry limits.                                           |
|  14 | Backoff mechanisms prevent conflicting or duplicate remedies; only one remedy runs per node at a time.                                             |
|  15 | Prometheus and Grafana used for metrics and visualization of maintenance/remediation status.                                                       |
|  16 | Automation reduced maintenance from weeks to hours; enables 24/7 operations and reduces errors.                                                    |
|  17 | Pod Disruption Budgets can delay upgrades; stuck nodes are tracked via dashboards.                                                                 |
|  18 | For stateful workloads, rack awareness and pod affinity prevent simultaneous failures.                                                             |
|  19 | Node Manager is not yet open source but may be in the future.                                                                                      |
|  20 | Debugging relies on node agent logs, wh                                                                                                            |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=_kAI0qEuoFA)