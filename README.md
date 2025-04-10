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

- AI Model  

We implemented a reinforcement learning based Deep Q-Network (DQN) model to optimize RIS configuration. The state of the system is defined by key parameters such as receiver’s position (X, Y coordinates), RIS configuration angles, and received power at receiver’s position for different angles.  

 

To train the model, we used a dataset generated though Wireless InSite simulations. We developed a script to automate the simulation process where the RIS was configured for each angle from –170° to 170°. The script collected received power values at different receiver positions, creating a comprehensive dataset for AI model training.  

 

The AI agent interacts with the environment by selecting an RIS reflection angle from the predefined range. It explores different angles to determine the optimal angle that enhances signal power. The agent receives awards or penalties based on how well the chosen angle enhances received signal power. The reward function is directly based on the received power level, meaning higher power values result in higher rewards. This guides the AI agent towards optimal angle selection. Through iterative learning and experience, the model refines its decision-making process to optimize reflection angles and maximize received power at different receiver positions.  
 

The results of using Deep Q-Network (DQN) algorithm demonstrated a good correlation between predicted and optimal RIS reflection angles with high R² score (0.979) and low Mean Absolute Error (5.316).

![image](https://github.com/user-attachments/assets/698caeb1-f272-44f8-9773-bc37cf66435f)
![image](https://github.com/user-attachments/assets/a77844b3-5b7d-4d4c-bf3a-69e274259e09)
![image](https://github.com/user-attachments/assets/94a6d4d5-71b6-4684-af57-3ef5adb1e7c7)


<p align="center">
  <span style="font-size:40px; font-weight:bold;">
    Wireless-Insite Without RIS and With RIS Simulation Results
  </span>
</p>
<p align="center">
  <img src="https://github.com/user-attachments/assets/36b17567-2be6-4c01-aee5-0f2b2489d5b9" width="45%" />
  <img src="https://github.com/user-attachments/assets/2db5cefa-551c-4220-b885-829c6da50e38" width="45%" />
</p>








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



