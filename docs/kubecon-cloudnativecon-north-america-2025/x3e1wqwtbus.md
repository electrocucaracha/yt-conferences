---
type: Video Note
title: "A Journey To Zero-Downtime Upgrades With Keycloak - Martin Bartoš, Ryan Emerson, IBM"
description: "Here is a summary of the video transcript in 3-5 sentences."
resource: https://www.youtube.com/watch?v=x3e1wqWTbUs
tags: ["kubecon-cloudnativecon-north-america-2025", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

Here is a summary of the video transcript in 3-5 sentences: Martin Bartto and Ryan Emerson from IBM's Keycloak team discuss how to upgrade a critical system without downtime, focusing on zero-downtime upgrades with Keycloak.
They introduce the concept of rolling updates, which allows for continuous deployment while minimizing disruptions, but acknowledge that not all configuration changes are compatible.
The team has developed a solution using a Java interface called the compatibility metadata provider, which generates and verifies metadata to determine if rolling updates are possible in a safe way.
This solution is currently being refined and tested, with plans to improve horizontal scalability, Kubernetes support, and observability.
# Main Points

|   # | Main point                                                                                                                                                 |
| --: | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Keycloak is an identity and access management solution that authenticates and authorizes users for services and APIs.                                      |
|   2 | Keycloak provides single sign-on capability, allowing users to log in once across an organization.                                                         |
|   3 | The solution allows for zero downtime upgrades by replacing instances of Keycloak one at a time while continuing to serve user requests.                   |
|   4 | The solution requires compatibility metadata provider implementations to generate and verify metadata to determine if rolling updates are possible safely. |
|   5 | Keycloak has reached 30,000 stars on GitHub and has over 1,300 contributors since its inception in 2013.                                                   |
|   6 | The solution is fully supported for Keycloak patch version upgrades, but only in preview support for major upgrades.                                       |
|   7 | Future plans include improving horizontal scalability, Kubernetes native databases, and support for client CRS.                                            |
|   8 | The operator will provide a Helm chart for quick deployment, but no concrete plans have been made yet.                                                     |
|   9 | There is no standard way to do blue-green deployments with Keycloak clustering, and it's not recommended due to the complexity of the system.              |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=x3e1wqWTbUs)