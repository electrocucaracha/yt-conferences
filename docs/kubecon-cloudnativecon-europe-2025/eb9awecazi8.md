---
layout: default
title:
  "Buildpacks: Pragmatic Solutions To Quick and Secure Image Builds - Juan Bustamante
  & Aidan Delaney"
nav_order: 37
parent: Kubecon Cloudnativecon Europe 2025
type: Video Note
description:
  The Cloud Native Build Pack project allows users to transform application
  source code into production-ready OCI images deployable on any OCI runtime environment,
  such as Kubernetes or Podman. The project provides a reference implementation...
resource: https://www.youtube.com/watch?v=Eb9AweCazi8
tags:
  - kubecon-cloudnativecon-europe-2025
  - video
  - learning
status: stable
generated:
  by: process:yt-conferences-okf
  at: 2026-09-12 00:00:00+00:00
---

# Summary

The Cloud Native Build Pack project allows users to transform application source code into production-ready OCI images deployable on any OCI runtime environment, such as Kubernetes or Podman.
The project provides a reference implementation of the specification and maintains implementations from downstream providers like Paxi and Kaxi.
It enables quick and secure image builds without requiring Docker files, making it ideal for organizations with complex application environments.
The build packs also offer features like rebase, dependency mirrors, and secure registries, providing control over base images, tool versions, and language families.

# Main Points

|   # | Main point                                                                                                                                                                                                         |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   1 | Cloud Native Build Pack project allows transforming source code into production-ready OCI images for deployment on Kubernetes or OCI runtime environments.                                                         |
|   2 | The project offers a reference implementation of the specification and maintains implementations by downstream providers (e.g., PTO, Heroku).                                                                      |
|   3 | The cloud native build pack will always keep a well-defined boundary between each layer category, allowing features like rebase.                                                                                   |
|   4 | Examples:                                                                                                                                                                                                          |
|   5 | Monorepo application with go and NodeJS front-end built using paketto and pack.                                                                                                                                    |
|   6 | Spring Boot Java application built using pack.                                                                                                                                                                     |
|   7 | Python application generated with AI built using pack.                                                                                                                                                             |
|   8 | Key changes in the past year:                                                                                                                                                                                      |
|   9 | PTO build packs now support dependency mirrors for internal dependencies.                                                                                                                                          |
|  10 | Heroku build packs added poetry support for Python collections.                                                                                                                                                    |
|  11 | PTO introduced extensions, which are now part of the spec and available as a feature flag.                                                                                                                         |
|  12 | KPAC now supports insecure registries for faster development loops.                                                                                                                                                |
|  13 | Benefits for platform operators:                                                                                                                                                                                   |
|  14 | Control over base images and tool versions.                                                                                                                                                                        |
|  15 | Ability to mirror internal dependencies and ensure production images only use those.                                                                                                                               |
|  16 | Custom build packs can be created with control over the workflow.                                                                                                                                                  |
|  17 | Key features of the cloud native build pack project: + Fast rebuilds due to small, focused layers. + Software bill of materials (SBOM) for secure image deployment. + Co-sign support for provenance certificates. |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=Eb9AweCazi8)
