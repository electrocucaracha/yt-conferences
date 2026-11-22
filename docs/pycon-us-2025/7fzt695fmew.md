---
layout: default
title: "Missing the Apex: Predicting F1 Races with Python - Josh Weissbock"
nav_order: 92
parent: PyCon US 2025
type: Video Note
description: "Josh Weisbach presents a Python-based analysis of Formula 1 races, aiming to improve upon a 2017 academic paper that only correlated starting and finishing positions."
resource: "https://www.youtube.com/watch?v=7fZT695FMEw"
youtube_stats:
  view_count: 905
  like_count: 23
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

Josh Weisbach presents a Python-based analysis of Formula 1 races, aiming to improve upon a 2017 academic paper that only correlated starting and finishing positions.
He details the process of scraping clean historical data from formula1.com using libraries like Requests, BeautifulSoup, and Pandas, while handling edge cases such as weather-canceled sessions.
After wrangling the data into a comprehensive dataset covering 2006 to 2023, he employs statistical methods including contingency coefficients, Spearman’s rank correlation, and ordinal logistic regression to evaluate performance predictors.
The analysis reveals that qualifying position is the strongest indicator of race success, significantly outperforming practice session results, and demonstrates that predictive stability has increased in recent years due to regulatory changes and reduced mechanical failures.
This work illustrates how simple Python tools can be effectively used for sports analytics and academic research.

# Main Points

|   # | Main point                                                                                                                                                                                                                  |
| --: | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | The presentation focuses on using Python to analyze Formula 1 race data to predict outcomes, inspired by a critique of a 2017 academic paper that lacked depth.                                                             |
|   2 | The speaker, Josh Weisbach, is a PhD student at Carleton University with a background in computer science and sports analytics, having used Python since 2006.                                                              |
|   3 | Formula 1 is described as the pinnacle of motorsport, featuring custom-built open-wheel cars where tiny margins determine championship points and financial rewards.                                                        |
|   4 | The F1 season runs from March to December with 20 to 25 races, where teams earn points based on finishing positions to win driver and constructor championships.                                                            |
|   5 | A typical race weekend includes practice sessions on Friday, practice and qualification on Saturday, and the main race on Sunday, with qualification determining the starting grid.                                         |
|   6 | The motivation for the project was to improve upon a previous study that only analyzed top eight drivers from 2006 to 2009, ignoring weather, penalties, and full weekend evolution.                                        |
|   7 | Data was scraped from formula1.com using Python libraries such as requests, BeautifulSoup, and pandas, leveraging the site's clean HTML structure and static generation.                                                    |
|   8 | The scraping process included handling network failures with the retry package, adding random delays to avoid bot detection, and saving data to local CSV files.                                                            |
|   9 | Edge cases such as races canceled due to flooding or severe weather in 2017 and 2023 were identified and skipped during the data collection process.                                                                        |
|  10 | Data wrangling involved cleaning artifacts, normalizing session names, handling missing data, and removing sprint sessions to create a unified dataset of over 7,800 driver-race entries from 2006 to 2023.                 |
|  11 | The analysis began by replicating the original paper's baseline using a contingency coefficient, which yielded a value of 0.63 for the top eight drivers.                                                                   |
|  12 | Expanding the analysis to the top 20 drivers increased the contingency coefficient to 0.77, suggesting a stronger association between starting and finishing positions.                                                     |
|  13 | Further analysis using Spearman's rho and contingency coefficients across all sessions revealed that qualification is the strongest predictor of race success.                                                              |
|  14 | Practice sessions showed a progressive signal, with Practice 3 being the strongest indicator, followed by Practice 2 and then Practice 1.                                                                                   |
|  15 | A heatmap visualization using Seaborn and Matplotlib demonstrated a strong diagonal trend where high qualifying positions correlate with high finishing positions.                                                          |
|  16 | Analysis across different engine eras (V10, V8/KERS, Turbo Hybrid) indicated that predictive stability has increased in recent years due to greater focus on reliability and cost management.                               |
|  17 | Ordinal logistic regression was used to model race outcomes, confirming that qualification has a beta value almost four times larger than the next closest predictor, Practice 3.                                           |
|  18 | The study concludes that qualification is the most significant predictor of race success, and the methodology improves upon previous academic work by using a larger dataset and more comprehensive statistical approaches. |

# Video

[![Video thumbnail](https://img.youtube.com/vi/7fZT695FMEw/hqdefault.jpg)](https://www.youtube.com/watch?v=7fZT695FMEw)

[Watch on YouTube](https://www.youtube.com/watch?v=7fZT695FMEw)
