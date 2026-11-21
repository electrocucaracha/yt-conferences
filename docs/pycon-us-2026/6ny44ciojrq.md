---
layout: default
title: "How to Build Your First Real Time Voice Agent in Python...- Camila Hinojosa Añez, Elizabeth Fuentes"
nav_order: 56
parent: PyCon US 2026
type: Video Note
description: "The video transcript outlines the process of building an AI voice agent, defining it as software comprising a model and tools that operate within an agentic loop to process user prompts and execute..."
resource: "https://www.youtube.com/watch?v=6NY44ciOjRQ"
youtube_stats:
  view_count: 322
  like_count: 5
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

The video transcript outlines the process of building an AI voice agent, defining it as software comprising a model and tools that operate within an agentic loop to process user prompts and execute actions.
Two primary architectural approaches are presented: a decoupled voice agentic pipeline using separate components for speech recognition, language processing, and speech synthesis, and a speech-to-speech model that offers lower latency and more natural interaction at the cost of reduced control and debugging difficulty.
The presentation highlights Pipe Chat, an open-source framework that orchestrates these components in real-time, while emphasizing critical best practices such as optimizing latency, selecting efficient models, ensuring clean audio input, and implementing robust evaluation and monitoring for functional correctness and pronunciation errors.
A live demonstration features an "English Speaking Buddy" agent that helps non-native speakers improve their skills by correcting grammar and pronunciation while discussing stories from a knowledge base.
Finally, the discussion transitions to production deployment using AWS Amazon Bedrock Agent Core, which provides serverless infrastructure, built-in short-term and long-term memory, and observability, allowing the prototype to be scaled securely with authentication and infrastructure-as-code capabilities.

# Main Points

|   # | Main point                                                                                                                                                           |
| --: | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | An AI agent consists of a model and tools operating within an agentic loop to process user prompts and execute actions.                                              |
|   2 | Voice AI agents utilize voice as both input and output, requiring real-time interaction and specific architectural approaches.                                       |
|   3 | The voice agentic pipeline uses decoupled components for automatic speech recognition, language model processing, and text-to-speech synthesis.                      |
|   4 | The speech-to-speech approach integrates all components into a single neural network, offering lower latency but reduced control and debugging difficulty.           |
|   5 | Key orchestration components include audio capture via WebRTC, voice activity detection, speech recognition, and large language model processing.                    |
|   6 | Pipe Chat is an open-source framework that connects language models, speech recognition, and text-to-speech into a single real-time pipeline.                        |
|   7 | Optimizing latency is critical for voice AI agents, as every millisecond saved compounds across the conversation to improve user experience.                         |
|   8 | Developers should select efficient models balancing size and quality, utilize prompt caching for reduced latency, and ensure clean audio input.                      |
|   9 | Building incrementally allows developers to verify core functionality before adding complex context, while evaluation and monitoring track performance per turn.     |
|  10 | Monitoring must assess functional correctness, hallucinations, speech errors, pronunciation issues, and effective context and memory management.                     |
|  11 | The demo application, English Speaking Buddy, helps non-native speakers improve English by detecting and correcting grammar and pronunciation errors.                |
|  12 | The agent uses a database of stories to provide context, allowing users to discuss characters and plot points while receiving real-time feedback.                    |
|  13 | Amazon Bedrock Agent Core provides serverless infrastructure for production deployment, including runtime containers that support up to eight hours of conversation. |
|  14 | Built-in memory features in Amazon Bedrock include short-term conversation memory and long-term memory using a vector database for persistent recall.                |
|  15 | The production application uses Amazon Cognito for authentication and stores knowledge bases in Amazon S3 vector stores for retrieval-augmented generation.          |
|  16 | Infrastructure as code using the Cloud Development Kit allows for single-command deployment of the entire voice AI agent application.                                |
|  17 | The easiest part of building a voice agent is selecting and invoking model providers, while managing pipeline latency and agent behavior is the most challenging.    |
|  18 | Developers can manage agent verbosity by using prompts to instruct the model to stop talking and wait for user input.                                                |

# Video

[![Video thumbnail](https://img.youtube.com/vi/6NY44ciOjRQ/hqdefault.jpg)](https://www.youtube.com/watch?v=6NY44ciOjRQ)

[Watch on YouTube](https://www.youtube.com/watch?v=6NY44ciOjRQ)
