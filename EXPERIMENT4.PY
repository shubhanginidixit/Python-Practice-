import pandas as pd

# Sample data
data = {
    "Marks": [78, 85, 96, 85, 67, 78, 90]
}

# Create DataFrame
df = pd.DataFrame(data)

# Calculate statistics
mean_value = df["Marks"].mean()
median_value = df["Marks"].median()
mode_value = df["Marks"].mode()

print("Mean:", mean_value)
print("Median:", median_value)
print("Mode:", mode_value[0])