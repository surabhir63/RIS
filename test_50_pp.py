import pandas as pd
import numpy as np
import gym
from stable_baselines3 import DQN  
from env_pp import RISAngleEnv  # ✅ Import the custom environment

# ✅ Load trained DQN model
env = RISAngleEnv("rl_training_data_50.csv", "best_angles_call.csv")  # Ensure dataset contains power info
model = DQN.load("ris_angle_rl_model_tuned_500")  # ✅ Ensure correct model name

# ✅ Test DQN model
results = []
obs = env.reset()
done = False
visited_positions = set()

while not done:
    if tuple(obs) in visited_positions:
        break  # Stop if already visited
    visited_positions.add(tuple(obs))

    # Store the current state (X, Y) before stepping
    current_x, current_y = obs[0], obs[1]

    # Predict the action and corresponding angle
    action, _ = model.predict(obs, deterministic=True)  
    predicted_angle = env.angles[action]

    # Step the environment and retrieve power from `info`
    obs, reward, done, info = env.step(action)
    predicted_power = info.get("power", None)  # Retrieve power from env

    # Append results
    results.append({"X": current_x, "Y": current_y, "Predicted Angle": predicted_angle, "Power (dBm)": predicted_power})

    # Debug prints
    print(f"Step: {len(results)}")
    print(f"  Current Position: [{current_x}, {current_y}]")
    print(f"  Predicted Action: {action}")
    print(f"  Predicted Angle: {predicted_angle}")
    print(f"  Predicted Power: {predicted_power}")
    print(f"  Reward: {reward}")
    print("-----------------------------")

# Save results to CSV
df_results = pd.DataFrame(results)
df_results.to_csv("rl_predicted_angles_dqn_final_50_poster.csv", index=False)
print("Predictions saved to rl_predicted_angles_dqn_final_50_poster.csv")
