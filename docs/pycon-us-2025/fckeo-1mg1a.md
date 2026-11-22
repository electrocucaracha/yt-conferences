---
layout: default
title: "Schemas: The Key To Data Happiness - Sev Leonard"
nav_order: 90
parent: PyCon US 2025
type: Video Note
description: "Sev Leonard presents a comprehensive overview of how formalized data schemas can mitigate common data engineering challenges, such as pipeline failures and data quality issues."
resource: "https://www.youtube.com/watch?v=fCkEo-1MG1A"
youtube_stats:
  view_count: 2942
  like_count: 71
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

Sev Leonard presents a comprehensive overview of how formalized data schemas can mitigate common data engineering challenges, such as pipeline failures and data quality issues.
He demonstrates practical applications of schemas, including validating data with Python libraries to catch errors early, orchestrating pipelines in Airflow and Kafka to handle invalid data through quarantine or dead-letter queues, and using schemas as a communication tool to define data expectations for teams.
The talk also explores leveraging schemas to generate synthetic test data using the Faker library or AI tools, and to automate code generation for frameworks like SQLAlchemy and dbt.
Additionally, Leonard discusses techniques for automating schema extraction and detecting data drift using PySpark, while cautioning that applying a schema is not the same as validating it, as extra fields may be silently ignored by default.
He concludes by advising that the decision to implement schemas should be based on organizational maturity, data risk, and the potential impact of errors, emphasizing that schemas are a powerful but resource-intensive tool that should be prioritized according to specific business needs.

# Main Points

|   # | Main point                                                                                                                                                                  |
| --: | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Schemas serve as formalized blueprints for data, defining types, required fields, and accepted values to mitigate pipeline failures.                                        |
|   2 | Data validation using libraries like JSON Schema allows for early detection of errors, providing detailed error messages that aid in debugging and logging.                 |
|   3 | In pipeline orchestration, validation failures can trigger either a complete pipeline stop or the quarantine of invalid data while processing valid records.                |
|   4 | Confluent Schema Registry for Kafka enables data validation and flow control, allowing malformed data to be routed to dead letter queues for monitoring.                    |
|   5 | Schemas act as a communication tool, clarifying data expectations for colleagues and enabling development in test environments when production access is restricted.        |
|   6 | The Faker library can generate synthetic data based on schema definitions, supporting unit testing, load testing, and the creation of anomalous events for fraud detection. |
|   7 | AI tools can be used to generate code artifacts such as SQL Alchemy definitions and dbt models directly from schema definitions to reduce boilerplate.                      |
|   8 | Schema extraction can be automated using tools like PySpark or the Jensen library to infer data structures, though this process requires careful review.                    |
|   9 | Detecting schema drift involves comparing inferred schemas against expected ones to identify changes in data shape, such as new attributes or type mismatches.              |
|  10 | Applying a schema to read data does not validate it, potentially leading to silent data loss if new fields are added to the source without updating the schema.             |
|  11 | By default, JSON Schema validation allows extra fields, so the additionalProperties setting must be explicitly set to false to reject unexpected attributes.                |
|  12 | The decision to implement schemas should be based on risk assessment, considering the likelihood of errors, the effort to fix them, and the impact of data quality issues.  |
|  13 | Schemas are most beneficial in high-stakes environments like clinical or government data processing, where data integrity is critical and the cost of errors is high.       |

# Video

[![Video thumbnail](https://img.youtube.com/vi/fCkEo-1MG1A/hqdefault.jpg)](https://www.youtube.com/watch?v=fCkEo-1MG1A)

[Watch on YouTube](https://www.youtube.com/watch?v=fCkEo-1MG1A)
