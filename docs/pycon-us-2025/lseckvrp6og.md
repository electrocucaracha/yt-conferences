---
layout: default
title: "Detecting Honeybee Swarms Using the Integration of OpenCV, Pandas, AI, & PyTorch - Michael Dahlberg"
nav_order: 85
parent: PyCon US 2025
type: Video Note
description: "Michael Dolberg, a Linux systems administrator and beekeeper, presented a project to detect honeybee swarms using a Raspberry Pi, OpenCV, and PyTorch."
resource: "https://www.youtube.com/watch?v=LseCKvrp6og"
youtube_stats:
  view_count: 665
  like_count: 24
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

Michael Dolberg, a Linux systems administrator and beekeeper, presented a project to detect honeybee swarms using a Raspberry Pi, OpenCV, and PyTorch.
The system monitors hive entrances by capturing images every 30 seconds via a solar-powered camera setup, addressing the lack of power and internet connectivity at remote apiaries.
Images are pre-processed with OpenCV to enhance bee visibility and uploaded to AWS S3, where they are analyzed using a YOLOv8 model trained to count bees, although the presenter noted that manual annotation was labor-intensive.
To distinguish actual swarming events from normal bearding behavior, the system employs pandas to calculate a moving average of bee counts, identifying significant spikes that indicate a swarm.
While the technical pipeline was successfully built, the results were inconclusive as the monitored hive did not swarm during the testing period, prompting plans to deploy the system on another hive in the future.

# Main Points

|   # | Main point                                                                                                                                                            |
| --: | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Michael Dolberg is a Linux systems administrator, beekeeper, and Python programmer presenting a project to detect honeybee swarms.                                    |
|   2 | Honeybee hives consist of workers, drones, and a queen, with the queen laying up to 2,500 eggs daily before the hive swarms.                                          |
|   3 | Swarming involves the queen and approximately 50% of the bees leaving the hive to find a new location, while the remaining bees raise a new queen.                    |
|   4 | Swarm events can result in the loss of a colony if the swarm is not captured and the daughter hive fails to raise a new queen.                                        |
|   5 | The project uses a Raspberry Pi with a camera to capture images of the hive entrance every 30 seconds to monitor bee egress.                                          |
|   6 | Power is supplied by a solar system with a battery bank, MPPT charge controller, and a 12V to 5V buck converter for the Raspberry Pi.                                 |
|   7 | Internet connectivity is achieved using Ubiquiti LightBeam 5AC wireless bridges and a SunMax solar point charge controller.                                           |
|   8 | Images are uploaded to an AWS S3 bucket to facilitate off-site storage and access for AI analysis.                                                                    |
|   9 | OpenCV is used for image pre-processing, with Contrast Limited Adaptive Histogram Equalization (CLAHE) providing the best results for distinguishing individual bees. |
|  10 | Initial attempts to count bees using Marvin AI were deemed too simple, leading to the decision to train a custom YOLO V8 model with PyTorch.                          |
|  11 | Manual annotation of bees using OpenCV's CVAT tool was found to be tedious, prompting the use of AI-generated annotations or alternative tools.                       |
|  12 | Data analysis uses pandas to calculate a moving average of bee counts to distinguish between bearding and actual swarming events.                                     |
|  13 | A z-score is calculated from the moving average to identify significant increases in bee activity indicative of a swarm.                                              |
|  14 | Notifications are sent via SMS using Amazon Web Services Simple Notification Service when a swarm event is detected.                                                  |
|  15 | The project results were inconclusive as the monitored hive died from parasitic mite syndrome before swarming, and the swarm season ended.                            |
|  16 | Future plans include setting up another observation hive and exploring alternative computer vision models like YOLO-E or PCodeT for Raspberry Pi compatibility.       |

# Video

[![Video thumbnail](https://img.youtube.com/vi/LseCKvrp6og/hqdefault.jpg)](https://www.youtube.com/watch?v=LseCKvrp6og)

[Watch on YouTube](https://www.youtube.com/watch?v=LseCKvrp6og)
