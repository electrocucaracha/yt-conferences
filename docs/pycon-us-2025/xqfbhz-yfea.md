---
layout: default
title: "Reduce the environmental footprint of your Python programs - Apoorv Garg"
nav_order: 20
parent: PyCon US 2025
type: Video Note
description: "Apor Aw, a software developer at Wells Fargo and open-source maintainer, presented a talk on reducing the environmental footprint of Python programs, highlighting that software development has a si..."
resource: "https://www.youtube.com/watch?v=XqFbHZ-YfeA"
youtube_stats:
  view_count: 783
  like_count: 10
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

Apor Aw, a software developer at Wells Fargo and open-source maintainer, presented a talk on reducing the environmental footprint of Python programs, highlighting that software development has a significant carbon impact, particularly with the rise of AI.
He explained that training a single large AI model can emit as much carbon as five cars produce in their lifetime, while data centers account for about 1% of global electricity use.
To measure this impact, he recommended tools like CodeCarbon, Green Algorithms, and Carbon Tracker, and identified key stakeholders including developers, companies, cloud providers, and regulatory bodies.
The core of the presentation focused on specific optimization techniques such as using efficient data structures, vectorization with NumPy, and memoization for general Python code, while for AI models, he detailed methods like quantization, pruning, caching, flash attention, and knowledge distillation.
These techniques were shown to significantly reduce energy consumption and memory usage—with quantization reducing emissions by 23–50% and distillation improving inference speed by up to 10x—often with minimal loss in accuracy.
Aw concluded by emphasizing the business value of green coding, noting that presenting these optimizations in terms of cost savings, speed improvements, and reduced technical debt helps secure buy-in from management and leadership.

# Main Points

|   # | Main point                                                                                                                                                             |
| --: | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | A single Google search generates approximately 2 to 7 grams of CO2, which accumulates significantly across the global population.                                      |
|   2 | Training a single large AI model can produce up to 500 metric tons of carbon, equivalent to the lifetime emissions of five cars.                                       |
|   3 | Data centers account for about 1% of global electricity usage, making them significant contributors to environmental impact.                                           |
|   4 | Python is an interpreted language, and certain operations can be more energy-intensive than those in compiled languages.                                               |
|   5 | Tools like CodeCarbon, Green Algorithms, and Carbon Tracker help measure the carbon footprint of Python programs and deep learning models.                             |
|   6 | Stakeholders who should care about code carbon footprints include developers, companies, cloud providers, end users, regulatory bodies, and future generations.        |
|   7 | Efficient data structures, such as using heaps or stacks over recursion, help minimize time and space complexity to reduce energy use.                                 |
|   8 | Vectorization using NumPy can significantly speed up Python programs when working with intensive arrays.                                                               |
|   9 | Memoization reduces execution time, for example from 1000 milliseconds to 100 milliseconds, by storing results of expensive function calls.                            |
|  10 | Efficient input and output operations are critical because they are heavy users of resources and produce substantial carbon emissions.                                 |
|  11 | Using generators and batching instead of loading all data into RAM at once helps manage memory usage and reduce energy consumption.                                    |
|  12 | Quantization reduces model size by using 8-bit integers instead of 32-bit floats, cutting emissions by 23% to 50% with minimal accuracy loss.                          |
|  13 | Pruning removes unnecessary components from neural networks, such as the smallest weights, to reduce energy consumption by 20% to 60%.                                 |
|  14 | Caching techniques in AI include data caching, prompt caching, semantic caching, and context caching to avoid redundant computations.                                  |
|  15 | Flash Attention optimizes transformer models by computing attention in blocks that fit in fast GPU memory, reducing data transfer bottlenecks.                         |
|  16 | Distillation involves training a smaller student model to mimic a larger teacher model, resulting in faster inferences and lower memory usage.                         |
|  17 | Communicating the value of green coding to stakeholders requires focusing on business benefits like reduced carbon taxes, improved speed, and maintained accuracy.     |
|  18 | Demonstrating proof of concepts and quantifying the effort required for implementation helps convince managers and product owners to prioritize sustainable practices. |

# Video

[![Video thumbnail](https://img.youtube.com/vi/XqFbHZ-YfeA/hqdefault.jpg)](https://www.youtube.com/watch?v=XqFbHZ-YfeA)

[Watch on YouTube](https://www.youtube.com/watch?v=XqFbHZ-YfeA)
