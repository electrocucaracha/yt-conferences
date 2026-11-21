---
layout: default
title: "Running Every Street in Paris with Python and PostGIS - Vinayak Mehta"
nav_order: 46
parent: PyCon US 2026
type: Video Note
description: "At PyCon, software engineer Ike presented a project to run every street in Paris, inspired by similar challenges in Pittsburgh and San Francisco."
resource: "https://www.youtube.com/watch?v=wPSLip5CsRE"
youtube_stats:
  view_count: 421
  like_count: 8
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

At PyCon, software engineer Ike presented a project to run every street in Paris, inspired by similar challenges in Pittsburgh and San Francisco.
The system utilizes OpenStreetMap data fetched via OSMnx to build a street network, which is then stored in a PostGIS database after cleaning and dissolving duplicate segments.
To track progress, the application uses a webhook from Strava to trigger a background job that reads GPX files, interpolates sparse GPS points, and performs map matching by projecting run coordinates onto the nearest street geometry.
This process calculates the percentage of each street covered, allowing for the visualization of progress and the upserting of new data as runs are completed.
Ike discussed the trade-offs of this simple nearest-neighbor approach, such as inaccuracies at complex intersections, and outlined future work including implementing the Viterbi algorithm for better path matching and solving the Chinese postman problem to optimize 10K routes.

# Main Points

|   # | Main point                                                                                                                                                                                        |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | The speaker is a software engineer in Paris who built a system to track running every street in the city, inspired by similar projects in Pittsburgh and San Francisco.                           |
|   2 | The project utilizes OpenStreetMap data, PostGIS for storage, and map matching to visualize progress on a 10K route challenge.                                                                    |
|   3 | The initial goal of computing the minimum number of 10K routes to cover all streets was identified as a variation of the Chinese postman problem but was temporarily set aside due to complexity. |
|   4 | The current approach involves manually drawing routes initially, then automatically matching runs to the street network via a Strava webhook that triggers a server-side process.                 |
|   5 | GIS concepts discussed include geographic versus projected coordinate systems, and the distinction between vector data (points, lines, polygons) and raster data.                                 |
|   6 | GPX files are used to store raw GPS run data, which often contains inaccuracies such as points appearing on buildings due to urban GPS limitations.                                               |
|   7 | OSMnx is used to fetch the street network, requiring custom filters to include walkable streets that are not accessible to cars, such as residential roads.                                       |
|   8 | Data cleaning involves handling null street names by assigning unique identifiers and using the dissolve function to combine fragmented street segments into single geometries.                   |
|   9 | Approximately 5,400 streets for Paris are stored in a PostGIS database with attributes including ID, name, and geometry.                                                                          |
|  10 | Map matching is performed by interpolating sparse GPS points to increase density, then querying the database for the nearest street to each point.                                                |
|  11 | Run points are projected onto the nearest street geometry to create accurate covered segments, which are stored in a separate table with a calculated progress percentage.                        |
|  12 | The system uses an upsert mechanism to update existing street coverage or insert new ones, combining line strings to reflect total distance covered.                                              |
|  13 | Progress is calculated by dividing the length of the covered line string by the total length of the street, allowing for percentage-based tracking.                                               |
|  14 | A known limitation is that the nearest street heuristic may incorrectly match segments at star intersections, though this is mitigated by requiring 90% coverage for completion.                  |
|  15 | Future work includes implementing the Viterbi algorithm with hidden Markov models for more accurate path finding and returning to the automatic route computation challenge.                      |
|  16 | The speaker has achieved 60% coverage of Paris streets and aims for full coverage within the year, noting that the city's small size makes this feasible compared to larger cities like Delhi.    |
|  17 | The project code and slides are available on a GitHub repository, and the speaker is open to discussing extensions such as real estate analysis or trail mapping.                                 |

# Video

[![Video thumbnail](https://img.youtube.com/vi/wPSLip5CsRE/hqdefault.jpg)](https://www.youtube.com/watch?v=wPSLip5CsRE)

[Watch on YouTube](https://www.youtube.com/watch?v=wPSLip5CsRE)
