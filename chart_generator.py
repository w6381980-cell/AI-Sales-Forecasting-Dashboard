import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/processed/clean_sales_data.csv")
df['Order_Date'] = pd.to_datetime(df['Order_Date'])

monthly = df.resample('ME', on='Order_Date').sum()

plt.figure()
monthly['Revenue'].plot()
plt.title("Sales Trend")
plt.savefig("visuals/charts/sales_trend.png")

plt.figure()
df.groupby("Region")['Revenue'].sum().plot(kind='bar')
plt.title("Region Sales")
plt.savefig("visuals/charts/region_sales.png")

print("✅ Charts Saved")