import sqlite3
import pandas as pd

df = pd.read_csv("data/processed/clean_sales_data.csv")

conn = sqlite3.connect("database/sales.db")

df.to_sql("sales", conn, if_exists="replace", index=False)

print("✅ SQL Loaded")