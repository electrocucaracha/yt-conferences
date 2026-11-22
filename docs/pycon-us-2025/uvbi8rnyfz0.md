---
layout: default
title: 'You can and Should Build XKCD''s "Sky Alarm" for Cool Space Things - Keith Murray'
nav_order: 97
parent: PyCon US 2025
type: Video Note
description: 'Keith Murray presents a practical guide to building a "sky alarm" inspired by the XKCD web comic, utilizing CircuitPython on a microcontroller to detect cool space phenomena.'
resource: "https://www.youtube.com/watch?v=UVbI8RnyFZ0"
youtube_stats:
  view_count: 549
  like_count: 20
  channel_subscriber_count: 34500
tags:
  - pycon-us-2025
  - video
  - learning
status: stable
generated:
  by: process:yt-summarizer-okf
  at: 2026-11-22T01:39:37+00:00
---

# Summary

Keith Murray presents a practical guide to building a "sky alarm" inspired by the XKCD web comic, utilizing CircuitPython on a microcontroller to detect cool space phenomena.
The project involves connecting an LED and a buzzer to a Metro ESP32S2 Express board, where the code remains highly familiar to standard Python syntax.
To determine when to trigger the alarm, the microcontroller connects to the internet via Wi-Fi to query the NOAA dashboard for Northern Lights forecasts, specifically monitoring the KP index for values of five or higher.
Murray enhances the basic setup by replacing the simple buzzer with audio playback and adding an animated LED strip using the Microlab library for a more engaging visual effect.
Furthermore, he integrates a local Flask server to handle time synchronization and data logging, allowing the system to record events and manage state without relying solely on the microcontroller’s limited resources.
Finally, the talk demonstrates how to expand the project’s capabilities by plugging in I2C sensors, such as air quality monitors, via the STEMMA QT connector, illustrating how easily Python can be used to create sophisticated, modular IoT devices.

# Main Points

|   # | Main point                                                                                                                                                  |
| --: | ----------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | The speaker introduces a project to build a sky alarm based on the XKCD web comic, which alerts users when cool space events occur.                         |
|   2 | The necessary components for the sky alarm include a box, a noise-making device, blinking lights, and a method to detect cool events.                       |
|   3 | The project utilizes microcontrollers and sensors, specifically using CircuitPython to maintain familiarity with standard Python coding.                    |
|   4 | Basic functionality involves blinking an LED and activating a buzzer when a cool space event is detected.                                                   |
|   5 | MicroPython and CircuitPython are implementations of Python subsets designed for low-power embedded systems with limited memory.                            |
|   6 | The specific hardware used is a Metro ESP32S2 Express board, chosen for its Wi-Fi capabilities and STEMMA QT port for easy sensor connection.               |
|   7 | The definition of a cool space event is restricted to Northern Lights, using the NOAA dashboard to forecast the KP index.                                   |
|   8 | The system queries the NOAA server for a 3-day forecast and triggers the alarm if the peak KP index is five or greater.                                     |
|   9 | Light pollution levels are considered to determine the feasibility of viewing Northern Lights from the user's location.                                     |
|  10 | Connecting to the web on a microcontroller requires initializing the Wi-Fi radio and signing on to the network using credentials stored in a settings file. |
|  11 | Data retrieval involves making a GET request to the server and parsing the response text to extract the relevant KP index values.                           |
|  12 | Enhancements to the basic alarm include using an LED strip with fading animations via the Microlab library for better visual effects.                       |
|  13 | Audio output is improved by playing wave files through a digital-to-analog converter instead of using a simple buzzer.                                      |
|  14 | A local Flask server can be built to provide real-time clock synchronization to the microcontroller, which lacks a built-in concept of current time.        |
|  15 | The server can also log data and handle remote queries, allowing the microcontroller to offload complex tasks to a more powerful Python environment.        |
|  16 | The architecture allows the Flask server to accept POST requests from the microcontroller and serve the latest data via GET requests.                       |
|  17 | Additional sensors, such as air quality monitors, can be connected via the STEMMA QT open standard connector without soldering.                             |
|  18 | The system can gather environmental data like temperature, humidity, and pressure, and send this information to the home server for further analysis.       |
|  19 | A machined aluminum base with drill holes is used to rigidly mount the microcontroller and sensors without permanent soldering.                             |
|  20 | The overall goal is to demonstrate how easily Python can be used to build interactive IoT devices that monitor and respond to real-world events.            |

# Video

[![Video thumbnail](https://img.youtube.com/vi/UVbI8RnyFZ0/hqdefault.jpg)](https://www.youtube.com/watch?v=UVbI8RnyFZ0)

[Watch on YouTube](https://www.youtube.com/watch?v=UVbI8RnyFZ0)
