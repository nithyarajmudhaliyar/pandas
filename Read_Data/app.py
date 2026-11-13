import pandas as pd

# Read data from CSV, Excel, JSON into a DataFrame
df_csv = pd.read_csv("sales_data.csv",encoding="latin1")
df_xlsx = pd.read_excel("sales_data.xlsx")
df_json = pd.read_json("sales_data.json")

print(df_csv, df_xlsx, df_json)

# GCSFS - Google Cloud Storage File System is used to read data from GCS into a DataFrame.
# We can also use it to write data from a DataFrame to GCS.

