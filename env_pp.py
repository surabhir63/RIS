import gym
import numpy as np
import pandas as pd
import random

class RISAngleEnv(gym.Env):
    def __init__(self, training_data_file, best_angles_file):
        # Load dataset
        self.data = pd.read_csv(training_data_file)

        # Load best angles dataset
        self.best_angle_data = pd.read_csv(best_angles_file).set_index(["X", "Y"])["Angle"].to_dict()

        # Extract unique (X, Y) positions (Zig-Zag Path)
        self.path = self.data[['X', 'Y']].drop_duplicates().values.tolist()
        self.current_index = 0  
        self.current_state = self.path[self.current_index]

        # Define available angles from -170 to 170 in 1-degree steps
        self.angles = np.arange(-170, 171, 1)  # Explores every degree!
        self.action_space = gym.spaces.Discrete(len(self.angles))

        # Observation space: (X, Y)
        self.observation_space = gym.spaces.Box(
            low=np.array([self.data["X"].min(), self.data["Y"].min()]),
            high=np.array([self.data["X"].max(), self.data["Y"].max()]),
            dtype=np.float32
        )

    def reset(self):
        """ Reset environment to first zig-zag path point """
        self.current_index = 0
        self.current_state = self.path[self.current_index]
        return np.array(self.current_state)

    def step(self, action_index):
        """ Choose an angle and get reward based on Power (dBm) """
        selected_angle = self.angles[action_index]

        # Get power value from dataset
        row = self.data[
            (self.data["X"] == self.current_state[0]) & 
            (self.data["Y"] == self.current_state[1]) & 
            (self.data["Angle"] == selected_angle)
        ]
        power = row["Power (dBm)"].values[0] if not row.empty else -150  # Default low power when missing

        # Get best possible angle and power
        best_angle = self.best_angle_data.get((self.current_state[0], self.current_state[1]), None)
        best_row = self.data[
            (self.data["X"] == self.current_state[0]) & 
            (self.data["Y"] == self.current_state[1]) & 
            (self.data["Angle"] == best_angle)
        ]
        best_power = best_row["Power (dBm)"].values[0] if not best_row.empty else -150

        # Improved Reward Function
        if best_angle is not None:
            if selected_angle == best_angle:
                reward = 100  # Max reward for choosing the best angle
            else:
                reward = -abs(selected_angle - best_angle) / 2  # ✅ Penalize based on distance from best angle
        else:
            reward = -50  # Strong penalty if no best angle exists

        # Print step details
        print(f"Step: {self.current_index + 1}")
        print(f"  Current Position: {self.current_state}")
        print(f"  Selected Angle: {selected_angle}")
        print(f"  Best Angle: {best_angle if best_angle is not None else 'Unknown'}")
        print(f"  Power Value: {power} dBm")
        print(f"  Best Power Value: {best_power} dBm")
        print(f"  Reward: {reward}")
        print("-" * 50)

        # Move to next receiver point
        self.current_index += 1
        done = self.current_index >= len(self.path)
        if not done:
            self.current_state = self.path[self.current_index]

        # Return power in `info` dictionary
        return np.array(self.current_state), reward, done, {"power": power}

    def render(self):
        print(f"Current Position: {self.current_state}, Best Angle: {self.best_angle_data.get(tuple(self.current_state), 'Unknown')}")
