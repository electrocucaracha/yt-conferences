---
layout: default
title: "Yes, You Can Test SQL - Paul Zuradzki"
nav_order: 28
parent: PyCon US 2026
type: Video Note
description: "Paul Juratsky, a lead senior data science engineer at Turquoise Health, presents a comprehensive guide on testing SQL within Python environments, emphasizing the challenges of database state reprod..."
resource: "https://www.youtube.com/watch?v=bQLN9PIo_rs"
youtube_stats:
  view_count: 439
  like_count: 4
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

Paul Juratsky, a lead senior data science engineer at Turquoise Health, presents a comprehensive guide on testing SQL within Python environments, emphasizing the challenges of database state reproduction and dialect differences.
He introduces the Arrange-Act-Assert pattern and explains various substitution strategies, such as using test fakes, mocking, and in-memory databases like SQLite or DuckDB to isolate transformation logic.
For scenarios requiring specific database features, Juratsky demonstrates techniques for transpiling SQL dialects and injecting queries into Common Table Expressions (CTEs) to simulate data without touching physical tables.
He further details how to leverage Docker Compose and pytest fixtures to manage real database connections, ensuring proper setup and teardown for isolated, reproducible tests.
The talk concludes with recommendations for using pre-commit hooks, CI/CD workflows, and metadata reflection tools to maintain code quality and schema consistency, while distinguishing between unit testing SQL logic and broader data quality validation.

# Main Points

|   # | Main point                                                                                                                                                                          |
| --: | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Testing SQL is challenging due to the need to reproduce database state, create dummy databases, handle stored procedures, and manage different SQL dialects.                        |
|   2 | The talk uses a simple orders table with region, item, and sales amount to demonstrate testing techniques that scale to complex queries.                                            |
|   3 | The Arrange-Act-Assert pattern is recommended for organizing tests to improve readability and separate setup, execution, and verification steps.                                    |
|   4 | Test doubles, including fakes and mocks, are strategies for substituting dependencies, though mocking may fail to test actual SQL logic if business rules reside in the database.   |
|   5 | Common Table Expressions (CTEs) serve as a useful alternative to subqueries and can be leveraged to create virtual tables for testing without physical database tables.             |
|   6 | The DB-API standard allows for swappable database connections, enabling tests to run against SQLite, Postgres, or other compliant databases using the same interface.               |
|   7 | Pytest fixtures manage resource setup and teardown, such as initializing and closing database connections, using the yield statement to define the resource lifecycle.              |
|   8 | In-memory SQLite or DuckDB can be used for quick testing, but they may not support all Postgres features or extensions, leading to potential translation issues.                    |
|   9 | SQL transpilation tools can rewrite SQL from one dialect to another, allowing Postgres queries to be tested against SQLite, though this may not cover all edge cases.               |
|  10 | A technique for testing against real databases involves injecting SQL into a CTE to seed data with SELECT statements, avoiding the need for physical table inserts.                 |
|  11 | Using Python dictionary merging with the pipe operator helps reduce redundancy in test data setup by allowing specific field overrides on default rows.                             |
|  12 | Pytest parametrize is a high-value feature for running the same test logic with multiple input sets, ensuring all cases execute even if one fails.                                  |
|  13 | Docker Compose or pytest-docker-tools can spin up real database instances like Postgres for integration testing, providing a more accurate environment than in-memory alternatives. |
|  14 | Test isolation is critical to prevent flaky tests, requiring careful management of transactions and cleanup to avoid data collisions between parallel or sequential tests.          |
|  15 | Schema change detection and round-trip type testing are useful for verifying that data types remain consistent when moving between Python and the database.                         |
|  16 | Metadata reflection tools like SQLAlchemy can copy schemas from remote databases to local environments, eliminating the need to manually write CREATE TABLE statements.             |
|  17 | Tools like DBT and SQL Mesh offer built-in testing capabilities, though they may differ from standard unit testing approaches and require specific configuration.                   |
|  18 | SQL formatters and linters combined with pre-commit hooks and CI/CD workflows ensure consistent code quality and automated test execution in remote environments.                   |
|  19 | Data quality testing tools like Great Expectations are distinct from unit testing and focus on validating data values rather than SQL transformation logic.                         |
|  20 | Cleanup logic for database connections should typically reside within the pytest fixture rather than the test body to ensure proper resource management.                            |
|  21 | Testing stored procedures or functions can be achieved by running them against a real database instance, though specific implementation details may vary.                           |
|  22 | Optimizing test speed can involve reusing fixtures across the entire test session or adjusting the scope of data seeding to avoid redundant setup per test method.                  |

# Video

[![Video thumbnail](https://img.youtube.com/vi/bQLN9PIo_rs/hqdefault.jpg)](https://www.youtube.com/watch?v=bQLN9PIo_rs)

[Watch on YouTube](https://www.youtube.com/watch?v=bQLN9PIo_rs)
