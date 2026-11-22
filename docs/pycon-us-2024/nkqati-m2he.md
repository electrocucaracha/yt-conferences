---
layout: default
title: "Talks - Eric Matthes: Using Python to assess landslide risk: A matter of life and death"
nav_order: 162
parent: PyCon US 2024
type: Video Note
description: "Eric Mattes, author of *Python Crash Course*, presented a project using Python to assess landslide risk in Southeast Alaska by analyzing stream gauge data."
resource: "https://www.youtube.com/watch?v=nKQaTi-M2hE"
youtube_stats:
  view_count: 211
  like_count: 4
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

Eric Mattes, author of _Python Crash Course_, presented a project using Python to assess landslide risk in Southeast Alaska by analyzing stream gauge data.
After experiencing fatal landslides in his hometown of Sitka, Mattes and local experts hypothesized that river behavior could serve as a proxy for soil saturation, a key factor in landslide activity.
He developed a simplified model that identifies "critical points" when the river rises at least 2.5 feet with a sustained rate of rise of 6 inches per hour, conditions historically correlated with landslide events.
By processing years of historical data, the tool demonstrated it could provide 30 to 60 minutes of warning before known slides, while also offering value by indicating when conditions are safe, helping to alleviate community anxiety during heavy rains.
Mattes released the tool as a public web application using Django, noting that while it has limitations such as a narrow geographic scope and potential false positives, it serves as a vital complement to official weather forecasts by providing real-time, localized insights into landslide risk.

# Main Points

|   # | Main point                                                                                                                                         |
| --: | -------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Eric Mattes, author of Python Crash Course, presented a tool using Python to assess landslide risk in Southeast Alaska.                            |
|   2 | The project originated from personal experience with fatal landslides in Sitka, Alaska, and a background in physics and education.                 |
|   3 | A shared hypothesis emerged that river behavior in small watersheds acts as a proxy for soil moisture and landslide risk.                          |
|   4 | Initial modeling attempts failed because they included too many variables, such as wind speed and rainfall.                                        |
|   5 | The refined approach focuses on two key factors: total river rise of at least 2.5 feet and a sustained rate of rise of at least 6 inches per hour. |
|   6 | Analysis of historical data showed that critical points were identified 30 to 60 minutes before known landslide events.                            |
|   7 | In a five-year period, the model identified nine critical periods, three of which were associated with known landslides.                           |
|   8 | The tool provides value by confirming when conditions are not critical, helping to reduce community anxiety during heavy rains.                    |
|   9 | The implementation uses standard Python libraries to process USGS stream gauge data and local landslide records.                                   |
|  10 | A Django web application was built to visualize real-time river data against historical critical thresholds.                                       |
|  11 | The tool was released to the public in June 2021 and has run reliably on a low-cost server since then.                                             |
|  12 | The approach complements official weather forecasts by providing short-term, real-time risk indicators.                                            |
|  13 | Limitations include the need for small, responsive watersheds and the inability to predict the exact location of a slide.                          |
|  14 | The project is not fully validated by geologists, and notification times are tight, ranging from 15 to 60 minutes.                                 |
|  15 | Mattes is moving to North Carolina and hopes an agency or local group will take over maintenance of the tool.                                      |
|  16 | Future work may include integrating river discharge rates and seismic data for better timestamping of events.                                      |
|  17 | The code contains an off-by-one error that was discovered late, though the current implementation remains valid for its evaluated scope.           |
|  18 | Community feedback is essential, as no tool can eliminate all false negatives without generating excessive false positives.                        |
|  19 | The project demonstrates that simple, focused data analysis can have significant real-world impact on public safety.                               |

# Video

[![Video thumbnail](https://img.youtube.com/vi/nKQaTi-M2hE/hqdefault.jpg)](https://www.youtube.com/watch?v=nKQaTi-M2hE)

[Watch on YouTube](https://www.youtube.com/watch?v=nKQaTi-M2hE)
