---
layout: default
title:
  Making Application Rollouts Observable, Actionable and Boring - Vasudev Bongale,
  LinkedIn
nav_order: 159
parent: Kubecon Cloudnativecon North America 2025
type: Video Note
description:
  Vasuv, a software engineer at LinkedIn, discusses how his team improved
  the reliability and developer experience of application rollouts on LinkedIn’s massive
  Kubernetes-based compute infrastructure. He explains the challenges faced by both...
resource: https://www.youtube.com/watch?v=8QS3hmsDjNE
tags:
  - kubecon-cloudnativecon-north-america-2025
  - video
  - learning
status: stable
generated:
  by: process:yt-conferences-okf
  at: 2026-09-12 00:00:00+00:00
---

# Summary

Vasuv, a software engineer at LinkedIn, discusses how his team improved the reliability and developer experience of application rollouts on LinkedIn’s massive Kubernetes-based compute infrastructure.
He explains the challenges faced by both application developers and platform engineers in tracking and debugging rollouts due to Kubernetes’ always-converging, declarative nature, which lacks clear terminal states.
To address this, the team built a system that makes rollouts observable by assigning each change a unique identity, owner, and timestamp, and actionable by introducing a structured taxonomy for failure reasons and providing clear, human-readable explanations and next steps for failures.
They also developed integrated tools and dashboards that streamline troubleshooting and surface relevant metrics and alerts, reducing operational overhead and enabling self-service debugging.
As a result, rollouts have become predictable and routine, freeing engineers to focus on innovation, and the platform now quickly identifies and addresses issues, driving continuous improvement.

# Main Points

|   # | Main point                                                                                                                                                         |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   1 | Vasuv, software engineer at LinkedIn, works on the compute infrastructure team building LinkedIn's Kubernetes platform.                                            |
|   2 | The platform supports 500,000 servers, 3,000 applications, and 1.5 million containers, with 50,000 rollouts per week.                                              |
|   3 | Two main user personas: Alice (application developer) and Bob (platform engineer).                                                                                 |
|   4 | Developers want to know if their rollout succeeded, why it failed, and what to do next; platform engineers care about overall platform health and rollout success. |
|   5 | Kubernetes' always-converging, declarative nature makes it hard to determine rollout completion or failure.                                                        |
|   6 | Rollout signals are scattered across clusters (YAML, events, logs), making debugging operationally expensive.                                                      |
|   7 | Solution: Built a system to make rollouts observable, actionable, and routine.                                                                                     |
|   8 | Each rollout is given an identity with context: who made the change, what was changed, when, and the outcome.                                                      |
|   9 | Custom resource "LI deployment" (CRD) captures developer intent; platform expands user input into detailed podspecs.                                               |
|  10 | Annotations added via mutating webhook: intent ID (unique identifier), intent username (initiator), and intent start time.                                         |
|  11 | Real-time rollout status is tracked with a "rollout successful" condition (unknown, true, false) and a progress deadline.                                          |
|  12 | Events are structured into "intents" for clear tracking and UI display.                                                                                            |
|  13 | Rollout failures are made actionable by providing clear, human-readable failure reasons and next steps.                                                            |
|  14 | Introduced a failure reason taxonomy: category, reason, and message for each failure.                                                                              |
|  15 | Pod failures are categorized (infra, initialization, image pull, app fail to start, etc.) and summarized for each rollout.                                         |
|  16 | Users can use internal CLI tools and dashboards for detailed rollout and pod information, with pre-formed commands and integrated metrics/logs.                    |
|  17 | Default alerts notify users of issues even before failures occur.                                                                                                  |
|  18 | Platform-wide failure categorization enables targeted improvements and root cause analysis.                                                                        |
|  19 | Rollout success rate i                                                                                                                                             |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=8QS3hmsDjNE)
