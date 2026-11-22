---
layout: default
title: Bridging IoT and Machine Learning with Python for Sustainable Agriculture
nav_order: 107
parent: PyCon US 2025
type: Video Note
description: "Alo from the Federal University of Technology, Akure, Nigeria, presented a talk on bridging IoT and machine learning with Python to enhance sustainable agriculture, highlighting the critical need f..."
resource: "https://www.youtube.com/watch?v=LF39_oyJtj0"
youtube_stats:
  view_count: 1418
  like_count: 28
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

Alo from the Federal University of Technology, Akure, Nigeria, presented a talk on bridging IoT and machine learning with Python to enhance sustainable agriculture, highlighting the critical need for data-driven solutions to combat food insecurity and climate change impacts in Africa.
The presentation introduced a case study involving a 75-day maize yield prediction experiment that utilized locally sourced IoT sensor data to address the limitations of international datasets, which often fail to account for specific regional soil and weather conditions.
By processing this data with Python libraries such as pandas, NumPy, and Scikit-learn, the team developed a smart farming pipeline that employed feature selection algorithms and machine learning models, including XGBoost, KNN, and Ridge Regressor, to accurately forecast crop yields.
The results demonstrated that XGBoost combined with SelectKBest feature selection achieved near-perfect accuracy, validating the effectiveness of integrating real-time IoT data with Python-based machine learning for precision farming.
The speaker emphasized that this scalable framework, with its publicly available dataset, aims to improve farm management decisions and resource efficiency, with future plans to expand the system’s application to other regions in Nigeria and across West Africa.

# Main Points

|   # | Main point                                                                                                                                                                      |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Agriculture is a crucial sector for global well-being, yet over 280 million people in Africa face food insecurity due to climate change and inefficient practices.              |
|   2 | Current farming methods have degraded over one-third of the world's productive topsoil while failing to meet the demands of a growing population.                               |
|   3 | Average global maize yields are projected to drop by 24% in the next 60 years, highlighting the urgent need for sustainable agricultural solutions.                             |
|   4 | The presentation focuses on bridging IoT and machine learning with Python to enable data-driven decision-making in smart farming.                                               |
|   5 | IoT devices collect real-time agricultural data from sensors, which is then processed and analyzed using Python libraries such as pandas, numpy, and scikit-learn.              |
|   6 | Machine learning applications in agriculture include predictive analysis for weather, disease outbreaks, and optimal harvest times using TensorFlow, PyTorch, and scikit-learn. |
|   7 | Smart farming leverages technology to optimize irrigation, pest control, and yield prediction, moving beyond traditional manual observations and intuition.                     |
|   8 | A case study on maize yield prediction utilized an IoT sensor-based microcontroller system with API functionalities to collect data over a 75-day experimental period.          |
|   9 | The experiment involved three land portions: a control section, one with manure, and one with fertilizer, to test different soil conditions.                                    |
|  10 | Data collected included soil parameters like pH, temperature, humidity, and nutrients, as well as atmospheric conditions and daily maize growth measurements.                   |
|  11 | The dataset was locally sourced in Africa to ensure relevance to regional weather and soil conditions, unlike standardized international datasets.                              |
|  12 | Data preprocessing involved removing irrelevant features, handling missing values with mean imputation, and converting non-numeric features to numeric values.                  |
|  13 | Exploratory data analysis used box plots, scatter plots, and Pearson correlation heatmaps to identify relationships between features and the target yield variable.             |
|  14 | Feature selection was performed using SelectKBest, Mutual Information, and Random Forest feature selectors to optimize model performance.                                       |
|  15 | Four machine learning models were trained and evaluated: XGBoost, Multilayer Perceptron, K-Nearest Neighbors, and Ridge Regressor.                                              |
|  16 | Model evaluation used Mean Absolute Error, Root Mean Squared Error, and R-squared score to assess accuracy.                                                                     |
|  17 | XGBoost combined with SelectKBest features achieved the highest accuracy with an R-squared score close to one, outperforming other models.                                      |
|  18 | The integration of IoT data with Python-based machine learning enables highly accurate maize yield prediction and improved farm management decisions.                           |
|  19 | The project provides a scalable framework for smart farming systems, particularly beneficial for developing regions in Africa.                                                  |
|  20 | The collected dataset is publicly available to support further research and application in African agriculture.                                                                 |
|  21 | Future plans include expanding the project to other regions in Nigeria and West Africa, where similar weather and soil conditions exist.                                        |
|  22 | Sensor selection depends on specific agricultural needs, with options ranging from combined multi-parameter sensors to individual specialized devices.                          |
|  23 | Sensors are monitored continuously for performance, and replacement is only necessary if adverse conditions affect their functionality.                                         |

# Video

[![Video thumbnail](https://img.youtube.com/vi/LF39_oyJtj0/hqdefault.jpg)](https://www.youtube.com/watch?v=LF39_oyJtj0)

[Watch on YouTube](https://www.youtube.com/watch?v=LF39_oyJtj0)
