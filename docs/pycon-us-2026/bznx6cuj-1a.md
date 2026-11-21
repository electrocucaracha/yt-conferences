---
layout: default
title: "Beyond the P-Value: A Data Scientist’s Guide to Tier-1 Feature Launches - Jyoti Yadav"
nav_order: 75
parent: PyCon US 2026
type: Video Note
description: "Jyoti, a data science leader at Loom (now part of Atlassian), presents a critical analysis of why standard data science metrics like p-values and confidence intervals often fail to capture the full..."
resource: "https://www.youtube.com/watch?v=bZNX6Cuj-1A"
youtube_stats:
  view_count: 193
  like_count: 2
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

Jyoti, a data science leader at Loom (now part of Atlassian), presents a critical analysis of why standard data science metrics like p-values and confidence intervals often fail to capture the full story of product launches.
Using a synthetic case study of Loom’s editing feature, she demonstrates how naive A/B testing can be misleading due to three key assumptions: non-random assignment, spillover effects where treatment impacts control users, and heterogeneous effects across different user segments.
To address these biases, she advocates for rigorous diagnostic methods, including propensity score matching (PSM) to correct for selection bias among opt-in power users and regression analysis to detect and account for social graph contamination.
By applying these techniques, the team discovered that the initial 38% increase in video recordings was overstated, with the true impact being significantly lower but still positive, particularly for team-based users who benefit from collaborative feedback loops.
The talk concludes with actionable recommendations, such as targeting specific high-value segments like enterprise accounts and emphasizing collaboration in marketing, to ensure that product decisions are based on accurate, deep-dive analysis rather than superficial headline metrics.

# Main Points

|   # | Main point |
| --: | ---------- |
|   1 | Standard data science tools like P-values and confidence intervals often fail to tell the entire story in product launches, potentially leading to inaccurate results with long-term negative effects. |
|   2 | The speaker presents a case study on Loom editing, where initial data showed a 38% increase in videos recorded per user with a very small P-value, suggesting a successful launch. |
|   3 | Three key assumptions must be questioned in any experiment: whether assignment was truly random, if treatment outcomes impact control users (spillover), and if the effect is constant across all users. |
|   4 | Selection bias occurs when comparing users who opted in versus those who did not, as opt-in users are often highly engaged power users, making the comparison non-random and biased. |
|   5 | Spillover effects happen when a user's treatment leaks into another user's outcome, contaminating the control group; this can be detected by regressing control users' activity on the number of treated teammates. |
|   6 | Propensity Score Matching (PSM) is recommended to correct for selection bias by matching opt-in users to similar non-opt-in users based on pre-engagement scores and other covariates. |
|   7 | PSM involves scoring users with logistic regression, matching nearest neighbors, applying a caliper threshold to drop poor matches, and calculating the difference in means for the matched sample. |
|   8 | In the Loom case, PSM corrected the estimated impact from a 4.28 increase to a 1.00 increase in videos per user, revealing that the initial naive baseline was wrong by a factor of five. |
|   9 | Standardized Mean Difference (SMD) should be checked before and after matching to ensure balance; an SMD below 0.1 indicates that the groups are sufficiently comparable. |
|  10 | Heterogeneous effects analysis, or uplift modeling, helps identify which specific user segments benefit most from a feature, rather than just looking at the average treatment effect. |
|  11 | Team-based users and enterprise accounts often benefit more from social features like Loom editing due to feedback cycles, while solo creators may see less value. |
|  12 | Uplift models can be built using simple methods like the S-learner, predicting outcomes for treated and control scenarios to determine individual user impact. |
|  13 | Key curves visualize the concentration of lift, showing that targeting the top 20% of users can capture 41% of the total value, allowing for more efficient resource allocation. |
|  14 | Product recommendations should be tailored to high-value segments, such as defaulting features on for team accounts and emphasizing collaboration in marketing copy. |
|  15 | Data scientists should spend time verifying randomization, checking for spillover, and applying PSM before finalizing launch decisions to avoid irreversible errors based on biased data. |

# Video

[![Video thumbnail](https://img.youtube.com/vi/bZNX6Cuj-1A/hqdefault.jpg)](https://www.youtube.com/watch?v=bZNX6Cuj-1A)

[Watch on YouTube](https://www.youtube.com/watch?v=bZNX6Cuj-1A)
