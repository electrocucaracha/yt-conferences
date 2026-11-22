---
layout: default
title: "Tutorials - Pandy Knight: def test_crash_course_with_pytest():"
nav_order: 31
parent: PyCon US 2024
type: Video Note
description: "In this PyCon US tutorial, instructor Andy Knight, known as the Automation Panda, guides attendees through a hands-on introduction to the pytest framework, emphasizing that testing is fundamentally..."
resource: "https://www.youtube.com/watch?v=Yq3M8Yj-uX0"
youtube_stats:
  view_count: 1242
  like_count: 17
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

In this PyCon US tutorial, instructor Andy Knight, known as the Automation Panda, guides attendees through a hands-on introduction to the pytest framework, emphasizing that testing is fundamentally about interaction and verification.
The session begins with setting up a Python virtual environment and writing basic test cases for mathematical operations to demonstrate core mechanics such as assertion introspection, which automatically displays variable values upon failure, and the use of `pytest.raises` for handling expected exceptions.
Knight then introduces the concept of equivalence classes and utilizes the `@pytest.mark.parametrize` decorator to create data-driven tests that efficiently cover multiple scenarios while maintaining test independence.
The tutorial progresses to writing unit tests for a custom `Accumulator` class, where Knight explains the critical role of fixtures for managing setup and teardown logic, including the use of generators for cleanup and different scopes like function and session.
He advocates for designing code with dependency injection to use "fakes" rather than complex mocking, ensuring cleaner and more maintainable test suites.
Additionally, the session covers advanced command-line options for filtering tests by name or custom markers, generating JUnit XML and HTML reports, and using plugins like `pytest-cov` for code coverage and `pytest-xdist` for parallel execution to reduce testing time.
The session concludes with a brief overview of API and UI testing examples, encouraging participants to explore further resources on Test Automation University and the official pytest documentation to deepen their understanding of quality feedback loops in software development.

# Main Points

|   # | Main point                                                                                                                                                                          |
| --: | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | The speaker, Andy Knight, introduced his experience at PyCon 2018 in Cleveland, which significantly impacted his career and perspective on the Python community.                    |
|   2 | The tutorial focuses on learning pytest by building a test project from scratch, emphasizing hands-on coding over passive listening to ensure deep understanding.                   |
|   3 | Participants are expected to have basic Python programming experience and a recent version of Python installed on their laptops for the interactive session.                        |
|   4 | The instructor recommends creating a virtual environment for each new project to manage dependencies locally and avoid conflicts between different Python projects.                 |
|   5 | Pytest is preferred over unittest because it allows tests to be written as functions rather than classes, offering a more extensible plugin framework and faster iteration.         |
|   6 | Test discovery in pytest relies on naming conventions, specifically looking for modules and functions that begin or end with the word "test".                                       |
|   7 | A fundamental definition of testing is provided as the combination of interaction with the system and verification of the expected results.                                         |
|   8 | Pytest uses Python's native assert statements, which enables assertion introspection to automatically display variable values at the point of failure for easier debugging.         |
|   9 | A test case is considered successful if it runs to completion and yields the appropriate result, even if that result is a failure due to an unhandled exception.                    |
|  10 | The pytest.raises context manager is the recommended Pythonic way to verify that specific exceptions are raised, allowing for cleaner code than try-except blocks.                  |
|  11 | Test cases should be atomic, covering exactly one behavior to prevent the loss of test coverage if an early assertion fails within a multi-assertion test.                          |
|  12 | Parameterization using the pytest.mark.parametrize decorator allows a single test function to run multiple times with different data sets, improving data-driven testing.           |
|  13 | Fixtures in pytest are functions used for setup and cleanup operations, identified by the pytest.fixture decorator and injected into test cases by name.                            |
|  14 | The conftest.py file serves as a special module for defining fixtures that need to be shared across multiple test modules within a directory hierarchy.                             |
|  15 | Fixture scope can be configured to control how often a fixture is instantiated, with function scope being the default for ensuring test independence.                               |
|  16 | Generators in fixtures allow for both setup and teardown logic within the same function, where code before the yield is setup and code after is cleanup.                            |
|  17 | The instructor advises against using mocking libraries when possible, recommending instead the design of code with interfaces that allow for the injection of fake implementations. |
|  18 | Command-line options such as -k allow for filtering tests by name substring, while custom markers defined in pytest.ini provide more precise and reliable test selection.           |
|  19 | The --max-fail option is recommended for stopping test execution after a specified number of failures, which is particularly useful for saving time in slow black-box test suites.  |
|  20 | Plugins like pytest-html generate human-readable reports, while pytest-cov integrates code coverage analysis, and pytest-xdist enables parallel test execution.                     |
|  21 | Code coverage should include branch coverage to ensure that all logical paths in the code are tested, not just the execution of individual statements.                              |
|  22 | The tutorial concludes with a reference to additional resources, including the instructor's GitHub repository and courses on Test Automation University for further learning.       |

# Video

[![Video thumbnail](https://img.youtube.com/vi/Yq3M8Yj-uX0/hqdefault.jpg)](https://www.youtube.com/watch?v=Yq3M8Yj-uX0)

[Watch on YouTube](https://www.youtube.com/watch?v=Yq3M8Yj-uX0)
