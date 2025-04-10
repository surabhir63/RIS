# AI-Based System for 6G Reconfigurable Intelligent Surfaces

## Table of Contents
- [Abstract](#abstract)
- [Overview](#overview)
- [Motivation & Problem Statement](#motivation--problem-statement)
- [Key Features](#key-features)
- [System Architecture](#system-architecture)
- [Technologies Used](#technologies-used)
- [Results Summary](#results-summary)
- [Repository Structure](#repository-structure)
- [Author](#author)
- [License](#license)

---

## Abstract
As wireless communication technologies are introduced into more aspects of our lives, from Internet of Things (IoT) to AI computing on the network edge, the number of wireless users and devices is also increasing. To meet this demand, the next generation of wireless communication requires a scalable and sustainable solution to ensure fast and reliable connectivity. Reconfigurable Intelligent Surfaces (RIS) use passive beamforming to reach wireless endpoints and reduce the impact of dead zones. However, the research and development of RIS systems is still in its early stages. Most research remains theoretical, with limited experimental implementations exploring its real-time adaptability. Additionally, prototypes tend to be narrowband, which are not ideal for the large frequency bands comprising 6G and are difficult to scale. We are designing a framework that combines machine learning, channel estimation, ray tracing simulation, and embedded design to tune the antenna elements on the surface in real time. Our approach combines three key components: RIS simulation to model surface behavior to ray trace with different configuration angles, a channel estimation pipeline utilizing synthetic channels from the simulation to evaluate throughput and signal strength, and AI-driven reflection angle optimization using a reinforcement learning model to achieve high signal to noise ratio (SNR). Using a trained Q-learning model, the RIS will configure its reflection angle to maximize throughput for an end user at a given position. 

 

 
---

## Overview
This project is the outcome of a senior design initiative at Drexel University (ECE 492), advised by Dr. Kapil Dandekar, conducted by Surabhi Rajbhandar, Loukas Athanitis, Brian Cole, and Mari Takizala. We leverage Wireless InSite simulations and deep reinforcement learning (DQN) to demonstrate a scalable, real-time RIS optimization framework for indoor wireless environments.

---

## Motivation & Problem Statement
In complex indoor environments, dead zones and signal degradation are common challenges. Traditional repeaters introduce noise and consume power. Our RIS system passively enhances signal coverage by optimizing reflection angles, making it an energy-efficient, scalable, and adaptive solution for next-generation 6G networks.

---

## Key Features
- Wireless InSite simulations of indoor environments with and without RIS
- Automated dataset generation through batch ray-tracing simulations to create custom Rl-ennvironment
- DQN-based reinforcement learning to predict optimal RIS reflection angles
- Supervised learning baseline models (Random Forest, K-Nearest Neighbors) for performance comparison
- Software-defined radio experiments with DragonRadio
- Visualizations of power distributions and model accuracy to assess optimization impact
---

## System Architecture
- **Simulation & Dataset Generation**: Wireless InSite used to simulate indoor propagation and collect received power values across angles (-170° to 170°)
- **AI Model**: DQN trained to maximize received power based on location and angle feedback
- **Validation**: SDR-based lab experiments using passive reflectors confirm simulation-based predictions (CURRENTLY ON PROGRESS)

---

## Technologies Used
- **Python**: Data pipelines, Machine Learning model training, visualization
- **Wireless InSite**: Ray tracing and dataset generation
- **MATLAB**: Signal processing, channel estimation prototypes
- **ZephyrOS on STM32**: Real-time middleware control
- **DragonRadio**: SDR-based signal testing

---

## Results Summary
- **DQN Evaluation**: MAE = 5.3°, RMSE = 11.1°, R² = 0.979
- **Comparative Models**:
  - K-Nearest Neighbors: MAE = 21.9°, R² = 0.72
  - Random Forest: MAE = 16.4°, R² = 0.808
- **Heatmaps**: Optimal RIS configuration resulted in significantly improved power distribution across 50 receiver points

![image](https://github.com/user-attachments/assets/698caeb1-f272-44f8-9773-bc37cf66435f)
![image](https://github.com/user-attachments/assets/a77844b3-5b7d-4d4c-bf3a-69e274259e09)
![image](https://github.com/user-attachments/assets/94a6d4d5-71b6-4684-af57-3ef5adb1e7c7)


<img width="379" alt="image" src="https://github.com/user-attachments/assets/a362c971-4224-40b7-842f-a3875343c504" />






## Repository Structure
```
Reconfigurable_Intelligent_Surface/
├── ML_scripts/                 # Python scripts and model training/testing
│   ├── models/                # Pretrained RL model files
├── data/                      # Datasets for RL and simulation
├── WireLess_Insite_models/   # XML/EES files for InSite simulations
├── Results/                   # Power plots, angle comparisons, heatmaps
├── Report/                    # Final documentation and figures
└── README.md
```

---
![Uploading image.png…]()


