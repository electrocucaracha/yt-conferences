---
type: Video Note
title: "To InGate and Beyond Ingress-nginx! - James Strong, Isovalent @ Cisco & Marco Ebert, Giant Swarm"
description: "The talk provides an update on the Ingress EngineX project, highlighting its long history, extensive feature set, and significant community contributions over the past decade, including around 8,000 closed pull requests and over 1,000 contr..."
resource: https://www.youtube.com/watch?v=GISpxPdNKfE
tags: ["kubecon-cloudnativecon-north-america-2025", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

The talk provides an update on the Ingress EngineX project, highlighting its long history, extensive feature set, and significant community contributions over the past decade, including around 8,000 closed pull requests and over 1,000 contributors.
However, due to a lack of maintainers and limited resources—currently only two active maintainers—the project has been in maintenance mode since the last London KubeCon, with only dependency updates and minor bug fixes being made.
The team announced that Ingress EngineX will be archived by March 2026, after which it will become read-only with no further updates, though existing images and Helm charts will remain available.
The related Ingate project, intended to help users migrate to Gateway API, will also be retired due to insufficient development and interest.
The speakers expressed gratitude to the community and recommended that users begin migrating to Gateway API, noting that the decline of Ingress EngineX is a natural part of the open source lifecycle and encouraging contributions to projects supporting this transition.
# Main Points

|   # | Main point                                                                                                                                                         |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   1 | Ingress EngineX has been active for about 10 years with over 8,000 closed PRs and more than 1,000 contributors.                                                    |
|   2 | The project has an extensive feature set, including many annotations beyond the basic ingress API.                                                                 |
|   3 | Maintenance has become difficult due to a lack of maintainers and limited resources; currently, only two people are actively involved.                             |
|   4 | Since the last CubeCon in London, the project has been in maintenance mode, with only dependency updates and minor bug fixes.                                      |
|   5 | No significant new features have been added recently; activity has been minimal.                                                                                   |
|   6 | Regular patch releases have continued, but mostly for dependency updates, not new features.                                                                        |
|   7 | After discussions with committee members, the decision was made to archive the project by March 2026 (Amsterdam).                                                  |
|   8 | After archiving, the project will be read-only with no further fixes, updates, or releases; images and Helm charts will remain available for existing deployments. |
|   9 | The planned migration path from ingress to Gateway API via Ingate will not proceed; Ingate will also be retired and made read-only.                                |
|  10 | The decline in project activity is attributed to limited maintainer availability and the rise of alternative solutions like Gateway API.                           |
|  11 | SIG Network recommends users migrate to Gateway API; the Gateway to Ingress project can assist with migration.                                                     |
|  12 | The community expressed gratitude to the maintainers for their efforts and encouraged contributions to the Ingress to Gateway project to ease the transition.      |
|  13 | Kubernetes' growth and success were acknowledged as being significantly supported by Ingress EngineX.                                                              |
|  14 | Further information about the project's retirement will be available in a blog post and slides.                                                                    |
|  15 | Attendees were invited to ask questions or seek support from SIG Network and security representatives.                                                             |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=GISpxPdNKfE)