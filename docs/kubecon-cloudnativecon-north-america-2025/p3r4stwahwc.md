---
type: Video Note
title: "Real-World Strategies for Cutting Kubernetes Costs: Why One Size Doesn’t Fit All - Dolis Sharma"
description: "The speaker discusses real-world strategies for reducing Kubernetes cloud costs, emphasizing that no single solution fits all environments due to differences in application needs and infrastructure. Key reasons for high costs include overpr..."
resource: https://www.youtube.com/watch?v=p3r4StwaHWc
tags: ["kubecon-cloudnativecon-north-america-2025", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

The speaker discusses real-world strategies for reducing Kubernetes cloud costs, emphasizing that no single solution fits all environments due to differences in application needs and infrastructure.
Key reasons for high costs include overprovisioning workloads, insufficient scaling strategies, idle or orphaned resources, and lack of visibility.
Solutions presented involve implementing policy-driven tools like Kyverno for automating best practices, using scaling tools such as Carpenter and Vertical Pod Autoscaler (VPA) to right-size resources, and employing cleanup policies or tools like Cloud Custodian to remove unused resources.
The speaker highlights the importance of automating resource requests and limits, labeling for cost tracking, and starting with small, incremental policy changes to measure impact before expanding.
The session concludes with a Q&A addressing policy enforcement and automation, and the suggestion to share practical policy examples via a public GitHub repository.
# Main Points

|   # | Main point                                                                                                                                                    |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | One solution does not fit all for Kubernetes cloud cost optimization; strategies depend on environment and application needs.                                 |
|   2 | Main reasons for high Kubernetes costs:                                                                                                                       |
|   3 | Overprovisioning workloads due to lack of continuous evaluation and automation.                                                                               |
|   4 | Insufficient scaling strategies for jobs and applications.                                                                                                    |
|   5 | Idle, orphan, or dangling resources (e.g., pods, PVCs, volumes) left running.                                                                                 |
|   6 | Lack of visibility and awareness into cluster resource usage.                                                                                                 |
|   7 | Solutions discussed:                                                                                                                                          |
|   8 | Use tools like Carpenter and policies to control node provisioning and scaling, specifying instance types and pod placement.                                  |
|   9 | Enforce policies with tools like Kyverno (Kubernetes-native, YAML-based policy engine) for automation and best practices.                                     |
|  10 | Implement Vertical Pod Autoscaler (VPA) with Kyverno policies to dynamically right-size workloads based on 24-hour usage cycles.                              |
|  11 | Store VPA recommendations in observability tools (e.g., Prometheus, Grafana) for historical tracking and decision-making.                                     |
|  12 | Clean up unused resources using cleanup policies, kube-downscaler, Cloud Custodian, or kube-janitor; automate scaling down dev environments during off-hours. |
|  13 | Use TTL labels in cleanup policies to automatically delete temporary resources after a set period.                                                            |
|  14 | Enforce best practices with policies for labels, tags, quotas, requests, and limits to improve cost tracking and resource boundaries.                         |
|  15 | Use observability tools (e.g., AWS Cost Explorer) with proper labeling for cost visualization and analysis.                                                   |
|  16 | Call to action: Start with one policy (e.g., cleanup or best practice), measure its impact, and expand gradually.                                             |
|  17 | Kyverno policies can validate, mutate, generate, and clean up resources; can operate in blocking or audit/reporting modes.                                    |
|  18 | Kyverno can query external APIs for advanced logic (e.g., checking traffic before scaling down).                                                              |
|  19 | Plans to create a public GitHub repo with example policies if there is community interest.                                                                    |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=p3r4StwaHWc)