---
type: Video Note
title: "Project Lightning Talk: What's Exciting Now In Bootc, And What's Next? - Colin Walters, Maintainer"
description: "Colin Walters introduces updates on two CNCF projects, Bootsie and ComposifS, emphasizing the importance of free and open source software for maintaining control over technology. Bootsie, a CNCF sandbox project since 2024, enables deploying..."
resource: https://www.youtube.com/watch?v=txFg5kPwQvY
tags: ["kubecon-cloudnativecon-europe-2026", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

Colin Walters introduces updates on two CNCF projects, Bootsie and ComposifS, emphasizing the importance of free and open source software for maintaining control over technology.
Bootsie, a CNCF sandbox project since 2024, enables deploying Linux-based OCI images directly to bare metal or virtual machines without an intermediate container runtime, offering transactional updates, strong integration with systemd and podman, and tools for converting existing systems.
New features include systemd soft reboots for efficient updates, a system reinstall tool, and integration with other CNCF projects like Kurd.
Walters also presents BCVK (Bootsie Virtualization Kit), which allows rapid iteration by running containers as ephemeral VMs, streamlining development cycles.
ComposifS aims to provide a versioned, immutable file system with on-disk integrity by separating metadata and data planes, supporting fsverity, and offering DMverity-style integrity; a new Rust implementation is in progress.
Both projects focus on end-to-end integrity from system power-on, with plans to extend these guarantees to generic OCI images, and Walters invites further community engagement.
# Main Points

|   # | Main point                                                                                                                                           |
| --: | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Colin Walters presented updates on Bootsie and ComposifS, two CNCF projects.                                                                         |
|   2 | Bootsie has been in CNCF sandbox since Salt Lake 2024.                                                                                               |
|   3 | Bootsie uses OCI images containing a Linux kernel, bootloader, and other components, deployable directly to bare metal or VMs.                       |
|   4 | No intermediate container runtime is required; container annotations in OCI images do not apply.                                                     |
|   5 | Bootsie is an image-based update system with transactional updates and strong integration with security tools, systemd, and podman.                  |
|   6 | Supports direct installation of containers to disk.                                                                                                  |
|   7 | New feature: integration with systemd soft reboots, allowing updates without full hardware or kernel reinitialization.                               |
|   8 | Introduced "system reinstall bootsie" tool to convert existing systems to Bootsie.                                                                   |
|   9 | Integrates with other CNCF projects like Kurd for orchestrating updates in Kubernetes clusters.                                                      |
|  10 | New component: BCVK (Bootsie Virtualization Kit) enables running containers as ephemeral VMs with kernel, initramfs, and systemd from the container. |
|  11 | BCVK mounts the container root via VirtioFS for fast iteration and can streamline integration with libvirt.                                          |
|  12 | Suggestion to integrate this approach by default in KubeVirt.                                                                                        |
|  13 | ComposifS aims to be a versioned, immutable file system storage system with on-disk integrity.                                                       |
|  14 | Architecture splits metadata plane (small metadata-only filesystem with fsverity) from data plane (plain files/objects with fsverity).               |
|  15 | Provides DM-Verity style integrity and data sharing on disk and in memory.                                                                           |
|  16 | Initial C version is stable; next-generation Rust version is being stabilized.                                                                       |
|  17 | Bootsie provides integrity from system power-on through secure boot, integrating with systemd's UKI project.                                         |
|  18 | Plans to extend integrity features to generic OCI images for broader application support.                                                            |
|  19 | Invitation to discuss or provide feedback at the community pavilion.                                                                                 |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=txFg5kPwQvY)