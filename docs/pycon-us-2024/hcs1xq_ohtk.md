---
layout: default
title: "Talks - Jeff Epler: Connecting Old to New with CircuitPython: Retrocomputer input devices on..."
nav_order: 173
parent: PyCon US 2024
type: Video Note
description: Jeff Epler from Adafruit presented a talk on using CircuitPython to convert vintage computer input devices into modern USB Human Interface Devices (HID).
resource: "https://www.youtube.com/watch?v=hCs1XQ_OHtk"
youtube_stats:
  view_count: 104
  like_count: 3
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

Jeff Epler from Adafruit presented a talk on using CircuitPython to convert vintage computer input devices into modern USB Human Interface Devices (HID).
He demonstrated three specific projects: converting a Commodore 16 keyboard, a Tandy 1000 keyboard, and a NeXT Cube mouse into functional peripherals for contemporary PCs.
The Commodore project involved directly scanning a simple key matrix using a microcontroller, while the Tandy project required handling a more complex serial protocol by leveraging the RP2040 microcontroller’s Programmable I/O (PIO) peripheral to manage high-speed data capture.
The NeXT mouse conversion utilized quadrature encoders to track movement and buttons, with the final device housed in a custom 3D-printed enclosure.
Epler emphasized that these modifications are non-invasive and open-source, allowing users to preserve historical hardware while making it usable on modern systems, and he provided links to the full documentation and code for these projects.

# Main Points

|   # | Main point                                                                                                                   |
| --: | ---------------------------------------------------------------------------------------------------------------------------- |
|   1 | Jeff Epler from Adafruit presented three projects converting vintage input devices to USB HID using CircuitPython.           |
|   2 | The projects include a Commodore 16 keyboard, a Tandy 1000 keyboard, and a NeXT Cube bus mouse.                              |
|   3 | All projects are open source with MIT licenses and documented on learn.adafruit.com.                                         |
|   4 | The conversions are non-invasive and non-destructive, using plug-in connectors rather than cutting wires.                    |
|   5 | CircuitPython runs on microcontrollers with modest resources and supports nearly 500 boards.                                 |
|   6 | USB HID emulation allows microcontrollers to act as keyboards, mice, or gamepads.                                            |
|   7 | The RP2040 microcontroller was used for all projects, specifically on Adafruit QT Py and KB2040 boards.                      |
|   8 | Keyboard matrices use a grid of switches to control many keys with few pins, requiring row and column scanning.              |
|   9 | Ghost keys occur in older keyboards lacking diodes, limiting simultaneous key presses.                                       |
|  10 | The Commodore 16 keyboard conversion used a 27-line Python script with a lookup table for key mapping.                       |
|  11 | The Tandy 1000 keyboard contains an internal microcontroller that sends 8-bit data sequenced by clock signals.               |
|  12 | CircuitPython uses the PIO (Programmable IO) peripheral to handle high-speed serial data from the Tandy keyboard.            |
|  13 | The PIO peripheral operates asynchronously to Python code, allowing precise timing for data capture.                         |
|  14 | The Tandy keyboard code manages Num Lock and Caps Lock states internally via lookup tables.                                  |
|  15 | The NeXT Cube mouse uses quadrature encoders for movement detection, supported by CircuitPython's incremental encoder class. |
|  16 | The NeXT mouse conversion includes a feature where pressing both buttons emulates a middle mouse button.                     |
|  17 | A 3D-printed enclosure was created for the NeXT mouse converter to conceal wires and improve durability.                     |
|  18 | Additional projects include converting a NeXT keyboard and a Super Nintendo mouse.                                           |
|  19 | The PIO peripheral can handle fast serial interfaces that standard microcontroller code might miss.                          |
|  20 | Adafruit offers a 10% discount code, PyConPen, for attendees of the talk.                                                    |
|  21 | Live demos of the converted devices were available in the hallway track after the presentation.                              |

# Video

[![Video thumbnail](https://img.youtube.com/vi/hCs1XQ_OHtk/hqdefault.jpg)](https://www.youtube.com/watch?v=hCs1XQ_OHtk)

[Watch on YouTube](https://www.youtube.com/watch?v=hCs1XQ_OHtk)
