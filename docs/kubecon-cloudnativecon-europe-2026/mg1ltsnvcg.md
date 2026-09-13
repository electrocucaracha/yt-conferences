---
layout: default
title:
  What's Coming Next in Containerd 2.3? - Mike Brown, IBM & Krisztian Litkey,
  Intel
nav_order: 397
parent: Kubecon Cloudnativecon Europe 2026
type: Video Note
description:
  The video features core maintainers and contributors of containerd discussing
  its development, extensibility, and integration with other projects like Kubernetes,
  Docker, and Rancher. They highlight containerd’s unopinionated design, its wi...
resource: https://www.youtube.com/watch?v=_mg1LtSNVCg
tags:
  - kubecon-cloudnativecon-europe-2026
  - video
  - learning
status: stable
generated:
  by: process:yt-conferences-okf
  at: 2026-09-12 00:00:00+00:00
---

# Summary

The video features core maintainers and contributors of containerd discussing its development, extensibility, and integration with other projects like Kubernetes, Docker, and Rancher.
They highlight containerd’s unopinionated design, its widespread adoption in cloud environments, and recent advancements such as support for new snapshotters, runtimes, and the Container Device Interface (CDI).
A significant focus is on the Node Resource Interface (NRI), an extension mechanism for CRI-compatible runtimes like containerd and CRI-O, which allows administrators to plug in custom logic for managing pod and container lifecycle events without recompiling the runtime.
NRI plugins can adjust container attributes, manage resources, and are validated through pluggable validators to ensure security and compliance.
The maintainers also discuss the move to a Kubernetes-like release cadence, the introduction of long-term support (LTS) releases, ongoing work toward NRI’s API stability, enhanced observability, and security features, as well as the differences between NRI plugins and Kubernetes mutating webhooks in terms of flexibility and control.

# Main Points

|   # | Main point                                                                                                                                                                               |
| --: | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | containerd is a CNCF graduated project since 2019 with many public repositories and extension points.                                                                                    |
|   2 | The team collaborates with Kubernetes, Docker, Rancher, and other ecosystem partners.                                                                                                    |
|   3 | containerd aims to be unopinionated, allowing various clients, runtimes, and extensions.                                                                                                 |
|   4 | Remote snapshotters and new runtimes like Wom and CDI have been added.                                                                                                                   |
|   5 | CDI (Container Device Interface) is now enabled by default in containerd 1.7+ and supported by DRA controllers.                                                                          |
|   6 | NRI (Node Resource Interface) is a plugin model for CRI-compatible runtimes (containerd, CRI-O) to manage pod/container resources and lifecycle events.                                  |
|   7 | NRI plugins are external binaries communicating via TTRPC over Unix domain sockets, allowing dynamic, portable, and pluggable logic.                                                     |
|   8 | NRI supports hooking into pod/container lifecycle events (create, start, update, stop, remove) and adjusting container attributes (annotations, mounts, devices, env vars, resources).   |
|   9 | Recent NRI enhancements include controls for Linux scheduling, IO prioritization, namespaces, seccomp policy, rlimits, network interface injection, and richer device injection via CDI. |
|  10 | Pluggable validation allows validator plugins to accept/reject changes from other plugins, enhancing security and administrative control.                                                |
|  11 | Support for required plugins and tolerations helps with cluster bootstrapping and plugin management.                                                                                     |
|  12 | New plugin types include built-in and WASM-based plugins for sandboxing and performance.                                                                                                 |
|  13 | NRI is working towards a stable 1.0 release with binary/source compatibility, improved metrics, audit logging, and authenticated plugins for finer-grained validation.                   |
|  14 | NRI provides more flexibility and control than mutating webhooks or CRI proxies, especially for resource management and runtime-level adjustments.                                       |
|  15 | Validators and restrictors are being developed to ensure plugins do not perform unauthorized or unsafe actions, with collaboration from the Kubernetes kubelet team.                     |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=_mg1LtSNVCg)
