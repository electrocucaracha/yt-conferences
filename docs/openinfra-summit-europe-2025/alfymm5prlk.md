---
layout: default
title: "OpenStack deployments made easy:   Kolla Ansible workshop"
nav_order: 1
parent: OpenInfra Summit Europe 2025
type: Video Note
description: "This workshop, led by Mikon Shhatka and Yakub, guides participants through deploying an OpenStack cloud using the Kolla-Ansible tool with the stable 2025.1 Epoxy release."
resource: "https://www.youtube.com/watch?v=aLfYmm5Prlk"
youtube_stats:
  view_count: 3393
  like_count: 37
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

This workshop, led by Mikon Shhatka and Yakub, guides participants through deploying an OpenStack cloud using the Kolla-Ansible tool with the stable 2025.1 Epoxy release.
The session begins with setting up a virtual environment, installing prerequisites such as Docker, and configuring global settings to use Ubuntu and disable unnecessary services like HAProxy for a single-node test deployment.
Attendees then execute pre-checks to validate the system state before running the main deployment command, which installs core OpenStack services.
Following the deployment, the instructors demonstrate how to initialize the cloud by creating networks, images, and flavors, and subsequently spawn a virtual machine that is accessible via a floating IP.
The presentation also covers the Kolla project’s background, its deliverables including Kolla and Kube, and various methods for contributing to the community, such as reporting bugs, reviewing patches, and participating in IRC channels.
Finally, the Q&A session addresses troubleshooting pre-checks, building custom containers, and managing service upgrades, emphasizing the importance of using stable branches and seeking help through official communication channels.

# Main Points

|   # | Main point                                                                                                                         |
| --: | ---------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Participants must connect to the guest network or the Open Infra Wi-Fi to receive email credentials for temporary internet access. |
|   2 | The workshop uses the Kolla-Ansible 2025.1 Epoxy release to avoid issues associated with the unstable master branch.               |
|   3 | Users must assign their names to specific virtual machines in the EtherPad document to prevent conflicts.                          |
|   4 | The SSH login credentials for the VMs are the username 'Ubuntu' and the password 'themopeninfra2025!'.                             |
|   5 | The deployment process begins by updating the operating system and installing required packages using sudo.                        |
|   6 | Ansible configuration is adjusted to increase fork amounts and disable host key checking for faster execution.                     |
|   7 | A separate virtual environment is created to install Kolla-Ansible from the Git repository.                                        |
|   8 | Example configuration files and the inventory file are copied to set up a single-node deployment for testing.                      |
|   9 | Dependencies for Kolla are installed from the Ansible Galaxy.                                                                      |
|  10 | A dummy network interface is added to serve as the external interface for Neutron.                                                 |
|  11 | Random passwords and secrets are generated and saved to a dedicated passwords file.                                                |
|  12 | The global configuration is modified to switch the distribution to Ubuntu and the release to Epoxy.                                |
|  13 | HAProxy and ProxySQL are disabled to simplify the single-node deployment and avoid VIP complexity.                                 |
|  14 | Prerequisites such as Docker are installed before running pre-checks to verify system readiness.                                   |
|  15 | Pre-checks validate missing packages, occupied ports, and other potential deployment blockers.                                     |
|  16 | The Kolla project provides production-ready containers and deployment tools for operating OpenStack clouds.                        |
|  17 | Kolla-Ansible is one of four main deliverables, alongside the Ansible collection, container images, and Kube.                      |
|  18 | Kube is used for deploying containerized OpenStack on bare metal, handling host provisioning and storage configuration.            |
|  19 | Contributors can help by writing code, testing, updating documentation, reporting bugs, or answering community questions.          |
|  20 | The project team encourages users to report bugs in Launchpad and propose fixes via Gerrit.                                        |
|  21 | Core reviewers are elected each cycle and are responsible for approving patches and steering project direction.                    |
|  22 | After deployment, the OpenStack client is installed to access the cloud via CLI using the generated cloud.yaml file.               |
|  23 | The Horizon dashboard is accessible via the public IP address of the deployed VM.                                                  |
|  24 | An init-run-once script creates necessary resources like images, networks, SSH keys, and flavors for testing.                      |
|  25 | A demo VM is spawned and accessed by configuring the external bridge gateway and attaching a floating IP.                          |
|  26 | Users can build custom containers using Kolla documentation and template overrides for additional packages.                        |
|  27 | CI jobs test upgrades between releases, including skip-level upgrades, to ensure stability.                                        |
|  28 | Configuration files can be tweaked by placing custom files in the etc/kolla/config directory.                                      |
|  29 | Neutron agent containers can be upgraded without affecting the data plane by using separate keepalived processes.                  |

# Video

[![Video thumbnail](https://img.youtube.com/vi/aLfYmm5Prlk/hqdefault.jpg)](https://www.youtube.com/watch?v=aLfYmm5Prlk)

[Watch on YouTube](https://www.youtube.com/watch?v=aLfYmm5Prlk)
