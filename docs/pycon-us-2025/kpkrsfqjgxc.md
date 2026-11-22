---
layout: default
title: "Working with Audio in Python (feat. Pedalboard) - Peter Sobot"
nav_order: 40
parent: PyCon US 2025
type: Video Note
description: "Peter Sobot, a staff machine learning engineer at Spotify, presents a comprehensive guide to working with audio in Python, focusing on the open-source library Pedalboard."
resource: "https://www.youtube.com/watch?v=kpKrsFqJgXc"
youtube_stats:
  view_count: 2762
  like_count: 119
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

Peter Sobot, a staff machine learning engineer at Spotify, presents a comprehensive guide to working with audio in Python, focusing on the open-source library Pedalboard.
He begins by explaining the fundamentals of digital audio, describing it as a stream of numerical samples representing pressure waves, and highlights the critical difference between compressed file sizes and the significantly larger memory footprint of uncompressed data.
Sobot demonstrates that while Python’s standard library can technically read and edit audio, it is low-level and inefficient; he advocates for using Pedalboard, which offers a natural, file-like interface for reading, slicing, and seeking through audio data.
A key takeaway is the importance of treating audio as a stream to prevent memory crashes in production environments, as loading entire files into memory can lead to excessive resource usage.
Furthermore, he illustrates that pure Python loops for digital signal processing are slow compared to vectorized operations or C++-backed libraries, showcasing how Pedalboard enables high-performance application of effects like reverb, distortion, and delay, as well as support for third-party VST plugins and real-time audio streaming.

# Main Points

|   # | Main point                                                                                                                                                          |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Peter Sobot, a staff machine learning engineer at Spotify, presented on working with audio in Python using the Pedalboard library.                                  |
|   2 | Sound is defined as pressure traveling through the air, and digital audio represents this as a stream of numbers measured at a specific sampling rate.              |
|   3 | Higher sampling rates, such as 44,100 Hz, capture more detail and higher frequencies, allowing for accurate reproduction of the original sound.                     |
|   4 | Digital audio data can be stored as uncompressed floating-point numbers, which are large, or compressed using formats like MP3, OGG, or FLAC to reduce file size.   |
|   5 | Python's standard library includes the wave module for reading WAV files, but it provides a low-level interface that requires manual parsing of byte strings.       |
|   6 | The Pedalboard library offers a high-level API that behaves like Python's built-in open function, allowing users to read, seek, and slice audio data easily.        |
|   7 | Audio editing in Python can be achieved by iterating through samples to apply effects like delay or distortion using mathematical functions such as tanh.           |
|   8 | Loading entire compressed audio files into memory can cause production crashes due to high compression ratios, where small files decompress into gigabytes of data. |
|   9 | To prevent memory issues, audio should be treated as a stream and processed in bounded chunks rather than loading the entire file at once.                          |
|  10 | Pure Python loops for digital signal processing are significantly slower than using optimized libraries like NumPy or C++-backed tools.                             |
|  11 | Pedalboard is a Python library that wraps C++ audio processing code, enabling fast application of effects like reverb, distortion, and delay.                       |
|  12 | The library supports chaining multiple plugins in series to create complex audio effects similar to a physical guitar pedalboard.                                   |
|  13 | Pedalboard can load third-party VST3 plugins, allowing users to access their GUIs and parameters directly within Python applications.                               |
|  14 | The library supports loading instrument plugins that accept MIDI input, enabling the rendering of synthesized audio from note data.                                 |
|  15 | Advanced features include on-the-fly resampling, time stretching, and encoding audio into various formats like MP3, FLAC, and OGG.                                  |
|  16 | Users can stream audio to speakers or record from microphones in real time using Pedalboard's audio stream functions.                                               |
|  17 | The library is lightweight enough to run on hardware like Raspberry Pi, as the heavy processing is handled by optimized C++ code.                                   |
|  18 | Seeking within compressed files is supported, with the library decoding frames as needed to reach the exact sample index requested.                                 |
|  19 | Pedalboard currently uses float32 as its internal format and does not support dithering or noise shaping for integer sample conversions.                            |
|  20 | The project is open source and available on GitHub, with documentation and an interactive browser demo provided for users to explore.                               |

# Video

[![Video thumbnail](https://img.youtube.com/vi/kpKrsFqJgXc/hqdefault.jpg)](https://www.youtube.com/watch?v=kpKrsFqJgXc)

[Watch on YouTube](https://www.youtube.com/watch?v=kpKrsFqJgXc)
