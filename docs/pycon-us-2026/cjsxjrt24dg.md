---
layout: default
title: "Securing and Scaling Jupyter at Bloomberg: How we run Notebooks on Kubernetes (Sponsor: Bloomberg)"
nav_order: 99
parent: PyCon US 2026
type: Video Note
description: "Ruturaj Singh and Yifan Jiang from Bloomberg’s AI training team present a detailed overview of their cloud-native Jupyter platform built on Kubernetes, designed to address infrastructure challenges..."
resource: "https://www.youtube.com/watch?v=CJsxJRt24dg"
youtube_stats:
  view_count: 621
  like_count: 2
  channel_subscriber_count: 34500
tags:
  - pycon-us-2026
  - video
  - learning
status: stable
generated:
  by: process:yt-summarizer-okf
  at: 2026-11-20T08:08:06+00:00
---

# Summary

Ruturaj Singh and Yifan Jiang from Bloomberg’s AI training team present a detailed overview of their cloud-native Jupyter platform built on Kubernetes, designed to address infrastructure challenges such as resource contention, security, and scalability in multi-tenant environments.
The platform leverages open-source technologies like Istio, Calico, and Open Policy Agent to enforce strict ingress and egress controls, ensuring that only authenticated and authorized users can access notebooks and that outbound traffic is restricted to approved services.
To enhance developer experience and reliability, the team decoupled the Jupyter server from the IPython kernel into separate pods, allowing for independent scaling and preventing data loss during kernel crashes, while also integrating SPIFFE/SPIRE for workload identity and Claude Code for AI-assisted coding via a secure internal gateway.
The presentation further highlights their robust monitoring strategy, which includes defining Service Level Objectives (SLOs) for launch times and success rates, using Argo Workflows for end-to-end validation, and implementing a workload runtime monitor to detect issues like zombie processes and track popular package usage.
Through these architectural decisions and operational practices, Bloomberg ensures a secure, flexible, and highly reliable data science platform that supports complex machine learning workloads across their on-premises infrastructure.

# Main Points

|   # | Main point |
| --: | ---------- |
|   1 | Bloomberg built a cloud-native Jupyter platform on Kubernetes to solve infrastructure challenges like resource contention, security, and compatibility issues arising from multi-team usage of remote clusters. |
|   2 | The data science platform is a multi-cluster, multi-tenant system using open-source tools including Jupyter, Kubeflow, Ray, KServe, and Karmada for orchestration. |
|   3 | Kubernetes concepts such as nodes, pods, services, and namespaces provide the foundational building blocks for deploying, scaling, and isolating Jupyter workloads. |
|   4 | A custom resource definition (CRD) and controller manage the lifecycle of Jupyter notebooks, allowing declarative configuration of hardware, packages, and identities. |
|   5 | Authentication is handled via Istio service mesh and Envoy filters that validate OAuth tokens against Bloomberg single sign-on, while authorization uses Open Policy Agent (OPA) to enforce access policies. |
|   6 | Egress traffic is restricted using Calico global network policies and network sets to ensure notebooks can only connect to approved external services like object storage. |
|   7 | Developer experience was improved by separating the Jupyter server and IPython kernel into distinct pods, allowing independent scaling and preventing data loss when kernels crash due to memory issues. |
|   8 | A shared persistent volume is mounted to both server and kernel pods to enable file sharing and consistent Python virtual environments across the separated architecture. |
|   9 | SPIFFE/SPIRE integration provides workload identity attestation and secure credential injection, supporting zero-trust authentication and mutual TLS between services. |
|  10 | Claude Code is integrated into Jupyter notebooks via an init container and internal AI gateway, enabling AI-assisted coding and access to pre-baked agents for training submission and notebook awareness. |
|  11 | Platform reliability is maintained through Argo Workflows for end-to-end testing, which validates notebook launch, kernel execution, GPU connectivity, and other core functionalities. |
|  12 | A workload runtime monitor detects zombie processes and tracks pip package usage to identify resource leaks and popular tools, aiding in capacity planning and troubleshooting. |
|  13 | Service Level Objectives (SLOs) and Service Level Agreements (SLAs) are defined for metrics like pod initialization time and launch success rate, with dashboards tracking burn rates and error budgets. |
|  14 | Continuous triaging involves correlating alerts with SLO metrics to identify root causes, such as pre-baking PyTorch into images to reduce launch times or fixing GPU driver issues. |
|  15 | The platform supports on-premises infrastructure, where GPU failures may stem from driver errors, overheating, or hardware issues, requiring proactive detection and SRE intervention. |
|  16 | Security concerns regarding AI-assisted coding are mitigated by routing all traffic through the secure, open-source Envoy AI gateway built by Bloomberg. |

# Video

[![Video thumbnail](https://img.youtube.com/vi/CJsxJRt24dg/hqdefault.jpg)](https://www.youtube.com/watch?v=CJsxJRt24dg)

[Watch on YouTube](https://www.youtube.com/watch?v=CJsxJRt24dg)
