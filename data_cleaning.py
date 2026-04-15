import pandas as pd

df = pd.read_csv("data/raw/sales_data.csv")

df['Order_Date'] = pd.to_datetime(df['Order_Date'])

df.drop_duplicates(inplace=True)
df.fillna(0, inplace=True)

df.to_csv("data/processed/clean_sales_data.csv", index=False)

print("✅ Data Cleaned")