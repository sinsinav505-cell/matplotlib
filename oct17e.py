# Sample Dataset ⿦: Yearly Revenue and Ad Spend
'''df_company = pd.DataFrame({
    'Year': [2018, 2019, 2020, 2021, 2022, 2023],
    'Revenue': [50000, 60000, 70000, 85000, 95000, 110000],
    'Ad Spend': [5000, 7000, 9000, 10000, 11000, 13000]
})'''

# ⿦ Create a 2x1 subplot layout:
#     - Top plot: Line chart showing 'Year' vs 'Revenue'.
#     - Bottom plot: Scatter plot showing 'Advertising Spend' vs 'Revenue'.

import matplotlib.pyplot as plt
import pandas as pd

df_company = pd.DataFrame({
    'Year': [2018, 2019, 2020, 2021, 2022, 2023],
    'Revenue': [50000, 60000, 70000, 85000, 95000, 110000],
    'Ad Spend': [5000, 7000, 9000, 10000, 11000, 13000]
})

print(df_company)

plt.subplot(2,1,1)
plt.plot(df_company['Year'],df_company['Revenue'])

plt.subplot(2,1,2)
plt.scatter(df_company['Ad Spend'],df_company['Revenue'])

plt.show()