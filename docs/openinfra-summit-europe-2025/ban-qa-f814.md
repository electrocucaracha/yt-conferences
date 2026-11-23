---
layout: default
title: "OpenInfra at the service of weather forecasting: An update from ECMWF"
nav_order: 25
parent: OpenInfra Summit Europe 2025
type: Video Note
description: "Harry Communos, an OpenStack engineer at the European Centre for Medium-Range Weather Forecasts (ECMWF), presented an overview of the organization’s mission to produce numerical weather forecasts a..."
resource: "https://www.youtube.com/watch?v=ban-qA-F814"
youtube_stats:
  view_count: 245
  like_count: 6
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

Harry Communos, an OpenStack engineer at the European Centre for Medium-Range Weather Forecasts (ECMWF), presented an overview of the organization’s mission to produce numerical weather forecasts and monitor the Earth system.
ECMWF, an intergovernmental body founded in 1975, processes nearly 800 million daily observations to create detailed weather snapshots, maintaining a massive data archive that grows by 800 terabytes each day.
Since 2019, the center has integrated OpenStack infrastructure to enhance its capabilities, currently operating two clouds that support approximately 2,000 virtual machines.
Communos highlighted three key projects leveraging this infrastructure: the Data Stores, a platform serving over 90 terabytes of climate and atmospheric data daily to thousands of users; Anamoy, a Python-based framework for AI-driven forecasting that bridges HPC and OpenStack environments; and Forecast in a Box, an experimental, containerized system that allows users to run data-driven forecasts on single GPUs or laptops.
The presentation concluded by emphasizing that while weather cannot be controlled, ECMWF’s staff and OpenStack technology enable better preparation for events like fires and floods, solidifying OpenStack’s critical role in the center’s operations.

# Main Points

|   # | Main point                                                                                                                                    |
| --: | --------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | ECMWF is an intergovernmental organization founded in 1975 to produce numerical weather forecasts and monitor the Earth system.               |
|   2 | The center receives nearly 800 million observations daily from global systems to create detailed snapshots of the Earth's weather.            |
|   3 | ECMWF maintains a tape archive that is currently 1.5 exabytes in size, with approximately 800 terabytes of data added daily.                  |
|   4 | In 2019, ECMWF began investigating OpenStack to support its mission, migrating infrastructure from England to Bologna in 2022.                |
|   5 | As of 2025, ECMWF operates two Caracal-based OpenStack clouds powering around 2,000 virtual machines.                                         |
|   6 | The Data Stores project, launched in 2017, serves as a data access platform transmitting subsets of archived data to users globally.          |
|   7 | OpenStack infrastructure supports the Data Stores by using VMs and Kubernetes containers to fetch, filter, and manipulate data from archives. |
|   8 | The Data Stores platform serves over 90 terabytes of data daily to more than 4,500 users from over 175 cataloged records.                     |
|   9 | Data Stores comprise three services: Climate Data Store, Atmospheric Data Store, and Emergency Management Service.                            |
|  10 | The Anamoy project generalizes the AIFS codebase to allow wider functionality for a greater set of users in AI-based forecasting.             |
|  11 | Anamoy consists of Python packages for training and modeling data-driven weather forecasts, available on GitHub under a permissive license.   |
|  12 | Anamoy operates between HPC and OpenStack, with training on HPC and inference, catalogs, and datasets served through OpenStack.               |
|  13 | Forecast in a Box is an experimental project packaging AI forecasting models into Docker containers and binaries for easy deployment.         |
|  14 | Forecast in a Box allows users to run complete forecasting systems on single GPUs, VMs, or laptops without relying on large data transfers.   |
|  15 | ECMWF staff of over 550 members use OpenStack to disseminate climate data and prepare for events like fires and flooding.                     |
|  16 | The organization emphasizes that while weather cannot be controlled, preparation is possible through advanced forecasting and data access.    |

# Video

[![Video thumbnail](https://img.youtube.com/vi/ban-qA-F814/hqdefault.jpg)](https://www.youtube.com/watch?v=ban-qA-F814)

[Watch on YouTube](https://www.youtube.com/watch?v=ban-qA-F814)
