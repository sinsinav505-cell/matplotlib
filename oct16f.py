# ⿤ LINE GRAPH: Category-wise Average Price
# ============================================================
# Task: Draw a line chart showing the average product price per category.
# Hint:
#   1. Group by 'Category' and calculate mean of 'Price'
#   2. Use plt.plot() with markers, colors, and line style
#   3. Label axes and add grid lines


import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('orders.csv')
print(df.to_string())

product_price = df.groupby('Category')['Price'].mean()

print(product_price)

line_style = dict(marker = 'o',
                  markersize = 2,
                  markeredgecolor = 'Red',
                  markerfacecolor = 'Red',
                  linestyle = 'solid',
                  linewidth = 2,
                  color = 'Green')

plt.xlabel('Category')
plt.ylabel('Mean of Price')

plt.grid(linewidth=0.5,
         color='#7dc8e3',
         linestyle='dashed')

plt.plot(product_price.index,product_price.values,**line_style)
plt.show()

