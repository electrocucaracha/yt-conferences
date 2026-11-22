---
layout: default
title: "Talks - Sergio Sanchez: What's up, pumpkin(_bot)? Data engineering for my mental health"
nav_order: 92
parent: PyCon US 2024
type: Video Note
description: 'Sergio Sánchez Zavala, a data engineer and creator of the "Tacos de Datos" community, presents a talk titled "¿Qué pasa, calabaza?" at PyCon, detailing his journey in developing a personal mental h...'
resource: "https://www.youtube.com/watch?v=kHyNVM8Fu8g"
youtube_stats:
  view_count: 86
  like_count: 1
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

Sergio Sánchez Zavala, a data engineer and creator of the "Tacos de Datos" community, presents a talk titled "¿Qué pasa, calabaza?" at PyCon, detailing his journey in developing a personal mental health tracking bot using Python.
Diagnosed with ADHD in 2021, he sought a solution to manage symptoms such as inattention, hyperactivity, and hyperfocus by creating a digital diary that minimizes the negative impact of these behaviors while channeling his energy into productive projects.
The system utilizes the Python Telegram Bot library to collect data in various formats, including text, images, and voice messages, which are stored in AWS S3 and processed through an ELT pipeline involving AWS Lambda, OpenAI’s Whisper for transcription, Snowflake, and dbt.
This architecture allows for the enrichment and analysis of personal data, enabling the bot to provide context-aware insights and reminders that help him organize his memories and maintain focus.
Ultimately, the presentation emphasizes the responsibility that comes with technical skills, advocating for the use of accessible, low-cost technologies to build impactful personal tools that enhance empathy and self-awareness.

# Main Points

|   # | Main point                                                                                                     |
| --: | -------------------------------------------------------------------------------------------------------------- |
|   1 | The speaker, Sergio Sánchez, is a data engineer at Talking Points and creator of Tacos de Datos.               |
|   2 | The talk focuses on building a Telegram bot to track mental health through text, images, and audio.            |
|   3 | The core theme is leveraging free or low-cost tools to create high-impact projects with minimal expense.       |
|   4 | The speaker was diagnosed with ADHD in 2021, which affects concentration, organization, and impulse control.   |
|   5 | The goal is to minimize the negative effects of ADHD symptoms like inattention, hyperactivity, and hyperfocus. |
|   6 | The solution involves organizing memories and using practices to manage attention and impulsivity.             |
|   7 | The bot is built using Python and the Python Telegram Bot library for easy interaction.                        |
|   8 | The application is deployed on fly.io using a Docker image.                                                    |
|   9 | Data is stored in an AWS S3 bucket for images, audio, and text entries.                                        |
|  10 | An AWS Lambda function triggers when audio files are uploaded to S3.                                           |
|  11 | The Lambda function converts OGG audio to MP3 using PyDub.                                                     |
|  12 | Transcribed audio is processed using OpenAI's Whisper model for text conversion.                               |
|  13 | Data is stored in a document database for flexibility in schema design.                                        |
|  14 | GitHub Actions automate data pipelines to send data to Snowflake.                                              |
|  15 | DBT is used within Snowflake to transform data using SQL and Jinja templates.                                  |
|  16 | Observable is used for business intelligence and data visualization from Snowflake.                            |
|  17 | The system allows for data collection, enrichment, and serving of raw or analyzed insights.                    |
|  18 | A web app within Telegram enables structured data collection via Likert scales and forms.                      |
|  19 | OpenAI Whisper costs approximately $0.006 per minute, making it cost-effective.                                |
|  20 | The project demonstrates how to extract, load, and transform data for personal analysis.                       |
|  21 | The speaker emphasizes the responsibility that comes with having technical skills to help others.              |
|  22 | The bot helps contextualize memories and provides reminders of past positive experiences.                      |
|  23 | The architecture supports multiple data formats to create a comprehensive digital diary.                       |
|  24 | The speaker encourages using automation to solve problems rather than manual tracking methods.                 |
|  25 | The project serves as a practical example of applying data engineering principles to personal life.            |

# Video

[![Video thumbnail](https://img.youtube.com/vi/kHyNVM8Fu8g/hqdefault.jpg)](https://www.youtube.com/watch?v=kHyNVM8Fu8g)

[Watch on YouTube](https://www.youtube.com/watch?v=kHyNVM8Fu8g)
