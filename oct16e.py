# ⿣ LINE GRAPH: Daily Sales Trend
# ============================================================
# Task: Plot a line graph showing total sales per day.
# Hint:
#   1. Convert 'OrderDate' to datetime: df['OrderDate'] = pd.to_datetime(df['OrderDate'])
#   2. Group by 'OrderDate' and sum 'Sales'
#   3. Use plt.plot() with markers and line style
#   4. Label X-axis, Y-axis, and add a title


import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('orders.csv')
print(df.to_string())

df['Sales'] = df['Quantity'] * df['Price']

df['OrderDate'] = pd.to_datetime(df['OrderDate'])

daily_sales = df.groupby('OrderDate')['Sales'].sum()

print(daily_sales)

line_style = dict(marker = 'o',
                  markersize = 2,
                  markeredgecolor = 'Red',
                  markerfacecolor = 'Red',
                  linestyle = 'solid',
                  linewidth = 2,
                  color = 'Blue')

plt.plot(daily_sales.index,daily_sales.values,**line_style)
plt.tight_layout()

plt.show()