
# Sample Dataset ⿥: Category and Quantity
'''df_sales = pd.DataFrame({
    'Product Category': ['Electronics', 'Clothing', 'Groceries', 'Toys', 'Books'],
    'Quantity Sold': [120, 200, 150, 90, 130]
})'''

# ⿥ Create a subplot with two plots side by side:
#     - Left plot: Bar chart of 'Product Category' vs 'Quantity Sold'.
#     - Right plot: Pie chart showing 'Category' wise sales percentage.

import matplotlib.pyplot as plt
import pandas as pd

df_sales = pd.DataFrame({
    'Product Category': ['Electronics', 'Clothing', 'Groceries', 'Toys', 'Books'],
    'Quantity Sold': [120, 200, 150, 90, 130]
})

print(df_sales)

plt.subplot(1,2,1)
plt.bar(df_sales['Product Category'],df_sales['Quantity Sold'])

plt.subplot(1,2,2)
plt.pie(df_sales['Quantity Sold'],labels=df_sales['Product Category'],autopct='%1.1f%%')

plt.show()

