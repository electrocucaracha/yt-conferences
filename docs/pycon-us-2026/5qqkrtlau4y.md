---
layout: default
title: "A bridge over (not) troubled waters: Collecting marine data from your couch - Sarah Kaiser"
nav_order: 47
parent: PyCon US 2026
type: Video Note
description: "At PyCon, two experimental physicists presented their open-source project, \"Troubled Waters,\" which uses over-engineered telemetry to monitor the health and safety of their 1979 Tollycraft boat, th..."
resource: "https://www.youtube.com/watch?v=5QQKRTlau4Y"
youtube_stats:
  view_count: 199
  like_count: 4
  channel_subscriber_count: 34500
tags:
  - pycon-us-2026
  - video
  - learning
status: stable
generated:
  by: process:yt-summarizer-okf
  at: 2026-11-20T08:08:06+00:00
---

# Summary

At PyCon, two experimental physicists presented their open-source project, "Troubled Waters," which uses over-engineered telemetry to monitor the health and safety of their 1979 Tollycraft boat, the Sea Knot.
To address anxiety about potential mechanical failures and leaks while the boat is unattended at a marina four and a half miles away, they built a custom device called Anode, a home-brewed chart plotter that aggregates data from various sensors.
The system integrates NMEA 2000, Bluetooth, and Zigbee inputs into a unified data model using the Signal K open-source platform, allowing for real-time monitoring of critical parameters such as bilge humidity, cabin temperature, and electrical status.
This data is transmitted via MQTT over a Tailscale VPN connection to their home’s Home Assistant instance, providing remote observability and alerting capabilities.
Additionally, the team is exploring Meshtastic mesh networking to ensure reliable telemetry transmission independent of the marina’s Wi-Fi, ultimately aiming to create a robust, low-cost, and community-driven solution for marine safety and maintenance.

# Main Points

|   # | Main point |
| --: | ---------- |
|   1 | The speakers purchased a 1979 Tollycraft Sedan boat named Sea Knot during the pandemic to use as a floating camper. |
|   2 | They built a custom telemetry system called Anode to monitor boat health and reduce anxiety about potential failures. |
|   3 | Anode is a home-brewed chart plotter containing a Raspberry Pi, a RAK Meshtastic node, and a Yacht Devices NMEA 2000 bridge. |
|   4 | The system integrates data from various sources including NMEA 2000, Bluetooth, and Zigbee sensors into a unified data model. |
|   5 | Signal K serves as the central open-source software platform for processing data and providing navigation dashboards. |
|   6 | Zigbee sensors are converted to MQTT packets using the Zigbee2MQTT project to facilitate data integration. |
|   7 | Data is transmitted from the boat to the speakers' home via a Tailscale VPN connection and MQTT messaging. |
|   8 | Home Assistant at their residence receives the telemetry data to monitor cabin temperature, bilge humidity, and electrical status. |
|   9 | The boat is powered by a 12V DC house battery bank that remains connected to a charger while docked at the marina. |
|  10 | The speakers plan to test Meshtastic mesh networking to maintain telemetry connectivity in areas without reliable Wi-Fi. |
|  11 | The project is documented in a repository named Troubled Waters, which includes slides and code for the system. |
|  12 | The speakers use a family wiki and paper schematics to organize their thoughts and manage the complexity of the project. |
|  13 | The boat's fiberglass and wood construction allows for reliable Zigbee and Bluetooth signal transmission within its 27-foot length. |
|  14 | The system monitors critical safety parameters such as bilge water levels and heater performance to prevent damage. |
|  15 | The speakers emphasize that safety begins with awareness and continuous monitoring of the vessel's condition. |
|  16 | They acknowledge the corrosive marine environment and the need for precautions to ensure long-term hardware reliability. |
|  17 | The project combines their backgrounds in experimental physics and software development to solve practical boating challenges. |

# Video

[![Video thumbnail](https://img.youtube.com/vi/5QQKRTlau4Y/hqdefault.jpg)](https://www.youtube.com/watch?v=5QQKRTlau4Y)

[Watch on YouTube](https://www.youtube.com/watch?v=5QQKRTlau4Y)
