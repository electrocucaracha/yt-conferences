---
type: Video Note
title: "What's New With Kubectl and Kustomize … and How You... Marly S, Yugo K, Eddie Z, Maciej S & Arda G"
description: "The video features a panel of Kubernetes SIG CLI maintainers discussing recent updates and ongoing work on tools like kubectl, kustomize, and the new QRC configuration system. They explain the SIG CLI’s role in managing Kubernetes CLI tooli..."
resource: https://www.youtube.com/watch?v=mfcdIa0NtCo
tags: ["kubecon-cloudnativecon-europe-2026", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

The video features a panel of Kubernetes SIG CLI maintainers discussing recent updates and ongoing work on tools like kubectl, kustomize, and the new QRC configuration system.
They explain the SIG CLI’s role in managing Kubernetes CLI tooling and invite community participation in their weekly meetings.
Key updates include bug fixes and new features in kustomize, enhancements to kubectl such as interactive delete defaults and QRC for customizing CLI behavior, and the migration of exec and port-forward commands to websockets.
The team highlights recent deprecations, the addition of multiple condition support in kubectl wait, and ongoing efforts to improve usability and security, such as CRI-native copy and audit headers for usage telemetry.
They encourage feedback and contributions, discuss challenges around backward compatibility, and address audience questions on topics like server-side apply, multiple kubeconfig support, and the future of kustomize features.
The session closes with a lighthearted discussion on the pronunciation of "kubectl" and an open invitation for further community involvement.
# Main Points

|   # | Main point                                                                                                                                  |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | SIG CLI owns Kubernetes CLI tooling, including kubectl and kustomize; meetings are Wednesdays 9am PT/6pm CET.                               |
|   2 | Kustomize latest version is B581; fixed regression bug in namespace propagation for child customizations (see issues #6044, #6058).         |
|   3 | Option added to retain previous namespace propagation behavior due to user reliance.                                                        |
|   4 | Helm chart name not set for all resources remains a problem.                                                                                |
|   5 | Backwards compatibility is a top priority for kubectl changes.                                                                              |
|   6 | QRC (kubectl resource config) introduced for customizing kubectl defaults (e.g., interactive delete, server-side apply); currently in beta. |
|   7 | QRC allows defining aliases, tweaking defaults, and credential plugin allow-lists; new qrc command added for easier management.             |
|   8 | Cayaml, a YAML/JSON hybrid, introduced to address YAML limitations; likely to be promoted to stable.                                        |
|   9 | Switched exec/port-forward protocol from SPDY to websockets (beta, planned GA in v1.37).                                                    |
|  10 | Deprecated: kubectl debug legacy profile, QRC preferences field, KUI, and KRM functions.                                                    |
|  11 | kubectl wait now supports multiple conditions (since v1.36); create/delete conditions handled specially.                                    |
|  12 | Interactive delete recommended via QRC to prevent accidental mass deletions.                                                                |
|  13 | Multiple kubeconfig support and a new server-side apply command are being considered; feedback requested.                                   |
|  14 | Considering improvements to JSONPath support and CRI-native kubectl cp to replace tar dependency.                                           |
|  15 | Audit headers added for CLI usage telemetry; only flags, not values, are logged to avoid secrets exposure.                                  |
|  16 | Prune in apply is still problematic; maintainers committed to working on a solution.                                                        |
|  17 | Server-side apply as a new command is planned to avoid breaking compatibility; naming suggestions welcome.                                  |
|  18 | Plugins are encouraged for new kubectl features; successful plugins may be upstreamed.                                                      |
|  19 | No plans to support arbitrary subresources in kubectl beyond scale and status due to API limitations.                                       |
|  20 | Community encouraged to join SIG CLI meetings and contribute.                                                                               |
|  21 | All pronunciations of ku                                                                                                                    |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=mfcdIa0NtCo)