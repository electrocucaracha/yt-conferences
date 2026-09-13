---
layout: default
title:
  "Tutorial: Your Application, Batteries In... Brandt K, Austin A, William C,
  Merijn K & Jessica K-D"
nav_order: 383
parent: Kubecon Cloudnativecon Europe 2026
type: Video Note
description:
  The video presents a tutorial session on Zarf, an open-source air gap
  package manager for Kubernetes, with a focus on application portability, determinism,
  and supply chain security. The presenters introduce themselves and outline the sessi...
resource: https://www.youtube.com/watch?v=BBdrp4KvhEo
tags:
  - kubecon-cloudnativecon-europe-2026
  - video
  - learning
status: stable
generated:
  by: process:yt-conferences-okf
  at: 2026-09-12 00:00:00+00:00
---

# Summary

The video presents a tutorial session on Zarf, an open-source air gap package manager for Kubernetes, with a focus on application portability, determinism, and supply chain security.
The presenters introduce themselves and outline the session, which includes hands-on modules for creating, deploying, and inspecting Zarf packages using the instruct platform.
They explain how Zarf packages applications and all dependencies—including Helm charts, OCI images, and Git repositories—into a single, portable tarball, enabling deployment in air-gapped or connected environments.
The tutorial demonstrates creating a Zarf YAML configuration, finding and including necessary images, packaging, deploying to a Kubernetes cluster, and verifying package integrity through checksums and signatures.
Throughout, the presenters address audience questions on topics such as registry customization, Helm and Kustomize support, multi-architecture images, and security features, emphasizing Zarf’s transparency, flexibility, and alignment with open-source security best practices.

# Main Points

|   # | Main point                                                                                                                                                    |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Tutorial session focused on Zarf, an air gap package manager for Kubernetes.                                                                                  |
|   2 | Zarf is typically used in airgapped environments but also supports connected environments for deterministic, portable, and declarative application packaging. |
|   3 | Presenters introduced themselves and outlined the session structure: packaging intro, workshop with modules (create, deploy, inspect), and a playground.      |
|   4 | The tutorial uses the Instruct platform; participants can also run locally with a Kubernetes cluster, Zarf, and the init package.                             |
|   5 | Zarf solves application portability by packaging applications and all dependencies for deployment in any environment.                                         |
|   6 | Zarf packages are declarative, version-controlled manifests that can be shared and deployed consistently.                                                     |
|   7 | Deployment determinism is achieved by declaring what to deploy and how, supporting secure, reproducible deployments.                                          |
|   8 | Zarf supports supply chain security: provenance checks, SBOM creation, and package signing.                                                                   |
|   9 | Zarf is an OpenSSF sandbox project, focusing on Kubernetes but can handle other artifacts.                                                                    |
|  10 | Zarf deployments use Helm charts under the hood; users are not locked into Zarf and can use Helm directly after deployment.                                   |
|  11 | Zarf packages include metadata, components (Helm charts, manifests, images, files, Git repos), and support for customizations.                                |
|  12 | The zarf.yaml file is central to configuration, containing documentation, components, Git repositories, OCI artifacts, and metadata.                          |
|  13 | Zarf can templatize components and find OCI images automatically or manually.                                                                                 |
|  14 | Zarf Connect provides easy access to deployed applications.                                                                                                   |
|  15 | Package creation bundles all components into a single tar.zst file for deployment.                                                                            |
|  16 | Zarf supports external registries and allows customization of registry settings.                                                                              |
|  17 | Helm templating occurs at deploy time using the Helm SDK built into Zarf.                                                                                     |
|  18 | Zarf supports Kubernetes manifests and Kustomize, with some limitations on deploy-time templating.                                                            |
|  19 | Zarf can package and deploy any OCI artifact, with user respo                                                                                                 |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=BBdrp4KvhEo)
