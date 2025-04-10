import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# ✅ Load dataset
df_predictions = pd.read_csv("rl_predicted_vs_actual_dqn_test_50_poster.csv")

# ✅ Debug: Check column names
print("Column Names in DataFrame:")
print(df_predictions.columns)

# ✅ Check if 'Power (dBm)' column exists
if 'Power (dBm)_predicted' not in df_predictions.columns:
    raise KeyError("Column 'Power (dBm)' not found in the DataFrame. Please check the column names.")

# ✅ Filter out invalid power values (-250 dBm)
df_filtered = df_predictions[df_predictions["Power (dBm)_predicted"] > -250]

# ✅ Create pivot table for heatmap
heatmap_data = df_filtered.pivot_table(index="Y", columns="X", values="Power (dBm)_predicted", aggfunc="mean")

# ✅ Fill NaN values in pivot table (if any)
heatmap_data = heatmap_data.fillna(heatmap_data.min())

# ✅ Create heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(
    heatmap_data,
    cmap="viridis",
    annot=False,
    cbar_kws={"label": "Power (dBm)"},
    vmin=-250,  # Set the minimum value for the color scale
    vmax=heatmap_data.max().max()  # Set the maximum value for the color scale
)

# ✅ Reduce the number of labels on X and Y axes
num_ticks = 10  # Number of labels you want on each axis
x_ticks = np.linspace(0, len(heatmap_data.columns) - 1, num_ticks, dtype=int)  # Spread labels evenly
y_ticks = np.linspace(0, len(heatmap_data.index) - 1, num_ticks, dtype=int)  # Spread labels evenly

# ✅ Set custom X and Y axis labels with zero decimal places
plt.xticks(x_ticks, labels=np.round(heatmap_data.columns[x_ticks], 0), rotation=45, fontsize=10)
plt.yticks(y_ticks, labels=np.round(heatmap_data.index[y_ticks], 0), rotation=0, fontsize=10)

# ✅ Labels and title
plt.xlabel("Receiver X-coordinate", fontsize=12)
plt.ylabel("Receiver Y-coordinate", fontsize=12)
plt.title("Power Distribution Across 50 Receiver Positions with optimal RIS configuration", fontsize=14, fontweight="bold")

# ✅ Save the plot
output_file = "power_distribution_heatmap_50_final_poster.png"  # File name for the saved plot
plt.savefig(output_file, dpi=300, bbox_inches="tight")  # Save as PNG with high resolution
print(f"Plot saved as {output_file}")

# ✅ Show plot
plt.tight_layout()  # Adjust layout to prevent label overlap
plt.show()