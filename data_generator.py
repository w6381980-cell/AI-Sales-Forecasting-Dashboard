import pandas as pd
import random
from datetime import datetime, timedelta

num_records = 5000

products = {
    "Laptop": ("Electronics", 50000),
    "Mobile": ("Electronics", 20000),
    "Shoes": ("Fashion", 3000),
    "Watch": ("Accessories", 2500)
}

regions = ["North", "South", "West", "East"]

start_date = datetime(2023,1,1)

data = []

for i in range(num_records):
    date = start_date + timedelta(days=random.randint(0, 700))
    product = random.choice(list(products.keys()))
    category, price = products[product]
    quantity = random.randint(1,5)
    region = random.choice(regions)

    revenue = quantity * price
    cost = price * 0.7
    profit = revenue - (quantity * cost)

    data.append([i, date, product, category, region, quantity, price, revenue, profit])

df = pd.DataFrame(data, columns=[
    "Order_ID","Order_Date","Product","Category",
    "Region","Quantity","Price","Revenue","Profit"
])

df.to_csv("data/raw/sales_data.csv", index=False)
print("✅ Data Generated")