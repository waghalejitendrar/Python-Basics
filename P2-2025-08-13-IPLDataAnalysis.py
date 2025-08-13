import pandas as pd

# Sample data
data = {
    "Player": ["Virat", "Rohit", "Dhoni"],
    "Runs": [973, 648, 455],
    "Matches": [16, 14, 15]
}
df = pd.DataFrame(data)

# Calculate average runs
df["Avg Runs"] = df["Runs"] / df["Matches"]
print(df)

# Plot
import matplotlib.pyplot as plt
plt.bar(df["Player"], df["Avg Runs"], color="orange")
plt.xlabel("Players")
plt.ylabel("Average Runs")
plt.title("IPL Player Performance")
plt.show()
