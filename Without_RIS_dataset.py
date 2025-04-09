import pandas as pd

input_file = "CallTest.power.t001_02.r004.p2m"  
output_file = "CallTest_withoutRIS.csv"

# ✅ Read the file and process lines
data = []
with open(input_file, "r") as file:
    for line in file:
        if line.startswith("#") or line.strip() == "":  # Skip metadata and empty lines
            continue
        data.append(line.split())  # Split values by whitespace

# ✅ Convert data to DataFrame
columns = ["Index", "X (m)", "Y (m)", "Z (m)", "Distance (m)", "Power (dBm)", "Phase (deg)"]
df = pd.DataFrame(data, columns=columns)

# ✅ Convert appropriate columns to numeric
df = df.astype({
    "Index": int,
    "X (m)": float,
    "Y (m)": float,
    "Z (m)": float,
    "Distance (m)": float,
    "Power (dBm)": float,
    "Phase (deg)": float
})

# ✅ Save as CSV
df.to_csv(output_file, index=False)
print(f"File saved as {output_file}")
