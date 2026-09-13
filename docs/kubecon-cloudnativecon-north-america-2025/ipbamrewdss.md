---
type: Video Note
title: "Container Runtime Customization at Netflix: A Case Study With NRI and OCI Hooks - Erikson Tung"
description: "In this talk, Erikson from Netflix's compute runtime team discusses the company's migration of its Titus container platform from a custom, monolithic runtime to a modern, industry-standard Kubernetes-based stack using stock kubelets and con..."
resource: https://www.youtube.com/watch?v=IPbamReWdss
tags: ["kubecon-cloudnativecon-north-america-2025", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

In this talk, Erikson from Netflix's compute runtime team discusses the company's migration of its Titus container platform from a custom, monolithic runtime to a modern, industry-standard Kubernetes-based stack using stock kubelets and containerd.
He outlines the challenges of preserving years of bespoke runtime logic and unique workload requirements—such as systemd support, multi-tenancy, and CPU isolation—while ensuring zero disruption for users.
The team adopted a "lift and shift" strategy, relocating existing functionality to runtime extension points like Node Resource Interface (NRI) plugins and OCI hooks, which allowed for dynamic container customizations at runtime and reliable cleanup operations.
This approach enabled Netflix to transparently modernize its infrastructure, improve observability, and reduce operational complexity, while also contributing upstream improvements.
Erikson shares key learnings about balancing pragmatism with platform purity, the importance of observability, and the value of incremental migration, concluding with a Q&A addressing technical details and open sourcing.
# Main Points

|   # | Main point                                                                                                                                                                                           |
| --: | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Erikson from Netflix's compute runtime team presented on container runtime customizations at Netflix.                                                                                                |
|   2 | Focus: Migrating Netflix's Titus platform from a custom runtime to a standard Kubernetes data plane using stock kubelets and containerd.                                                             |
|   3 | Titus is Netflix’s container platform, running hundreds of thousands of pods globally for diverse workloads, including streaming, batch, data pipelines, and machine learning.                       |
|   4 | Original Titus implementation was built on Mesos, later adopted Kubernetes control plane but retained a custom data plane using virtual kubelet and a monolithic runtime layer (Titus executor).     |
|   5 | Challenges: Years of custom runtime logic, VM-like environment expectations (systemd, multi-tenancy), CPU isolation, and need for zero user disruption during migration.                             |
|   6 | Migration strategy: Lift-and-shift approach, relocating custom code to runtime extension points (NRI plugins, OCI hooks) to minimize risk, validate architecture, and reduce operational complexity. |
|   7 | Runtime extensions used:                                                                                                                                                                             |
|   8 | Admission webhooks: Policy enforcement, pod annotation mutation.                                                                                                                                     |
|   9 | CNI plugin: Custom container networking and IP assignment.                                                                                                                                           |
|  10 | NRI plugins: Modify OCI runtime spec, coordinate startup, manage CPU isolation, and platform service lifecycle.                                                                                      |
|  11 | OCI hooks: Cleanup and direct container modifications at lifecycle events.                                                                                                                           |
|  12 | Run wrapper: Temporary layer for unsupported OCI spec adjustments.                                                                                                                                   |
|  13 | Use cases:                                                                                                                                                                                           |
|  14 | Systemd support in containers via OCI spec modifications.                                                                                                                                            |
|  15 | CPU isolation with node-level decisions using NRI and a local service (Titus isolate).                                                                                                               |
|  16 | Per-pod platform services managed as systemd instances, coordinated by NRI and OCI hooks.                                                                                                            |
|  17 | Orchestration pattern: Tini as init, NRI for setup, OCI hooks for teardown.                                                                                                                          |
|  18 | Guidelines: Use webhooks for pre-scheduling changes, NRI for runtime coordination, OCI hooks for stateless lifecycle operations.                                                                     |
|  19 | Migration results: Near 100% migration, zero major incidents, improved observability, easier maintenance, and access to                                                                              |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=IPbamReWdss)