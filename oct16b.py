#combining pandas and matplotlib (bargraph)

import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('orders.csv')
print(df.to_string())


category_quantity = df.groupby('Category')['Quantity'].sum()
print(category_quantity)

#barchart

plt.bar(category_quantity.index,category_quantity.values,color='Red')
plt.show()