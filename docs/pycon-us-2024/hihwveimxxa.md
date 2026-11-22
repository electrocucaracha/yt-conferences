---
layout: default
title: "Talks - Jacob Lapenna: Open Source Industrial Control: Turning 2,800 Tons of Metal with Python..."
nav_order: 167
parent: PyCon US 2024
type: Video Note
description: "Jacob, an electrical engineer at the US Bureau of Reclamation, presents an open-source industrial control system designed to precisely rotate massive hydroelectric turbines for maintenance tasks su..."
resource: "https://www.youtube.com/watch?v=HIHwvEImxxA"
youtube_stats:
  view_count: 275
  like_count: 7
  channel_subscriber_count: 34500
tags:
  - pycon-us-2024
  - video
  - learning
status: stable
generated:
  by: process:yt-summarizer-okf
  at: 2026-11-22T10:18:11+00:00
---

# Summary

Jacob, an electrical engineer at the US Bureau of Reclamation, presents an open-source industrial control system designed to precisely rotate massive hydroelectric turbines for maintenance tasks such as bearing alignment and sensor mapping.
By converting these large machines into DC stepper motors, the system allows for slow, controlled rotation without the safety risks and inefficiencies of manual labor.
The solution utilizes a distributed computing architecture featuring Raspberry Pi controllers, Python, and a web-based interface, which offers advantages over traditional PLC ladder logic, including version control, ease of use, and scalability.
Key components include a custom hardware setup with power distribution boxes, SCR-based current routing, and sensors like rotary encoders and laser pulses to determine drive ratios and machine geometry.
The system also enables advanced diagnostics, such as real-time partial discharge mapping using NFC antennas and air gap analysis, providing asset managers with critical data to optimize repairs and prevent catastrophic failures.

# Main Points

|   # | Main point                                                                                                                                                                                          |
| --: | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | The speaker is an electrical engineer at the US Bureau of Reclamation managing water infrastructure, including 600 dams and 53 hydro plants across 17 western states.                               |
|   2 | Rotating machines consist of a rotor (rotating part) and stator (stationary part), with the rotor acting as an electromagnet spinning past stator windings to generate current.                     |
|   3 | Slow roll testing is required for tasks like bearing alignment and signal mapping, which previously involved unsafe manual pushing by personnel.                                                    |
|   4 | The system converts giant rotating machines into DC stepper motors by applying current to stator phases to create magnetic fields that align with rotor poles, enabling precise, discrete rotation. |
|   5 | A 2020 prototype used physical switches and potentiometers but was cumbersome, required specialized knowledge, and lacked precise positioning or modularity.                                        |
|   6 | The improved system uses Python, Raspberry Pi, and web technologies (Flask, Celery, Redis, WebSockets) to create a browser-based application for control and monitoring.                            |
|   7 | A browser-based interface was chosen to avoid software installation on government-furnished machines, reduce training needs, and leverage proven, scalable web technologies.                        |
|   8 | The system is fully air-gapped for security, using local hosting for libraries and communication, and is housed in portable Pelican cases for easy deployment.                                      |
|   9 | Hardware includes a distribution box for 480V power, control boxes with Raspberry Pis, and power supplies controlled via PMBus (I2C) for scalable current injection into rotor and stator.          |
|  10 | A distributed computing architecture uses the rotor box as the central controller, sending tasks via a Redis message broker to Celery workers on stator boxes for execution.                        |
|  11 | Current direction is controlled using SCRs (Silicon Controlled Rectifiers) triggered by a 555 timer and pulse transformer, allowing precise routing of current through stator phases.               |
|  12 | Sensors include a once-per-revolution laser pulse and an 8-bit Gray code rotary encoder to measure rotation and determine the drive ratio for calibration.                                          |
|  13 | A real-time oscilloscope in the web interface visualizes sensor data, enabling calibration by tracking encoder counts between laser pulses to map pole positions.                                   |
|  14 | Future work includes automating continuous rotation and parking, approximating slip ring circumference using a machined jig and laser distance measurement for automated calibration.               |
|  15 | Partial discharge mapping uses an NFC antenna on the rotor to detect insulation degradation in stator windings, allowing trend analysis for predictive maintenance.                                 |
|  16 | Air gap measurement uses a proximity probe and rotary encoder to monitor machine shape in real time, preventing cyclic forcing that could damage the machine.                                       |
|  17 | The project was self-funded through a grant with no initial organizational support, but regions are now purchasing test sets and seeking facilitated adoption.                                      |
|  18 | Safety is ensured by air-gapping the system and limiting power to 40 kW, which is significantly lower than the machine’s normal operating power, preventing damage from control errors.             |

# Video

[![Video thumbnail](https://img.youtube.com/vi/HIHwvEImxxA/hqdefault.jpg)](https://www.youtube.com/watch?v=HIHwvEImxxA)

[Watch on YouTube](https://www.youtube.com/watch?v=HIHwvEImxxA)
