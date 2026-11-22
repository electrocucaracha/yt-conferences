---
layout: default
title: "Talks - Esther Alter: Procedurally Generated Monsters! A complete example of Python game development"
nav_order: 157
parent: PyCon US 2024
type: Video Note
description: 'Esther Alter, a game developer from Boston, presents "Procedurally Generated Monsters," a 2D monster-collecting game developed in Python and released on Steam and itch.io in 2022.'
resource: "https://www.youtube.com/watch?v=ZjBDoF_iD9Y"
youtube_stats:
  view_count: 318
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

Esther Alter, a game developer from Boston, presents "Procedurally Generated Monsters," a 2D monster-collecting game developed in Python and released on Steam and itch.io in 2022.
She explains that she chose Python for its rapid prototyping capabilities and convenient libraries, specifically leveraging Pygame CE for rendering and NumPy for high-performance image manipulation and procedural generation.
The game’s core mechanic involves generating unique monsters, maps, stats, and animations using bounded random algorithms, which creates a "low-fi" aesthetic that embraces glitchy visuals rather than treating them as bugs.
Alter details her code architecture, which uses an abstract renderer class to allow any game state to be easily tested as an entry point, significantly speeding up debugging and development.
Despite Python’s limitations in speed and 3D rendering, she argues that these constraints foster creativity, allowing her to complete the project in nine months with a total cost of only $100.
She also discusses the challenges of deploying Python games, noting that while tools like PyInstaller exist, cross-compiling and uploading to platforms like Steam required complex workarounds involving GitHub workflows and manual steps.
Finally, she advises aspiring developers to embrace constraints and start with the hardest part of their project first to ensure the core concept is viable before investing further time.

# Main Points

|   # | Main point                                                                                                                                                                                                              |
| --: | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Esther Alter is a game developer from Boston who presented a talk on her Python-based game "Pramon: You Must Catch Them," released in 2022.                                                                             |
|   2 | The game is a 2D monster-collecting title featuring turn-based battles and extensive procedural generation of maps, monsters, stats, and animations.                                                                    |
|   3 | Procedural generation in the game uses bounded algorithms to create unique but consistent content, such as maps with specific land-to-water ratios and monster sprites from 72 categories.                              |
|   4 | Monster flavor text is generated using Markov chains built from Wikipedia data scraped prior to development.                                                                                                            |
|   5 | The game does not use modern AI or neural networks; the developer argues that procedural generation is simpler, older, and more efficient for this type of game.                                                        |
|   6 | Development took nine months from the first commit to Steam release, with a total cost of $100 for the Steam fee, as the developer worked alone using open-source tools.                                                |
|   7 | Python was chosen for its ease of prototyping and debugging, allowing any renderer class to serve as an entry point for testing specific game states.                                                                   |
|   8 | The core game loop uses an abstract renderer class where each scene returns a new renderer, facilitating modular development and easy state transitions.                                                                |
|   9 | Pygame CE (a fork of Pygame) is used for rendering, input, and audio, offering pixel-perfect rendering and easy conversion to NumPy arrays.                                                                             |
|  10 | NumPy is used for heavy image manipulation and procedural generation, treating image data as 3D arrays (width, height, RGB) for fast CPU-based processing.                                                              |
|  11 | A key optimization involves batching blit operations into a sequence to improve performance, as multiple individual blit calls are slower in Python.                                                                    |
|  12 | A complex world-transition animation is generated on the fly using NumPy to blend noise arrays, glitch arrays, and world surfaces, simulating a shader effect without GPU acceleration.                                 |
|  13 | Deployment is a significant weakness of Python for games; PyInstaller is used to create executables but does not protect source code or support cross-compilation.                                                      |
|  14 | The developer used GitHub Actions to compile builds for Windows, Mac, and Linux, uploading to itch.io via Butler and to Steam via a manual FTP and local script workaround due to Steam's lack of headless CLI support. |
|  15 | The developer advises against using advanced engines for simple 2D games, arguing that constraints force creativity and Python is sufficient for this scope.                                                            |
|  16 | Hybrid approaches using C++ for graphics and Python for logic are possible but deemed unnecessary if one is already using fast compiled code.                                                                           |
|  17 | Game balance is maintained through bounded procedural generation, ensuring stats and encounters remain fair while allowing for unique "freakazoid" monster encounters.                                                  |
|  18 | The developer recommends tackling the hardest part of a game first to validate feasibility before proceeding with full development.                                                                                     |
|  19 | Python 3 and modern Pygame versions have significantly improved game development capabilities compared to earlier Python 2.7 projects.                                                                                  |
|  20 | Audio is generated algorithmically using chord progressions and rhythm scripts, creating unique UI sounds and music tracks for each playthrough.                                                                        |

# Video

[![Video thumbnail](https://img.youtube.com/vi/ZjBDoF_iD9Y/hqdefault.jpg)](https://www.youtube.com/watch?v=ZjBDoF_iD9Y)

[Watch on YouTube](https://www.youtube.com/watch?v=ZjBDoF_iD9Y)
