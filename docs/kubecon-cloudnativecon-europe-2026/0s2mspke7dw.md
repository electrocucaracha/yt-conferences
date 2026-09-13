---
type: Video Note
title: "Cloud Native Theater | Data on Kubernetes Day: KubeVirt Benchmar... Bhumitra Nagar & Dhruv Bhatnagar"
description: "The video discusses real-world challenges faced by organizations migrating from VMware to KubeVirt environments, particularly when scaling up to thousands of virtual machines (VMs). To address issues such as performance, reliability, recove..."
resource: https://www.youtube.com/watch?v=0s2mSPkE7dw
tags: ["kubecon-cloudnativecon-europe-2026", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

The video discusses real-world challenges faced by organizations migrating from VMware to KubeVirt environments, particularly when scaling up to thousands of virtual machines (VMs).
To address issues such as performance, reliability, recovery, and capacity at scale, the presenters introduce Wordbench, an open-source, vendor-neutral benchmarking framework designed for KubeVirt.
Wordbench enables users to benchmark VM provisioning, bootstorm scenarios, live migration, node failure recovery, and storage I/O performance across any Kubernetes distribution or storage backend.
The tool provides detailed metrics and visualizations through an integrated dashboard, supporting both on-premises and cloud deployments.
The presenters demonstrate Wordbench’s capabilities, share customer use cases, and outline upcoming features, encouraging community contributions to the project.
# Main Points

|   # | Main point                                                                                                                                                                                                    |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Customers face challenges when migrating from VMware to KubeVirt environments, especially when scaling to thousands of VMs.                                                                                   |
|   2 | Common customer concerns include performance, reliability and recovery, and cluster capacity.                                                                                                                 |
|   3 | Wordbench is an open-source, vendor-neutral, end-to-end benchmarking framework for KubeVirt.                                                                                                                  |
|   4 | Wordbench benchmarks VM cloning speed, live migration time, cluster capacity, and in-VM IO performance.                                                                                                       |
|   5 | It supports any storage backend, Kubernetes provider, and can run on-premises or in the cloud.                                                                                                                |
|   6 | Wordbench provides a dashboard for visualizing test results and trends.                                                                                                                                       |
|   7 | The tool is operated via a single CLI and is easy to install and use.                                                                                                                                         |
|   8 | Typical workflow: run pre-requisite checks, select and configure benchmarks, execute tests, and visualize results.                                                                                            |
|   9 | Benchmark scenarios include VM provisioning, bootstorm (simultaneous VM boot), live migration (sequential, parallel, node evacuation), cluster/node capacity testing, failure recovery, and FIO benchmarking. |
|  10 | Failure recovery tests support both automated (with fence agent remediation operator) and manual modes.                                                                                                       |
|  11 | FIO benchmarking aggregates IOPS, throughput, and latency metrics across VMs.                                                                                                                                 |
|  12 | Dashboard allows comparison of different configurations, runs, and storage solutions.                                                                                                                         |
|  13 | Example: Live migration of 400 VMs took under 5 minutes with Portworx Enterprise, versus 22 minutes with another CSI.                                                                                         |
|  14 | HSBC uses Wordbench to evaluate VM performance at scale with KubeVirt.                                                                                                                                        |
|  15 | Upcoming features: pip install, container image, Grafana dashboards, hot plug disk operations, selective VM power operations, support for additional benchmarking tools and workloads.                        |
|  16 | Wordbench is open source; contributions are welcome via wordbench.io.                                                                                                                                         |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=0s2mSPkE7dw)