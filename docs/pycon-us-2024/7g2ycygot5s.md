---
layout: default
title: "Tutorials - Juliana Karoline de Sous: Introduction to MicroPython getting started with BBC micro:bit"
nav_order: 12
parent: PyCon US 2024
type: Video Note
description: "Juliana Kulu, a software engineer and Python community lead, presents an introductory tutorial on MicroPython using the BBC micro:bit, designed for pairs to work collaboratively."
resource: "https://www.youtube.com/watch?v=7g2YCygot5s"
youtube_stats:
  view_count: 1220
  like_count: 17
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

Juliana Kulu, a software engineer and Python community lead, presents an introductory tutorial on MicroPython using the BBC micro:bit, designed for pairs to work collaboratively.
The session covers the fundamentals of microcontrollers and MicroPython, explaining how this lightweight Python implementation runs on constrained hardware with limited memory.
Participants explore the micro:bit’s hardware components, including its LED matrix, buttons, accelerometer, and radio capabilities, using the online Python editor and simulator to test code before flashing it to the physical device.
The core of the tutorial involves building a Battleship game, starting with a single-player version where users tilt the board to aim and press buttons to shoot against a computer-generated map.
Finally, the group extends the project to a multiplayer mode, utilizing the micro:bit’s radio protocol to allow two devices to communicate, exchange shot coordinates, and determine a winner based on who sinks all ships first.

# Main Points

|   # | Main point                                                                                                                     |
| --: | ------------------------------------------------------------------------------------------------------------------------------ |
|   1 | The tutorial introduces MicroPython and the BBC micro:bit, focusing on physical computing and IoT applications.                |
|   2 | MicroPython is a Python 3 implementation written in C, optimized for microcontrollers with limited memory and power.           |
|   3 | The micro:bit is a pocket-sized computer designed for education, featuring an LED matrix, buttons, sensors, and a speaker.     |
|   4 | Participants work in pairs using the online Python editor at python.microbit.org to write and test code.                       |
|   5 | The editor includes a simulator for testing code without hardware and a reference guide for API documentation.                 |
|   6 | Key hardware components include the 5x5 LED display, A and B buttons, accelerometer, compass, microphone, and radio antenna.   |
|   7 | The display supports predefined images, custom pixel brightness levels, and scrolling text capabilities.                       |
|   8 | Input methods include button presses, accelerometer gestures, and radio communication between devices.                         |
|   9 | The radio module allows devices to communicate in groups using 2.4 GHz frequency, similar to Wi-Fi channels.                   |
|  10 | The main project is a Battleship game, starting with a single-player version against the computer.                             |
|  11 | The single-player game uses a 5x5 grid where ships are placed randomly without touching each other.                            |
|  12 | Players use the accelerometer to aim and button A to shoot, with feedback provided via sounds and images.                      |
|  13 | The game logic includes classes for the Sea (ship placement), Player (shooting logic), and Game (loop control).                |
|  14 | The multiplayer version requires two micro:bits communicating via radio to exchange shot coordinates and results.              |
|  15 | In multiplayer mode, players select their roles (Player 1 or 2) by pressing specific buttons before starting.                  |
|  16 | Player 1 shoots first, and the opponent responds with hit or miss status, alternating turns until all ships are sunk.          |
|  17 | The winner is determined by who sinks all opponent ships first, with distinct audio and visual feedback for victory or defeat. |
|  18 | Code templates are provided in a GitHub repository for participants to complete the single and multiplayer games.              |
|  19 | Potential improvements include tracking scores, allowing manual ship placement, and marking previous shots on the board.       |
|  20 | The tutorial emphasizes debugging using the REPL and handling radio communication errors during multiplayer testing.           |

# Video

[![Video thumbnail](https://img.youtube.com/vi/7g2YCygot5s/hqdefault.jpg)](https://www.youtube.com/watch?v=7g2YCygot5s)

[Watch on YouTube](https://www.youtube.com/watch?v=7g2YCygot5s)
