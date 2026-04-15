import pandas as pd

df = pd.read_csv("data/processed/clean_sales_data.csv")

# KPIs
total_revenue = df['Revenue'].sum()
total_profit = df['Profit'].sum()
total_orders = len(df)

# Insights
top_product = df.groupby('Product')['Revenue'].sum().idxmax()
top_region = df.groupby('Region')['Revenue'].sum().idxmax()

# Monthly trend
df['Order_Date'] = pd.to_datetime(df['Order_Date'])
monthly = df.resample('ME', on='Order_Date').sum()

best_month = monthly['Revenue'].idxmax().strftime('%B %Y')

# Create report text
insights = f"""
Top Product: {top_product}
Top Region: {top_region}
Best Month: {best_month}
"""

impact = """
- Identified high revenue generating products
- Found best performing regions
- Detected monthly sales trends
- Enabled data-driven decision making
"""

# Save Excel
report = pd.DataFrame({
    "Metric": ["Total Revenue", "Total Profit", "Total Orders"],
    "Value": [total_revenue, total_profit, total_orders]
})

report.to_excel("reports/excel/report.xlsx", index=False)

# Save text insights separately
with open("reports/excel/insights.txt", "w") as f:
    f.write(insights + "\n" + impact)

print("✅ Report + Insights Generated")