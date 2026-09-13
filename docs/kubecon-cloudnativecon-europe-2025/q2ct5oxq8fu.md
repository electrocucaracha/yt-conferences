---
type: Video Note
title: "Challenges of and Solutions for Migrating Spark From Legacy Hadoop Clu... Neha Singla & Rasik Pandey"
description: "Here is a summary of the video transcript in 3-5 sentences."
resource: https://www.youtube.com/watch?v=Q2ct5OXQ8fU
tags: ["kubecon-cloudnativecon-europe-2025", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

Here is a summary of the video transcript in 3-5 sentences: Apple's Nay and Nha discuss their journey from moving Spark workloads from legacy Hadoop clusters to Kubernetes, highlighting challenges such as resource management, storage, and networking issues.
They introduce Unicorn, a specialized layer between Kubernetes control plane and Spark applications, which provides hierarchical resource management with guaranteed quotas per user.
The team also discusses the importance of proper porting, shuffle tracking, and dynamic allocation in optimizing Spark performance on Kubernetes.
# Main Points

|   # | Main point                                                                                                                                                                                                                                                                          |
| --: | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Moving Spark workloads from legacy Hadoop clusters to Kubernetes ecosystem.                                                                                                                                                                                                         |
|   2 | Evolving Spark techniques to make it work in a Kubernetes environment.                                                                                                                                                                                                              |
|   3 | Key takeaways for making Spark work well on Kubernetes:                                                                                                                                                                                                                             |
|   4 | Best practices and pitfalls.                                                                                                                                                                                                                                                        |
|   5 | Separating storage and compute.                                                                                                                                                                                                                                                     |
|   6 | Cluster autoscaling.                                                                                                                                                                                                                                                                |
|   7 | Containerization.                                                                                                                                                                                                                                                                   |
|   8 | Dependency management.                                                                                                                                                                                                                                                              |
|   9 | Better resource utilization.                                                                                                                                                                                                                                                        |
|  10 | Challenges with the current architecture:                                                                                                                                                                                                                                           |
|  11 | No dynamic scaling of cluster resources.                                                                                                                                                                                                                                            |
|  12 | Admin had to provision resources for peak demands.                                                                                                                                                                                                                                  |
|  13 | Storage and computes were tightly coupled.                                                                                                                                                                                                                                          |
|  14 | No data lake concept.                                                                                                                                                                                                                                                               |
|  15 | No built-in orchestration.                                                                                                                                                                                                                                                          |
|  16 | No interactive experiment interface.                                                                                                                                                                                                                                                |
|  17 | Solutions:                                                                                                                                                                                                                                                                          |
|  18 | Moving to virtualized environment using VMware.                                                                                                                                                                                                                                     |
|  19 | Introducing Jupyter classic for interactivity.                                                                                                                                                                                                                                      |
|  20 | Implementing proper portuling.                                                                                                                                                                                                                                                      |
|  21 | Configuring comprehensive monitoring.                                                                                                                                                                                                                                               |
|  22 | Unicorn scheduleuler:                                                                                                                                                                                                                                                               |
|  23 | Provides hierarchical resource management with guaranteed resource quotas per Q.                                                                                                                                                                                                    |
|  24 | Addresses scheduling limitations for Spark workloads.                                                                                                                                                                                                                               |
|  25 | Enables dynamic allocation and queuing support.                                                                                                                                                                                                                                     |
|  26 | Supports priority, fairness, and job prioritization.                                                                                                                                                                                                                                |
|  27 | Key takeaways: + Assess current workload pattern before moving to Kubernetes. + Design a phase strategy and start with hybrid approach. + Optimize resource utilization. + Use unicorn scheduleuler for Spark workloads. + Implement proper portuling and comprehensive monitoring. |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=Q2ct5OXQ8fU)