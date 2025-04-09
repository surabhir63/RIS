import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load datasets
df_predictions = pd.read_csv("rl_predicted_vs_actual_dqn_test_50_pp.csv")
df_calltest = pd.read_csv("Without_RIS_data.csv")



df_calltest = df_calltest.rename(columns={"X (m)": "X", "Y (m)": "Y"})


# Debug: Check column names
print("Column Names in Predictions DataFrame:", df_predictions.columns)
print("Column Names in CallTest DataFrame:", df_calltest.columns)

# Check if required columns exist
required_columns = ["X", "Y", "Power (dBm)"]
for col in required_columns:
    if col not in df_predictions.columns:
        raise KeyError(f"Column '{col}' not found in Predictions DataFrame.")
    if col not in df_calltest.columns:
        raise KeyError(f"Column '{col}' not found in CallTest DataFrame.")

# Merge datasets on (X, Y) to retain only common positions
df_merged = df_predictions.merge(df_calltest, on=["X", "Y"], suffixes=("_pred", "_calltest"))

# Debug: Check merged DataFrame
print("Merged DataFrame Shape:", df_merged.shape)

# Filter out invalid power values (-250 dBm)
## df_filtered = df_merged[df_merged["Power (dBm)_calltest"] > -250]

# Create pivot table for heatmap using CallTest power values
heatmap_data = df_merged.pivot_table(index="Y", columns="X", values="Power (dBm)_calltest", aggfunc="mean")

# Fill NaN values in pivot table (if any)
heatmap_data = heatmap_data.fillna(heatmap_data.min())

# Create heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(
    heatmap_data,
    cmap="viridis",
    annot=False,
    cbar_kws={"label": "Power (dBm)"},
    vmin=-250,
    vmax=heatmap_data.max().max()
)

# Reduce the number of labels on X and Y axes
num_ticks = 10  # Number of labels you want on each axis
x_ticks = np.linspace(0, len(heatmap_data.columns) - 1, num_ticks, dtype=int)
y_ticks = np.linspace(0, len(heatmap_data.index) - 1, num_ticks, dtype=int)

# Set custom X and Y axis labels
plt.xticks(x_ticks, labels=np.round(heatmap_data.columns[x_ticks], 0), rotation=45, fontsize=10)
plt.yticks(y_ticks, labels=np.round(heatmap_data.index[y_ticks], 0), rotation=0, fontsize=10)

# Labels and title
plt.xlabel("Receiver X-coordinate", fontsize=12)
plt.ylabel("Receiver Y-coordinate", fontsize=12)
plt.title("Power Distribution Across 50 Receiver Positions without optimal RIS configuration", fontsize=14, fontweight="bold")

# Save the plot
output_file = "power_distribution_heatmap_calltest.png"
plt.savefig(output_file, dpi=300, bbox_inches="tight")
print(f"Plot saved as {output_file}")

# Show plot
plt.tight_layout()
plt.show()
