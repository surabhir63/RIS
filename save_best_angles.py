import pandas as pd

# Load the dataset
df = pd.read_csv("extracted_power_dataset_call_dataset.csv")

# Find the optimal angle for each unique (N, X, Y) based on max power
optimal_angles = df.loc[df.groupby(['N', 'X', 'Y'])['Power (dBm)'].idxmax(), ['N', 'X', 'Y', 'Angle', 'Power (dBm)']]

# Save the results to a new CSV file
optimal_angles.to_csv("best_angles_call.csv", index=False)

print("Optimal angles saved to 'optimal_angles.csv'")
