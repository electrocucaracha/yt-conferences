---
type: Video Note
title: "Kubernetes SIG-Windows Updates - Mark Rossetti, Microsoft & Jose Valdes, Red Hat"
description: "The Kubernetes SIG Windows project maintainer talk, led by Mark Rosetti from Microsoft and J.R. from Red Hat, provided an overview of the evolution and current state of Windows node support in Kubernetes. The presenters discussed recent enh..."
resource: https://www.youtube.com/watch?v=08q8UsJV_3Y
tags: ["kubecon-cloudnativecon-north-america-2025", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

The Kubernetes SIG Windows project maintainer talk, led by Mark Rosetti from Microsoft and J.R.
from Red Hat, provided an overview of the evolution and current state of Windows node support in Kubernetes.
The presenters discussed recent enhancements, including improvements to kube-proxy, updated documentation for Windows networking, and the progression of graceful node shutdown from alpha to beta, which now allows Windows nodes to handle shutdown signals more reliably.
They highlighted the addition of stable CI coverage for Windows Server 2025, the introduction of container image portability across Windows Server versions, and the implementation of the node log query feature for consistent log retrieval across Windows and Linux nodes.
The team emphasized the need for more community contributions, particularly to achieve feature parity with Linux, and encouraged feedback and participation to help prioritize future work and address ongoing challenges such as stability and adapting new features for Windows workloads.
# Main Points

|   # | Main point                                                                                                                                         |
| --: | -------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Introduction of presenters: Mark Rosetti (Microsoft) and J.R. (Red Hat/OpenShift), both maintainers for Kubernetes SIG Windows.                    |
|   2 | Overview of Windows node evolution in Kubernetes and recent features.                                                                              |
|   3 | Windows node support in Kubernetes became stable in version 1.14 (2019).                                                                           |
|   4 | Windows nodes reuse the Linux control plane; major cloud providers (Azure, AWS, GKE) offer mechanisms to add Windows nodes.                        |
|   5 | OpenShift and other solutions (Rancher, etc.) provide alternative ways to run Windows nodes.                                                       |
|   6 | CNI integrations for Windows include Calico, OVN-Kubernetes, and others.                                                                           |
|   7 | Observability for Windows nodes is supported via Prometheus, Datadog, OpenTelemetry, etc.                                                          |
|   8 | Recent work focused on kube-proxy enhancements and documentation overhaul for Windows networking.                                                  |
|   9 | Graceful node shutdown for Windows progressed from alpha to beta; now recommends running kubelet as a Windows service with Qlogrunner for logging. |
|  10 | Improved CI signal for Windows: Windows node e2e tests now run in Kubernetes CI, including stable coverage for Windows Server 2025.                |
|  11 | Windows Server 2025 introduces container image portability: N-1 version images can run on newer hosts, easing upgrades.                            |
|  12 | Roadmap includes flushing alpha/beta enhancements and supporting in-place pod resize for Windows (add CPU/memory without rescheduling).            |
|  13 | Demo of graceful node shutdown: non-critical pods terminated before critical ones; node returns to ready state after reboot.                       |
|  14 | Node log query feature (beta in 1.30): enables querying logs from Windows and Linux nodes via kubelet API, behind a feature gate.                  |
|  15 | Kubectl plugin "node-logs" simplifies log querying across nodes.                                                                                   |
|  16 | Community contributions highlighted, including resolving kubelet panic on certain Intel processors.                                                |
|  17 | Leadership updates: new tech lead Yan Leang; call for contributors, especially for Windows implementations of SIG Node enhancements.               |
|  18 | Host process containers enable privileged workloads on Windows nodes.                                                                              |
|  19 | Request for feedback and use cases from the community;                                                                                             |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=08q8UsJV_3Y)