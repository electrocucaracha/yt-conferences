---
layout: default
title: Towards Secure Container Infrastructure on RISC V  the Development from rust vmm to Kata Containers
nav_order: 56
parent: OpenInfra Summit Europe 2025
type: Video Note
description: "Roing from the Institute of Software, Chinese Academy of Sciences, presented a roadmap for expanding the RISC-V software ecosystem, specifically focusing on secure container infrastructure."
resource: "https://www.youtube.com/watch?v=U1jOKydoGGY"
youtube_stats:
  view_count: 142
  like_count: 1
  channel_subscriber_count: 46800
tags:
  - openinfra-summit-europe-2025
  - video
  - learning
status: stable
generated:
  by: process:yt-summarizer-okf
  at: 2026-11-22T23:38:50+00:00
---

# Summary

Roing from the Institute of Software, Chinese Academy of Sciences, presented a roadmap for expanding the RISC-V software ecosystem, specifically focusing on secure container infrastructure.
The talk detailed the foundational work done in the Rust VMM community to make RISC-V the third officially supported architecture, overcoming challenges such as the lack of hardware with virtualization extensions by implementing CI workflows using emulated RISC-V virtual machines on x86 hosts.
Building on this, the team successfully enabled Cloud Hypervisor to boot Linux on RISC-V, addressing architecture-specific issues in memory management and interrupt handling.
This progress allowed for the integration of RISC-V support into the Kata Containers project, where the team established build and test pipelines using available RISC-V hardware to validate the Go and Rust runtimes.
A live demonstration showed a Kata Container successfully booting and running on an emulated RISC-V machine using QEMU, confirming the functionality of the full software stack.
The speaker concluded by outlining future goals, including supporting additional hypervisors like Dragonball and LibKVM, and aiming to officially announce RISC-V support for Kata Containers by the end of next year.

# Main Points

|   # | Main point                                                                                                                                                                                     |
| --: | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | The speaker from the Institute of Software, Chinese Academy of Sciences, presents work on expanding the RISC-V software ecosystem for secure container infrastructure.                         |
|   2 | RISC-V is considered essential for achieving sovereignty in cloud infrastructure and hardware, making it a critical foundation for Kata Containers.                                            |
|   3 | The project roadmap involves supporting RISC-V at the OS level using distributions like OpenEuler, Fedora, and Debian, followed by virtualization libraries and hypervisors.                   |
|   4 | Key hypervisors targeted for RISC-V support include Cloud Hypervisor, QEMU, Dragon Ball, and Stratovirt, with Cloud Hypervisor being the primary focus for initial integration.                |
|   5 | The Rust VMM community previously supported only x86 and ARM; RISC-V is now the third officially supported architecture following contributions to crates like KVM bindings and Linux loaders. |
|   6 | Due to the lack of RISC-V hardware with virtualization extensions (H extension), CI workflows were established using QEMU-emulated RISC-V virtual machines on x86 hosts.                       |
|   7 | Cloud Hypervisor was successfully adapted for RISC-V by addressing architecture-specific code, memory management, and interrupt handling, enabling direct booting of Linux guests.             |
|   8 | Testing challenges due to hardware scarcity were mitigated by providing x86 machines to run emulated RISC-V environments for CI jobs in the Cloud Hypervisor community.                        |
|   9 | Current efforts focus on closing feature gaps in Cloud Hypervisor, including enabling vTPM, PMU, UEFI, ACPI, and device hot-plugging for RISC-V.                                               |
|  10 | Kata Containers integration is progressing with the Go runtime using QEMU and the Rust runtime using Cloud Hypervisor, both verified on RISC-V emulated environments.                          |
|  11 | CI for Kata Containers currently performs build tests on RISC-V hardware, such as the SG2042 board with 64 cores, to ensure reliability without full integration test suites.                  |
|  12 | A live demonstration showed a Kata Container booting on an emulated RISC-V machine using QEMU, confirming the isolation and distinct instruction set of the guest environment.                 |
|  13 | The team aims to secure reliable RISC-V hardware with proper interrupt controllers to stabilize CI and expand testing coverage.                                                                |
|  14 | The goal is to officially announce RISC-V support for Kata Containers by the end of the next year, pending hardware availability and feature completion.                                       |

# Video

[![Video thumbnail](https://img.youtube.com/vi/U1jOKydoGGY/hqdefault.jpg)](https://www.youtube.com/watch?v=U1jOKydoGGY)

[Watch on YouTube](https://www.youtube.com/watch?v=U1jOKydoGGY)
