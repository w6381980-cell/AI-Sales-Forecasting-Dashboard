import pandas as pd
from statsmodels.tsa.holtwinters import ExponentialSmoothing

df = pd.read_csv("data/processed/clean_sales_data.csv")
df['Order_Date'] = pd.to_datetime(df['Order_Date'])

monthly = df.resample('ME', on='Order_Date').sum()

model = ExponentialSmoothing(monthly['Revenue']).fit()

forecast = model.forecast(6)

forecast.to_csv("data/forecast/forecast.csv")

print("✅ Forecast Generated")