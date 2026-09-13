---
type: Video Note
title: "Bringing Cloud Native PaaS To Space: Onboard Edge Computing f... Adele Karam Hankache & Sergiu Weisz"
description: "The presentation introduces the Orchid project, a European initiative aimed at advancing edge computing on satellites by enabling onboard data processing and orchestration of AI applications. Traditionally, Earth observation satellites proc..."
resource: https://www.youtube.com/watch?v=QbEpoZuWT9I
tags: ["kubecon-cloudnativecon-europe-2026", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

The presentation introduces the Orchid project, a European initiative aimed at advancing edge computing on satellites by enabling onboard data processing and orchestration of AI applications.
Traditionally, Earth observation satellites process and transmit data sequentially, constrained by limited downlink bandwidth and tightly coupled hardware-software systems, which restrict software updates and efficient data use.
Orchid proposes a distributed, hardware-agnostic platform using lightweight Kubernetes (K3S), unikernels (via MirageOS and Unicraft), and custom tools to orchestrate and accelerate AI workflows directly on satellites, significantly reducing the need to transmit large raw datasets to the ground.
The platform includes components for mission planning, storage management, workflow orchestration, and security, allowing satellites to process data in real time and transmit only valuable results, such as detected ships or fire alerts, thus improving efficiency and enabling new use cases.
The project is currently a demonstrator targeting low Earth orbit satellites, with plans to open source the software and expand to multisatellite constellations, ultimately aiming to transform satellites into flexible, service-oriented computing platforms.
# Main Points

|   # | Main point                                                                                                                                                                         |
| --: | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Presentation focuses on bringing software platforms and edge computing to satellites.                                                                                              |
|   2 | Current Earth observation satellites process data sequentially and are limited by hardware-software coupling and downlink bandwidth.                                               |
|   3 | Large volumes of high-resolution data cannot always be downloaded, leading to data loss or reduced value.                                                                          |
|   4 | New space paradigm includes more commercial actors, CubeSats, new business models, and technical enablers like cloud, virtualization, 5G, AI, and advanced hardware (GPUs, FPGAs). |
|   5 | Shift proposed: process data directly onboard using orchestrators to schedule AI applications, reducing unnecessary data transmission.                                             |
|   6 | Example use cases: onboard cloud detection (delete cloudy images), ship detection (transmit only coordinates), fire detection, maritime surveillance.                              |
|   7 | European project "Orchid" involves five partners; aims to develop an onboard orchestrator for heterogeneous hardware.                                                              |
|   8 | Ground tools include SDK for packaging/simulating applications and a management framework for data/metrics transfer.                                                               |
|   9 | Space Edge Platform as a Service: structured mission plans enhanced with AI workflows per acquisition.                                                                             |
|  10 | Platform supports multiple hardware types (Nvidia GPU, FPGA, ARM CPU, MPPA) and is hardware-agnostic.                                                                              |
|  11 | Uses CNCF solutions and custom services for satellite missions.                                                                                                                    |
|  12 | Unikernels (MirageOS, Unicraft) chosen for small size, performance, and security; run inside Kubernetes via UR runtime.                                                            |
|  13 | Custom project "ukaxel" enables unikernels to use hardware accelerators via TCP interface.                                                                                         |
|  14 | K3S selected as lightweight Kubernetes distribution.                                                                                                                               |
|  15 | Key components: monitor manager, storage manager (with distributed POSIX file system and Zot registry), mission manager (turns plans into Argo workflows), security manager.       |
|  16 | Workflow: mission plan triggers acquisition, data stored, mission planner schedules workflow, processing occurs onboard, results transmitted.                                      |
|  17 | Monitoring and metrics aggregated and sent to ground stations.                                                                                                                     |
|  18 | Project aims for open-source                                                                                                                                                       |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=QbEpoZuWT9I)