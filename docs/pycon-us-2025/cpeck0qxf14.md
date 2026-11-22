---
layout: default
title: "Looking At Audio - Łukasz Langa"
nav_order: 96
parent: PyCon US 2025
type: Video Note
description: "Lucas Schlanga presents a session on understanding sound through visual aids, explaining that audio is a mechanical wave requiring a medium like air to propagate."
resource: "https://www.youtube.com/watch?v=CPECk0QXF14"
youtube_stats:
  view_count: 740
  like_count: 31
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

Lucas Schlanga presents a session on understanding sound through visual aids, explaining that audio is a mechanical wave requiring a medium like air to propagate.
He demonstrates how regular cyclic pulses create beats and tempo, while higher frequencies result in pitch and harmony, using PyScript and Three.js to render interactive 3D visualizations of sound propagation and waveforms directly in the browser.
The talk covers the technical aspects of digital audio, including sample rates, amplitude, and the use of the Fast Fourier Transform to generate spectrograms that reveal frequency content and harmonics over time.
Schlanga showcases practical applications of these concepts, such as converting a Python logo image into an audible audio file and creating real-time frequency analyzers that react to live input.
He concludes by emphasizing that all these complex audio processing tasks can be achieved with concise Python code running client-side, highlighting the power of Pyodide and PyScript for creating engaging, interactive audio-visual experiences without server-side dependencies.

# Main Points

|   # | Main point                                                                                                                         |
| --: | ---------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Sound is a mechanical wave that requires a medium, such as air, to propagate by moving air molecules.                              |
|   2 | A simplified speaker produces sound by changing electric current to move a coil, which pushes air to create pressure disturbances. |
|   3 | Regular cyclic pulses create beats and tempo, while irregular pulses result in non-musical noise.                                  |
|   4 | The visualization of sound propagation was created using PyScript, allowing Python code to run in the browser.                     |
|   5 | The 3D scene is built with Three.js, a JavaScript library accessible via PyScript and Pyodide.                                     |
|   6 | An orthographic camera is used to render the scene, providing a view where parallel lines do not converge at the horizon.          |
|   7 | Audio amplitude is stored in 32-bit floating-point wave files as values between -1 and +1.                                         |
|   8 | Real-world audio oscillations are smooth curves rather than sudden digital steps, a phenomenon known as true peak.                 |
|   9 | Standard sample rates include 44.1 kHz for CD audio and 48 kHz for modern platforms like YouTube.                                  |
|  10 | Waveform visualizations display left and right stereo channels, allowing users to see specific instruments like drums.             |
|  11 | Oscilloscopes are useful for viewing single oscillation cycles to aid in tuning and synthesis analysis.                            |
|  12 | A 2:3 frequency ratio creates a perfect fifth interval, which is a consonant and desirable musical harmony.                        |
|  13 | Increasing the frequency of a repeating signal transitions the perception from rhythm and beats to pitch and harmony.              |
|  14 | Spectrograms display frequency over time, with white indicating loudness and black representing silence at -120 dB.                |
|  15 | Higher harmonics, or overtones, determine the timbre of a sound, distinguishing instruments like violins from saxophones.          |
|  16 | Sine waves do not have higher harmonics, unlike square waves which contain multiple frequency components.                          |
|  17 | The Fast Fourier Transform (FFT) is used to analyze signals, approximating the continuous Fourier Transform for digital audio.     |
|  18 | PyScript enables the use of NumPy and SciPy in the browser to convert visual data, such as images, into audio files.               |
|  19 | Real-time frequency analysis can drive 3D visualizations, allowing scenes to react dynamically to audio input.                     |
|  20 | Browser frame rates adapt to the display output, typically capping at 60 fps for standard HDMI connections.                        |
|  21 | An inaudible frequency above 20 kHz can be embedded in audio to synchronize visual effects with tempo changes.                     |
|  22 | All code examples are open source and available on PyScript.com for users to explore and modify.                                   |

# Video

[![Video thumbnail](https://img.youtube.com/vi/CPECk0QXF14/hqdefault.jpg)](https://www.youtube.com/watch?v=CPECk0QXF14)

[Watch on YouTube](https://www.youtube.com/watch?v=CPECk0QXF14)
