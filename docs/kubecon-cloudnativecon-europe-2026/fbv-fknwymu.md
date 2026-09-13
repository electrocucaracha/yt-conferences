---
type: Video Note
title: "Project Lightning Talk: Let’s Deploy etcd Operator - Arka Saha, Maintainer"
description: "Orco Shaha, a software engineer at Broadcom and reviewer for the etcd operator project, introduces the city operator, a community-supported and native operator designed to address challenges in managing etcd clusters, such as authentication..."
resource: https://www.youtube.com/watch?v=FBV-fkNwyMU
tags: ["kubecon-cloudnativecon-europe-2026", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

Orco Shaha, a software engineer at Broadcom and reviewer for the etcd operator project, introduces the city operator, a community-supported and native operator designed to address challenges in managing etcd clusters, such as authentication, scaling, and upgrades.
Previously, users built their own operators due to a lack of comprehensive solutions, but the city operator aims to unify efforts and support workload applications on Kubernetes.
The latest release, version 0.2, adds certificate support for production environments, though the operator is not yet production-ready, with future releases planned to include recovery, backup, and Helm chart support.
Orco demonstrates how to deploy the operator, scale clusters, and configure secure communication using built-in or cert-manager-based certificates, highlighting both development and production use cases.
He concludes by inviting viewers to a maintainer summit for further questions.
# Main Points

|   # | Main point                                                                                                                                         |
| --: | -------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Orco Shaha from Broadcom is a software engineer and reviewer in the etcd operator project.                                                         |
|   2 | The etcd operator project addresses the management of etcd clusters, which was previously unaddressed by the community.                            |
|   3 | Earlier, users built their own operators due to lack of a unified solution; a previous CoreOS project was not fully developed.                     |
|   4 | The revived etcd operator aims to provide a community-supported, native operator to handle pain points like authentication, scaling, and upgrades. |
|   5 | The operator is initially focused on supporting workload applications running on Kubernetes, rather than Kubernetes itself.                        |
|   6 | Two releases have been made; the latest is version 0.2, released last week.                                                                        |
|   7 | Version 0.2 adds certificate support to help use the operator in production environments, though it is not yet production-ready.                   |
|   8 | Upcoming releases will include features like recovery, backup, and a Helm chart release.                                                           |
|   9 | Users can experiment with the operator; the official image is version 0.2.                                                                         |
|  10 | For local development on a kind cluster, users can clone the repo, build the Docker image, and deploy locally.                                     |
|  11 | Deploying the official image brings up the etcd operator controller pod and installs the etcd clusters CRD.                                        |
|  12 | The cluster object specifies the etcd version and cluster size; scaling out adds members until the desired size is reached.                        |
|  13 | Scaling in allows reducing the cluster size by editing the object, and the operator reconciles the change.                                         |
|  14 | For development, an in-built certificate mechanism is available for secure member communication; this is not recommended for production.           |
|  15 | The TLS section in the configuration allows specifying auto-generated certificates, which are mounted to member pods.                              |
|  16 | For production, it is recommended to use cert-manager as the certificate provider.                                                                 |
|  17 | The TLS section can specify cert-manager as the provider, along with certificate name, validity, issuer, and type.                                 |
|  18 | Cert-manager creates and mounts certificates and secrets to the pods.                                                                              |
|  19 | A maintaine                                                                                                                                        |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=FBV-fkNwyMU)