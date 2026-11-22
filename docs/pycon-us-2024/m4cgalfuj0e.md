---
layout: default
title: "Tutorials - Rodrigo Girão Serrão: The Pokémon trainer's guide to pandas and matplotlib"
nav_order: 11
parent: PyCon US 2024
type: Video Note
description: "In this three-hour tutorial, instructor Rodrigo guides attendees through the fundamentals of data manipulation using Python’s pandas library and data visualization with Matplotlib, utilizing a Poké..."
resource: "https://www.youtube.com/watch?v=M4CGalfUj0E"
youtube_stats:
  view_count: 1716
  like_count: 36
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

In this three-hour tutorial, instructor Rodrigo guides attendees through the fundamentals of data manipulation using Python’s pandas library and data visualization with Matplotlib, utilizing a Pokémon dataset as a practical example.
The session begins with an introduction to core pandas concepts, including loading CSV files, understanding DataFrames and Series, and managing data types such as integers, floats, and booleans.
Rodrigo demonstrates how to efficiently transform data by selecting specific columns, converting data types, and using broadcasting to apply mathematical formulas across entire columns or DataFrames without the need for slow loops.
He further explains how to use Boolean indexing to filter data based on specific conditions and introduces categorical data types to optimize memory usage and ensure data integrity.
The second half of the tutorial focuses on creating effective visualizations using Matplotlib, starting with basic line plots and progressing to more complex bar charts and violin plots.
Participants learn to customize plots by adjusting labels, titles, colors, and axis orientations to enhance readability and aesthetic appeal.
A key highlight is the creation of a detailed bar plot showing the distribution of Pokémon types, where the instructor demonstrates how to align tick labels with data values and apply specific colors to each bar using a dictionary mapping.
The session concludes with an analysis of speed statistics across different Pokémon types using violin plots, illustrating how to compare distributions and identify trends in the data.
Throughout the tutorial, the instructor emphasizes the importance of non-destructive data manipulation, allowing users to experiment freely and chain transformations together for clean, reproducible code.

# Main Points

|   # | Main point                                                                                                                                             |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   1 | The tutorial covers pandas and Matplotlib concepts using a Pokémon dataset to demonstrate data manipulation and visualization techniques.              |
|   2 | Participants are instructed to sync code via a GitHub repository and use a specific CSV file containing 898 rows of Pokémon data.                      |
|   3 | The session is structured into two 90-minute segments: introductory pandas concepts followed by Matplotlib plotting, with a coffee break in between.   |
|   4 | The instructor emphasizes an interactive approach where attendees type along with the code and complete small challenges to verify understanding.      |
|   5 | The goal is to teach key pandas methods and concepts that serve as a foundation for further self-study rather than covering the entire library.        |
|   6 | Data is loaded into a DataFrame using the read_csv method, which is the fundamental data structure for tabular data in pandas.                         |
|   7 | The head method is used to inspect the first few rows of the DataFrame to understand the data structure and column names.                              |
|   8 | Columns in a DataFrame are accessed as Series objects, which are one-dimensional arrays with specific data types and indices.                          |
|   9 | Indices are used to identify rows and facilitate alignment during operations, though they are not part of the actual data values.                      |
|  10 | Subsets of columns can be selected by indexing the DataFrame with a list of column names, resulting in a new DataFrame.                                |
|  11 | Data types such as int64, float64, and object are automatically inferred by pandas, with object serving as a generic fallback for strings.             |
|  12 | Boolean columns can be created by converting integer columns with 0 and 1 values using the astype method.                                              |
|  13 | Broadcasting allows mathematical operations to be applied element-wise across entire Series or DataFrames, which is significantly faster than looping. |
|  14 | Formulas for calculating final Pokémon stats are applied using broadcasting, with different constants added to HP versus other stats.                  |
|  15 | New columns are added to the DataFrame using the assign method, which creates a copy rather than modifying the original data in place.                 |
|  16 | The join method is used to combine DataFrames, requiring suffixes to handle overlapping column names.                                                  |
|  17 | The sum method with axis=1 calculates the total stats for each row, providing a single summary value per Pokémon.                                      |
|  18 | Boolean indexing allows filtering DataFrames to select rows that meet specific conditions, such as legendary status or high total stats.               |
|  19 | Categorical data types are used for columns with a predefined set of values, such as primary types, to optimize memory and prevent errors.             |
|  20 | Matplotlib plots are initialized using plt.subplots, which returns a Figure object and an Axes object for customization.                               |
|  21 | Line plots are created using the plot method on the Axes object, accepting x and y values or a single Series for y-values.                             |
|  22 | Plot customization includes setting titles, axis labels, and markers to improve readability and visual appeal.                                         |
|  23 | Bar plots are generated using the bar method, requiring positions and heights, with tick labels customized to display category names.                  |
|  24 | The order of bars in a plot must match the order of labels, which can be achieved by using the index of value counts for alignment.                    |
|  25 | Colors are applied to bars using a dictionary mapping types to RGB values, ensuring the order matches the data series.                                 |
|  26 | Horizontal bar plots are created by using the barh method, which requires adjusting tick labels and figure size for readability.                       |
|  27 | Violin plots are used to compare the distribution of a numerical variable across different categories, such as speed by type.                          |
|  28 | The width of a violin plot represents data density, while the central line indicates the mean value.                                                   |
|  29 | The tutorial concludes with a summary of the workflow, emphasizing the importance of non-destructive data transformations and clean code structure.    |

# Video

[![Video thumbnail](https://img.youtube.com/vi/M4CGalfUj0E/hqdefault.jpg)](https://www.youtube.com/watch?v=M4CGalfUj0E)

[Watch on YouTube](https://www.youtube.com/watch?v=M4CGalfUj0E)
