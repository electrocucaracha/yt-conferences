---
layout: default
title: "Running the Runners: How CNCF Powers GitHub Actions at Scale - Koray Oksay, Kubermatic"
nav_order: 1
parent: "Maintainer Summit 2026 - Europe"
type: Video Note
description: "Koray from Kubermatic presented a talk at the KubeCon maintainers summit detailing how CNCF transitioned its CI/CD infrastructure to self-hosted GitHub Action runners to address rising costs and se..."
resource: "https://www.youtube.com/watch?v=1Nm9TPCwqS8"
tags:
  - maintainer-summit-2026-europe
  - video
  - learning
status: stable
generated:
  by: process:yt-summarizer-okf
  at: 2026-11-16T15:59:05+00:00
---

# Summary

Koray from Kubermatic presented a talk at the KubeCon maintainers summit detailing how CNCF transitioned its CI/CD infrastructure to self-hosted GitHub Action runners to address rising costs and service discontinuations.
The initiative was triggered by GitHub ending free access to large runners in June 2024 and Equinix shutting down its bare-metal services in November 2024, which threatened the sustainability of CNCF’s 230+ projects.
Initially, the team used GitHub’s Action Runner Controller (ARC) to run jobs as containers within Kubernetes clusters on Oracle Cloud, but this approach failed to support projects requiring nested virtualization, KVM, or specific low-level networking capabilities.
To resolve these limitations, the team developed a solution that leverages ARC to trigger the creation of actual virtual machines on Oracle Cloud, using custom Packer templates to generate OS images for both x86 and ARM architectures.
Although this VM-based approach reduced costs from approximately $1,000 per day to $1,000 per month, it introduced challenges such as longer startup times and complex dependency management, leading the team to explore KubeVirt on bare-metal clusters to improve performance and scalability.

# Main Points

|   # | Main point                                                                                                                                                                                      |
| --: | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | CNCF provides infrastructure and self-hosted GitHub Action runners for over 240 projects with diverse technology stacks and pipeline needs.                                                     |
|   2 | Infrastructure costs are primarily covered by donations, which present challenges due to varying validity periods, fluctuating amounts, and the need for immediate utilization.                 |
|   3 | CNCF maintains a strong partnership with GitHub, which provides free or discounted runner minutes and larger runner capacities for CNCF projects.                                               |
|   4 | In June 2024, GitHub announced that larger runners would no longer be free, and in November 2024, Equinix shut down its bare metal services, creating a cost and availability crisis.           |
|   5 | The initial solution used the GitHub Action Runner Controller (ARC) to run runners as containers within Kubernetes clusters managed by Argo CD.                                                 |
|   6 | Container-based runners failed to support nested virtualization, KVM, and specific low-level networking requirements needed by certain projects.                                                |
|   7 | To address these limitations, the team transitioned to using Virtual Machines (VMs) by adapting GitHub’s Packer templates to create custom Ubuntu OS images for both x86 and ARM architectures. |
|   8 | A custom application was developed to bridge ARC and cloud providers, allowing ARC to trigger VM creation on Oracle Cloud instead of just spinning up containers.                               |
|   9 | ARM image creation required significant manual adjustments to Packer files to handle inconsistent package naming conventions across different ARM versions.                                     |
|  10 | VM startup times on Oracle Cloud are approximately five minutes, which is slower than GitHub-hosted runners but acceptable for current operational needs.                                       |
|  11 | The team is currently proof-of-concepting KubeVirt on a bare metal cluster to reduce VM startup times to around two minutes and improve scalability.                                            |
|  12 | Operational challenges include managing Kubernetes upgrades, handling Cgroups version mismatches on Oracle nodes, and resolving communication timeouts between containers and VMs.              |
|  13 | Monitoring is implemented via Grafana dashboards and Slack alerts to track runner capacity, synchronization status, and system health.                                                          |
|  14 | The migration successfully reduced costs from approximately one thousand dollars per day to around one thousand dollars per month.                                                              |
|  15 | The infrastructure supports various runner shapes, including x86, ARM, and recently added GPU shapes for projects like Kubeflow.                                                                |
|  16 | All configuration and automation code is maintained in the open-source CNCF automation repository, allowing projects to contribute fixes and improvements.                                      |
|  17 | Onboarding new projects to the self-hosted runners requires only changing the runner name in GitHub Actions workflows and updating organization settings.                                       |
|  18 | The solution remains cloud-agnostic to facilitate future migrations away from Oracle Cloud if donations or requirements change.                                                                 |

# Video

[![Video thumbnail](https://img.youtube.com/vi/1Nm9TPCwqS8/hqdefault.jpg)](https://www.youtube.com/watch?v=1Nm9TPCwqS8)

[Watch on YouTube](https://www.youtube.com/watch?v=1Nm9TPCwqS8)
