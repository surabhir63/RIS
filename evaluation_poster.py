import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# Load predicted angles
df_predicted = pd.read_csv("rl_predicted_angles_dqn_final_50_poster.csv")

# Load actual angles
df_actual = pd.read_csv("best_angles_call.csv")

# Merge datasets on (X, Y) to compare predicted vs actual
df_merged = df_predicted.merge(df_actual, on=["X", "Y"], suffixes=("_predicted", "_actual"))

# Remove rows where Power is 250
##df_merged_filtered = df_merged[df_merged["Power (dBm)"] != 250]

# Calculate MAE, RMSE, and R² after filtering
mae_filtered = mean_absolute_error(df_merged["Angle"], df_merged["Predicted Angle"])
rmse_filtered = mean_squared_error(df_merged["Angle"], df_merged["Predicted Angle"], squared=False)
r2_filtered = r2_score(df_merged["Angle"], df_merged["Predicted Angle"])

print(f"Model Evaluation Metrics (DQN) - Filtered Data:")
print(f" MAE  (Mean Absolute Error): {mae_filtered:.3f}")
print(f" RMSE (Root Mean Squared Error): {rmse_filtered:.3f}")
print(f" R² Score: {r2_filtered:.3f}")

# Save filtered merged results
df_merged.to_csv("rl_predicted_vs_actual_dqn_test_50_poster.csv", index=False)
print("Merged predictions (filtered) saved to rl_predicted_vs_actual_dqn_test_50_pp_filtered.csv")

# Plot actual vs. predicted angles after filtering
plt.figure(figsize=(8, 6))
plt.scatter(df_merged["Angle"], df_merged["Predicted Angle"], color="blue", label="Predicted vs. Actual")
plt.plot([-180, 180], [-180, 180], color="red", linestyle="--", label="Perfect Prediction (y=x)")
plt.xlabel("Actual Optimal Angle (°)")
plt.ylabel("Predicted Optimal Angle (°)")
plt.title("DQN: Actual vs. Predicted Optimal RIS Angles (Filtered Data) for 50 Receiver Positions")
plt.legend()
plt.grid(True)
plt.savefig("actual_vs_predicted_angles_dqn_50_poster_plot.png")
plt.show()
