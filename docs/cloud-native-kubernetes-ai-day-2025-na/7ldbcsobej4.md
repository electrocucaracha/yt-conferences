---
type: Video Note
title: "Sponsored Keynote: Kubernetes Challenges at Lambda - Andrew Godwin, Lambda Labs"
description: "The speaker, Lambda’s lead software architect, provides an overview of the company’s approach to running GPU clouds and managing Kubernetes workloads. Lambda is an emerging hyperscaler that owns its hardware and infrastructure, running both..."
resource: https://www.youtube.com/watch?v=7ldbcSoBEJ4
tags: ["cloud-native-kubernetes-ai-day-2025-na", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

The speaker, Lambda’s lead software architect, provides an overview of the company’s approach to running GPU clouds and managing Kubernetes workloads.
Lambda is an emerging hyperscaler that owns its hardware and infrastructure, running both a platform Kubernetes layer for cloud services and a managed Kubernetes offering for customers.
Unique challenges arise from the high failure rates of GPUs and the physical constraints of server placement, making machine failures a routine issue that requires in-place remediation and limits the use of spare machines.
The team has implemented solutions such as continuous validation, automated remediation via Kubernetes operators, and a custom bare metal cluster API provider, while also exploring predictive failure analysis to proactively manage hardware issues.
The speaker concludes by highlighting the ongoing complexity of GPU workloads compared to CPU workloads and invites interested individuals to learn more about opportunities at Lambda.
# Main Points

|   # | Main point                                                                                                                 |
| --: | -------------------------------------------------------------------------------------------------------------------------- |
|   1 | Lambda is an emerging hyperscaler owning its own hardware and physical space.                                              |
|   2 | The company builds its infrastructure from the power level upwards.                                                        |
|   3 | Lambda runs two layers of Kubernetes: platform Kubernetes on physical hardware, and managed Kubernetes for customers.      |
|   4 | Platform Kubernetes manages cloud components like services and databases.                                                  |
|   5 | The cloud provides virtual machines or bare metal as a service.                                                            |
|   6 | Managed Kubernetes offers an all-in-one solution, handling cluster setup and validation for customers.                     |
|   7 | Managed Kubernetes can run the cloud for large customers or directly on bare metal.                                        |
|   8 | GPUs have high failure rates, leading to multiple failures daily in large clusters.                                        |
|   9 | Machine failure is a normal occurrence; servers have fixed physical locations due to sensitive wiring.                     |
|  10 | Replacing failed machines is challenging; replacements must be in the same rack and slot to avoid performance degradation. |
|  11 | There are no spare machines in large clusters as all switch ports are used.                                                |
|  12 | Remediation includes automated reboots via a Kubernetes operator and, if needed, full power drains of chassis.             |
|  13 | Power Distribution Units (PDUs) are integrated into the Kubernetes cluster for power cycling.                              |
|  14 | Automatic node cordoning and health monitoring are in place, but long-running jobs can delay remediation.                  |
|  15 | Continuous validation runs on clusters to ensure all networks are functioning.                                             |
|  16 | Fully automatic remediation process: cordon node, drain, reboot, and power drain if necessary.                             |
|  17 | Lambda developed its own bare metal cluster API provider for automated cluster provisioning.                               |
|  18 | Predictive failure analysis is being explored using metrics like thermals and power draw.                                  |
|  19 | Efforts are underway to share code between the two Kubernetes layers.                                                      |
|  20 | GPU workloads present unique, unsolved challenges compared to CPU workloads.                                               |
|  21 | Lambda is hiring for multiple positions.                                                                                   |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=7ldbcSoBEJ4)