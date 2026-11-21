---
layout: default
title: "From Messy Clinical Data to Interoperable FHIR: A Python-First Mapping and Validation... -Lisa Smith"
nav_order: 45
parent: PyCon US 2026
type: Video Note
description: "Lisa Smith, a full-stack Python developer at the Wilmot Cancer Institute, presented a project designed to transform messy healthcare data into structured, standards-compliant HL7 FHIR output to fac..."
resource: "https://www.youtube.com/watch?v=AJkdevs4zOY"
youtube_stats:
  view_count: 464
  like_count: 15
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

Lisa Smith, a full-stack Python developer at the Wilmot Cancer Institute, presented a project designed to transform messy healthcare data into structured, standards-compliant HL7 FHIR output to facilitate interoperability.
The application addresses the challenge of fragmented Electronic Health Record systems by allowing clinicians and researchers to upload CSV or Excel files, which are then processed through a stateless, secure architecture that prioritizes speed and user simplicity.
To achieve rapid and reproducible results, Smith utilized offline LLM-assisted Python dictionaries for initial column mapping and RapidFuzz for fuzzy matching against standardized terminologies like LOINC and SNOMED CT, intentionally avoiding slower runtime generative AI matching.
The system employs a "garbage in, garbage out" model where human experts retain sole responsibility for data accuracy, ensuring that no transformations occur without explicit user knowledge, while FHIR extensions allow for the preservation of unstructured clinical data.
Ultimately, the tool uses the Smart on FHIR Python client and Pandas to validate and bundle the data into JSON or XML formats, enabling seamless data exchange and supporting future applications in cybersecurity compliance.

# Main Points

|   # | Main point                                                                                                                                                   |
| --: | ------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   1 | Lisa Smith is a full-stack Python developer and data engineer at the Wilmot Cancer Institute, University of Rochester.                                       |
|   2 | The project transforms messy healthcare data into structured, standards-compliant HL7 FHIR output to improve interoperability.                               |
|   3 | Healthcare data is often disorganized and fragmented across over 600 different EHR vendors, making seamless data transfer difficult.                         |
|   4 | HL7 FHIR standards were introduced to replace older HL7 standards, offering a modern, database-like approach to data exchange.                               |
|   5 | Design constraints include high speed, simplicity, human-in-the-loop validation, scalability, and strict security for healthcare data.                       |
|   6 | The system uses a "garbage in, garbage out" model where health professionals are the sole source of truth to prevent data corruption.                        |
|   7 | The application is stateless, processing uploads transiently in memory to enhance security and reduce operational complexity.                                |
|   8 | The backend architecture utilizes Flask, Pandas, SQL, and the Smart on FHIR Python client library.                                                           |
|   9 | An offline LLM-assisted generation process created dictionaries for fast, deterministic auto-matching of column names to FHIR elements.                      |
|  10 | Python dictionaries were chosen for their speed and efficiency in handling finite static vocabularies for initial data matching.                             |
|  11 | A two-layer matching process handles both column name identification and specific value standardization, such as vital status or race.                       |
|  12 | Deterministic dictionary matching was preferred over runtime generative LLM matching for speed, reproducibility, and ease of validation.                     |
|  13 | Users can upload CSV or Excel files and select deterministic or random UUID generation for patient continuity.                                               |
|  14 | FHIR extensions are used to preserve important data that lacks a specific FHIR element, such as days between diagnosis and treatment.                        |
|  15 | RapidFuzz is employed for secondary fuzzy matching of medical observations, procedures, and medications against standardized codes like LOINC and SNOMED CT. |
|  16 | The application identifies missing metadata, such as age units or observation statuses, which are critical for accurate FHIR resource construction.          |
|  17 | Pandas handles data cleaning, formatting, encoding, and vectorization to assemble FHIR resources efficiently.                                                |
|  18 | The final output is validated using the Smart on FHIR library to ensure compliance before providing JSON or XML downloads.                                   |
|  19 | The tool is currently in testing and is designed modularly to allow for the addition of more FHIR resources.                                                 |
|  20 | Future plans include releasing the tool publicly and applying the data transformation methodology to cybersecurity compliance standards.                     |
|  21 | The project emphasizes that a confident wrong answer is worse than an incomplete one, prioritizing user control and data integrity.                          |
|  22 | The system supports mapping ICD-10, SNOMED CT, LOINC, and RxNorm codes using a small set of database tables.                                                 |
|  23 | Data provenance is preserved, and the tool deduplicates records while flagging potential errors for user review.                                             |

# Video

[![Video thumbnail](https://img.youtube.com/vi/AJkdevs4zOY/hqdefault.jpg)](https://www.youtube.com/watch?v=AJkdevs4zOY)

[Watch on YouTube](https://www.youtube.com/watch?v=AJkdevs4zOY)
