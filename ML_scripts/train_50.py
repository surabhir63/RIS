import matplotlib.pyplot as plt
import numpy as np
import gym
from stable_baselines3 import DQN  
from rl_ris_env import RISAngleEnv

# ✅ Load RL environment
env = RISAngleEnv("rl_training_data_50.csv", "best_angles_call.csv")


# ✅ Train RL agent
model = DQN(
    "MlpPolicy", 
    env, 
    verbose=1,
    learning_rate=0.0001,   # Learning rate remains the same
    buffer_size=100000,     # Experience replay buffer
    learning_starts=1000,   # Delay learning start
    batch_size=64,          # Batch size for updates
    gamma=0.99,             # Discount factor for future rewards
    tau=0.005,              # Soft target update
    train_freq=(1, "step"), # Train at every step
    gradient_steps=2,       # More updates per step
    target_update_interval=1000, # Update target network every 5000 steps
    exploration_fraction=0.3,    # 30% exploration before switching to exploitation
    exploration_final_eps=0.02,  # Minimum exploration rate
    device="auto"           # Use GPU if available
)

# ✅ Train model
model.learn(total_timesteps=50000)

# ✅ Save trained model
model.save("ris_angle_rl_model_tuned_500")
print("✅ RL model trained and saved as ris_angle_rl_model_tuned")
