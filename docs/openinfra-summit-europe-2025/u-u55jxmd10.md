---
layout: default
title: Kolla User Forum
nav_order: 124
parent: OpenInfra Summit Europe 2025
type: Video Note
description: 'The video transcript records a community forum for the OpenStack Kolla project, where the project lead provides an update on the upcoming "Flamingo" release, targeted for November.'
resource: "https://www.youtube.com/watch?v=U-u55JXmd10"
youtube_stats:
  view_count: 45
  like_count: 1
  channel_subscriber_count: 46800
tags:
  - openinfra-summit-europe-2025
  - video
  - learning
status: stable
generated:
  by: process:yt-summarizer-okf
  at: 2026-11-22T23:38:50+00:00
---

# Summary

The video transcript records a community forum for the OpenStack Kolla project, where the project lead provides an update on the upcoming "Flamingo" release, targeted for November.
Key technical changes include the migration of services like Cinder, Nova, and Heat to WSGI HTTP mode to improve performance, the removal of VMware and HAProxy database load balancing support, and the splitting of Neutron into four distinct containers to align with upstream changes.
The session also highlights ongoing efforts to enhance the development process, such as updating the contribution guide, establishing IRC and Matrix communication channels, and addressing the need for more active reviewers to manage the patch queue.
Participants discussed various feature requests and issues, including support for dual-stack IPv4/IPv6 on external load balancers, DNS-01 challenges for ACME, and the need for better CI coverage for external MariaDB and RabbitMQ clusters.
The team encouraged community members to contribute patches, report bugs with detailed logs, and participate in upcoming virtual events to help plan new features and resolve outstanding problems.

# Main Points

|   # | Main point                                                                                                                                                         |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   1 | A virtual project team gathering for users and developers is scheduled for the week after the forum to discuss new features, problems, and upstream contributions. |
|   2 | The Flamingo release is targeted for November, though Ansible Core 2.19 has caused issues with data tracking APIs requiring play and module rewrites.              |
|   3 | Services are being migrated from Apache to UWSGI HTTP mode to improve API performance and address Python setup tool limitations.                                   |
|   4 | VMware support has been dropped due to the discontinuation of the ironic inspector, favoring the built-in ironic service.                                          |
|   5 | Database load balancing with HAProxy is no longer supported, defaulting to ProxySQL which has been the standard since the Epoxy cycle.                             |
|   6 | OpenStack containers now include environment variables allowing commands to run on any controller node, not just the active one.                                   |
|   7 | Prometheus exporters have been split into separate roles for node and cAdvisor to improve deployment performance.                                                  |
|   8 | Fluentd now sends logs directly to OpenSearch nodes, bypassing the load balancer.                                                                                  |
|   9 | Neutron services are split into four distinct containers: server, RPC server, maintenance worker, and OVN maintenance worker.                                      |
|  10 | A check in Nova has been added to prevent downgrading the library.                                                                                                 |
|  11 | Better support is requested for splitting external and internal load balancers without overlays to improve security and separation of concerns.                    |
|  12 | Users request improved support for active-active setups using BGP anycast without keepalived, suggesting sequential restarts and IP deactivation.                  |
|  13 | Dual-stack IPv4 and IPv6 support for the external load balancer is requested to allow simultaneous use of both protocols.                                          |
|  14 | The development process is being improved by updating the contributor guide with contact information and review processes.                                         |
|  15 | More reviewers are needed to move patches forward, with an emphasis on meaningful reviews over simple approvals.                                                   |
|  16 | Communication channels include IRC, Matrix bridge, and mailing lists, with weekly meetings held on Wednesdays.                                                     |
|  17 | Dedicated domains for services are confirmed to still be supported and functional.                                                                                 |
|  18 | Speeding up Ansible for large numbers of hypervisors is a priority, requiring users to provide timing details and logs for debugging.                              |
|  19 | DNS-01 challenge support for ACME via Lego is being worked on, with potential refactoring of Let's Encrypt integration.                                            |
|  20 | Configuration generation changes are requested to allow custom directories for primitive YAML files.                                                               |
|  21 | Handling Ansible inventories for offline hosts is being improved, with documentation updates planned for the 25.1 release.                                         |
|  22 | Support for the BGP agent is limited due to lack of CI testing and reviewers, though native OVN support is expected to reduce this need.                           |
|  23 | A push gateway container is not currently deployed, and a port conflict with the default metrics port has been identified.                                         |
|  24 | External MariaDB and RabbitMQ clusters are supported but lack CI coverage, leading to occasional breakage with new versions.                                       |
|  25 | PostgreSQL support is complicated by community CI failures, but it may be possible to enable via container image overrides.                                        |
|  26 | Debian support is expected to improve as maintainers from Infomaniac join the project.                                                                             |
|  27 | Cherry-picking bugfixes to stable releases is encouraged to ensure all supported versions receive updates.                                                         |
|  28 | The OpenStack community is planning to transition from Slack to Matrix for communication.                                                                          |
|  29 | Published container images are intended for testing and development, while production use should involve building custom images with timestamps.                   |

# Video

[![Video thumbnail](https://img.youtube.com/vi/U-u55JXmd10/hqdefault.jpg)](https://www.youtube.com/watch?v=U-u55JXmd10)

[Watch on YouTube](https://www.youtube.com/watch?v=U-u55JXmd10)
