import pandas as pd
import os
import re
from glob import glob

# Define the folder containing .p2m files
data_folder = r"C:\Users\scsdc\senior_design\Power"  # CHANGE THIS to your actual folder

# Get all .p2m files
p2m_files = glob(os.path.join(data_folder, "*.p2m"))

# Initialize a list to store extracted data
data_list = []

# Process each .p2m file
for file_path in p2m_files:
    # Extract angle from filename using regex
    angle_match = re.search(r"sin_(-?\d+)", file_path)
    if angle_match:
        angle = int(angle_match.group(1))  # Extracted angle
    else:
        continue  # Skip file if angle not found

    # Read file content
    with open(file_path, 'r', encoding="utf-8") as file:
        lines = file.readlines()

    # Extract data (skip first 3 header lines)
    for line in lines[3:]:  
        parts = line.strip().split()
        if len(parts) >= 7:  # Ensure correct data format
            try:
                n, x, y, z, distance, power, phase = map(float, parts[:7])  # Extract first 6 columns
                data_list.append([n, x, y, z, distance, power, phase, angle])
            except ValueError:
                continue  # Skip lines that cannot be converted

# Create DataFrame
columns = ["N","X", "Y", "Z", "Distance", "Power (dBm)", "Phase (deg)", "Angle"]
df = pd.DataFrame(data_list, columns=columns).sort_values(by=["Angle"], ascending=True)

# Save dataset for analysis
df.to_csv("extracted_power_dataset_call_dataset.csv", index=False)
print("Dataset saved as extracted_power_dataset.csv")
