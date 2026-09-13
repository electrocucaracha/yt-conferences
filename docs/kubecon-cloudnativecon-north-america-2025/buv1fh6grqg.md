---
type: Video Note
title: "GitOps Without Variables - Brian Grant & Alexis Richardson, ConfigHub Inc."
description: "Brian Grant, the original architect of Kubernetes, discusses the challenges of managing configuration in modern applications. He introduces Config Hub, a platform that stores configuration as data in a database, rather than generating it pr..."
resource: https://www.youtube.com/watch?v=buv1fh6grqg
tags: ["kubecon-cloudnativecon-north-america-2025", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

Brian Grant, the original architect of Kubernetes, discusses the challenges of managing configuration in modern applications.
He introduces Config Hub, a platform that stores configuration as data in a database, rather than generating it programmatically.
This approach allows for more flexibility and control over configuration changes, making it easier to manage complex configurations across multiple environments.
With Config Hub, users can make changes to individual resources without affecting the entire cluster, reducing the risk of "blast radius" issues.
The platform also provides features like automated validation and integration with existing tools like Kubernetes, Flux, and Argo.
By separating data from programmatic logic, Config Hub enables more efficient and safer configuration management, making it easier to achieve "Ops Nirvana."
# Main Points

|   # | Main point                                                                                                                           |
| --: | ------------------------------------------------------------------------------------------------------------------------------------ |
|   1 | Brian Grant is the original architect of Kubernetes and creator of customize.                                                        |
|   2 | He was part of the team that created Kubernetes and worked at Google for 17 years.                                                   |
|   3 | The current configuration sprawl problem can be solved by using a fully rendered, explicit configuration model.                      |
|   4 | This approach separates data from programmatic changes, making it easier to manage and update configurations.                        |
|   5 | Config Hub is a tool that stores configuration as data in objects in a database, rather than storing generation code in git.         |
|   6 | It provides an API for the configuration data, enabling automation of changes through functions or tools built on top of Config Hub. |
|   7 | The approach allows for more efficient and safer configuration management, reducing the risk of blast radius errors.                 |
|   8 | It enables mass changes to be made easily, with opportunities for review and validation before deployment.                           |
|   9 | The key takeaway is to separate data from programmatic changes, using a fully rendered, explicit configuration model.                |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=buv1fh6grqg)