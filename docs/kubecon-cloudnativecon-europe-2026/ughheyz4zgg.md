---
layout: default
title:
  "Pull Request Wars: The Flux Awakens - Ephemeral Kubernetes Environ... Matteo
  Bianchi & Stefan Prodan"
nav_order: 303
parent: Kubecon Cloudnativecon Europe 2026
type: Video Note
description:
  In this presentation, Mat Bankei and Stefan Prodan introduce a workflow
  for creating declarative, pull request-driven, GitOps-native preview environments
  using Flux, designed to balance developer self-service with platform team governance...
resource: https://www.youtube.com/watch?v=uGhHeYZ4zGg
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

In this presentation, Mat Bankei and Stefan Prodan introduce a workflow for creating declarative, pull request-driven, GitOps-native preview environments using Flux, designed to balance developer self-service with platform team governance.
They describe a setup involving three repositories: a platform repo managed by platform engineers, an application repo for developers, and a Helm charts repo, enabling developers to deploy preview environments by simply labeling a pull request.
The demo showcases how Flux Operator automates the deployment and cleanup of these ephemeral environments, integrates with GitHub Actions for CI, and provides feedback directly in pull requests.
The presenters also demonstrate debugging failed deployments using GitHub Copilot and Flux MCP, emphasizing the importance of access controls and observability.
They conclude by sharing resources and best practices for adopting this workflow, highlighting its flexibility, automation, and support for multiple providers beyond GitHub.

# Main Points

|   # | Main point                                                                                                                                                                                                     |
| --: | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | The talk is presented by Mat Bankei (GitHub solutions engineer, CNCF ambassador, Kubernetes contributor) and Stefan Prodan (principal engineer at Control Plane, creator of Flagger, core maintainer of Flux). |
|   2 | The session focuses on declarative, PR-driven, GitOps-native preview environments for developers, owned by platform teams.                                                                                     |
|   3 | Challenges in current CI/CD pipelines include maintenance difficulty, inconsistency, long review cycles, and lack of standardization.                                                                          |
|   4 | Developers want self-service and minimal infrastructure involvement; platform teams require governance, control, and observability.                                                                            |
|   5 | AI and agentic coding increase the need for real environment testing.                                                                                                                                          |
|   6 | The proposed solution uses three repositories: a platform repo (Flux operator config, cluster bootstrap), an app repo (developer-only, no secrets), and a Helm charts repo (platform-owned).                   |
|   7 | The workflow uses GitHub Actions for CI (build and push images), but CI does not interact with the cluster.                                                                                                    |
|   8 | Flux operator monitors pull requests with a specific label and deploys preview environments automatically.                                                                                                     |
|   9 | The system supports multiple providers (GitHub, GitLab, Azure DevOps) and can use GitHub Actions to push manifests.                                                                                            |
|  10 | Preview environments are created per pull request; merging or closing the PR deletes the environment.                                                                                                          |
|  11 | Limits can be set on the number of concurrent preview environments to control costs.                                                                                                                           |
|  12 | Flux UI provides visibility into deployments, configuration, and resource sets.                                                                                                                                |
|  13 | Each PR triggers a unique Helm release using templating based on PR number and commit SHA.                                                                                                                     |
|  14 | Developers receive automated PR comments with deployment status and can access preview URLs.                                                                                                                   |
|  15 | Integration with GitHub Deploy API provides commit status updates.                                                                                                                                             |
|  16 | Demonstrated debugging with GitHub Copilot and Flux MCP, which can diagnose issues in Kubernetes clusters.                                                                                                     |
|  17 | MCP server can be set to read-only mode for safety; RBAC is recommended for access control.                                                                                                                    |
|  18 | All resources, documentation, and demo repos are available on                                                                                                                                                  |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=uGhHeYZ4zGg)
