import pandas as pd
import json

df = pd.read_csv("data/twcs.csv", nrows=1000)
print("Schema info:")
print(df.dtypes)
print("\nFirst 5 rows:")
print(df.head().to_string())

# Also check for 'inbound' or similar columns.
print("\nColumns:", df.columns.tolist())
