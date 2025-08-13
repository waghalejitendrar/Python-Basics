# Reading CSV (example CSV file path)
# df = pd.read_csv("ipl_data.csv")

# Creating DataFrame manually
df = pd.DataFrame({
    "Name": ["A", "B", "C"],
    "Score": [10, 20, 30]
})
print(df.head())
print(df.describe())
