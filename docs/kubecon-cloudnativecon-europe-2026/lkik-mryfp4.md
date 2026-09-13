---
type: Video Note
title: "Project Lightning Talk: Argo CD Source Hydrator: Rendered Manifests Made Easy! - Michael Crenshaw"
description: "Michael Crenshaw, a senior staff software engineer at Intuit and lead maintainer for Argo CD, introduces the Argo CD source hydrator feature, which streamlines the rendered manifest pattern for GitOps users. Previously, users either relied..."
resource: https://www.youtube.com/watch?v=Lkik-mrYfP4
tags: ["kubecon-cloudnativecon-europe-2026", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

Michael Crenshaw, a senior staff software engineer at Intuit and lead maintainer for Argo CD, introduces the Argo CD source hydrator feature, which streamlines the rendered manifest pattern for GitOps users.
Previously, users either relied on Argo CD to render manifests directly from Git changes or maintained custom pipelines to pre-render and push manifests to Git, both approaches having drawbacks such as lack of transparency or additional maintenance overhead.
The new source hydrator feature allows Argo CD to render manifests and automatically push them to Git as manifest.yaml files, providing users with an audit trail and improved visibility into changes.
Enabling this feature is straightforward, requiring only minor adjustments to the application manifest, and it introduces new UI elements to track the hydration and synchronization process.
Additionally, the hydrate two capability allows pushing hydrated manifests to a separate branch for further automation or security checks, and Intuit uses this in conjunction with their open-sourced GitOps Promoter tool to automate environment promotion.
# Main Points

|   # | Main point                                                                                                                                           |
| --: | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Michael Crenshaw is a senior staff software engineer at Intuit and lead maintainer for Argo CD.                                                      |
|   2 | The talk focuses on the Argo CD source hydrator feature.                                                                                             |
|   3 | Previously, GitOps users relied on Argo CD to render manifests from changes in Git using tools like Helm, JSONet, Kustomize, or plugins.             |
|   4 | The rendered manifest pattern evolved to have a separate process render manifests and push them to Git before Argo CD applies them.                  |
|   5 | Maintaining the render process requires custom internal code and lacks Argo CD’s UI and reliability features.                                        |
|   6 | The source hydrator feature brings the rendered manifest process into Argo CD as a first-class feature.                                              |
|   7 | With source hydrator, Argo CD renders manifests and pushes them to Git as manifest.yaml, providing an audit trail and transparency.                  |
|   8 | Enabling source hydrator involves copying existing source fields into spec.sourcehydrator.drysource and adding a sync source for hydrated manifests. |
|   9 | Intuit uses this approach to deploy 50 Argo CD instances in six waves.                                                                               |
|  10 | The UI adds a toolbar showing where manifests were pulled from, pushed to, and synced from.                                                          |
|  11 | Source hydrator includes a "hydrate two" feature to push hydrated manifests to a different branch, allowing for automation and security checks.      |
|  12 | Intuit uses GitOps Promoter to automate environment promotion between branches.                                                                      |
|  13 | Michael invites attendees to visit the Intuit booth at Argo Con or the Argo booth at KubeCon.                                                        |
|  14 | He requests users to fill out an annual Argo CD user survey via a QR code to help prioritize project improvements.                                   |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=Lkik-mrYfP4)