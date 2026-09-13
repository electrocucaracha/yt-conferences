---
type: Video Note
title: "Project Lightning Talk: ModelPack: An Open Standard for Packaging, Distributing, and... Tao Peng"
description: "Top from Mr introduces Model Bank, a new open-source project aimed at providing a vendor-neutral specification for packaging, distributing, and running AI models in cloud-native environments. The project allows users to package their AI mod..."
resource: https://www.youtube.com/watch?v=kb9L9E5matI
tags: ["kubecon-cloudnativecon-north-america-2025", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

Top from Mr introduces Model Bank, a new open-source project aimed at providing a vendor-neutral specification for packaging, distributing, and running AI models in cloud-native environments.
The project allows users to package their AI models, including code and weights, into an OCI artifact similar to a container image, which can then be pushed to any OCI-compatible registry such as Docker Hub or Harbor.
Model Bank offers tools for building, pushing, and pulling these model artifacts, with integration support for Kubernetes, Harbor, CRI-O, and Django Flight for efficient distribution within clusters.
The project is still a work in progress, with upcoming presentations showcasing its integration with Harbor and Django Flight.
Interested users can find more information, documentation, and ways to get involved on the project's website, GitHub, and Slack.
# Main Points

|   # | Main point                                                                                                                                                                                             |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   1 | Model Bank is a new open standard for packaging, distributing, and running models in the cloud native ecosystem.                                                                                       |
|   2 | The project was established this year and donated to Sensf in May.                                                                                                                                     |
|   3 | Model Bank packages AI code and weights into a format similar to container images.                                                                                                                     |
|   4 | The specification is vendor-neutral and open source.                                                                                                                                                   |
|   5 | Tools are provided to build and push AI models as OCI artifacts following the model format specification.                                                                                              |
|   6 | Users can package models from a git repository into a model artifact with a manifest describing its contents.                                                                                          |
|   7 | Model artifacts can be pushed to any OCI-compatible registry, such as Docker Hub, Harbor, or cloud registries.                                                                                         |
|   8 | Models stored in registries can be pulled and used with Kubernetes, mounted as local volumes, and accessed from pods like local storage.                                                               |
|   9 | Integrations exist with Kubernetes, Harbor, CRI-O, and Django Flight for distribution.                                                                                                                 |
|  10 | The project is a work in progress.                                                                                                                                                                     |
|  11 | Model Bank will be showcased at the Chaos event with two presentations: a project update from Harbor maintainers and an introduction to Django Flight for efficient AI model distribution in clusters. |
|  12 | The website is up to date; contact is available via Slack and GitHub.                                                                                                                                  |
|  13 | The specification markdown and a getting started document are available for more details.                                                                                                              |
|  14 | A QR code links to the GitHub repository and Slack.                                                                                                                                                    |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=kb9L9E5matI)