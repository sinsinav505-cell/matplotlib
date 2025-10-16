# ⿥ PIE CHART: Order Distribution by Category
# ============================================================
# Task: Create a pie chart showing the percentage of total orders for each category.
# Hint:
#   1. Use df['Category'].value_counts() to count orders
#   2. Use plt.pie() with autopct='%1.1f%%' and startangle=90
#   3. Add a title

import matplotlib.pyplot as plt 
import pandas as pd

df = pd.read_csv('orders.csv')
print(df.to_string())

countorders = df['Category'].value_counts()
print(countorders)

plt.pie(countorders,labels=countorders.index,
        autopct='%1.1f%%',startangle=90,
        shadow = True)

plt.title('Order Distribution by Category')

plt.show()