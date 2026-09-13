---
type: Video Note
title: "KubeVirt's Evolution: Governance, Features, and Community Growth - Sreeja Varnam & Luboslav Pivarc"
description: "Lo Slapage and Sria present on the evolution and management of the KubeVirt project, which integrates virtual machines into the Kubernetes ecosystem. They describe KubeVirt’s growth from a small, chaotic project to a mature community, empha..."
resource: https://www.youtube.com/watch?v=goCjV2xJDnk
tags: ["kubecon-cloudnativecon-europe-2026", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

Lo Slapage and Sria present on the evolution and management of the KubeVirt project, which integrates virtual machines into the Kubernetes ecosystem.
They describe KubeVirt’s growth from a small, chaotic project to a mature community, emphasizing the adoption of structured processes inspired by Kubernetes, such as the use of Virtualization Enhancement Proposals (VEPs) to guide development, prioritize features, and maintain transparency and predictability.
The talk highlights the VM Pool feature, which enables scalable, declarative management of groups of similar virtual machines, offering benefits like automated scaling, controlled updates, and auto-healing, all managed through a clear API and update strategies.
The presenters explain that the structured proposal and review process has improved collaboration, early feedback, and feature stability, making project management more manageable despite the added administrative tasks.
They also discuss community practices, such as open meetings and distributing responsibilities among special interest groups, to ensure sustainable project growth and effective feature delivery.
# Main Points

|   # | Main point                                                                                                                         |
| --: | ---------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Lo Slapage and Sria presented on behalf of the KubeVirt project at CubeCon.                                                        |
|   2 | KubeVirt brings virtual machines into the Kubernetes ecosystem, following a similar architecture.                                  |
|   3 | The project is about 8 years old and is in the process of graduating in the CNCF.                                                  |
|   4 | KubeVirt has evolved from a small, chaotic project to a mature community with structured processes.                                |
|   5 | The project adopted a roadmap and increased the number of maintainers, following Kubernetes processes closely.                     |
|   6 | KubeVirt uses "Virtualization Enhancement Proposals" (VEPs) to collect, review, and prioritize new features and designs.           |
|   7 | VEPs are tracked via issues and PRs in the repository for transparency and progress tracking.                                      |
|   8 | Ownership of VEPs is managed by one or more Special Interest Groups (SIGs).                                                        |
|   9 | The collection of VEPs forms the project roadmap, aligning with Kubernetes’ three-releases-per-year schedule.                      |
|  10 | The release cycle includes feature selection, enhancement freeze, development, code freeze, stabilization, and release candidates. |
|  11 | Community meetings and open-door VEP meetings are held for collaboration and feedback.                                             |
|  12 | Key goals achieved: transparency, predictability, and planning.                                                                    |
|  13 | Notable recent changes include DR integration from Nvidia and Microsoft’s multihypervisor framework.                               |
|  14 | AI is being explored to assist in the process.                                                                                     |
|  15 | VM Pool is a new feature that manages groups of similar VMs natively in Kubernetes.                                                |
|  16 | VM Pool combines concepts from jobs, replica sets, and stateful sets for scalable, declarative VM management.                      |
|  17 | Features include scaling, batch updates, auto-healing, state preservation, and update/scaling strategies.                          |
|  18 | VM Pool simplifies management for platform teams by allowing declarative control over VM fleets.                                   |
|  19 | The VEP process enabled structured, predictable, and community-aligned feature development.                                        |
|  20 | VM health is monitored via readiness/liveness probes and a guest agent, similar to VMware tools.                                   |
|  21 | Project management is handled by maintainers and SIGs, with processes evol                                                         |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=goCjV2xJDnk)