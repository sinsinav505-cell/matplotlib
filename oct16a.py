#combining pandas and matplotlib

import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('orders.csv')
print(df.to_string())

line_style = dict(marker = 'o',
                  markersize = 10,
                  markeredgecolor = 'Red',
                  markerfacecolor = 'Red',
                  linestyle = 'solid',
                  linewidth = 2,
                  color = 'Blue')

category_quantity = df.groupby('Category')['Quantity'].sum()
print(category_quantity)

#linechart

plt.plot(category_quantity.index,category_quantity.values,**line_style)

plt.title('Total  Quantity sold by Category')
plt.xlabel('Category')
plt.ylabel('Total Quantity')

plt.show()
