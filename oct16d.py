#  BAR GRAPH: Total Sales by Country
# ============================================================
# Task: Create a bar chart showing total sales for each country.
# Hint:
#   1. Add a 'Sales' column: df['Sales'] = df['Quantity'] * df['Price']
#   2. Group by 'Country' and sum 'Sales'
#   3. Sort values in descending order
#   4. Use plt.bar() to plot
#   5. Display the sales value above each bar

import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('orders.csv')
print(df.to_string())

df['Sales'] = df['Quantity'] * df['Price']

country_sales = df.groupby('Country')['Sales'].sum().sort_values(ascending=False)

print(country_sales)

plt.barh(country_sales.index,country_sales.values)

plt.show()
