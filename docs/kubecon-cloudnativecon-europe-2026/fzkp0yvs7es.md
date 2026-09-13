---
type: Video Note
title: "The Hills Are Alive with the Sound of Kubernetes - Stevie Caldwell, Fairwinds"
description: 'In this talk, Stevie Caldwell, a senior tech lead at Fairwinds, explores the intersection of music and Kubernetes through the concept of sonification—using non-speech audio to represent data. Drawing on the "cocktail party effect," Caldwell...'
resource: https://www.youtube.com/watch?v=fzKp0YvS7Es
tags: ["kubecon-cloudnativecon-europe-2026", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

In this talk, Stevie Caldwell, a senior tech lead at Fairwinds, explores the intersection of music and Kubernetes through the concept of sonification—using non-speech audio to represent data.
Drawing on the "cocktail party effect," Caldwell explains how humans are adept at detecting meaningful changes in background sounds, making auditory cues potentially valuable for observability in technical systems.
The demo showcases a system where a Go-based controller listens for Kubernetes events (such as pod creation, deletion, crash looping, and deployment scaling) and sends messages via the OSC protocol to SuperCollider, a real-time audio synthesis environment, which then generates distinct sounds for each event.
Caldwell demonstrates how this setup can help users recognize cluster activity through sound alone, discusses the challenges of sound design, and suggests that integrating audio with visual monitoring can reduce cognitive load and screen fatigue.
The talk concludes by encouraging creative approaches to infrastructure, showing that Kubernetes can be both functional and fun.
# Main Points

|   # | Main point                                                                                                                       |
| --: | -------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Stevie Caldwell is a senior tech lead for the SRE team at Fairwinds and a musician.                                              |
|   2 | Fairwinds is a managed services provider for Kubernetes, building and maintaining clusters for clients.                          |
|   3 | The talk focuses on sonification and observability.                                                                              |
|   4 | Sonification is the use of non-speech audio to convey information or represent data.                                             |
|   5 | There are practical applications of sonification in various industries, such as astronomy.                                       |
|   6 | The idea for the talk came from combining music and Kubernetes.                                                                  |
|   7 | The human brain is sensitive to changes in background sounds, known as the cocktail party effect.                                |
|   8 | The cocktail party effect allows people to focus on specific sounds while monitoring background noise for important information. |
|   9 | Auditory input can result in faster response times than visual input.                                                            |
|  10 | Audio cues are effective in monitoring, as seen with Geiger counters and hospital devices.                                       |
|  11 | Combining audio and visual input increases memory retention and reduces cognitive load.                                          |
|  12 | Audio can help relieve visual fatigue from prolonged screen time.                                                                |
|  13 | The demo architecture includes:                                                                                                  |
|  14 | Kubernetes cluster as the data source.                                                                                           |
|  15 | A Go-based controller that watches for events using the watch API.                                                               |
|  16 | The controller sends messages to SuperCollider via OSC (Open Sound Control) protocol.                                            |
|  17 | SuperCollider is a real-time audio synthesis environment.                                                                        |
|  18 | The demo maps Kubernetes events to sounds:                                                                                       |
|  19 | Pod created                                                                                                                      |
|  20 | Pod deleted                                                                                                                      |
|  21 | Pod crash looping                                                                                                                |
|  22 | Deployment scaling up                                                                                                            |
|  23 | SuperCollider uses OSC devs to listen for messages and synth devs to generate sounds.                                            |
|  24 | The demo includes an interactive experiment where the audience identifies events by sound.                                       |
|  25 | Chaos Mesh is used to simulate multiple events for a more realistic scenario.                                                    |
|  26 | The project could be expanded to sonify continuous metrics like CPU, memory, or error rates.                                     |
|  27 | Sound design was more challenging than the controller implementation.                                                            |
|  28 | SuperCollider supports advanced audio synthesis and integration with external tools.                                             |
|  29 | The talk enc                                                                                                                     |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=fzKp0YvS7Es)