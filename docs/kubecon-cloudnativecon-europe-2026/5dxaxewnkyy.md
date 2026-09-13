---
type: Video Note
title: "Detect, Decide, Defend: Building Cloud Native Security That Fights Back - Matthias Bertschy, ARMO"
description: "In this talk, Matias, a Kubernetes security expert and CNCF project maintainer, addresses the challenges of detecting and responding to security incidents in Kubernetes environments, where multiple security tools generate isolated alerts th..."
resource: https://www.youtube.com/watch?v=5DxaxeWNkYY
tags: ["kubecon-cloudnativecon-europe-2026", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

In this talk, Matias, a Kubernetes security expert and CNCF project maintainer, addresses the challenges of detecting and responding to security incidents in Kubernetes environments, where multiple security tools generate isolated alerts that are difficult to correlate into a coherent incident narrative.
He proposes a framework called CADR (Cloud Native Application Detect and Response), which emphasizes building an application profile—a declarative contract capturing the baseline, expected behaviors of workloads using Kubernetes metadata and eBPF signals.
By correlating deviations from this baseline across layers, teams can achieve high-confidence detection of real attacks and safely automate remediation operations (remops), such as isolating compromised pods, rotating credentials, and updating profiles.
Matias highlights the importance of open, composable, and declarative approaches to detection and response, encourages industry collaboration to develop better correlation tools, and distinguishes application profiles from more generic software bills of behaviors (SBOPs).
The session concludes with a call to action for the community to work together on open-source solutions for automated, context-aware incident remediation in cloud native systems.
# Main Points

|   # | Main point                                                                                                                                                             |
| --: | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Security in Kubernetes is layered, leading to fragmented alerts and lack of coherent incident understanding.                                                           |
|   2 | Multiple tools (WAF, eBPF, Kubernetes API, cloud security) generate separate signals for the same incident.                                                            |
|   3 | The main issue is not lack of signals, but lack of connected understanding across layers.                                                                              |
|   4 | Proposes building a baseline of normal application behavior, called an application profile, as a Kubernetes CRD.                                                       |
|   5 | Baseline includes expected processes, network behavior, system calls, file access, and RBAC rules.                                                                     |
|   6 | Deviations from the baseline indicate potential incidents.                                                                                                             |
|   7 | Correlating signals across layers creates a coherent incident story, distinguishing real attacks from noise.                                                           |
|   8 | Introduces the CADR (Cloud Native Application Detect and Response) framework for connecting signals and automating response.                                           |
|   9 | Application profile should be a contract capturing allowed processes, syscalls, network destinations, file access, and security posture.                               |
|  10 | High-confidence detection enables safe, automated remediation operations (remops).                                                                                     |
|  11 | Remops actions include rolling back deployments, patching network policies, rotating service account tokens, applying stricter profiles, and triggering redeployments. |
|  12 | Automated response can contain incidents quickly (e.g., injection to containment in 7 seconds).                                                                        |
|  13 | Reinforcement step strengthens workloads after incidents, making future attacks harder.                                                                                |
|  14 | CADR architecture: observe with existing tools, create and save profiles, correlate events, remediate confidently.                                                     |
|  15 | Emphasizes open, composable, declarative architecture using CNCF tools, not proprietary solutions.                                                                     |
|  16 | Correlation tools for multi-layer events do not yet exist; call to action for industry to develop them.                                                                |
|  17 | Application profiles are environment- and revision-specific; SBOMs of behavior (SBOPs) aim to generalize profiles safely.                                              |
|  18 | SBOPs should be signed for traceability and tested for safety across environments.                                                                                     |
|  19 | Remediation should be triggered by correlated, high-conf                                                                                                               |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=5DxaxeWNkYY)