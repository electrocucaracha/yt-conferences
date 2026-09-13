---
type: Video Note
title: "Open Source at the Edge: Hardware, Firmware, and AI Stacks - Miley Fu & Saiyam Pathak"
description: "In this talk, Miley Fu and Sam Bak introduce Echo Kit, an open-source, Rust-based framework for building, customizing, and self-hosting voice AI agents on affordable edge devices like the ESP32 and Raspberry Pi. Echo Kit features open hardw..."
resource: https://www.youtube.com/watch?v=W9Uj8x_qimE
tags: ["kubecon-cloudnativecon-north-america-2025", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

In this talk, Miley Fu and Sam Bak introduce Echo Kit, an open-source, Rust-based framework for building, customizing, and self-hosting voice AI agents on affordable edge devices like the ESP32 and Raspberry Pi.
Echo Kit features open hardware, firmware, and server components, allowing users full ownership, transparency, and flexibility, with the ability to swap out AI service providers for ASR, LLM, and TTS functions.
The system captures audio via the device, sends it to a local or cloud-hosted server for processing, and returns responses in customizable voices, including user-trained or celebrity voices, with a focus on low latency and high performance.
The presenters demonstrate Echo Kit’s configuration, deployment, and use cases, including educational settings where Kubernetes and vcluster can manage multiple devices and classrooms efficiently.
They encourage contributions to the project and highlight the importance of open-source collaboration in advancing AI at the edge.
# Main Points

|   # | Main point                                                                                                                                    |
| --: | --------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Introduction of speakers: Miley Fu (Second State) and Sam Bak (vcluster, Cipmplify, CNCF TAG Operational Resilience)                          |
|   2 | Discussion topic: Open source edge hardware, firmware, and AI stacks                                                                          |
|   3 | Second State's CNCF project uses WebAssembly on the server side, suitable for AI inference, microservices, serverless, and embedded use cases |
|   4 | Go Sim is an open source conference co-hosted with Rust, with 2400 attendees                                                                  |
|   5 | Main focus: Rust-based open source project for voice AI agents                                                                                |
|   6 | AI services are often proprietary, black-box, with data privacy and customization concerns                                                    |
|   7 | Project: Echo Kit – a full stack, customizable, self-hosted voice AI agent framework                                                          |
|   8 | Echo Kit features open hardware, open firmware, and open server, all built in Rust                                                            |
|   9 | Edge device: ESP32 (captures/plays audio, connects via Wi-Fi), communicates with server via WebSockets                                        |
|  10 | Server orchestrates ASR (Automatic Speech Recognition), LM (Language Model), TTS (Text-to-Speech), and tool calls (e.g., MCPS)                |
|  11 | Porting to Raspberry Pi in collaboration with Raspberry Pi Foundation                                                                         |
|  12 | Device includes microphone, speaker, optional display; firmware initializes hardware components                                               |
|  13 | Server can be self-hosted locally or in the cloud; supports Docker/containerized deployment                                                   |
|  14 | AI pipeline: device sends voice data to server, server performs VAD (Voice Activity Detection), ASR, LM, TTS, and returns speech              |
|  15 | All pipeline components (ASR, LM, TTS) are swappable; supports various providers or local models                                              |
|  16 | YAML configuration file allows customization and swapping of components                                                                       |
|  17 | Option to use end-to-end models (e.g., Gemini Live), but with less customization and higher cost                                              |
|  18 | Live demo of Echo Kit device and server; supports training custom voices with a web tool (requires ~3 minutes of clean audio)                 |
|  19 | Use cases include AI education, workshops, hackathons, and voice-controlled devices (e.g., toy car)                                           |
|  20 | Kubernetes integration: each classroom can have a Raspberry Pi running Echo Kit server as a Kubernetes cluster (K3s)                          |
|  21 | Centr                                                                                                                                         |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=W9Uj8x_qimE)