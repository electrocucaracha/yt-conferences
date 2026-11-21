---
layout: default
title: "Python in the Cloud: Introduction to AWS with Boto3 - Alison Orellana-Rios"
nav_order: 18
parent: PyCon US 2026
type: Video Note
description: "The speaker presents a fundamental introduction to using Python and the Boto3 library to automate Amazon Web Services (AWS) tasks, highlighting the benefits of replacing manual console operations w..."
resource: "https://www.youtube.com/watch?v=lBw1ABtOqbw"
youtube_stats:
  view_count: 137
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

The speaker presents a fundamental introduction to using Python and the Boto3 library to automate Amazon Web Services (AWS) tasks, highlighting the benefits of replacing manual console operations with reproducible scripts to reduce human error.
The presentation covers the setup process, including installing Boto3 via pip and configuring AWS credentials using IAM roles, named profiles, or environment variables, while emphasizing security best practices such as avoiding hardcoded credentials.
Through live demonstrations, the speaker illustrates how to interact with core AWS services by listing S3 buckets, uploading files to storage, creating and managing EC2 instances, and executing serverless Lambda functions.
The talk also discusses the advantages of automation, such as scalability and reproducibility, and suggests using mocks for safe testing environments to prevent costly resource leaks.
Finally, the speaker outlines a learning path that progresses from basic Python syntax to understanding AWS services, mastering Boto3, and implementing CI/CD cycles, while briefly comparing this approach to other infrastructure-as-code tools like Terraform and CloudFormation.

# Main Points

|   # | Main point |
| --: | ---------- |
|   1 | The presentation introduces Python in the cloud using AWS and Boto3, focusing on automating manual processes to reduce human error and improve reproducibility. |
|   2 | Boto3 is identified as the official SDK for Python that allows users to create, configure, and manage AWS resources such as EC2, S3, and Lambda. |
|   3 | The speaker highlights the importance of avoiding manual console operations, which can lead to broken configurations, by using scripts that can be tested and verified before execution. |
|   4 | Setting up Boto3 requires installing the library via pip and configuring AWS credentials using the `aws configure` command, environment variables, or named profiles. |
|   5 | Named profiles are recommended for portability across machines, while environment variables are noted as less secure because credentials can be easily exposed. |
|   6 | A demonstration of listing S3 buckets involves importing Boto3, creating an S3 client, and iterating through the response to display bucket names. |
|   7 | Uploading files to S3 is achieved by using the `upload_file` function, specifying the local file path, the target bucket, and the desired key or folder structure. |
|   8 | Creating EC2 instances requires defining specific parameters such as instance name, capacity type, and region, with a strong recommendation to delete instances after testing to avoid unexpected costs. |
|   9 | Executing serverless code via Lambda is demonstrated by calling a basic function from Python, illustrating how to trigger and manage serverless workflows programmatically. |
|  10 | The benefits of using Boto3 include automation, scalability for complex test cases, and reproducibility of infrastructure cycles without manual intervention. |
|  11 | Best practices emphasize not hardcoding credentials, using IAM roles for security, and testing in secure environments to prevent data breaches or financial losses. |
|  12 | The suggested learning path includes mastering Python syntax, understanding core Amazon services, learning Boto3 for automation, and adopting CI/CD cycles for robust deployment. |
|  13 | A comparison with other tools like Terraform or CloudFormation indicates that the choice depends on specific use cases, as each tool has different configurations and strengths in automation versus code flow. |
|  14 | The speaker encourages leveraging AI tools to assist in writing and debugging scripts, making the process of automating cloud services more accessible and efficient. |
|  15 | Participation in communities like PyLadies, Women Techmakers, and AWS User Groups is recommended for learning and networking opportunities in the tech field. |

# Video

[![Video thumbnail](https://img.youtube.com/vi/lBw1ABtOqbw/hqdefault.jpg)](https://www.youtube.com/watch?v=lBw1ABtOqbw)

[Watch on YouTube](https://www.youtube.com/watch?v=lBw1ABtOqbw)
