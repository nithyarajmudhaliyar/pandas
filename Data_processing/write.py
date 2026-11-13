import pandas as pd

# Create a DataFrame
df = pd.DataFrame({
    "Name": ["John", "Anna", "Peter", "Linda"],
    "Age": [28, 24, 35, 32],
    "City": ["New York", "Los Angeles", "Chicago", "Houston"]
})

print(df)

# Save DataFrame to CSV
df.to_csv("Create_Data/output.csv", index=False)

# Save DataFrame to Excel
df.to_excel("Create_Data/output.xlsx", index=False)

# Save DataFrame to JSON
df.to_json("Create_Data/output.json", index=False)

# index=False -> Not save index in the file