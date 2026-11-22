---
layout: default
title: "Talks - Tim Paine: Building FPGA-based Machine Learning Accelerators in Python"
nav_order: 174
parent: PyCon US 2024
type: Video Note
description: "Tim Pay, a quantitative software developer at Cubist and Columbia University, presented a talk on building FPGA-based machine learning accelerators using Python."
resource: "https://www.youtube.com/watch?v=pFRFZDLnr-s"
youtube_stats:
  view_count: 2648
  like_count: 94
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

Tim Pay, a quantitative software developer at Cubist and Columbia University, presented a talk on building FPGA-based machine learning accelerators using Python.
He highlighted the significant evolution of the hardware ecosystem over the last decade, noting that tools like Vitis, Yosys, and open-source silicon projects have made hardware development more accessible and less expensive than in the past.
Pay demonstrated a workflow using PyTorch, Brevitas for quantization, and FIN to compile neural networks into hardware bitfiles for Xilinx Zynq boards, specifically the Pynq Z2, which he noted costs under $200.
Through live demos, he showed how to train a simple sine wave predictor and run an MNIST digit recognition model on the FPGA, achieving high accuracy and processing speeds of over 133,000 images per second.
He also introduced the LiteX framework for more complex system-on-chip designs, emphasizing that Python-based libraries now allow developers to create sophisticated hardware accelerators without needing deep expertise in traditional hardware description languages like Verilog.

# Main Points

|   # | Main point                                                                                                                                                                                      |
| --: | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | Tim Pay, a quantitative software developer at Cubist and Columbia University, presented on building FPGA-based machine learning accelerators using Python.                                      |
|   2 | The talk highlights that the hardware development ecosystem has transformed over the last decade, making FPGA design more accessible and affordable for hobbyists.                              |
|   3 | Key concepts include FPGAs as reconfigurable logic, ASICs as fixed-function chips, and System-on-Chip (SoC) architectures that bundle CPUs, GPUs, and accelerators.                             |
|   4 | Major FPGA manufacturers include Intel (Altera), AMD (Xilinx), and Lattice, with board makers like Digilent and Antmicro creating development hardware.                                         |
|   5 | The hardware development workflow involves logic design, simulation, verification, and synthesis, with tools like Verilog, VHDL, and Python-based libraries such as MyHDL, Amaranth, and Migen. |
|   6 | Open-source tools like Verilator, Cocotb, and Yosys are increasingly replacing proprietary vendor tools, similar to the software ecosystem's shift in the 1990s.                                |
|   7 | The Pynq project by Xilinx combines an ARM processor with FPGA fabric, allowing users to interact with custom hardware designs directly through Python and Jupyter notebooks.                   |
|   8 | The Pynq Z2 board is recommended as an entry-level device under $200 that supports Python-based hardware interaction and accelerator deployment.                                                |
|   9 | A workflow was demonstrated using PyTorch for model creation, Brevitas for quantization-aware training, and FIN to compile ONNX models into FPGA hardware.                                      |
|  10 | A simple sine wave prediction model was built from scratch in PyTorch, quantized, and successfully deployed on the FPGA to predict data points with minimal error.                              |
|  11 | An off-the-shelf MNIST digit recognition model was run on the Pynq device, achieving approximately 93% accuracy and processing 133,000 images per second.                                       |
|  12 | For more advanced projects, the LiteX framework allows users to define complex hardware systems, including DDR3 memory and PCIe interfaces, entirely in Python.                                 |
|  13 | The Night Fury board, a LiteX-based platform, offers higher performance and connectivity options for users ready to move beyond entry-level devices.                                            |
|  14 | The speaker emphasized that while the ecosystem is still in transition, Python serves as a crucial on-ramp for learning hardware design without requiring prior knowledge of Verilog or VHDL.   |
|  15 | Additional resources mentioned include the Chips Alliance, HLS4ML, XLS, and the Free and Open Source Silicon Foundation for chip fabrication.                                                   |
|  16 | High-level synthesis (HLS) tools are improving rapidly, often providing performance comparable to hand-optimized hardware designs for many use cases.                                           |
|  17 | The community around open-source silicon is vibrant, with many talented developers contributing to tools that make hardware development more accessible and less expensive.                     |

# Video

[![Video thumbnail](https://img.youtube.com/vi/pFRFZDLnr-s/hqdefault.jpg)](https://www.youtube.com/watch?v=pFRFZDLnr-s)

[Watch on YouTube](https://www.youtube.com/watch?v=pFRFZDLnr-s)
