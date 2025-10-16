#combining pandas and matplotlib

import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('orders.csv')
print(df.to_string())


category_quantity = df.groupby('Category')['Quantity'].sum()
print(category_quantity)

#piechart

plt.pie(category_quantity.values,
        labels=category_quantity.index,
        shadow=True,
        explode=[0.3,0,0],
        autopct="%1.1f%%")

plt.show()