---
layout: default
title: "Tutorials - Renne Rocha: Gathering data from the web using Python"
nav_order: 24
parent: PyCon US 2024
type: Video Note
description: "This three-hour tutorial, led by a Brazilian developer and Scrapy maintainer, provides a comprehensive guide to web scraping using Python, focusing on the Scrapy framework."
resource: "https://www.youtube.com/watch?v=sD30nvc1ff0"
youtube_stats:
  view_count: 1621
  like_count: 29
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

This three-hour tutorial, led by a Brazilian developer and Scrapy maintainer, provides a comprehensive guide to web scraping using Python, focusing on the Scrapy framework.
The session begins with an overview of why automated data collection is essential for business intelligence, machine learning, and government transparency, introducing key tools like Requests, BeautifulSoup, and headless browsers.
The instructor demonstrates Scrapy’s architecture, explaining how spiders, schedulers, and downloaders work together to handle asynchronous requests, rate limiting, and data pipelines efficiently.
Through four practical exercises on a sandbox site, attendees learn to parse static HTML using CSS and XPath selectors, reverse-engineer dynamic sites by identifying hidden API endpoints, extract data embedded in JavaScript variables using regular expressions, and manage multi-page item construction.
The tutorial concludes with advanced topics, including the use of Playwright for JavaScript-heavy sites, the importance of monitoring scrapers with tools like Spidermon, and ethical considerations regarding proxies, legal compliance, and polite scraping practices.

# Main Points

|   # | Main point                                                                                                                                                      |
| --: | --------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | The tutorial covers web scraping fundamentals, the Scrapy framework, and practical exercises using Python.                                                      |
|   2 | Web scraping is essential for gathering data to make business decisions, train machine learning models, and monitor competitors or government data.             |
|   3 | Common Python libraries for scraping include Requests, Beautiful Soup, HTTPX, Parsel, Selenium, and Playwright.                                                 |
|   4 | Scrapy is an application framework that handles asynchronous requests, data pipelines, session management, and extensibility.                                   |
|   5 | The Scrapy architecture involves Spiders, the Engine, Scheduler, Downloader, and Item Pipelines for processing data.                                            |
|   6 | Spiders define how to crawl a site, extract data, and follow links using start URLs or start requests.                                                          |
|   7 | Data extraction can be performed using CSS selectors, XPath expressions, or regular expressions within Scrapy responses.                                        |
|   8 | Scrapy supports exporting data to various formats such as CSV, JSON, XML, and JSON Lines for efficient memory management.                                       |
|   9 | Exercise one involves scraping a static quotes site with pagination using CSS selectors and following next-page links.                                          |
|  10 | Exercise two addresses infinite scrolling by identifying and directly requesting the underlying API endpoints found in browser network tabs.                    |
|  11 | Exercise three handles data embedded in JavaScript variables within script tags by using regular expressions to extract and parse JSON.                         |
|  12 | Exercise four demonstrates building complete items by sending multiple requests and passing metadata between them using request.meta or callback kwargs.        |
|  13 | Headless browsers like Playwright are useful for rendering JavaScript-heavy pages but are slower than standard HTTP requests.                                   |
|  14 | The scrapy-playwright library integrates headless browser capabilities into Scrapy by replacing the default downloader.                                         |
|  15 | Monitoring tools like Spidermon are recommended to track scraper health, validate data quality, and detect layout changes.                                      |
|  16 | Proxies are necessary for avoiding IP bans, accessing region-specific content, and scaling scraping operations.                                                 |
|  17 | Scrapers must be polite by managing request rates and adhering to site terms of service.                                                                        |
|  18 | Legal considerations include respecting copyright, handling personal data according to local laws, and understanding precedents like the HiQ vs. LinkedIn case. |

# Video

[![Video thumbnail](https://img.youtube.com/vi/sD30nvc1ff0/hqdefault.jpg)](https://www.youtube.com/watch?v=sD30nvc1ff0)

[Watch on YouTube](https://www.youtube.com/watch?v=sD30nvc1ff0)
