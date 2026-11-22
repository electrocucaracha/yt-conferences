---
layout: default
title: "Talks - Kat Scott: Open Source Robotics with Python: Learn Robotics with No Robot Required"
nav_order: 180
parent: PyCon US 2024
type: Video Note
description: "Katherine Scott, a developer advocate for the ROS project, presents a tutorial on learning open-source robotics with Python using the ROS 2 framework and the Gazebo simulator."
resource: "https://www.youtube.com/watch?v=YwozYGCslUY"
youtube_stats:
  view_count: 513
  like_count: 8
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

Katherine Scott, a developer advocate for the ROS project, presents a tutorial on learning open-source robotics with Python using the ROS 2 framework and the Gazebo simulator.
The session demonstrates how to set up a development environment using a Rocker container to avoid complex hardware dependencies, allowing users to simulate a TurtleBot 4 robot.
Scott explains core ROS concepts, such as nodes, topics, and the publish-subscribe model, by showing how to read odometry data to determine the robot's position and send velocity commands to control its movement.
The tutorial progresses to building a custom Python node that executes a "barrel roll" behavior via a ROS service, utilizing a timer to continuously publish motion commands until the robot returns to its starting point.
Finally, the presentation integrates sensor data by subscribing to a hazard detection topic, enabling the robot to automatically stop and reset its behavior when it collides with a wall, thereby illustrating a complete sense-think-act robotic loop.

# Main Points

|   # | Main point                                                                                                                                                              |
| --: | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Katherine Scott, a developer advocate for the ROS project, presents a session on open-source robotics using Python without requiring physical hardware.                 |
|   2 | The talk utilizes Gazebo, an open-source robot simulator, to replace physical hardware, allowing for safe and accessible learning of robotics concepts.                 |
|   3 | ROS (Robot Operating System) is described as a free, open-source framework that acts as a layer on top of operating systems like Linux to facilitate robot development. |
|   4 | The core robotics paradigm discussed is "sense, think, act," where robots gather environmental data, process it with code, and execute physical actions.                |
|   5 | The session uses the Turtlebot 4, a simulated robot composed of a base, depth camera, 2D LiDAR, and a Raspberry Pi 4, to demonstrate practical applications.            |
|   6 | A Rocker container, which supports GPU and GUI, is used to simplify the installation of ROS, Gazebo, and dependencies for a consistent development environment.         |
|   7 | Key ROS concepts are mapped to Python equivalents: workspaces correspond to virtual environments, nodes are programs, and topics function as pub/sub data channels.     |
|   8 | The tutorial demonstrates creating a ROS Python package named `tb4_toy` with a node called `toy_node` using the `ros2 pkg create` command.                              |
|   9 | Command-line tools such as `ros2 topic list` and `ros2 topic echo` are used to introspect robot data, specifically reading odometry to determine the robot's position.  |
|  10 | A Python node is developed to subscribe to the `/odom` topic and log the robot's XYZ coordinates, illustrating the basic publish/subscribe API.                         |
|  11 | Robot movement is controlled by publishing Twist messages to the `/cmd_vel` topic, which defines linear and angular velocity components.                                |
|  12 | The `ros2 topic pub` command is used to manually send velocity commands, demonstrating how to drive the robot via the command line.                                     |
|  13 | A "barrel roll" behavior is implemented by combining odometry data with velocity commands to move the robot in a circle until it returns to its start position.         |
|  14 | ROS services are introduced as synchronous function calls, allowing the robot to execute complex behaviors like the loop when triggered by a service call.              |
|  15 | A ROS timer is used to periodically publish velocity commands at 10 Hz to maintain the circular motion of the robot.                                                    |
|  16 | The `package.xml` file is updated to declare dependencies on specific message types, such as `nav_msgs` and `geometry_msgs`, required for the node to function.         |
|  17 | Hazard detection is integrated by subscribing to the `/hazard_detection` topic to monitor bumper sensor inputs.                                                         |
|  18 | The robot's behavior is modified to stop immediately and publish a zero-velocity command when a wall collision is detected, preventing continuous bumping.              |
|  19 | The session concludes by emphasizing the ROS community resources, including Discord, Stack Exchange, and documentation, for further learning and support.               |

# Video

[![Video thumbnail](https://img.youtube.com/vi/YwozYGCslUY/hqdefault.jpg)](https://www.youtube.com/watch?v=YwozYGCslUY)

[Watch on YouTube](https://www.youtube.com/watch?v=YwozYGCslUY)
