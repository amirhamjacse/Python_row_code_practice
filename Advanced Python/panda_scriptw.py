import pandas as pd
# Read CSV
df = pd.read_csv("data.csv")

# Read Excel
df = pd.read_excel("data.xlsx")

# Save to CSV
df.to_csv("output.csv", index=False)