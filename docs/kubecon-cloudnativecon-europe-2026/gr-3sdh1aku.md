---
layout: default
title:
  "Project Lightning Talk: Modelpack: Standardizing The Packaging And Distribution
  Of... Andrew Block"
nav_order: 276
parent: Kubecon Cloudnativecon Europe 2026
type: Video Note
description:
  The speaker introduces Model Pack, a vendor-neutral, open standards project
  designed to simplify the packaging, distribution, and management of AI and ML models.
  Model Pack addresses common challenges in the AI/ML space, such as handling di...
resource: https://www.youtube.com/watch?v=gR-3Sdh1AKU
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

The speaker introduces Model Pack, a vendor-neutral, open standards project designed to simplify the packaging, distribution, and management of AI and ML models.
Model Pack addresses common challenges in the AI/ML space, such as handling diverse files, proprietary information, storage locations, and serving models across different frameworks and infrastructures.
By leveraging the Open Container Initiative (OCI) standards, Model Pack allows models to be packaged as OCI artifacts, enabling easy integration with existing cloud-native tools, infrastructure, and CI/CD pipelines.
It offers features like standardized packaging, a dedicated CLI, built-in security through artifact signing and SBOM generation, and seamless interoperability with current tools.
The project is open source and community-driven, allowing users to publish, manage, and consume models using familiar container registries and runtimes, with resources available for further learning and community engagement.

# Main Points

|   # | Main point                                                                                                                         |
| --: | ---------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Model Pack enables distribution and packaging of AI/ML models.                                                                     |
|   2 | Managing AI/ML content involves packaging, storage, and serving challenges.                                                        |
|   3 | Storage options include S3 buckets, Git, or proprietary model stores.                                                              |
|   4 | Serving models varies by framework and infrastructure (e.g., Python, Kubernetes).                                                  |
|   5 | Model Pack is a vendor-neutral, open standards project for managing AI/ML models.                                                  |
|   6 | It is a CNCF sandbox project since May 2025.                                                                                       |
|   7 | Packages AI/ML models as OCI artifacts for standardized distribution and consumption.                                              |
|   8 | Leverages open cloud-native standards and the Open Container Initiative (OCI).                                                     |
|   9 | OCI now supports managing artifacts beyond container images, such as Helm charts.                                                  |
|  10 | Allows reuse of existing container infrastructure for AI/ML models.                                                                |
|  11 | Provides interoperability with existing tools and frameworks.                                                                      |
|  12 | Features standard packaging for model files, dependencies, and metadata.                                                           |
|  13 | Includes a CLI to simplify packaging and building AI/ML models.                                                                    |
|  14 | Supports CI/CD integration with tools like Jenkins and GitHub Actions.                                                             |
|  15 | Built-in security through OCI content signing and SBOM generation.                                                                 |
|  16 | Enables use of existing OCI security and compliance tooling.                                                                       |
|  17 | Community-driven open source project for standardization and collaboration.                                                        |
|  18 | Publishing involves creating a model artifact and pushing it to a container registry.                                              |
|  19 | Benefits include version management, distribution, access control, security, and compliance.                                       |
|  20 | Models can be consumed using model pack CLI, container runtimes (Docker, Podman), or Kubernetes (CSI driver, image volume source). |
|  21 | Additional resources: model.org, github.com/modelpack, Model Pack kiosk, CNCF Slack channel.                                       |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=gR-3Sdh1AKU)
