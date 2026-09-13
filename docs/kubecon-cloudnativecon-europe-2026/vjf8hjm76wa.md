---
type: Video Note
title: "Building a Kubernetes Platform That Scales From SaaS To Self-Managed - Florian Forster, GitLab"
description: "Florian, an SRE and tech lead at GitLab, discusses how GitLab is evolving its platform to scale from single-node self-managed installations to its large-scale SaaS offering. He explains that GitLab’s monolithic Ruby on Rails architecture, w..."
resource: https://www.youtube.com/watch?v=vjF8HjM76wA
tags: ["kubecon-cloudnativecon-europe-2026", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

Florian, an SRE and tech lead at GitLab, discusses how GitLab is evolving its platform to scale from single-node self-managed installations to its large-scale SaaS offering.
He explains that GitLab’s monolithic Ruby on Rails architecture, while effective so far, is showing scalability limitations, prompting the development of "runway," an internal platform to deploy modular satellite services.
Initially, runway leveraged Google Cloud Run for rapid deployment, but this approach did not meet the needs of self-managed customers due to vendor lock-in and regulatory requirements.
To address this, GitLab is transitioning to Kubernetes and Helm charts as open standards, enabling consistent deployment across SaaS and self-managed environments while maintaining a streamlined developer experience.
The team is also working to balance modularity with simplicity, ensuring backward compatibility and supporting existing installation methods like Omnibus, while providing tools and frameworks to ease infrastructure provisioning and application integration for both internal teams and customers.
# Main Points

|   # | Main point                                                                                                                                                                  |
| --: | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | GitLab platform scales from single-node self-managed installations to SaaS (gitlab.com).                                                                                    |
|   2 | Majority of audience runs vendored software in production; many use GitLab.                                                                                                 |
|   3 | GitLab is built on a large Ruby on Rails monolith, serving both SaaS and self-managed customers.                                                                            |
|   4 | Monolithic architecture causes scalability and coupling issues; need to decouple and scale services independently.                                                          |
|   5 | Runway is GitLab’s internal platform to deploy satellite services around the monolith.                                                                                      |
|   6 | Runway team is small (about six engineers); simplicity is prioritized to manage complexity.                                                                                 |
|   7 | Runway currently handles deployments for gitlab.com; integration for self-managed and GitLab Dedicated is in progress.                                                      |
|   8 | Initial version of Runway used Cloud Run for rapid delivery, but Cloud Run is unsuitable for many self-managed customers due to data residency and regulatory requirements. |
|   9 | Need for a more portable, vendor-neutral solution led to adopting Kubernetes as the common platform.                                                                        |
|  10 | Kubernetes chosen for open standards and portability across different environments (GKE, EKS, home labs).                                                                   |
|  11 | Helm charts are used for packaging and deploying services; same charts used for SaaS and self-managed.                                                                      |
|  12 | Developers have a CI pipeline that builds and deploys containers automatically for gitlab.com.                                                                              |
|  13 | Self-managed customers must deploy and manage their own infrastructure; GitLab provides the GitLab Environment Toolkit (GET) to help provision resources.                   |
|  14 | Satellite services are deployed as add-ons; core GitLab functionality remains in the monolith (Omnibus package).                                                            |
|  15 | Omnibus package will not be discontinued; new services will be Kubernetes-focused add-ons.                                                                                  |
|  16 | Unified Helm chart is convenient but hard to maintain; discussions ongoing about future chart structure.                                                                    |
|  17 | Kubernetes adoption increases operational complexity for customers; training and infrastructure responsibility shift to them.                                               |
|  18 | Backwards compatibility is managed via strict API contracts and static checks, but challenges remain.                                                                       |
|  19 | LabKit application                                                                                                                                                          |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=vjF8HjM76wA)