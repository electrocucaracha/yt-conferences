---
layout: default
title: Unveiling a TUI for Simple OpenStack Deployments
nav_order: 91
parent: OpenInfra Summit Europe 2025
type: Video Note
description: "The speaker presents a free-time project designed to simplify the complex process of deploying OpenStack by creating a guided, text-based user interface (TUI) abstraction layer."
resource: "https://www.youtube.com/watch?v=Ag0337UQbaM"
youtube_stats:
  view_count: 69
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

The speaker presents a free-time project designed to simplify the complex process of deploying OpenStack by creating a guided, text-based user interface (TUI) abstraction layer.
This tool, built using Python and leveraging OpenStack Ansible as its core engine, aims to hide underlying complexity by offering a self-contained, dependency-free wizard that guides users through crucial configuration steps such as selecting versions, managing hosts, and defining networks.
During the live demonstration, the speaker showcased the tool’s ability to handle inventory management, validate inputs like IP addresses and netmasks, and generate configuration files, while acknowledging that the project is still in an MVP stage with some bugs and missing features like actual deployment execution.
The presentation also briefly introduced a complementary tool for monitoring cloud health, and the speaker outlined future plans to add support for Metal networking, predefined settings, and the ability to execute upgrades and encrypt secrets via Ansible Vault.

# Main Points

|   # | Main point                                                                                                                                                                          |
| --: | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | The presenter is a found architect in Cura working on a free-time project to simplify OpenStack deployment using a textual user interface.                                          |
|   2 | Getting started with OpenStack is difficult due to complex architecture, networking choices, and the need to learn specific deployment tools and their hidden parameters.           |
|   3 | The project aims to create a lightweight abstraction layer that hides complexity without introducing new heavy dependencies or requiring users to learn a new tool.                 |
|   4 | The tool, called Open Wizard, uses a guided process to lead users through crucial configuration and deployment steps while avoiding reinventing the wheel.                          |
|   5 | OpenStack Ansible was selected as the core deployment engine because the presenter is a project leader for it and knows it best.                                                    |
|   6 | The tooling is licensed under Apache 2.0, published on GitHub, and built using a Python framework for textual UIs.                                                                  |
|   7 | The current MVP release allows users to select an OpenStack version, pull repositories, prepare hosts, and configure inventory and parameters.                                      |
|   8 | The bootstrap process handles pulling requirements, Ansible roles, and collections, then reports status upon completion.                                                            |
|   9 | Users can manage hosts by adding them to groups with IP addresses, with safeguards preventing invalid inputs like incorrect netmasks.                                               |
|  10 | The tool includes an editor for the OpenStack inventory file, allowing users to view and edit configurations such as networks and interfaces.                                       |
|  11 | Service configuration options include internal and external endpoints, PKI settings, proxy settings, and interface bindings with help messages.                                     |
|  12 | The tool is designed to work with existing deployments by catching up and editing configurations in place, though this is not guaranteed.                                           |
|  13 | Future plans include adding Metal networking configuration, safe deployment execution, upgrade capabilities, and Ansible Vault encryption for secrets.                              |
|  14 | Additional features planned for end of the year include predefined settings for huge pages, aggregates, and creating OpenStack resources like flavors and images.                   |
|  15 | The presenter also demonstrated Cloudification Try, a separate textual UI tool for checking cloud state and service health, which uses Swift and is designed for macOS.             |
|  16 | Help texts in the tool are currently written manually by the presenter based on OpenStack talks and implementation knowledge, with dynamic loading considered a future possibility. |

# Video

[![Video thumbnail](https://img.youtube.com/vi/Ag0337UQbaM/hqdefault.jpg)](https://www.youtube.com/watch?v=Ag0337UQbaM)

[Watch on YouTube](https://www.youtube.com/watch?v=Ag0337UQbaM)
