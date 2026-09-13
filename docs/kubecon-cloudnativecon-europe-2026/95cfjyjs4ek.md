---
layout: default
title:
  "Virtual Power Plants (VPP): How They Work and What They Are - LeRenzo Malcom
  & Mario Flores, Enpal"
nav_order: 386
parent: Kubecon Cloudnativecon Europe 2026
type: Video Note
description:
  In this KubeCon presentation, Lorenzo and Mario from Enpal explain the
  concept of a virtual power plant (VPP) and its role in modernizing the energy grid.
  They begin by describing how traditional power grids operate, emphasizing the need
  fo...
resource: https://www.youtube.com/watch?v=95cFjYJS4ek
tags:
  - kubecon-cloudnativecon-europe-2026
  - video
  - learning
status: stable
generated:
  by: process:yt-conferences-okf
  at: 2026-09-12 00:00:00+00:00
---

# Summary

In this KubeCon presentation, Lorenzo and Mario from Enpal explain the concept of a virtual power plant (VPP) and its role in modernizing the energy grid.
They begin by describing how traditional power grids operate, emphasizing the need for generators to remain synchronized and the challenges posed by grid failures, such as the 2021 Texas blackout.
The speakers highlight the limitations of the current grid, especially as renewable energy sources like solar and wind become more prevalent, leading to issues like energy overproduction and curtailment.
To address these challenges, they propose integrating distributed batteries—located in homes with solar panels and electric vehicles—into a VPP, which can store excess energy and release it when needed, thereby stabilizing the grid and enabling rapid response to frequency fluctuations.
The technical architecture involves IoT devices, cloud-based control systems, and real-time data aggregation, allowing for efficient energy trading and grid management.
The presenters also discuss regulatory, technical, and market considerations, answer audience questions about scalability, integration, and security, and emphasize the complementary role of both large-scale and distributed storage in achieving a resilient, renewable-powered grid.

# Main Points

|   # | Main point                                                                                                                      |
| --: | ------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Presentation on virtual power plants (VPP) by Lorenzo and Mario from Enpal, a German solar panel company.                       |
|   2 | Enpal aims to build Europe’s largest VPP, connecting about 100,000 homes, equivalent to 1 gigawatt of energy.                   |
|   3 | The grid operates at a synchronized frequency (50 Hz in Europe, 60 Hz in the US); imbalance leads to failures.                  |
|   4 | Texas 2021 winter storm caused grid failures due to frozen wind, gas, coal, and nuclear assets, nearly resulting in a blackout. |
|   5 | The European grid is the largest machine ever, with 2.3 million workers, 305,000 transmission lines, and 400 million consumers. |
|   6 | The grid has no buffer; supply and demand must be balanced instantly, with a margin of only 2.5 Hz.                             |
|   7 | Traditional grid balancing uses spinning reserves, peaker plants, and load shedding; these methods are costly and inefficient.  |
|   8 | Renewables are rapidly growing, causing overproduction during the day (duck curve), leading to negative prices and curtailment. |
|   9 | Since 2015, 66 TWh of renewable energy has been curtailed in Germany, costing €6.5 billion and 28 megatons of CO2.              |
|  10 | Batteries can store excess renewable energy, enabling load shifting and grid stabilization.                                     |
|  11 | VPPs aggregate distributed assets (solar, batteries, EVs) to participate in energy markets and provide grid services.           |
|  12 | Enpal’s VPP uses IoT Home Energy Management Systems (HEMS) connected via MQTT (EMQX broker) to the cloud.                       |
|  13 | Real-time data aggregation and analytics are performed using Spark and Databricks, visualized in Grafana/DataDog.               |
|  14 | VPPs provide frequency containment/restoration, peak shaving, and energy arbitrage, responding in milliseconds.                 |
|  15 | Example: Tesla’s VPP in Australia stabilized the grid in 6 seconds after a major plant failure.                                 |
|  16 | Participation in VPPs requires a battery and smart meter; solar panels are optional.                                            |
|  17 | Enpal’s infrastructure runs mainly on Azure, with small Databricks clusters for streaming analytics.                            |
|  18 | Security: IoT devices authenticate via EMQX with username/password; future improvements                                         |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=95cFjYJS4ek)
