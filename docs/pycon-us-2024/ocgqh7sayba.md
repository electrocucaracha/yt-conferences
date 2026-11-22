---
layout: default
title: "Tutorials - Caroline Frasca, Tony Kipkemboi: Advanced Streamlit for Python Developers"
nav_order: 18
parent: PyCon US 2024
type: Video Note
description: "This tutorial guides participants through building a two-part Streamlit application, beginning with an analytics dashboard that visualizes GitHub repository statistics such as code changes, commit ..."
resource: "https://www.youtube.com/watch?v=oCGQH7saYBA"
youtube_stats:
  view_count: 1452
  like_count: 18
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

This tutorial guides participants through building a two-part Streamlit application, beginning with an analytics dashboard that visualizes GitHub repository statistics such as code changes, commit activity, and contributor data.
The session starts by installing necessary dependencies and creating a Python file to import libraries like Streamlit, Pandas, and Plotly, followed by loading CSV data files into a structured directory.
The first major component involves creating a modular data loading function with error handling and caching, then configuring the app’s page layout and setting up three distinct tabs for different data views.
Within the first tab, the instructor demonstrates how to preprocess date columns, implement a date range slider to filter data, and generate visualizations using area and scatter charts to display weekly and cumulative code changes.
Subsequent steps cover building the commit activity tab with metrics and bar charts, and the contributors tab, which includes data cleaning, grouping by author, and using experimental fragments to create interactive plots for individual contributor analysis.
The tutorial concludes by briefly introducing the second part of the app, a RAG-based chatbot using LlamaIndex and GPT-3.5, which augments the LLM with Markdown documentation to provide up-to-date answers about Streamlit features.

# Main Points

|   # | Main point                                                                                                                                          |
| --: | --------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | The tutorial covers building a two-part Streamlit app: a GitHub analytics dashboard and a RAG chatbot using LlamaIndex.                             |
|   2 | Participants are provided with a hosted demo link, slide deck with code snippets, and a GitHub repository containing step-by-step Python files.     |
|   3 | The analytics dashboard visualizes statistics from the Streamlit GitHub repository, including code changes, commit activity, and contributor data.  |
|   4 | Users can customize the dashboard by using their own repositories or data instead of the provided Streamlit example.                                |
|   5 | The chatbot component uses a Retrieval Augmented Generation pipeline to answer questions based on Markdown files that contain recent documentation. |
|   6 | This approach allows the chatbot to access information newer than the training data of the underlying large language model, such as GPT-3.5.        |
|   7 | To begin coding, users must install required packages by creating a requirements.txt file and running pip install -r requirements.txt.              |
|   8 | It is recommended to use a virtual environment to isolate the application dependencies during the installation process.                             |
|   9 | The main application file should be created with a specific name to display a custom icon in the Streamlit sidebar.                                 |
|  10 | Essential libraries to import include Streamlit, Pandas, and Plotly Express for data manipulation and visualization.                                |
|  11 | Three CSV files containing contributor, commit activity, and code frequency data must be downloaded and saved in a data folder.                     |
|  12 | A generic load_data function should be created using Pandas read_csv and decorated with st.cache_data to improve performance.                       |
|  13 | Error handling should be implemented in the data loading function to catch missing files or empty data and display user-friendly error messages.    |
|  14 | The main app structure is set up using st.set_page_config to define the layout, icon, and title of the application.                                 |
|  15 | Three tabs are created for the dashboard: Code Frequency, Commit Activity, and Contributors.                                                        |
|  16 | The Code Frequency tab requires converting the week column to Pandas datetime and displaying raw data in an st.expander.                            |
|  17 | A date range slider is implemented to allow users to filter data based on specific start and end dates.                                             |
|  18 | Weekly code changes are visualized using an area chart with color-coded additions and deletions.                                                    |
|  19 | Cumulative code changes are displayed using a scatter chart based on the filtered date range.                                                       |
|  20 | The Commit Activity tab loads specific CSV data, converts dates, and displays raw data in an expander.                                              |
|  21 | Metrics for total commits, average commits, and weekly changes are displayed using st.metric within three columns.                                  |
|  22 | Commit activity is further visualized using a bar chart showing the total commits per week.                                                         |
|  23 | The Contributors tab involves renaming abbreviated columns to readable labels and dropping unnecessary columns.                                     |
|  24 | Total activity per contributor is calculated by grouping data by author and determining the date range of their contributions.                      |
|  25 | An experimental fragment is used to create a plot chart that reruns only the specific visualization without reloading the entire app.               |
|  26 | The if **name** == "**main**" block is required at the end of the script to execute the main function and render the app.                           |
|  27 | Splitting the screen between the code editor and the local host browser is recommended for efficient development and real-time preview.             |

# Video

[![Video thumbnail](https://img.youtube.com/vi/oCGQH7saYBA/hqdefault.jpg)](https://www.youtube.com/watch?v=oCGQH7saYBA)

[Watch on YouTube](https://www.youtube.com/watch?v=oCGQH7saYBA)
