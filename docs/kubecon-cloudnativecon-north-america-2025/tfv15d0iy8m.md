---
type: Video Note
title: "Flux - The GitLess GitOps Edition - Stefan Prodan, ControlPlane & Dipti Pai, Microsoft"
description: 'The video features a discussion with Dipy, a Flux maintainer, about advancements in Flux and the concept of "Gitless GitOps." The presenters explain how traditional GitOps workflows rely on Git repositories and container registries to manag...'
resource: https://www.youtube.com/watch?v=TFv15d0iy8M
tags: ["kubecon-cloudnativecon-north-america-2025", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

The video features a discussion with Dipy, a Flux maintainer, about advancements in Flux and the concept of "Gitless GitOps." The presenters explain how traditional GitOps workflows rely on Git repositories and container registries to manage desired state and deployments, but Flux has evolved to support alternative sources like S3 buckets and OCI (container) registries for storing and reconciling configurations.
This shift offers advantages in security, availability, and operational simplicity, including unified signing and verification of artifacts and reduced reliance on maintaining Git infrastructure in production.
Dipy demonstrates how Flux integrates with cloud provider identity systems (OIDC) to enable passwordless, credential-free authentication for pulling and pushing resources, enhancing security and supporting multi-tenant scenarios.
The session concludes with highlights of new features in Flux 2.7, such as the source watcher and artifact generator for improved monorepo support, and mentions upcoming integrations and a new status page UI for Flux users.
# Main Points

|   # | Main point                                                                                                                                                                                    |
| --: | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Dipy, a Flux maintainer from Microsoft, joins to discuss Flux and GitOps.                                                                                                                     |
|   2 | Overview of GitOps: desired state stored in Git repos, container images in registries; Flux reconciles clusters to match desired state.                                                       |
|   3 | Flux image automation scans registries, updates Git with new image versions, and synchronizes clusters.                                                                                       |
|   4 | Flux v2 introduced the source controller, which caches artifacts from sources (e.g., Git) for drift correction even if Git is unavailable.                                                    |
|   5 | Flux expanded to support S3 buckets and container registries (OCI) as sources for desired state.                                                                                              |
|   6 | Using container registries as sources offers advantages: unified storage, easier signing/verification (cosign, notation), machine-based identity, improved availability, and reduced latency. |
|   7 | Migrating from Git to OCI sources in Flux involves minor API changes, mainly in verification (cosign keyless verification).                                                                   |
|   8 | Helm charts are supported via OCI, simplifying API usage and unifying storage.                                                                                                                |
|   9 | Flux CLI supports pushing artifacts to registries with traceability to original Git source.                                                                                                   |
|  10 | Gitless GitOps still relies on Git for collaboration; OCI acts as intermediary storage.                                                                                                       |
|  11 | GitHub Actions can automate pushing and signing OCI artifacts for Flux.                                                                                                                       |
|  12 | Flux Operator enables bootstrapping clusters from OCI sources, supporting cloud-native authentication (e.g., AWS workload identity).                                                          |
|  13 | Flux supports passwordless authentication (OIDC) for Git, OCI, and Helm repositories across Azure, AWS, and Google Cloud.                                                                     |
|  14 | OIDC integrations eliminate the need for secrets, reducing security risks and operational burden.                                                                                             |
|  15 | Per-object identity configuration enables multi-tenant scenarios in Kubernetes clusters.                                                                                                      |
|  16 | Flux 2.7 introduces the source-watcher controller and artifact generator API for efficient monorepo handling and artifact composition from multiple sources.                                  |
|  17 | Backstage now has a Flux extension/plugin.                                                                                                                                                    |
|  18 | Upcoming features: Helm 4 integration, Flux 2.8, and a new status page embedded in Flux Operator.                                                                                             |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=TFv15d0iy8M)