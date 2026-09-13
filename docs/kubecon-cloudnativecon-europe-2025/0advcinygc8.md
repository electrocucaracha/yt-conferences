---
type: Video Note
title: "Lightning Talk: High Availability With '503: Unavailable' - Robert-Jan Huijsman, Reboot"
description: 'The speaker discusses high availability in software systems, emphasizing that users'' happiness is the ultimate goal. They acknowledge that returning a 503 "unavailable" status code can be problematic, as it''s meant to be retryable. Instead...'
resource: https://www.youtube.com/watch?v=0adVcinYGC8
tags: ["kubecon-cloudnativecon-europe-2025", video, learning]
status: stable
generated: { by: process:yt-conferences-okf, at: 2026-09-12T00:00:00Z }
---

# Summary

The speaker discusses high availability in software systems, emphasizing that users' happiness is the ultimate goal.
They acknowledge that returning a 503 "unavailable" status code can be problematic, as it's meant to be retryable.
Instead, they introduce Reboot, an open-source framework for cloud-native applications that encourages clients to retry errors, making it easier for back-end engineers to return 503s without compromising availability.
By trusting clients to retry and ensuring safe retries through item potency, Reboot enables systems to remain highly available while still returning meaningful error codes.
# Main Points

|   # | Main point |
| --: | ---------- |

# Video

[Watch on YouTube](https://www.youtube.com/watch?v=0adVcinYGC8)