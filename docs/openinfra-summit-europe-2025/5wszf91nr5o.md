---
layout: default
title: Hands On Migration from VMware to OpenStack with Ansible and AWX
nav_order: 44
parent: OpenInfra Summit Europe 2025
type: Video Note
description: "Pedro, a product manager at Red Hat, introduces a hands-on lab session focused on migrating virtual machines from VMware to Red Hat OpenStack Service on OpenShift."
resource: "https://www.youtube.com/watch?v=5Wszf91NR5o"
youtube_stats:
  view_count: 172
  like_count: 2
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

Pedro, a product manager at Red Hat, introduces a hands-on lab session focused on migrating virtual machines from VMware to Red Hat OpenStack Service on OpenShift.
The session features two distinct migration methods: one using a bastion host with an Ansible playbook command and another utilizing AWX, the upstream project for Ansible Automation Platform, installed on Kubernetes.
Participants are provided with a dedicated, pre-configured OpenStack environment running on nested virtualization, which includes a conversion host, a compute node, and target VMs for both Linux and Windows.
Due to network restrictions that block direct SSH ports, attendees are instructed to access the bastion terminal by duplicating their browser tab and appending "/terminal" to the URL, rather than using their local terminals.
The presenters emphasize the importance of deleting migrated VMs before starting the next migration to avoid resource exhaustion in the nested environment and provide troubleshooting tips, such as checking conversion logs on the host and using specific OpenShift commands to access the Horizon dashboard if standard routes fail.

# Main Points

|   # | Main point                                                                                                                         |
| --: | ---------------------------------------------------------------------------------------------------------------------------------- |
|   1 | The session is led by Pedro, Amy, and Matthew from Red Hat to demonstrate VMware to OpenStack migrations.                          |
|   2 | Two migration methods are covered: one using an Ansible playbook via a bastion host and another using AWX installed in Kubernetes. |
|   3 | Participants receive a dedicated Red Hat OpenStack Service on OpenShift environment with pre-installed components.                 |
|   4 | The lab environment uses nested virtualization, so bare-metal performance should not be expected.                                  |
|   5 | The infrastructure includes a bastion host, a vCenter, three OpenShift master workers, and one compute node.                       |
|   6 | Two target virtual machines are provided for migration: one running Haroxy and one running Windows.                                |
|   7 | Users must delete the migrated VM before starting the second migration to avoid resource exhaustion failures.                      |
|   8 | Lab access requires logging in with a consistent email address to resume sessions if disconnected.                                 |
|   9 | The password for the lab environment is OpenStack.                                                                                 |
|  10 | Direct SSH connections are blocked by Wi-Fi restrictions, so users must use the provided web terminal.                             |
|  11 | To access the terminal, users should duplicate the lab tab and add /terminal to the URL.                                           |
|  12 | The web terminal is pre-logged in as the lab user, eliminating the need for manual SSH authentication.                             |
|  13 | The lab is accessible via mobile devices, though it is less convenient than using a desktop.                                       |
|  14 | Users can inspect conversion logs by logging into the conversion host and checking the /tmp directory.                             |
|  15 | The training materials and code are open source and available on GitHub for review and pull requests.                              |
|  16 | Migration processes and AWX installation require significant waiting time due to distributed lab deployment locations.             |
|  17 | A known bug prevents direct Horizon access, but users can retrieve the Horizon root URL using the oc get routes command.           |
|  18 | The session may extend beyond the scheduled time to assist participants who need more help.                                        |
|  19 | Feedback on the lab experience is encouraged to help improve future training sessions.                                             |

# Video

[![Video thumbnail](https://img.youtube.com/vi/5Wszf91NR5o/hqdefault.jpg)](https://www.youtube.com/watch?v=5Wszf91NR5o)

[Watch on YouTube](https://www.youtube.com/watch?v=5Wszf91NR5o)
