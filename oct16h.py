# ⿦ PIE CHART: Country-wise Share of Total Sales
# ============================================================
# Task: Plot a pie chart showing the share of total sales by country.
# Hint:
#   1. Group by 'Country' and sum 'Sales'
#   2. Use plt.pie() with labels, autopct='%1.1f%%', colors, and shadow=True
#   3. Add a title

import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('orders.csv')
print(df.to_string())

df['Sales'] = df['Quantity'] * df['Price']

total_sales = df.groupby('Country')['Sales'].sum()

print(total_sales)

color = ['Red','Yellow','Blue','Green','Orange','skyblue']

plt.figure(figsize=(40,40))

plt.pie(total_sales, labels =total_sales.index, 
        autopct='%1.1f%%' ,colors= color , shadow=True,)


plt.tight_layout()

plt.show()