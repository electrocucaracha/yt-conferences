---
layout: default
title: "Talks - Lazouich Ford: Geospatial Validations Using FastAPI and PostGIS"
nav_order: 199
parent: PyCon US 2024
type: Video Note
description: "László Ford presents a technical overview of geospatial data validation using FastAPI and PostGIS, emphasizing the importance of understanding spatial reference systems and the inherent distortions..."
resource: "https://www.youtube.com/watch?v=6x8sRJUnk4I"
youtube_stats:
  view_count: 444
  like_count: 6
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

László Ford presents a technical overview of geospatial data validation using FastAPI and PostGIS, emphasizing the importance of understanding spatial reference systems and the inherent distortions of projecting a spherical Earth onto a flat plane.
The talk covers the fundamentals of geospatial geometries, such as points, lines, and polygons, and explains how to load shape files into PostgreSQL using the `shape2pgsql` utility to create indexed geometry columns.
Ford demonstrates key PostGIS functions, including `ST_MakePoint`, `ST_SetSRID`, `ST_Intersects`, `ST_Contains`, and `ST_Distance`, highlighting the necessity of consistent coordinate systems to ensure accurate spatial queries.
The presentation then transitions to integrating these database capabilities with Python, utilizing the GeoAlchemy2 library to translate raw SQL spatial functions into SQLAlchemy ORM queries for cleaner code.
Finally, Ford illustrates two methods for validating incoming geospatial data in a FastAPI application: using dependency injection to check if a point intersects a specific boundary like Pennsylvania, and employing Pydantic model validators to enforce both input and output data integrity, thereby preventing computational waste from processing invalid requests.

# Main Points

|   # | Main point                                                                                                                                                                                                     |
| --: | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Geospatial data is commonly encountered in applications like maps and earthquake shake maps, typically represented as points, line strings, polygons, or collections of these geometries.                      |
|   2 | The Earth is a spheroid, so projecting it onto a flat surface requires choosing a spatial reference system (SRS) that involves trade-offs regarding distortion, with WGS84 being the standard for GPS.         |
|   3 | Shape files are a common data format but consist of multiple files containing different data types, whereas SQL files are preferred for direct database loading without additional processing.                 |
|   4 | PostGIS is a PostgreSQL extension that enables geospatial data management, installed via the command `CREATE EXTENSION IF NOT EXISTS postgis`.                                                                 |
|   5 | The `shape2pgsql` utility converts shape files into SQL files, allowing users to specify options like creating new tables, using PostgreSQL dump format, and indexing geometry columns.                        |
|   6 | Key PostGIS functions include `ST_MakePoint` for creating points, `ST_SetSRID` for assigning a spatial reference ID, and `ST_Intersects` to check if geometries share any points.                              |
|   7 | ST_Contains`verifies if all points of one geometry are inside another, while`ST_Distance` calculates the minimum geodesic distance between geographies in meters, accounting for Earth's curvature.            |
|   8 | ST_Transform` converts geometries between different coordinate systems, which is essential for ensuring data compatibility when performing spatial queries.                                                    |
|   9 | Validating geospatial data in FastAPI helps fail fast on bad requests, reduces computational costs by avoiding unnecessary processing, and keeps business logic concise.                                       |
|  10 | The project demonstrates validating data using both Pydantic models and FastAPI dependency injection, with database tables containing geometries for Pennsylvania and Pittsburgh neighborhoods.                |
|  11 | SQLAlchemy and GeoAlchemy2 allow developers to use PostGIS functions directly within Python ORM queries, avoiding the need for raw SQL strings.                                                                |
|  12 | In the dependency injection approach, a function checks if a point intersects Pennsylvania and raises a 422 error if it does not, otherwise returning the specific neighborhood.                               |
|  13 | The Pydantic validation approach uses a model validator to check the point's location, raising a ValueError that Pydantic converts to a 422 response, and can also validate outgoing data via response models. |
|  14 | Testing the endpoints shows that valid points inside Pennsylvania return the neighborhood or echo the point, while invalid points outside the boundary trigger 422 errors.                                     |
|  15 | Managing SRIDs and transforms depends on the specific use case, as different projections preserve different properties like distance or area, and local coordinate systems can be difficult to handle.         |
|  16 | Shape file conversion to SQL is generally lossless if the complete set of shape file components is present, consolidating geometry and attribute data into standard insert statements.                         |

# Video

[![Video thumbnail](https://img.youtube.com/vi/6x8sRJUnk4I/hqdefault.jpg)](https://www.youtube.com/watch?v=6x8sRJUnk4I)

[Watch on YouTube](https://www.youtube.com/watch?v=6x8sRJUnk4I)
