---
layout: default
title: "Make Python Talk, Make Python Listen - Al Sweigart"
nav_order: 33
parent: PyCon US 2025
type: Video Note
description: "At the PyConUS conference, Al Sweigart and Monty presented a talk on leveraging Python for text-to-speech, speech recognition, and optical character recognition (OCR)."
resource: "https://www.youtube.com/watch?v=bHUvzkuf3Qk"
youtube_stats:
  view_count: 1616
  like_count: 63
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

At the PyConUS conference, Al Sweigart and Monty presented a talk on leveraging Python for text-to-speech, speech recognition, and optical character recognition (OCR).
They introduced `pyttsx3` and `gTTS` for converting text to audio, noting that while `pyttsx3` uses local operating system voices, `gTTS` relies on Google’s API for consistent but internet-dependent results.
For speech recognition, they highlighted OpenAI’s Whisper model, which runs offline, supports multiple languages, and generates punctuated transcripts, making it ideal for creating searchable audio databases.
The presentation also covered OCR using the Tesseract engine and `pytesseract` library, demonstrating how to extract text from scanned documents and create searchable PDFs.
Beyond technical implementation, the speakers emphasized the ethical responsibilities of developers, warning that these accessible tools can be misused for mass surveillance, such as tracking individuals via license plate recognition or creating invasive data profiles, urging the audience to consider the societal impact of their code.

# Main Points

|   # | Main point                                                                                                                               |
| --: | ---------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Al Sweigart and Monty presented a talk on making Python talk, listen, and read images at PyCon US.                                       |
|   2 | The presentation covered three main areas: text-to-speech, speech recognition, and optical character recognition (OCR).                  |
|   3 | All discussed packages are free and compatible with Windows, macOS, and Linux.                                                           |
|   4 | Slides and code examples are available for download at inventwithpython.com/makepython talk2025.                                         |
|   5 | The pyttsx3 package converts text to audio using the operating system's built-in speech engine.                                          |
|   6 | Pyttsx3 requires calling the runAndWait method to execute speech, which blocks the program until finished.                               |
|   7 | Pyttsx3 currently supports saving audio only in the wave file format.                                                                    |
|   8 | The gTTS package uses Google Translate's undocumented API to generate speech, requiring an internet connection.                          |
|   9 | GTTS provides a consistent voice across operating systems but may stop working if Google changes its API.                                |
|  10 | OpenAI's Whisper package performs offline speech recognition without requiring an API key or subscription.                               |
|  11 | Whisper downloads machine learning models on first use and supports nearly every spoken human language.                                  |
|  12 | The base model of Whisper is recommended for most use cases, while the tiny model is faster but less accurate.                           |
|  13 | Whisper can generate subtitle files with timestamps, which is useful for searching long audio recordings.                                |
|  14 | The pytesseract package enables OCR by interfacing with the separately installed Tesseract engine.                                       |
|  15 | Tesseract is designed for typewritten text on light backgrounds and may require image preprocessing for accuracy.                        |
|  16 | Pytesseract supports multiple languages using ISO language codes and can extract text from images into strings.                          |
|  17 | The NAPS 2 application can be used via Python's subprocess module to create searchable PDFs from scanned images.                         |
|  18 | Text-to-speech technology can be used for creating audio books or generating mass disinformation campaigns.                              |
|  19 | Speech recognition technology lowers the cost of mass surveillance by allowing individuals to process large audio files locally.         |
|  20 | OCR technology can be used to track individuals via license plate recognition from low-cost hardware like Raspberry Pis.                 |
|  21 | Retailers can correlate license plates from parking lot cameras with credit card purchases to identify customers.                        |
|  22 | The Drivers Privacy Protection Act of 1994 limits DMV data sharing but does not prevent private companies from collecting location data. |
|  23 | Developers have a responsibility to consider the social effects and potential abuse of the powerful tools they create.                   |
|  24 | The third edition of Automate the Boring Stuff with Python covers these specific packages and techniques.                                |

# Video

[![Video thumbnail](https://img.youtube.com/vi/bHUvzkuf3Qk/hqdefault.jpg)](https://www.youtube.com/watch?v=bHUvzkuf3Qk)

[Watch on YouTube](https://www.youtube.com/watch?v=bHUvzkuf3Qk)
