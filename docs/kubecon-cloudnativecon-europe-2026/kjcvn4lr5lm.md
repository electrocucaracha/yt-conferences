---
type: Video Note
title: "Cloud Native Theater | Cloud Native University: Kubernetes: The API of Everything - Tibo Beijen"
description: "Tibayian, an experienced Kubernetes professional at DPG Media, introduces Kubernetes from an API-centric perspective rather than just as a container orchestrator. He explains that Kubernetes’ core is its API, which enables data exchange and..."
resource: https://www.youtube.com/watch?v=kJCvn4LR5lM
tags: ["kubecon-cloudnativecon-europe-2026", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

Tibayian, an experienced Kubernetes professional at DPG Media, introduces Kubernetes from an API-centric perspective rather than just as a container orchestrator.
He explains that Kubernetes’ core is its API, which enables data exchange and automation through controllers—components that reconcile the desired and actual states defined in YAML specifications.
By extending the API with custom resource definitions and additional controllers (often called operators), users can automate and manage a wide variety of workloads, both inside and outside Kubernetes, following a repeating pattern of spec, status, and reconciliation.
Tibayian illustrates this with examples like canary deployments, Kafka clusters, and infrastructure management, emphasizing that Kubernetes is a flexible, extensible platform for orchestrating much more than containers.
He concludes by encouraging attendees to view Kubernetes primarily as an extensible API platform rather than just a tool for running containers.
# Main Points

|   # | Main point                                                                                                                                                                                                                            |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Tibayian has worked with Kubernetes for about eight years and is employed at DPG Media, a major media company in the Netherlands and Belgium.                                                                                         |
|   2 | Kubernetes is commonly seen as a container orchestrator, but it is fundamentally an API designed to orchestrate various resources, not just containers.                                                                               |
|   3 | An API primarily exchanges, stores, and retrieves data, but in Kubernetes, controllers act as the "brains" that manage and automate tasks.                                                                                            |
|   4 | Controllers interpret specifications (YAML files) that define the desired state and work to achieve it, reporting back the actual state via status.                                                                                   |
|   5 | Multiple controllers work together to achieve orchestration, such as deployment controllers spawning replica sets, which in turn create pods, scheduled by other controllers.                                                         |
|   6 | The kubelet on each node acts as a controller to run containers and report status.                                                                                                                                                    |
|   7 | Kubernetes automation can be extended by adding new API types (Custom Resource Definitions, CRDs) and corresponding controllers (operators).                                                                                          |
|   8 | Extending the API involves creating a new data type (CRD) and a controller that manages resources of that type, following the reconciliation loop of desired vs. actual state.                                                        |
|   9 | Examples include extending the API for advanced autoscaling, canary and blue-green deployments (e.g., Argo Rollouts), and managing Kafka clusters (e.g., Strimzi).                                                                    |
|  10 | The pattern of extending the API with new types and controllers repeats across many use cases, including infrastructure management (Crossplane), policy enforcement, external secrets management, and cluster creation (Cluster API). |
|  11 | Kubernetes can manage resources both inside and outside the cluster using this extensible API pattern.                                                                                                                                |
|  12 | The key takeaway is to view Kubernetes as an extensible API platform capable of orchestrating a wide range of resources, not just containers.                                                                                         |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=kJCvn4LR5lM)